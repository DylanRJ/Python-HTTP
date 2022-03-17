import src.implementation as implementation
from unittest.mock import Mock

#Tests

##Live implementation tests

# def test_live_get_request():
#   assert implementation.get_request('http://checkip.amazonaws.com/')["URL"] == 'http://checkip.amazonaws.com/'
#   assert implementation.get_request('http://checkip.amazonaws.com/')["Status-code"] == 200
#   assert implementation.get_request('http://checkip.amazonaws.com/')["Content-length"] == 15

##Mock implementation tests

def test_mock_get_request(): 
  get_request_mock = Mock()
  get_request_mock.get_request.return_value = {"URL": 'http://google.com/', "Status-code": 200, "Content-length": 15}

  assert get_request_mock.get_request()["URL"] == 'http://google.com/'

def test_mock_create_json():
  string = 'http://google.com/'

  assert len(implementation.create_json(string)) == 1