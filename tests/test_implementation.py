import src.implementation as implementation
from unittest.mock import Mock

#Tests

##live implementation tests

def test_live_get_request():
  assert implementation.get_request('http://checkip.amazonaws.com/')["URL"] == 'http://checkip.amazonaws.com/'
  assert implementation.get_request('http://checkip.amazonaws.com/')["Status-code"] == 200
  assert implementation.get_request('http://checkip.amazonaws.com/')["Content-length"] == 15

##Mock implementation tests

def test_mock_get_request(): 
  implementation_mock = Mock()
  implementation_mock.get_request.return_value = {"URL": 'http://checkip.amazonaws.com/', "Status-code": 200, "Content-length": 15}

  assert implementation_mock.get_request()["URL"] == 'http://checkip.amazonaws.com/'
  