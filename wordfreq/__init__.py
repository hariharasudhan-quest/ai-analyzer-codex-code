"""Count word frequencies from text."""

from collections import Counter
import re


# Match runs of Unicode letters and digits, but not underscores.
_WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)


def count_words(text: str) -> Counter[str]:
    """Return lowercase word counts for *text*."""
    return Counter(_WORD_RE.findall(text.lower()))


def top_words(text: str, limit: int = 10, min_length: int = 1) -> list[tuple[str, int]]:
    """Return the most frequent words, with alphabetical tie-breaking."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if min_length < 0:
        raise ValueError("min_length must be non-negative")
    counts = {
        word: count for word, count in count_words(text).items() if len(word) >= min_length
    }
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]
