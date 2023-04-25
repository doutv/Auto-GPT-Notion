# Auto-GPT Notion Plugin
> Under rapid development

Extend Auto-GPT capabilities:
- Read Notion pages
- Write to Notion pages

Applications:
- Automatically collects information from the web and archives it to Notion.
- Notion as a knowledge base, chat with it on Discord/Slack.

## Demo
```
python -m autogpt
Plugins found: 1
--------------------
autogpt-notion: 0.1.0 - Notion API integrations using notion-sdk-py
```
## Install
**Do not clone this repo**, the working directory and environment are under **Auto-GPT**.

1. Install [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) and make sure you can run it successfully.
2. Install extra dependencies for this plugin.
    ```
    pip install notion-client python-dotenv auto_gpt_plugin_template
    ```
3. [Click Here](https://github.com/doutv/Auto-GPT-Notion/archive/refs/heads/master.zip) to download the source code as **ZIP**, and place the **ZIP** file under `plugins/`.
4. Create an Notion integration:
   1. Create an integration and get the token `NOTION_TOKEN`.
   2. Create a database based on this template.
   3. Share the database with your integration.
   4. Save the database ID `NOTION_DATABASE_ID`.
   5. [Check the Notion official docs for detailed instructions.](https://developers.notion.com/docs/create-a-notion-integration)
5. Edit `.env`:
   1. Add this plugin `AutoGPTNotion`to Auto-GPT plugin whitelist.
        ```
        ALLOWLISTED_PLUGINS=AutoGPTNotion
        ```
   2. Add Notion token and database id to `.env` under Auto-GPT directory.
        ```
        ################################################################################
        ### Notion
        ################################################################################

        NOTION_TOKEN=<Notion integration token>
        NOTION_DATABASE_ID=<Notion database id>
        ```
6. Run Auto-GPT and enjoy!

If you encounter problems or have any ideas, feel free to discuss:
- [Issues](https://github.com/doutv/Auto-GPT-Notion/issues)
- [Discord Channel](https://discord.com/channels/1092243196446249134/1098882305000472626)

## Contribution
This plugin is under development. 

Join me by submitting issues and pull requests.