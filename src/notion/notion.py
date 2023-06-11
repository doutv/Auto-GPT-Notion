from . import AutoGPTNotion

plugin = AutoGPTNotion()


def _unwrap_rich_text(rich_text: list):
    return "".join([each.get("text").get("content") for each in rich_text])


def create_page(title, summary, tags, content):
    """
    Creates a new Notion page

    Parameters:
        - title: The title of the page.
        - summary: A brief summary of the page.
        - tags: A list of tags associated with the page.
        - content: The content of the page.

    Returns:
        - If the page is created successfully, returns a string indicating the success
            and the URL of the newly created page.
        - If there is an error during the creation process, returns the error message.
    """
    # Get database id from config
    database_id = plugin.database_id
    parent = {"database_id": database_id}

    # Page properties
    properties = {
        "Title": {"title": [{"text": {"content": title}}]},
        "Summary": {"rich_text": [{"text": {"content": summary}}]},
        "Tags": {"multi_select": [{"name": tag} for tag in tags]},
    }

    # Page content
    children = [
        {
            "object": "block",
            "paragraph": {"rich_text": [{"text": {"content": content}}]},
        }
    ]
    page = plugin.notion.pages.create(
        parent=parent, properties=properties, children=children
    )
    return f"""Create Notion page successfully!
        link: {page.get('url')}
        page_id: {page.get('id')}"""


def get_all_pages():
    """
    Retrieves all pages properties from a database

    Returns:
    - A list of dictionaries, each dictionary has the following keys:
        - id: The ID of the page in the database.
        - title: The title of the page.
        - summary: The summary of the page, or None if it doesn't exist.
        - tags: A list of tags associated with the page.
    """
    # Get the database ID from the plugin object
    database_id = plugin.database_id

    # Query the database using the Notion API to get all pages
    pages = plugin.notion.databases.query(
        **{
            "database_id": database_id,
        }
    ).get("results")

    # Initialize an empty list to store information about each page
    page_info = []

    # Loop through each page and extract its properties
    for page in pages:
        page_properties = page.get("properties")

        # Get the title of the page
        try:
            title = (
                page_properties.get("Title").get("title")[0].get("text").get("content")
            )
        except IndexError or AttributeError:
            title = None

        # Try to get the summary of the page, or set it to None if it doesn't exist
        try:
            summary = (
                page_properties.get("Summary", {})
                .get("rich_text")[0]
                .get("text")
                .get("content")
            )
        except IndexError or AttributeError:
            summary = None

        # Get the tags of the page
        tags = [
            tag.get("name") for tag in page_properties.get("Tags").get("multi_select")
        ]

        # Add the page's information to the list
        page_info.append(
            {"id": page.get("id"), "title": title, "summary": summary, "tags": tags}
        )

    # Return the list of page information
    return page_info


def update_page_properties(page_id, title, summary, tags):
    """
    Update page properties by id
    """
    properties = {
        "Title": {"title": [{"text": {"content": title}}]},
        "Summary": {"rich_text": [{"text": {"content": summary}}]},
        "Tags": {"multi_select": [{"name": tag} for tag in tags]},
    }
    page = plugin.notion.pages.update(page_id=page_id, properties=properties)
    return f"Update Notion page successfully! {page.get('url')}"


def append_page(page_id, content):
    """
    Append page content by id
    """
    children = [
        {
            "object": "block",
            "paragraph": {"rich_text": [{"text": {"content": content}}]},
        }
    ]
    # get the last block_id from page_id
    block_id = (
        plugin.notion.blocks.children.list(block_id=page_id)
        .get("results")[-1]
        .get("id")
    )
    page = plugin.notion.blocks.children.append(block_id=block_id, children=children)
    return f"Append Notion page successfully! {page.get('url')}"


def retrieve_page(page_id):
    """
    Retrieve page properties and content by id
    """
    # Get page properties
    properties = plugin.notion.pages.retrieve(page_id=page_id).get("properties")
    # Get page contents from all its child blocks
    blocks = plugin.notion.blocks.children.list(block_id=page_id).get("results")
    content = ""
    for block in blocks:
        content += _unwrap_rich_text(block[block["type"]].get("rich_text"))
    return {
        "title": properties.get("Title").get("title")[0].get("text").get("content"),
        "summary": _unwrap_rich_text(properties.get("Summary").get("rich_text")),
        "tags": [tag.get("name") for tag in properties.get("Tags").get("multi_select")],
        "content": content,
    }
