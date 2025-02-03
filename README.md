<p align="left">
  <a href="https://github.com/Toktom/PamonhaWikiBot/" target="_blank">
    <img alt="Version" src="https://img.shields.io/badge/Version-0.1.0-brightgreen">
  </a>
  <a href="https://www.python.org/downloads/release/python-3124/" target="_blank">
    <img alt="Python version" src="https://img.shields.io/badge/Python-3.12.4-blue">
  </a>
</p>

# PamonhaWikiBot

## Overview

PamonhaWikiBot is a Python toolbox for bot-based editting, designed to interact with Runescape Wiki pages, specifically processing page templates, and other small tools. The bot uses the `pywikibot` library to connect to Runescape Wiki and perform various tasks.

## Features

- Download images from Runescape Wiki file pages.
- Pre-process Runescape Wiki pages and extract templates.
- Retrieve and manipulate template parameters.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/PamonhaWikiBot.git
    cd PamonhaWikiBot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Downloading Images

The <u>image_file_downloader.py</u> script downloads images from the wiki file pages and saves them to the "downloaded_images" directory.

1. Open the <u>image_file_downloader.py</u> script and modify the <u>fish</u> and <u>fish_english</u> lists with the desired fish names in Portuguese and English, respectively.
2. Run the script:
    ```sh
    python wikibot_scripts/examples/image_file_downloader.py
    ```

## Functions

- **connect_to_wiki**: Connects to the specified Wikipedia language site.
- **get_page**: Retrieves the content of a specified Wikipedia page.
- **page_preprocessing**: Pre-processes a Wikipedia page and returns a Wikicode object and a boolean indicating if the page exists.
- **get_page_templates**: Extracts templates from a Wikipedia page.
- **get_template_by_name**: Retrieves a template by its name.
- **get_template_parameter**: Extracts a parameter from a template.
- **get_file_page_url**: Retrieves the URL of a Wikipedia file page.
- **save_image**: Downloads and saves an image from a specified URL.
- **save_page**: Saves content to a specified Wikipedia page.


## TO-DO's

- [ ] Add an example on how to use the available tools to create a simple item page.
- [ ] Add tools for checking pages in different ways, i.e. categories, changes on the page, etc.
- [ ] Improve the current README.md file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Toktom** (
    **RS Wiki: PT-BR Admin**)