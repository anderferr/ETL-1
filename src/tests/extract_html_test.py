from src.tests.tests.http_requester import HttpRequesterSpy
from src.tests.tests.html_collector import HtmlCollectorSpy
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.extract.extract_html import ExtractHtml
from src.errors.extract_error import ExtractError



def test_extract():
    http_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    print(response)

    assert isinstance(response, ExtractContract)
    """Will garantee request_from_page will always be called"""
    assert http_requester.request_from_page_count == 1
    assert "html" in html_collector.collect_essential_information_attributes

def tests_extract_error():
    http_requester = "Will return an error"
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        extract_html.extract()
    except Exception as exception: #pylint: disable=broad-except
        assert isinstance(exception, ExtractError)