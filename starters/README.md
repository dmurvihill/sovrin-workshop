Starter Kits
============

This is a small collection of simple static agent "starter kits." Each starter
kit is oriented towards a specific use case and contains a small amount of code
to get you started with your static agent.

To use your static agent, you need to connect it to another agent. See the
instructions below.

Connecting to another agent
---------------------------

### Using the Aries Toolbox

For agent's supporting `admin-static-connections`, the Aries Toolbox can be used
to connect your static agent to a full agent.

1. Open your toolbox and open the agent to which you would like to connect your
   static agent.
2. Navigate to the "Static Connections" section.
3. Ensure you started your static agent (instructions can be found within each
   starter kit directory) and copy your DID and verification key (VK) to the
   form in the "Static Connections" section. Submit the form.
4. From the returned static connection info, copy the verification key of the
   full agent and paste into the input for your static agent. Copy the endpoint
   of the full agent and paste into the input for your static agent.

Your static agent and your full agent are now connected!

### Connecting directly to the Aries Toolbox

Connecting your static agent directly to the Aries Toolbox allows you to
experiment and explore the capabilities of both the toolbox and your agent. For
example, you can use the "Compose" section of the toolbox to construct and send
messages to your static agent to test out a new protocol programmed into your
static agent. Or, you could configure your static agent to support one of the
admin protocols the toolbox uses and interact with it through the use of the
toolbox UI.

To connect your static agent to the toolbox, your static agent must support a
subset of the connection protocol; it must implement at least the "inviter" role
and be able to maintain that one set of keys for the lifetime of its interaction
with the toolbox. Included in this repository is a [connection protocol
module](../protocols/connections.py) that provides this functionality. [A
starter kit](with_connections) that utilizes this module is included in this
collection to demonstrate its usage.
