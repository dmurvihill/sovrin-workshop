"""IIW Demo"""
import argparse
import hashlib
import json
import os

from aiohttp import web

from aries_staticagent import (
    StaticConnection,
    crypto,
    utils,
)

from protocols.connections import Connections
from protocols.feature_discovery import FeatureDiscovery

# Config Start

def config():
    """ Get config """
    def environ_or_required(key):
        if os.environ.get(key):
            return {'default': os.environ.get(key)}
        return {'required': True}

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', **environ_or_required('PORT'))
    args = parser.parse_args()
    return args

def main():
    """ Main startup """
    args = config()

    connections = Connections(
        'http://localhost:{}'.format(args.port)
    )
    discovery = FeatureDiscovery()

    conn, invitation_url = connections.create_invitation()
    print('Invite:', invitation_url)

    conn.route_module(connections)
    conn.route_module(discovery)

    @conn.route('did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/basicmessage/1.0/message')
    async def basic_message_auto_responder(msg, conn):
        await conn.send_async({
            "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/"
                     "basicmessage/1.0/message",
            "~l10n": {"locale": "en"},
            "sent_time": utils.timestamp(),
            "content": "You said: {}".format(msg['content'])
        })


    async def handle(request):
        """aiohttp handle POST."""
        response = []
        with conn.reply_handler(response.append):
            await conn.handle(await request.read())

        if response:
            return web.Response(body=response.pop())

        raise web.HTTPAccepted()

    app = web.Application()
    app.add_routes([web.post('/', handle)])

    web.run_app(app, port=args.port)


if __name__ == '__main__':
    main()
