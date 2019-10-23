Connections Protocol enabled Starter Kit
========================================

This starter kit uses the connection protocol to establish connections with
other agents. This starter kit can be used to connect directly to the Aries
Toolbox for experimentation and other purposes (see [the starters
readme](../README.md##connecting-directly-to-the-aries-toolbox) for more
details).

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
