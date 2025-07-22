from flask import Blueprint, render_template, session, current_app
from datetime import datetime
import random
import logging

bp = Blueprint('routes', __name__)
logger = logging.getLogger(__name__)

face_emojis = [
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐻‍❄️", "🐨",
    "🐯", "🦁", "🐮", "🐷", "🐽", "🐸", "🐵", "🙈", "🙉", "🙊",
    "🐒", "🐔", "🐧", "🐦", "🐤", "🐣", "🐥", "🦆", "🦅", "🦉",
    "🦇", "🐺", "🐗", "🐴", "🫎", "🫏", "🦄", "🐝", "🐛", "🦋",
    "🐌", "🐞", "🐜", "🪲", "🪳", "🪰", "🪱", "🐢", "🐍", "🦎",
    "🦖", "🦕", "🐙", "🦑", "🦐", "🦞", "🦀", "🐡", "🐠", "🐟",
    "🐬", "🐳", "🐋", "🦈", "🪸", "🐊", "🐆", "🐅", "🐃", "🐂",
    "🐄", "🦌", "🦬", "🐪", "🐫", "🦙", "🦒", "🐘", "🦣", "🦏",
    "🦛", "🐐", "🐏", "🐑", "🐎", "🐖", "🐓", "🦃", "🪽", "🕊️",
    "🦚", "🦜", "🦢", "🦩", "🦨", "🦡", "🦦", "🦥", "🐁", "🐀",
    "🦫", "🐿️", "🦔"
]


def generate_guest_username():
    timestamp = datetime.now().strftime('%H%M')
    return f'{random.choice(face_emojis)} Guest{timestamp}{random.randint(1,100)}'

@bp.route('/')
def index():
    if 'username' not in session:
        session['username'] = generate_guest_username()
        logger.info(f"New user session created: {session['username']}")
    
    return render_template(
        'index.html',
        username=session['username'],
        rooms=current_app.config['CHAT_ROOMS']
    )


@bp.route('/healthCheck')
def healthCheck():
    return {"state":"live"}
