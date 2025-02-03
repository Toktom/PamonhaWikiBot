from .pamonha import (
    page_preprocessing,
    get_page_templates,
    get_template_by_name,
    get_templates_by_name,
    connect_to_wiki,
    get_page,
    get_template_parameter,
    save_page,
    get_file_page_url
)
from .utils import save_image

__all__ = [
    "page_preprocessing",
    "get_page_templates",
    "get_template_by_name",
    "get_templates_by_name",
    "get_page",
    "get_template_parameter",
    "connect_to_wiki",
    "save_page",
    "save_image",
    "get_file_page_url"
]


__author__ = "Michael Markus Ackermann"
__version__ = "0.1.0"
__license__ = "MIT"
__status__ = "Development"
