import argparse
import os

from openai import OpenAI

from ai_ml_labs.multimodal import windshield_prompt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--good-reference", required=True)
    parser.add_argument("--damaged-reference", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--model", default=os.getenv("OPENAI_VISION_MODEL"))
    args = parser.parse_args()

    if not args.model:
        parser.error("Pass --model or set OPENAI_VISION_MODEL.")

    prompt = windshield_prompt(
        good_reference_url=args.good_reference,
        damaged_reference_url=args.damaged_reference,
        target_url=args.target,
    )
    response = OpenAI().responses.create(
        model=args.model,
        input=prompt.response_input(),
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
