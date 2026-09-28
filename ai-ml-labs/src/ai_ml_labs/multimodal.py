from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VisionPrompt:
    instruction: str
    image_urls: tuple[str, ...]

    def response_input(self) -> list[dict[str, object]]:
        content: list[dict[str, str]] = [
            {"type": "input_text", "text": self.instruction}
        ]
        content.extend(
            {"type": "input_image", "image_url": url}
            for url in self.image_urls
        )
        return [{"role": "user", "content": content}]


def house_detection_prompt(image_url: str) -> VisionPrompt:
    return VisionPrompt(
        instruction=(
            "Determine whether a house is visible in the image. "
            "Return exactly two lines: 'House: Yes' or 'House: No', "
            "followed by a short evidence line."
        ),
        image_urls=(image_url,),
    )


def windshield_prompt(
    *,
    good_reference_url: str,
    damaged_reference_url: str,
    target_url: str,
) -> VisionPrompt:
    return VisionPrompt(
        instruction=(
            "The first reference shows a windshield in good condition and the second "
            "shows a damaged windshield. Evaluate the third image. Return a condition "
            "of Good or Bad and briefly explain the visible evidence. Do not infer "
            "damage that is not visible."
        ),
        image_urls=(good_reference_url, damaged_reference_url, target_url),
    )
