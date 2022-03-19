import src.implementation as implementation
from unittest.mock import Mock
import requests
import requests_mock

#Tests

##Live implementation tests

# def test_live_get_request():
#   assert implementation.get_request('http://checkip.amazonaws.com/')["URL"] == 'http://checkip.amazonaws.com/'
#   assert implementation.get_request('http://checkip.amazonaws.com/')["Status-code"] == 200
#   assert implementation.get_request('http://checkip.amazonaws.com/')["Content-length"] == 15

##Mock implementation tests with unittest

# def test_mock_get_request(): 
#   get_request_mock = Mock()
#   get_request_mock.get_request.return_value = {"URL": 'http://google.com/', "Status-code": 200, "Content-length": 15}

#   assert get_request_mock.get_request()["URL"] == 'http://google.com/'

# def test_mock_create_json():
#   string = 'http://google.com/'

#   assert len(implementation.create_json(string)) == 1

##Mock implementation tests with requests_mock

with requests_mock.Mocker() as mock:
  mock.get('http://test.com/', headers={"Status-code": '200', "Content-length": '15'})
  resp = requests.get('http://test.com/')

  assert resp.url == 'http://test.com/'
  assert resp.headers['Status-code'] == '200'
  assert resp.headers['Content-length'] == '15'
