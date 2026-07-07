from app.knowledge_service import (
    load_knowledge,
    split_into_sections,
    search_sections,
)

knowledge = load_knowledge()
sections = split_into_sections(knowledge)

keywords = ["home", "delivery"]

matches = search_sections(sections, keywords)

for match in matches:
    print("=" * 40)
    print(match)