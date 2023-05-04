<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![Discord][discord-shield]][discord-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://user-images.githubusercontent.com/20609724/236097216-c6516099-5823-49d3-9941-fa0193c81acd.png" alt="Logo" width="80" height="80">

  <h3 align="center">Auto-GPT-Notion</h3>

  <p align="center">
    Power Auto-GPT with Notion!
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li>
        <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#commands">Commands</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Features

- Read & Create & Update Notion databases/pages.
- Automatically collects information from the web and archives it to Notion.
- Save Auto-GPT's ideas to Notion.

### Demo
[Visit this database](https://doutv.notion.site/doutv/e3187aaa1aed42c39f0f372fdf84655e?v=b892e5b7d13f49ec8ff200916e79cf5b) managed by Auto-GPT.

```yaml
# ai_settings.yaml
ai_goals:
- Use "google" command to search what is Auto-GPT, and save the result to a Notion page
ai_name: Notion-GPT
ai_role: Research assistant
```

![image](https://user-images.githubusercontent.com/20609724/234296458-f303140f-bf58-48d8-89e2-06f52806893d.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
**Do not clone this repo**, the working directory and environment are under **Auto-GPT**.

### Prerequisites
1. Install [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT), **checkout the [latest release v0.3.0](https://github.com/Significant-Gravitas/Auto-GPT/releases/tag/v0.3.0) which add plugins support**, and make sure you can run it successfully.
2. Install extra dependencies for this plugin.
    ```
    pip install notion-client python-dotenv auto_gpt_plugin_template
    ```

### Download
[Click Here](https://github.com/doutv/Auto-GPT-Notion/archive/refs/heads/master.zip) to download the source code as **ZIP**, and place the **ZIP** file under `Auto-GPT/plugins/`.

### Notion Settings
> Check the [Notion official docs](https://developers.notion.com/docs/create-a-notion-integration) for more details.
1. Create an integration [here](https://www.notion.so/my-integrations), and get the token `NOTION_TOKEN`.
2. Duplicate [this database template](https://doutv.notion.site/e3187aaa1aed42c39f0f372fdf84655e?v=b892e5b7d13f49ec8ff200916e79cf5b), click "Duplicate" on upper right corner.
3. Share the newly created database with your integration, click "..." on upper right corner, then click "Add connections" and input the integration name in the first step.
4. Save the database ID `NOTION_DATABASE_ID`, you can get from the database url.
    ```
    https://www.notion.so/doutv/2e2030693c624c258bcc402ef8d4b357?v=...
                               |--------- database ID ----------|
    NOTION_DATABASE_ID=2e2030693c624c258bcc402ef8d4b357
    ```


### Edit Environment
`Auto-GPT/.env`
1. Add this plugin to whitelist. If you have other plugins enabled, append `AutoGPTNotion` to `ALLOWLISTED_PLUGINS`.
    ```
    ALLOWLISTED_PLUGINS=AutoGPTNotion
    ```
2. Add Notion token and database id.
    ```
    ################################################################################
    ### Notion
    ################################################################################

    NOTION_TOKEN=<Notion integration token>
    NOTION_DATABASE_ID=<Notion database id>
    ```

Run Auto-GPT and enjoy!


### FAQ
If you encounter problems or have any ideas, feel free to discuss:
- [Issues](https://github.com/doutv/Auto-GPT-Notion/issues)
- [Discord Channel](https://discord.com/channels/1092243196446249134/1098882305000472626)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Commands
- `notion_get_all_pages` Retrieves all pages properties from a database.
- `notion_retrieve_page` Retrieves a page's properties and content by id.
- `notion_create_page` Create a new Notion page.
- `notion_append_page` Append page content by id.
- `notion_update_page_properties` Update a page's properties by id.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contribution
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

### Run Tests
```
pytest -vs
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments
- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
- [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/doutv/Auto-GPT-Notion.svg?style=for-the-badge
[contributors-url]: https://github.com/doutv/Auto-GPT-Notion/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/doutv/Auto-GPT-Notion.svg?style=for-the-badge
[forks-url]: https://github.com/doutv/Auto-GPT-Notion/network/members
[stars-shield]: https://img.shields.io/github/stars/doutv/Auto-GPT-Notion.svg?style=for-the-badge
[stars-url]: https://github.com/doutv/Auto-GPT-Notion/stargazers
[issues-shield]: https://img.shields.io/github/issues/doutv/Auto-GPT-Notion.svg?style=for-the-badge
[issues-url]: https://github.com/doutv/Auto-GPT-Notion/issues
[license-shield]: https://img.shields.io/github/license/doutv/Auto-GPT-Notion.svg?style=for-the-badge
[license-url]: https://github.com/doutv/Auto-GPT-Notion/blob/master/LICENSE.txt
[discord-shield]: https://img.shields.io/badge/Discord-channel-brightgreen?style=for-the-badge
[discord-url]: https://discord.com/channels/1092243196446249134/1098882305000472626
