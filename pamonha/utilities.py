import pywikibot as pwb
import mwparserfromhell as mw


def page_preprocessing(
    page: mw.wikicode.Wikicode, raw: bool = False
) -> tuple[mw.wikicode.Wikicode, bool]:
    """
    Pre-processes a page, returning a Wikicode object and a boolean value indicating if the page exists or not.

    Args:
        page (mw.wikicode.Wikicode): The page to be pre-processed.
        raw (bool, optional): If True, returns the raw page. Defaults to False.

    Returns:
        tuple[mw.wikicode.Wikicode, bool]: A tuple containing the pre-processed page and a boolean value indicating if the page exists or not.

    """
    wiki_ptbr = pwb.Site()
    extracted_page = pwb.Page(wiki_ptbr, page)
    page_existance = extracted_page.exists()

    if raw:
        return extracted_page, page_existance
    else:
        return mw.parse(extracted_page.get()), page_existance


def get_page_templates(
    page: mw.wikicode.Wikicode,
) -> list[mw.nodes.template.Template]:
    """
    Extracts the templates from a page.

    Args:
        pagina (mw.wikicode.Wikicode): The page to extract the templates from.

    Returns:
        list[mw.nodes.template.Template]: A list containing the extracted templates.
    """
    return page.filter_templates()


def get_template_by_name(
    templates: list[mw.nodes.template.Template], name: str
) -> mw.nodes.template.Template:
    """
    Gets a template by its name.

    Args:
        templates (list[mw.nodes.template.Template]): A list of templates.
        name (str): The name of the template to be retrieved.

    Returns:
        mw.nodes.template.Template: The desired template.
    """
    for template in templates:
        if templates.name.matches(name):
            return template


def get_templates_by_name(
    templates: list[mw.nodes.template.Template], name: str
) -> mw.nodes.template.Template:
    """
    Gets a template by its name.

    Args:
        templates (list[mw.nodes.template.Template]): A list of templates.
        name (str): The name of the template to be retrieved.

    Returns:
        mw.nodes.template.Template: The desired templates.
    """
    templates_list = [
        template
        for template in templates
        if template.name.matches(name)
    ]
    return templates_list


def get_template_parameter(
    template: mw.nodes.template.Template, parameter: str
) -> str:
    """
    Extracts a parameter from a template.

    Args:
        predefinicao (mw.nodes.template.Template): The template to extract the parameter from.
        parametros (list[str]): The parameter to be extracted.

    Returns:
        str: The extracted parameter.
    """
    return template.get(parameter).value if template.has(parameter) else None
