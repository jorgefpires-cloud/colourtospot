from reference.selective import compute_rgb, compute_cmyk


def one_hot(index, value=100):
    p = [0] * 18
    p[index] = value
    return p


def test_rgb_region_geometry_is_reachable():
    cases = [
        ((255, 128, 0), 8),
        ((255, 0, 128), 13),
        ((128, 255, 0), 11),
        ((0, 255, 128), 10),
        ((128, 0, 255), 9),
        ((0, 128, 255), 9),
    ]
    for rgb, region in cases:
        p = one_hot(region)
        assert compute_rgb(*rgb, p) >= 0


def test_rgb_output_is_clamped_and_inverted():
    assert compute_rgb(255, 255, 255, one_hot(14, 100)) == 255
    assert compute_rgb(0, 0, 0, one_hot(14, 100)) == 0


def test_cmyk_black_parameter():
    p = one_hot(17, 100)
    assert compute_cmyk(0, 0, 0, 255, p) == 255
