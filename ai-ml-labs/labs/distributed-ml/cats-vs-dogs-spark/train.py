import argparse
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from pyspark.ml.classification import (
    DecisionTreeClassifier,
    LinearSVC,
    MultilayerPerceptronClassifier,
)
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer, UnivariateFeatureSelector
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, udf


def image_to_vector(path: str, image_size: int):
    image = Image.open(path).convert("L")
    image = image.resize((image_size, image_size))
    image = image.filter(ImageFilter.FIND_EDGES)
    array = np.asarray(image, dtype=np.float32) / 255.0
    return Vectors.dense(array.flatten())


def metrics(predictions) -> dict[str, float]:
    multiclass = MulticlassClassificationEvaluator(
        labelCol="label",
        predictionCol="prediction",
    )
    binary = BinaryClassificationEvaluator(
        labelCol="label",
        rawPredictionCol="rawPrediction",
        metricName="areaUnderROC",
    )
    return {
        "accuracy": multiclass.evaluate(
            predictions,
            {multiclass.metricName: "accuracy"},
        ),
        "f1": multiclass.evaluate(
            predictions,
            {multiclass.metricName: "f1"},
        ),
        "weighted_precision": multiclass.evaluate(
            predictions,
            {multiclass.metricName: "weightedPrecision"},
        ),
        "weighted_recall": multiclass.evaluate(
            predictions,
            {multiclass.metricName: "weightedRecall"},
        ),
        "auc": binary.evaluate(predictions),
    }


def fit_and_measure(name: str, estimator, train_data, test_data):
    started = time.perf_counter()
    model = estimator.fit(train_data)
    elapsed = time.perf_counter() - started
    scores = metrics(model.transform(test_data))
    print(name, {"train_seconds": round(elapsed, 2), **scores})
    return model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path, help="Directory containing Cat/ and Dog/")
    parser.add_argument("--samples-per-class", type=int, default=500)
    parser.add_argument("--image-size", type=int, default=224)
    parser.add_argument("--selection-percentile", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=34)
    args = parser.parse_args()

    spark = SparkSession.builder.appName("CatsDogsImageClassification").getOrCreate()

    image_paths = []
    for class_name in ("Cat", "Dog"):
        directory = args.dataset / class_name
        image_paths.extend(
            str(path)
            for path in sorted(directory.iterdir())[: args.samples_per_class]
            if path.is_file()
        )

    frame = spark.createDataFrame([(path,) for path in image_paths], ["image_path"])
    frame = frame.withColumn(
        "label_name",
        regexp_extract(col("image_path"), r"(?:/|\\)(Cat|Dog)(?:/|\\)", 1),
    )
    frame = StringIndexer(
        inputCol="label_name",
        outputCol="label",
    ).fit(frame).transform(frame)

    vectorize = udf(
        lambda path: image_to_vector(path, args.image_size),
        VectorUDT(),
    )
    frame = frame.withColumn("image_features", vectorize(col("image_path"))).cache()

    selector = UnivariateFeatureSelector(
        featuresCol="image_features",
        outputCol="selected_features",
        labelCol="label",
        selectionMode="percentile",
    )
    selector = selector.setFeatureType("continuous").setLabelType("categorical")
    selector = selector.setSelectionThreshold(args.selection_percentile)
    selected = selector.fit(frame).transform(frame).cache()

    train_raw, test_raw = frame.randomSplit([0.8, 0.2], seed=args.seed)
    train_selected, test_selected = selected.randomSplit([0.8, 0.2], seed=args.seed)

    input_size_raw = len(train_raw.select("image_features").first()["image_features"])
    input_size_selected = len(
        train_selected.select("selected_features").first()["selected_features"]
    )

    experiments = [
        (
            "decision-tree/raw",
            DecisionTreeClassifier(
                labelCol="label",
                featuresCol="image_features",
                seed=args.seed,
            ),
            train_raw,
            test_raw,
        ),
        (
            "decision-tree/selected",
            DecisionTreeClassifier(
                labelCol="label",
                featuresCol="selected_features",
                seed=args.seed,
            ),
            train_selected,
            test_selected,
        ),
        (
            "linear-svc/raw",
            LinearSVC(
                labelCol="label",
                featuresCol="image_features",
                maxIter=500,
                regParam=0.1,
            ),
            train_raw,
            test_raw,
        ),
        (
            "linear-svc/selected",
            LinearSVC(
                labelCol="label",
                featuresCol="selected_features",
                maxIter=500,
                regParam=0.1,
            ),
            train_selected,
            test_selected,
        ),
        (
            "mlp/raw",
            MultilayerPerceptronClassifier(
                labelCol="label",
                featuresCol="image_features",
                layers=[input_size_raw, 64, 32, 2],
                maxIter=500,
                blockSize=128,
                seed=args.seed,
            ),
            train_raw,
            test_raw,
        ),
        (
            "mlp/selected",
            MultilayerPerceptronClassifier(
                labelCol="label",
                featuresCol="selected_features",
                layers=[input_size_selected, 64, 32, 2],
                maxIter=500,
                blockSize=128,
                seed=args.seed,
            ),
            train_selected,
            test_selected,
        ),
    ]

    for name, estimator, train_data, test_data in experiments:
        fit_and_measure(name, estimator, train_data, test_data)

    spark.stop()


if __name__ == "__main__":
    main()
