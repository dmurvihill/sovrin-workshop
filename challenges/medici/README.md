Medici Coding Challenge Checklist
==========================================

Basics and Setup
----------------

- [ ] Setup and run one of the agent starter kits.
- [ ] Connect your starter kit to one of your full agents.
- [ ] Successfully ping the full agent.

Tier 1 Goals
------------

- [ ] Programmatically pull down your agent's connection list.
- [ ] Programmatically pull down your agent's list of schemas or credential
	definitions (Use the toolbox to create schemas and credential definitions).

Tier 2 Goals
------------

- [ ] Programmatically list your credentials and the attributes attested in them
	(make sure your starter kit is connected to an agent that has credentials to
	list, i.e. your "Holder" agent).
- [ ] Programmatically list your credential definitions and the attributes each
	definition would attest.

Tier 3 Goals
------------

- [ ] Programmatically issue a credential to one of your connections.

Tier 4 Goals
------------

- [ ] Using the [connections protocol module](../protocols/connections.py) found
	in this repository, connect your starter kit directly to the toolbox and
	experiment with writing your own protocol.

Tier 5 Goals
------------

- [ ] Using your experimental protocol from tier 4, write a protocol handler for
	Aries Cloud Agent - Python that handles your protocol.
