"""Clean-room reference implementation of ArabesqueMC Selective core.

Recovered from instruction-level analysis of Bx_TSelective in the legacy
binary. No proprietary binary is required to run this module.
"""

REGIONS = [
    "BLUE", "BLUE_CYAN", "CYAN", "SCYAN", "CYAN_GREEN", "GREEN",
    "GREEN_YELLOW", "YELLOW", "SYELLOW", "YELLOW_RED", "RED",
    "RED_MAGENTA", "MAGENTA", "SMAGENTA", "MAGENTA_BLUE", "WHITE",
    "BLACK", "SBLACK",
]


def _rgb_geometry(r: int, g: int, b: int):
    """Return hi, mid, lo, i, j, k using the recovered unsigned branches."""
    r &= 0xff; g &= 0xff; b &= 0xff
    if b > r:
        if b > g:
            if r > g:
                return b, r, g, 8, 0, 5
            return b, g, r, 9, 0, 4
        return g, b, r, 10, 2, 4
    if g < r:
        if g > b:
            return r, g, b, 12, 1, 3
        return r, b, g, 13, 1, 5
    return g, r, b, 11, 2, 3


def _cmy_geometry(c: int, m: int, y: int):
    c &= 0xff; m &= 0xff; y &= 0xff
    if c > m:
        if c > y:
            if m > y:
                return c, m, y, 3, 11, 2
            return c, y, m, 3, 12, 1
        return y, c, m, 4, 10, 2
    if m > y:
        if c > y:
            return m, c, y, 5, 13, 1
        return m, y, c, 4, 9, 1
    return y, m, c, 5, 8, 0


def _div100_signed(n: int) -> int:
    # Python's int(n/100) gives truncation toward zero, matching the
    # signed division semantics recovered from the reciprocal multiply.
    return int(n / 100)


def compute_rgb(r: int, g: int, b: int, p):
    if len(p) != 18:
        raise ValueError("expected 18 Selective parameters")
    r &= 0xff; g &= 0xff; b &= 0xff
    hi, mid, lo, i, j, k = _rgb_geometry(r, g, b)
    a = hi - mid
    bb = mid - lo
    t = 2 * min(a, bb)
    s = (
        p[i] * t
        + p[7] * (255 - hi)
        + p[14] * (255 - r)
        + p[15] * (255 - g)
        + p[16] * (255 - b)
        + p[j] * a
        + p[k] * bb
        + p[6] * b
    )
    q = max(0, min(255, _div100_signed(s)))
    return 255 - q


def compute_cmyk(c: int, m: int, y: int, k_in: int, p):
    if len(p) != 18:
        raise ValueError("expected 18 Selective parameters")
    c &= 0xff; m &= 0xff; y &= 0xff; k_in &= 0xff
    hi, mid, lo, i, j, k = _cmy_geometry(c, m, y)
    a = hi - mid
    bb = mid - lo
    t = 2 * min(a, bb)
    s = (
        p[i] * t
        + p[6] * (255 - mid)
        + p[j] * a
        + p[k] * bb
        + p[7] * lo
        + p[14] * (255 - c)
        + p[15] * (255 - m)
        + p[16] * (255 - y)
        + p[17] * k_in
    )
    return max(0, min(255, _div100_signed(s)))
