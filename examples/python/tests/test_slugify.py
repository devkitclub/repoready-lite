import pytest

from repoready_example import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("RepoReady Lite", "repoready-lite"),
        ("  Hello   World  ", "hello-world"),
        ("Hello\tWorld\nAgain", "hello-world-again"),
        ("", ""),
        ("   ", ""),
        ("Already-Slugged", "already-slugged"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected
