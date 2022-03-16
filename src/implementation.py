import requests

def get_request():
  r = requests.get('http://checkip.amazonaws.com/')
  return(r.url)