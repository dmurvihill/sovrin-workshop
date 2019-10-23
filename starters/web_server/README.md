Web Server Style Starter Kit
============================

This starter kit starts a web server and listens for messages, asynchronously
processing them through registered handlers.

This starter kit will setup keys, taking the connected full agent's keys as
inputs and then send a trust ping, awaiting a reply, before starting up the web
server.

Requirements
------------

- Python 3.6 or higher

Quickstart
----------

Create and activate a python virtual environment:
```sh
$ python3 -m venv env
$ source env/bin/activate
```

Install requirements into the virtual environment:
```sh
$ pip install -r requirements.txt
```

Run the agent:
```sh
$ python my_agent.py --port 3001
```
