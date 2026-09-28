import cv2
import numpy as np


def cartoonize(
    image_bgr: np.ndarray,
    *,
    median_kernel: int = 5,
    adaptive_block_size: int = 5,
    adaptive_c: int = 5,
    bilateral_diameter: int = 9,
    sigma_color: float = 300.0,
    sigma_space: float = 300.0,
) -> np.ndarray:
    """Create a simple cartoon effect while preserving the input resolution."""
    if image_bgr is None or image_bgr.ndim != 3 or image_bgr.shape[2] != 3:
        raise ValueError("Expected a BGR image with shape (height, width, 3).")
    if median_kernel < 3 or median_kernel % 2 == 0:
        raise ValueError("median_kernel must be an odd integer >= 3.")
    if adaptive_block_size < 3 or adaptive_block_size % 2 == 0:
        raise ValueError("adaptive_block_size must be an odd integer >= 3.")

    grayscale = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.medianBlur(grayscale, median_kernel)
    edges = cv2.adaptiveThreshold(
        smoothed,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        adaptive_block_size,
        adaptive_c,
    )
    colour = cv2.bilateralFilter(
        image_bgr,
        bilateral_diameter,
        sigma_color,
        sigma_space,
    )
    return cv2.bitwise_and(colour, colour, mask=edges)
