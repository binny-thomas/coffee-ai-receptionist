from app.knowledge_service import (
    preprocess_question,
    retrieve_relevant_knowledge,
)


def test_preprocess_question():
    question = "What are your opening hours?"

    keywords = preprocess_question(question)

    assert keywords == ["opening", "hours"]


def test_retrieve_opening_hours():
    matches = retrieve_relevant_knowledge(
        "What are your opening hours?"
    )

    assert matches
    assert matches[0].startswith("Opening Hours")


def test_retrieve_home_delivery():
    matches = retrieve_relevant_knowledge(
        "Do you offer home delivery?"
    )

    assert matches
    assert matches[0].startswith("Services")


def test_unknown_information_returns_no_matches():
    matches = retrieve_relevant_knowledge(
        "Do you sell pizza?"
    )

    assert matches == []