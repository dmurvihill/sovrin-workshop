"""Web Server Starter Kit"""
import argparse
import json
import os

from aiohttp import web

from aries_staticagent import (
    StaticConnection,
    crypto,
    utils,
    Message
)


def config():
    """Get config."""
    def environ_or_required(key):
        if os.environ.get(key):
            return {'default': os.environ.get(key)}
        return {'required': True}

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', **environ_or_required('PORT'))
    parser.add_argument(
        '--replace-keys',
        action='store_true',
        dest='replace'
    )
    args = parser.parse_args()
    return args

def create_or_recall_keys(replace: bool = False):
    """Generate keys and save to .keys file."""
    if not os.path.exists('.keys') or replace:
        # Create keypair and write to file
        my_vk, my_sk = crypto.create_keypair()
        did = crypto.bytes_to_b58(my_vk[:16])

        print('DID:', did)
        print('VK:', crypto.bytes_to_b58(my_vk))
        their_vk = input('Their VK: ')
        endpoint = input('Their Endpoint: ')

        with open('.keys', 'w+') as key_file:
            json.dump({
                'did': did,
                'my_vk': crypto.bytes_to_b58(my_vk),
                'my_sk': crypto.bytes_to_b58(my_sk),
                'their_vk': their_vk,
                'endpoint': endpoint
            }, key_file)
    else:
        with open('.keys', 'r') as key_file:
            info = json.load(key_file)
            did = info['did']
            my_vk = info['my_vk']
            my_sk = info['my_sk']
            their_vk = info['their_vk']
            endpoint = info['endpoint']

    return did, my_vk, my_sk, their_vk, endpoint

def main():
    """Main."""
    args = config()
    _did, my_vk, my_sk, their_vk, endpoint = create_or_recall_keys(args.replace)

    conn = StaticConnection(my_vk, my_sk, their_vk, endpoint)

    ping = Message({
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/trust_ping/1.0/ping",
        "response_requested": True
    })
    print('Pinging connection:', ping.pretty_print())
    reply = conn.send_and_await_reply(
        ping,
        return_route='all',
        timeout=5
    )
    print('Response:', reply.pretty_print())

    @conn.route('did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/basicmessage/1.0/message')
    async def basic_message_auto_responder(msg, conn):
        """Automatically respond to basicmessages."""
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
