from notion_client import Client
from pprint import pprint

from . import AutoGPTNotion

plugin = AutoGPTNotion()


def create_page(title, summary, tags, content):
    """Creates a new page that is a child of an existing database."""
    database_id = plugin.database_id
    parent = {"database_id": database_id}
    properties = {
        "Title": {"title": [{"text": {"content": title}}]},
        "Summary": {"rich_text": [{"text": {"content": summary}}]},
        "Tags": {"multi_select": [{"name": tag} for tag in tags]},
    }
    children = [
        {
            "object": "block",
            "paragraph": {"rich_text": [{"text": {"content": content}}]},
        }
    ]
    try:
        page = plugin.notion.pages.create(
            parent=parent, properties=properties, children=children
        )
        return f"Create Notion page successfully! {page.get('url')}"
    except Exception as e:
        return e


def get_all_pages():
    """
    Retrieves all pages from a database and returns a list of dictionaries containing
    the page's title, summary, and tags.
    """
    database_id = plugin.database_id
    pages = plugin.notion.databases.query(
        **{
            "database_id": database_id,
        }
    ).get("results")
    page_info = []
    for page in pages:
        page_properties = page.get("properties")
        title = page_properties.get("Title").get("title")[0].get("text").get("content")
        try:
            summary = (
                page_properties.get("Summary", {})
                .get("rich_text")[0]
                .get("text")
                .get("content")
            )
        except IndexError or AttributeError:
            summary = None
        tags = [
            tag.get("name") for tag in page_properties.get("Tags").get("multi_select")
        ]
        page_info.append(
            {"id": page.get("id"), "title": title, "summary": summary, "tags": tags}
        )
    return page_info


'''
if __name__ == "__main__":
    database_id = "e3187aaa1aed42c39f0f372fdf84655e"
    pprint(get_all_pages(database_id))
    print(
        create_page(
            database_id=database_id,
            title="Hello World",
            content="Hello GPT!",
            summary="This is a summary",
            tags=["information", "test"],
        )
    )
'''