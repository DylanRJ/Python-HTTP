import requests

def get_request(url):
  r = requests.get(url)
  return r.url, r.status_code, int(r.headers['Content-Length'])
