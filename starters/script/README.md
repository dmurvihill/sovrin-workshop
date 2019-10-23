Script Style Starter Kit
========================

This starter kit operates like a script that could be automated to run as a cron
script, by a user at the command line, etc.

This starter kit will setup keys, taking the connected full agent's keys as
inputs and then send a trust ping, awaiting a reply.

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
$ python my_agent.py
```
