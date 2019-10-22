Script Style Starter Kit
========================

This starter kit operates like a script that could be automated to run as a cron script, by a user at the command line,
etc.

This starter kit will setup keys, taking the connected full agent's keys as inputs and then send a trust ping, awaiting
a reply.

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

Connecting using the Aries Toolbox
----------------------------------

Static agents are generally statically connected to a "full" agent and serve a specific purpose in triggering actions in
the full agent. For agent's supporting `admin-static-connections`, the Aries Toolbox can be used to connect your static
agent to your full agent.

1. Open your toolbox and connect it to the agent you'd like your static agent to connect to.
2. Navigate to the "Static Connections" section.
3. Ensure you started your static agent and copy your DID and verification key (VK) to the form in the "Static
   Connections" section. Submit the form.
4. From the returned static connection info, copy the verification key of the full agent and paste into the input for
   your static agent. Copy the endpoint of the full agent and paste into the input for your static agent.

Your static agent and your full agent are now connected!
