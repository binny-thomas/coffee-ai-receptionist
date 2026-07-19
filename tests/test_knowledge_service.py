import pytest

from app.knowledge_service import (
    clear_knowledge_cache,
    get_knowledge_sections,
    preprocess_question,
    retrieve_relevant_knowledge,
)


@pytest.fixture(autouse=True)
def reset_knowledge_cache():
    """
    Ensure every test starts and finishes with an empty cache.

    This prevents one test's cached state from affecting another test.
    """
    clear_knowledge_cache()

    yield

    clear_knowledge_cache()


def test_preprocess_question():
    result = preprocess_question(
        "What are your opening hours?"
    )

    assert result == ["opening", "hours"]


def test_retrieve_opening_hours():
    result = retrieve_relevant_knowledge(
        "What are your opening hours?"
    )

    assert result
    assert "opening hours" in result[0].lower()


def test_retrieve_home_delivery():
    result = retrieve_relevant_knowledge(
        "Do you provide home delivery?"
    )

    assert result
    assert any(
        "home delivery" in section.lower()
        for section in result
    )


def test_unknown_question_returns_empty_list():
    result = retrieve_relevant_knowledge(
        "Do you repair motorcycles?"
    )

    assert result == []


def test_get_knowledge_sections_returns_tuple():
    sections = get_knowledge_sections()

    assert isinstance(sections, tuple)


def test_get_knowledge_sections_reuses_cached_object():
    first_result = get_knowledge_sections()
    second_result = get_knowledge_sections()

    assert first_result is second_result


def test_clear_knowledge_cache_creates_new_object():
    first_result = get_knowledge_sections()

    clear_knowledge_cache()

    second_result = get_knowledge_sections()

    assert first_result == second_result
    assert first_result is not second_result


def test_knowledge_sections_cache_records_hit_and_miss():
    get_knowledge_sections()
    get_knowledge_sections()

    cache_info = get_knowledge_sections.cache_info()

    assert cache_info.misses == 1
    assert cache_info.hits == 1
    assert cache_info.currsize == 1
    assert cache_info.maxsize == 1