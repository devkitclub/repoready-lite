"""Small, dependency-free example used to demonstrate pytest CI."""


def slugify(text: str) -> str:
    """Lowercase text and join whitespace-separated words with hyphens."""
    return "-".join(text.lower().split())
