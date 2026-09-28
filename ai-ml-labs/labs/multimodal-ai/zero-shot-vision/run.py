import argparse
import os

from openai import OpenAI

from ai_ml_labs.multimodal import house_detection_prompt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_url")
    parser.add_argument("--model", default=os.getenv("OPENAI_VISION_MODEL"))
    args = parser.parse_args()

    if not args.model:
        parser.error("Pass --model or set OPENAI_VISION_MODEL.")

    prompt = house_detection_prompt(args.image_url)
    response = OpenAI().responses.create(
        model=args.model,
        input=prompt.response_input(),
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
