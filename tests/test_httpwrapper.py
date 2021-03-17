from gitsync.httpwrapper import HttpStatus, HttpClient, HttpResponse
import requests

def test_http_status():
    assert HttpStatus.OK.value == 200
    assert HttpStatus.NOT_FOUND.value == 404
    assert HttpStatus.ERROR.value == 500

def get_http_client():
    return HttpClient("https://api.github.com", 443, "/meta")

def test_http_client_init():
    client = get_http_client()
    assert client.base_url == "https://api.github.com"
    assert client.port == 443
    assert client.path == "/meta"
    assert client.url == client.base_url + ":" + str(client.port) + client.path

def test_http_client_get():
    client = get_http_client()
    response = client.get("")
    assert isinstance(response, HttpResponse)

def test_http_response():
    client = get_http_client()
    response = client.get("")
    assert isinstance(response.response, requests.Response)
    assert response.is_status_ok()
    assert response.length > 0
    assert isinstance(response.json, dict)
