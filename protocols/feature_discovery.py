from aries_staticagent import (
    StaticConnection,
    Module,
    route,
    crypto,
    Message
)


class FeatureDiscovery(Module):
    """ Module for Feature Discovery Protocol """
    DOC_URI = 'did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/'
    PROTOCOL = 'discover-features'
    VERSION = '1.0'

    @route
    async def query(self, msg, conn):
        """Handle query message."""
        print(msg.pretty_print())
        results = set()
        for type_, _handler in conn._dispatcher.handlers.items():
            results.add('{}{}/{}'.format(
                type_.doc_uri, type_.protocol, type_.version
            ))
        await conn.send_async({
            '@type': self.type('disclose'),
            'protocols': [{'pid': protocol} for protocol in results]
        })
