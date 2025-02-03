import requests

def save_image(file_name: str, page_url: str) -> None:
    """
    Saves an image from a given link to a file.

    Args:
        file_name (str): The name of the file to be saved.
        page_url (str): The url to the page where the image is located.
    
    Returns:
        None
    """
    image_file = open(file_name, 'wb')
    image_file.write(requests.get(page_url).content)
    image_file.close()
    return None
