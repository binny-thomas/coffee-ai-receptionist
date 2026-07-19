import re
from pathlib import Path

STOP_WORDS = {
    "a", "an", "the",
    "is", "are", "was", "were",
    "what", "when", "where", "who", "why", "how",
    "do", "does", "did",
    "can", "could", "would", "should",
    "i", "me", "my",
    "you", "your",
    "we", "our",
    "to", "of", "for", "in", "on", "at", "with",
    "and", "or"
}


def load_knowledge():
    """Load the coffee shop knowledge base."""

    knowledge_path = Path("knowledge/coffee_shop.txt")

    return knowledge_path.read_text(encoding="utf-8")


def split_into_sections(knowledge):
    """Split the knowledge into individual sections."""

    sections = []

    for section in knowledge.split("##"):
        section = section.strip()

        if section:
            sections.append(section)

    return sections


def preprocess_question(question):
    """Convert a question into searchable keywords."""
    keywords = re.findall(r"\w+", question.lower())

    return [
        keyword
        for keyword in keywords
        if keyword not in STOP_WORDS
    ]


def search_sections(sections, keywords):
    """Search sections and rank them by keyword relevance."""

    matches = []

    for section in sections:
        section_lower = section.lower()
        score = 0

        for keyword in keywords:
            if keyword in section_lower:
                score += 1

        if score > 0:
            matches.append((section, score))

    matches.sort(key=lambda item: item[1], reverse=True)

    return [
        section
        for section, score in matches
    ]


def retrieve_relevant_knowledge(question):
    """Retrieve knowledge relevant to the user's question."""

    knowledge = load_knowledge()

    sections = split_into_sections(knowledge)

    keywords = preprocess_question(question)

    matches = search_sections(sections, keywords)

    return matches