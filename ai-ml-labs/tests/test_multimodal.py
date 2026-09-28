from ai_ml_labs.multimodal import house_detection_prompt, windshield_prompt


def test_house_prompt_has_one_image():
    prompt = house_detection_prompt("https://example.com/house.jpg")
    payload = prompt.response_input()

    assert payload[0]["role"] == "user"
    assert len(payload[0]["content"]) == 2
    assert payload[0]["content"][1]["type"] == "input_image"


def test_windshield_prompt_preserves_reference_order():
    prompt = windshield_prompt(
        good_reference_url="good",
        damaged_reference_url="damaged",
        target_url="target",
    )
    content = prompt.response_input()[0]["content"]

    assert [item["image_url"] for item in content[1:]] == [
        "good",
        "damaged",
        "target",
    ]
