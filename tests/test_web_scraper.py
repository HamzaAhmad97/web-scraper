import pytest
from web_scraper import __version__, get_citations_needed_count


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize(
    "url, count",
    [
        ("https://en.wikipedia.org/wiki/Uncertainty_principle", 1),
        ("https://en.wikipedia.org/wiki/Albert_Einstein", 2),
        ("https://en.wikipedia.org/wiki/Quantum_mechanics",0),
    ],
)
def test_get_citations_needed_count(url, count):
    assert get_citations_needed_count(url) == count
