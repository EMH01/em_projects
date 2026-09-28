# OpenCV Cartoonizer

A compact classical-computer-vision lab that turns an image into a cartoon-like rendering.

## Pipeline

```text
BGR image
  → grayscale
  → median blur
  → adaptive threshold edges
  → bilateral colour smoothing
  → edge mask × smoothed colour image
```

This is a modernized version of an earlier Streamlit/OpenCV cartoonization demo.

### Improvements

- image resolution is preserved instead of forcing every upload to `400 × 600`
- `np.frombuffer` replaces deprecated `np.fromstring` binary usage
- BGR/RGB conversion is explicit and correct
- processing is separated from the Streamlit UI
- parameters are validated
- the core transformation has automated tests

Run with:

```bash
pip install -e ".[streamlit]"
streamlit run labs/computer-vision/cartoonizer/app.py
```

This is intentionally a **small CV demo**, not presented as a deep-learning project.
