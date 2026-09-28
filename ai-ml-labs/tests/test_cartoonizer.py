import numpy as np
import pytest

from ai_ml_labs.cartoonizer import cartoonize


def test_cartoonizer_preserves_shape_and_dtype():
    image = np.zeros((24, 32, 3), dtype=np.uint8)
    image[:, 16:] = 255

    result = cartoonize(image)

    assert result.shape == image.shape
    assert result.dtype == image.dtype


def test_cartoonizer_rejects_invalid_kernel():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    with pytest.raises(ValueError, match="odd"):
        cartoonize(image, median_kernel=4)
