Medici Coding Challenge Checklist
=================================

### Basics and Setup

- [x] Setup and run one of the agent starter kits.
- [x] Connect your starter kit to one of your full agents.
- [x] Successfully ping the full agent.

### Tier 1 Goals

- [x] Programmatically pull down your agent's connection list.
- [ ] Programmatically pull down your agent's list of schemas or credential
	definitions (Use the toolbox to create schemas and credential definitions).

### Tier 2 Goals

- [ ] Programmatically list your credentials and the attributes attested in them
	(make sure your starter kit is connected to an agent that has credentials to
	list, i.e. your "Holder" agent).
- [ ] Programmatically list your credential definitions and the attributes each
	definition would attest.

### Tier 3 Goals

- [ ] Programmatically issue a credential to one of your connections.

### Tier 4 Goals

- [ ] Using the [connections protocol module](../../protocols/connections.py) or
	[connection protocol enabled starter kit](../../starters/with_connections)
	found in this repository, connect your starter kit directly to the toolbox
	and experiment with writing your own protocol.

### Tier 5 Goals

- [ ] Using your experimental protocol from tier 4, write a protocol handler for
	Aries Cloud Agent - Python that handles your protocol.

Tips, Tricks, and Hints
-----------------------

### What's going on?
As a reminder, the toolbox is not the issuer or holder of credentials. Rather,
the toolbox "puppet strings" your Company and Holder agents, providing a UI to
trigger actions in either agent.

For this coding challenge, we're using a static agent to fill the same role of
puppet stringing your company and holder agents but this time automating some of
the tasks with code.

### Starter Kits
[A collection of starter kits](../../starters) is provided in this repository as
a solid starting point for completing the tasks on this checklist.

- ["Script" style starter kit](../../starters/script) - This is the simplest
	starter kit; it is intended to be used like a script and can potentially be
	used by cron jobs or easily adapted to fit into a wider system.
- ["Web Server" style starter kit](../../starters/web_server) - This is a
	starter kit that starts and listens on a web server (using
	[aiohttp](https://docs.aiohttp.org/en/stable/index.html)). Using this web
	server, you could create a simple web page that triggers sending of messages
	to your agent, create simplified HTTP API for issuing a credential, etc.
- [Connection protocol enabled starter kit](../../starters/with_connections) -
	This starter kit can be used to connect your static agent directly to the
	Aries Toolbox (rather than to your Aries Cloud Agent). This is most useful
	for Tier 4 and 5 goals, allowing you to experiment with creating your own
	protocol and crafting messages in the toolbox to test that protocol.

### Connecting to your static agent
Instructions for connecting your static agent can be found in the [starter kits
README](../../starters).

### Message Cheatsheet
You accomplish nearly all of the above goals by sending messages to your agents.
A [cheatsheet](../../guides/Issue_Credential_Admin_Message_Cheatsheet.md) has
been provided for the format and schema of those messages.

If you want to explore more functionality beyond what is shown in the cheat
sheet, you can use the "Message History" tab of the toolbox to examine how the
toolbox performs that other functionality.
