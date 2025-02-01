import pywikibot as pwb
import mwparserfromhell as mw


def connect_to_wiki(lang="pt-br") -> pwb.Site:
    """
    Connects to the Portuguese Wikipedia.

    Returns:
        pwb.Site: The Portuguese Wikipedia site.
    """
    if lang == "pt-br":
        return pwb.Site("pt-br", fam="rsw")
    elif lang == "en-gb" or lang == "en":
        return pwb.Site("en-gb", fam="rsw")
    else:
        raise NotImplementedError("Only pt-br is supported.")


def get_page_content(wiki_site: pwb.Site, page: str) -> str:
    """
    Gets the content of a page.

    Args:
        page (str): The page to get the content from.

    Returns:
        str: The content of the page.
    """
    return pwb.Page(wiki_site, page)


def page_preprocessing(
    page: mw.wikicode.Wikicode, raw_page: bool = False, lang: str = "pt-br"
) -> tuple[mw.wikicode.Wikicode, bool]:
    """
    Pre-processes a page, returning a Wikicode object and a boolean value indicating if the page exists or not.

    Args:
        page (mw.wikicode.Wikicode): The page to be pre-processed.
        raw_page (bool, optional): If True, returns the raw page. Defaults to False.

    Returns:
        tuple[mw.wikicode.Wikicode, bool]: A tuple containing the pre-processed page and a boolean value indicating if the page exists or not.

    """
    wiki_ptbr = connect_to_wiki(lang)
    extracted_page = get_page_content(wiki_ptbr, page)
    page_existance = extracted_page.exists()

    if raw_page:
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
    template_list: list[mw.nodes.template.Template], template_name: str
) -> mw.nodes.template.Template:
    """
    Gets a template by its name.

    Args:
        templates (list[mw.nodes.template.Template]): A list of templates.
        name (str): The name of the template to be retrieved.

    Returns:
        mw.nodes.template.Template: The desired template.
    """
    for template in template_list:
        if template.name.matches(template_name):
            return template
    return None


def get_templates_by_name(
    templates: list[mw.nodes.template.Template], template_name: str
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
        template for template in templates if template.name.matches(template_name)
    ]
    return templates_list


def get_template_parameter(
    template: mw.nodes.template.Template, parameter_name: str
) -> str:
    """
    Extracts a parameter from a template.

    Args:
        predefinicao (mw.nodes.template.Template): The template to extract the parameter from.
        parametros (list[str]): The parameter to be extracted.

    Returns:
        str: The extracted parameter.
    """
    return template.get(parameter_name).value if template.has(parameter_name) else None
