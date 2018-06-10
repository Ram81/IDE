import json
import yaml
from channels import Group # noqa: ignore=F405
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    print('connection being established...')
    Group("modelSharing").add(message.reply_channel)
    message.reply_channel.send({
        "accept": True
    })


@channel_session_user
def ws_disconnect(message):
    Group("modelSharing").discard(message.reply_channel)
    print('disconnected...')


@channel_session_user
def ws_receive(message):
    print('message received...')
    data = yaml.safe_load(message["text"])
    networkId = int(data['networkId'])
    net = data['net']
    message.reply_channel.send({
        "text": json.dumps({
            "net": net,
            "networkId": networkId
        })
    })
