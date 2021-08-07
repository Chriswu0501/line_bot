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

line_bot_api = LineBotApi('JGLVAi4cxnBtfYZCkyDe1EPFYHkemY9IWvTTp5UgBRPqSVVnKikHAUkmfXQxJ3ZTQRuPDi0dLjMMzFFgvp/ZMo5Dk3LSjpsUxtPlu4i9O1g4je6FmGdr7BQTBVl0MGA5gHQ9uSZtc0UrDZzG7wyK5QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('05306c1db5774ed416b68e8d5306d1df')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
