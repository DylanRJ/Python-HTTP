import requests
import json

def get_request(url):
  r = requests.get(url)
  custom_dictionary = {"URL": r.url, "Status-code": r.status_code, "Content-length": int(r.headers['Content-Length'])}
  print(json.dumps(custom_dictionary, indent=2))

def create_json(string):
  websites = string.splitlines()
  for item in websites:
    get_request(item)

print("Type website URLs to get the JSON, finish your input with Ctrl-D:")
user_input = ''
while True:
  try:
    user_input += (input() + '\n')
  except EOFError:
    print("Results:")
    break

create_json(user_input)