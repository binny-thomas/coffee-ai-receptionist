import re
from collections.abc import Sequence
from functools import lru_cache
from pathlib import Path


KNOWLEDGE_FILE = (
    Path(__file__).resolve().parent.parent
    / "knowledge"
    / "coffee_shop.txt"
)


STOP_WORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "what",
    "when",
    "where",
    "who",
    "why",
    "how",
    "do",
    "does",
    "did",
    "can",
    "could",
    "would",
    "should",
    "i",
    "me",
    "my",
    "you",
    "your",
    "we",
    "our",
    "to",
    "of",
    "for",
    "in",
    "on",
    "at",
    "with",
    "and",
    "or",
}


def load_knowledge() -> str:
    """
    Load the complete coffee shop knowledge base from disk.

    This function performs file I/O. It is intentionally kept separate
    from caching and retrieval logic.
    """
    return KNOWLEDGE_FILE.read_text(encoding="utf-8")


def split_into_sections(knowledge: str) -> list[str]:
    """
    Split the knowledge document into individual sections.

    Sections in the knowledge file begin with ## headings.
    Empty sections are discarded.
    """
    return [
        section.strip()
        for section in knowledge.split("##")
        if section.strip()
    ]


@lru_cache(maxsize=1)
def get_knowledge_sections() -> tuple[str, ...]:
    """
    Load, process, and cache the knowledge sections.

    The first call reads and processes the knowledge file.
    Later calls return the cached tuple without reading the file again.
    """
    knowledge = load_knowledge()
    sections = split_into_sections(knowledge)

    return tuple(sections)


def clear_knowledge_cache() -> None:
    """
    Clear cached knowledge sections.

    The knowledge file will be reloaded the next time
    get_knowledge_sections() is called.
    """
    get_knowledge_sections.cache_clear()


def preprocess_question(question: str) -> list[str]:
    """
    Normalize a user question and remove common stop words.
    """
    words = re.findall(r"\w+", question.lower())

    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]


def search_sections(
    sections: Sequence[str],
    keywords: list[str],
) -> list[str]:
    """
    Rank knowledge sections according to keyword relevance.

    A section receives one point for each query keyword it contains.
    Sections with higher scores appear first.
    """
    ranked_sections: list[tuple[int, str]] = []

    for section in sections:
        normalized_section = section.lower()

        score = sum(
            1
            for keyword in keywords
            if keyword in normalized_section
        )

        if score > 0:
            ranked_sections.append((score, section))

    ranked_sections.sort(
        key=lambda result: result[0],
        reverse=True,
    )

    return [
        section
        for _, section in ranked_sections
    ]


def retrieve_relevant_knowledge(question: str) -> list[str]:
    """
    Retrieve relevant knowledge sections for a user question.
    """
    keywords = preprocess_question(question)

    if not keywords:
        return []

    sections = get_knowledge_sections()

    return search_sections(sections, keywords)