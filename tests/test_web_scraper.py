import pytest
from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize(
    "url, count",
    [
        ("https://en.wikipedia.org/wiki/Leonhard_Euler", 0),
        ("https://en.wikipedia.org/wiki/Albert_Einstein", 2),
        ("https://en.wikipedia.org/wiki/Quantum_mechanics",0),
    ],
)
def test_get_citations_needed_count(url, count):
    """
    Test if the function get_citations_needed_count returns the correct number of occurances of the span with the string "citation needed" in the page with the provided URL.

    Args:
        url (str): The URL of the page to be scrapped.
        count (int): The number of occurances of a span with the string "citation needed"
    """
    assert get_citations_needed_count(url) == count

def test_get_citations_needed_report():
    """
    Test if the function get_citations_needed_report returns the correct report which is a string which is a combination of the paragraphs that contain the spans.
    """
    url = "https://en.wikipedia.org/wiki/Quantum_mechanics"
    expected  = ""
    actual = get_citations_needed_report(url)
    assert actual == expected