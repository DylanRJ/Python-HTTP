# Setup

```sh
$ git clone https://github.com/DylanRJ/Python-HTTP.git
$ cd Python-HTTP
$ pip install -r requirements.txt
$ python3 src/implementation.py
```

### Run tests with

```
$ pytest
```

## Reflections

- Learnt a lot about Python, the requests library, JSON, testing frameworks in Python and Mocking.
- Didn't strictly follow a TDD process at the beginning and ended up paying for it in the end. Thought instantly about the implementation code and didn't concentrate enough on testing which led to retrospectively trying to include tests which didn't work.
- Whilst the implementation code was easy enough to eek out, considerations about bad inputs for the request library i.e. anything not beginning with 'http://' are not included. Think more about potential edge case scenarios and how to account for them within the program.

## Actions

- Go back and reinforce understanding and commitment to a TDD approach for tech challenges such as this.
- Investigate Mocking and how it can be used in the instance of HTTP calls and other connection-dependent processes.
- Investigate environments, program structure and initialisation in Python.
