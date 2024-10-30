from src.drivers import http_requester

def test_request_from_page():
    http_request = http_requester.HttpRequester()
    response = http_request.request_from_page()
    print(response)
# test_request_from_page()
# print("it works")
test_request_from_page()