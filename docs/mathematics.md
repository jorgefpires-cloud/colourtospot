# Selective mathematics — recovered core

The Selective operation uses 18 integer parameters, one for each region:

0 BLUE, 1 BLUE_CYAN, 2 CYAN, 3 SCYAN, 4 CYAN_GREEN, 5 GREEN,
6 GREEN_YELLOW, 7 YELLOW, 8 SYELLOW, 9 YELLOW_RED, 10 RED,
11 RED_MAGENTA, 12 MAGENTA, 13 SMAGENTA, 14 MAGENTA_BLUE, 15 WHITE,
16 BLACK, 17 SBLACK.

For RGB input, the recovered `ComputeFromRgb` first orders the three 8-bit components and forms:

- `a = hi - mid`
- `b = mid - lo`
- `t = 2 * min(a, b)`

The branch-selected region indices are preserved in `reference/selective.py`; equality boundaries should be treated according to the original unsigned byte comparisons.

The recovered RGB weighted sum is:

`S = P[i]*t + P[7]*(255-hi) + P[14]*(255-R) + P[15]*(255-G) + P[16]*(255-B) + P[j]*a + P[k]*b + P[6]*B`

The original then performs signed integer division by 100, clamps to `[0,255]`, and returns `255 - result`.

The CMYK path similarly uses CMY ordering and includes `P[17]*K`; its final value is not inverted.

These formulas are **recovered from static instruction-level analysis**. Pixel-perfect status still requires runtime comparison against the legacy application.
