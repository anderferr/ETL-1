from src.drivers import http_requester

def test_request_from_page(requests_mock):
    url = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"
    response_context = "<h1>Hello, world!</h1>"
    requests_mock.get(url, status_code=200, text=response_context)
    
    http_request = http_requester.HttpRequester()
    request_response = http_request.request_from_page()
    
    assert "status_code" in request_response
    assert "html" in request_response
    assert request_response["status_code"]==200
    assert request_response["html"]==response_context
    print(request_response)
    