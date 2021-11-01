import requests
from bs4 import BeautifulSoup as BS

def get_citations_needed_count(URL):
    """
    A function that accepts a URL and then returns the number of occurances of spans that say "citation needed"

    Args:
        URL (str): The URL of the page to be scrapped.

    Returns:
        int: The number of occurances of the span with the string "citation needed"
    """
    page = requests.get(URL)
    content = BS(page.content, "html.parser")
    citations = content.find_all( "span", string="citation needed")
    return len(citations)

def get_citations_needed_report(URL):
    """
    A function that accpets a URL of a page and returns the paragraphs that contain spans that contain string "citation needed" 

    Args:
        URL (str): The URL of the page to be scrapped.

    Returns:
        str: A string containing the paragraphs that contain spans with the string "citation needed"
    """
    page = requests.get(URL)
    content = BS(page.content, "html.parser")
    citations = content.find_all( "span", string="citation needed")
    report = "\n".join([span.parent.parent.parent.parent.text for span in citations])
    return report