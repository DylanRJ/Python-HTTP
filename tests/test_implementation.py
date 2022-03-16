import src.implementation as implementation

def test_implmentation():
  assert implementation.get_request('http://checkip.amazonaws.com/')["URL"] == 'http://checkip.amazonaws.com/'
  assert implementation.get_request('http://checkip.amazonaws.com/')["Status-code"] == 200
  assert implementation.get_request('http://checkip.amazonaws.com/')["Content-length"] == 15
