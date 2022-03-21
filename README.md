# Setup

```sh
$ git clone https://github.com/DylanRJ/Python-HTTP.git
$ cd Python-HTTP
$ pip install -r requirements.txt
$ python3 src/implementation.py
```

# Tech Test

The task is to write a program that makes HTTP requests and reports on certain properties of the responses it receives back.

Please write your code in Java or Python (if you wish to use a different languages please check with us)

Your code should be sent to us as a zipped tar archive (.tar.gz file). We would like to see your version control commit history so please include .git or .svn directory structure in the tar archive.

Please provide instructions so that we can run your program and run your tests from the command line (Linux/Unix platform).

If we invite you for an interview we may ask you to present your work and to modify the program to meet an additional requirement or make improvements.

## Requirements

The program should be invoked from the command line.

It should read its input from stdin.

It should write its output to stdout.

The input format is a newline separated list of web addresses, such as:

```
http://www.bbc.co.uk/iplayer
http://checkip.amazonaws.com
https://www.bbc.co.uk/missing/thing
https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/220px-Juvenile_Ragdoll.jpg
https://site/mockito.org/
```

The program should make an HTTP GET request to each address in its input.

It should output the HTTP status code and the content length for each successful http response along with the URL requested.

The output should be formatted as a stream of short JSON documents such as:

```
{
“Url”: “http://www.bbc.co.uk/iplayer”,
“Status-code”: 301,
“Content-length”: 169
}

{
“Url”: “http://checkip.amazonaws.com”,
“Status-code”: 200,
“Content-length”: 169
}

etc.
```

You should include automated tests.

It should be possible to execute the tests while not connected to the internet.

## Assessment Criteria

We will assess your submission based on the following.

How well the program meets the requirements.

The structure and clarity of your program code.

The structure and clarity of your automated tests.

The quality of your instructions for running the program and running the tests.
