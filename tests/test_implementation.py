from itsdangerous import json
import src.implementation as implementation

def test_implmentation():
  assert implementation.get_request() == 'http://checkip.amazonaws.com/'