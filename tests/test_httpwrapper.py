from gitsync.httpwrapper import HttpStatus, HttpClient, HttpResponse
import requests


def test_when_http_status_value_then_get_its_valid_value():
    assert HttpStatus.OK.value == 200
    assert HttpStatus.NOT_FOUND.value == 404
    assert HttpStatus.ERROR.value == 500


def test_given_httpclient_when_init_then_instance_is_set():
    client = _get_http_client()
    assert client.base_url == "https://api.github.com"
    assert client.port == 443
    assert client.path == "/meta"
    assert client.url == client.base_url + ":" + str(client.port) + client.path


def _get_http_client():
    return HttpClient("https://api.github.com", 443, "/meta")


def test_given_empty_url_when_get_then_get_response_from_base_url():
    client = _get_http_client()
    response = client.get("")
    assert isinstance(response, HttpResponse)


def test_given_httpresponse_when_get_successful_then_contains_data():
    client = _get_http_client()
    response = client.get("")
    assert isinstance(response.response, requests.Response)
    assert response.is_status_ok()
    assert response.length > 0
    assert isinstance(response.json, dict)


def test_given_httpresponse_when_get_null_then_json_is_empty():
    client = HttpClient("https://github.com", 443, "")
    response = client.get("/null")
    assert response.json == {}


def test_given_httpresponse_when_get_unknown_resource_then_not_status_ok():
    client = _get_http_client()
    response = client.get("/not_found")
    assert not response.is_status_ok()
