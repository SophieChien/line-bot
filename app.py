# SDK :Software Development Kit
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('JTB+2l+kbknCNEEef1f6D06uhgkUFjCSr8B5mefy9x3C8YO2/XoYq+uyirBHGy/zDymnW288lhbKPXK5GzI/w/XHXUqESM9QJS4LAnAi8qIZ8GM/65QPb7kKV+UzDOpsLAUb4tD51HQVmJGVlePaxQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9eb6abeaf74b1a25444c668fb94fbda7')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = '窩聽不冬中穩'
    if msg in ['Hi', 'hi']:
        reply == 'Hello'
    elif msg == '你的名字':
        reply == '我是科基器人'
    elif msg in ['吃飽沒', '吃飯']:
        reply == '仙女不用吃飯'
    elif msg == 'good morning':
        reply == 'good morning'
    elif msg == 'good afternoon':
        reply == 'good afternoon'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = msg))


if __name__ == "__main__":
    app.run()