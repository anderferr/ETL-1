from src.drivers import http_requester

def test_request_from_page():
    http_request = http_requester.HttpRequester()
    http_request.request_from_page()