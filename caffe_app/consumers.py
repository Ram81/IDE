from channels import Group # noqa: ignore=F405
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    print('connection being established...')
    message.reply_channel.send({
        "accept": True
    })


@channel_session_user
def ws_disconnect(message):
    print('disconnected...')
    pass


@channel_session_user
def ws_receive(message):
    print('message received...')
    print(message)
    message.reply_channel.send({
        "accept": True,
        "text": 'ola'
    })
