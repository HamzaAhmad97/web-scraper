import requests
from bs4 import BeautifulSoup as BS

def get_citations_needed_count(URL):
    page = requests.get(URL)
    content = BS(page.content, "html.parser")
    citations = content.find_all( "span", string="citation needed")
    return len(citations)

def get_citations_needed_report(URL):
    page = requests.get(URL)
    content = BS(page.content, "html.parser")
    citations = content.find_all( "span", string="citation needed")
    report = "\n".join([span.parent.parent.parent.parent.text for span in citations])
    return report