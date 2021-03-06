from flask import Flask, request

from src.errors import Error
from src.models.bots.bot import Bot
import src.common.constants as Constants

app = Flask(__name__)

@app.route("/bot_call", methods=['POST'])
def get_channel_info():
    if request.method == 'POST':
        try:
            text = request.form['text']
            channel = request.form['channel_id']
            user_id = request.form['user_id']
            user = request.form['user_name']
        except:
            raise Error.ParameterError("Parameters are not correct")
        try:
            Bot(channel_id=channel, reply_user_id=user_id, reply_user_name=user).query_wit(text=text)
        except:
            raise Error.MessageError("Message is incorrect")
        return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)