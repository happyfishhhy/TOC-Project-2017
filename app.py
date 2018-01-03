import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '523271669:AAGko0YjqKeniLCUiMBtW4jZTYkTBT3rNX4'
WEBHOOK_URL = 'https://08f6994f.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'helmet',
        'motogp',
        'clothes',
        'shockabsorber',
        'below2000',
        'from2000to8000',
        'above8000',
        'sol1',
        'sol2',
        'zeus1',
        'zeus2',
        'thh1',
        'thh2',
        'agv'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'helmet',
            'conditions': 'is_going_to_helmet'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'motogp',
            'conditions': 'is_going_to_motogp'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'clothes',
            'conditions': 'is_going_to_clothes'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'shockabsorber',
            'conditions': 'is_going_to_shockabsorber'
        },
        {
            'trigger': 'advance',
            'source': 'helmet',
            'dest': 'below2000',
            'conditions': 'is_going_to_below2000'
        },
        {
            'trigger': 'advance',
            'source': 'helmet',
            'dest': 'from2000to8000',
            'conditions': 'is_going_to_from2000to8000'
        },
        {
            'trigger': 'advance',
            'source': 'helmet',
            'dest': 'above8000',
            'conditions': 'is_going_to_above8000'
        },
        {
            'trigger': 'advance',
            'source': 'below2000',
            'dest': 'sol1',
            'conditions': 'is_going_to_sol1'
        },
        {
            'trigger': 'advance',
            'source': 'from2000to8000',
            'dest': 'sol2',
            'conditions': 'is_going_to_sol2'
        },
        {
            'trigger': 'advance',
            'source': 'below2000',
            'dest': 'zeus1',
            'conditions': 'is_going_to_zeus1'
        },
        {
            'trigger': 'advance',
            'source': 'from2000to8000',
            'dest': 'zeus2',
            'conditions': 'is_going_to_zeus2'
        },
        {
            'trigger': 'advance',
            'source': 'below2000',
            'dest': 'thh1',
            'conditions': 'is_going_to_thh1'
        },
        {
            'trigger': 'advance',
            'source': 'from2000to8000',
            'dest': 'thh2',
            'conditions': 'is_going_to_thh2'
        },
        {
            'trigger': 'advance',
            'source': 'above8000',
            'dest': 'agv',
            'conditions': 'is_going_to_agv'
        },
        {
            'trigger': 'go_back',
            'source': [
                'helmet',
                'motogp',
                'clothes',
                'shockabsorber',
                'below2000',
                'from2000to8000',
                'above8000',
                'helmetbrand1',
                'helmetbrand2',
                'helmetbrand3'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
