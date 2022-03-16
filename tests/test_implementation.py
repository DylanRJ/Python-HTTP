import src.implementation as implementation

def test_implmentation():
  assert 'http://checkip.amazonaws.com/' in implementation.get_request('http://checkip.amazonaws.com/')
  assert 200 in implementation.get_request('http://checkip.amazonaws.com/')
  assert 15 in implementation.get_request('http://checkip.amazonaws.com/')
  