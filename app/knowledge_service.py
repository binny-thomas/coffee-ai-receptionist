from pathlib import Path

def load_knowledge():
    """Load and return the knowledge base """

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

def search_sections(sections, keywords):
    """Search sections for matching keywords."""

    matches = []

    for section in sections:
        section_lower = section.lower()

        for keyword in keywords:
            if keyword in section_lower:
                matches.append(section)
                break

    return matches

def retrieve_relevant_knowledge(question):
    """Retrieve knowledge relevant to the user's question."""

    knowledge = load_knowledge()

    sections = split_into_sections(knowledge)

    keywords = question.lower().split()

    matches = search_sections(sections, keywords)

    return matches

