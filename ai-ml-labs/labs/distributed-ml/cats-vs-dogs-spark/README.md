# Cats vs Dogs with Spark ML

A cleaned-up version of the original PySpark image-classification notebook.

This experiment intentionally approaches image classification as a **distributed feature-engineering + classical ML** problem rather than as a CNN problem:

1. load Cat/Dog image paths
2. resize and convert to grayscale
3. apply an edge filter
4. flatten pixels into Spark vectors
5. optionally perform univariate feature selection
6. compare Decision Tree, Linear SVM, and MLP classifiers

The dataset reference remains the Kaggle **Dogs vs. Cats** dataset used by the original notebook. Dataset files are not committed.

## Corrections made during modernization

This maintained lab corrects several issues identified in the earlier notebook:

- the MLP output layer now has **2 units**, matching the binary Cat/Dog task rather than 10
- the selected-feature LinearSVC now actually uses `selected_features`
- selected-feature MLP also uses the selected vector dimension
- AUC uses Spark's `rawPrediction` output rather than the predicted class as its score
- feature-selection threshold is explicit and configurable
- paths are local/portable instead of tied to Google Drive
- train/test randomness is seeded

Run:

```bash
pip install -e ".[spark]"
python labs/distributed-ml/cats-vs-dogs-spark/train.py /path/to/PetImages
```

Useful options:

```bash
--samples-per-class 500
--image-size 224
--selection-percentile 0.5
--seed 34
```

## Historical observation

The original notebook reported metrics broadly around **0.5–0.6** on its 1,000-image experiment, with LinearSVC performing somewhat better than the alternatives.

Those are retained as historical observations, not as fresh benchmark results. A modern rerun should record exact metrics, Spark version, hardware, runtime, and dataset cleaning decisions.
