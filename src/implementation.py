import requests

def get_request(url):
  r = requests.get(url)
  custom_dictionary = {"URL": r.url, "Status-code": r.status_code, "Content-length": int(r.headers['Content-Length'])}
  return custom_dictionary
