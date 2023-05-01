import datetime
from pprint import pprint

from .notion import (
    append_page,
    create_page,
    get_all_pages,
    retrieve_page,
    update_page_properties,
)

# Integration tests


def create_test_page(title, summary, tags, content) -> str:
    """Create a test page and return its id"""
    output = create_page(
        title=title,
        summary=summary,
        tags=tags,
        content=content,
    )
    page_id = output[output.find("page_id: ") + len("page_id: ") :]
    return page_id


def test_create_page():
    pprint(
        create_test_page(
            title="test_create_page",
            summary="pass",
            tags=["test"],
            content=f"running test_create_page() on {datetime.datetime.now()}",
        )
    )


def test_get_all_pages():
    pprint(get_all_pages())


def test_append_page():
    page_id = create_test_page(
        title="test_append_page",
        summary="pass",
        tags=["test"],
        content="",
    )
    pprint(
        append_page(
            page_id=page_id,
            content=f"running test_append_page() on {datetime.datetime.now()}",
        )
    )


def test_retrieve_page():
    page_id = create_test_page(
        title="test_retrieve_page",
        summary="unknown",
        tags=["test"],
        content="",
    )
    pprint(retrieve_page(page_id))


def test_update_page_properties():
    page_id = create_test_page(
        title="test_update_page_properties",
        summary="failed",
        tags=["test", "test-failed"],
        content="update_page_properties() failed",
    )
    pprint(
        update_page_properties(
            page_id=page_id,
            title="test_update_page_properties",
            summary="pass",
            tags=["test", "test-updated"],
        )
    )
