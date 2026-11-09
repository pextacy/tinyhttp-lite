from tinyhttp import parse_range


def test_open_range():
    assert parse_range('bytes=0-', 100) == (0, 100)
