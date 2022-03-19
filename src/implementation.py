import requests

def get_request(url):
  r = requests.get(url)
  custom_dictionary = {"URL": r.url, "Status-code": r.status_code, "Content-length": int(r.headers['Content-Length'])}
  return custom_dictionary

def create_json(string):
  websites = string.splitlines()
  websites_array = []
  for item in websites:
    websites_array.append(item)
  return websites_array