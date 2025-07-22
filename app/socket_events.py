from flask import request, session, current_app
from flask_socketio import emit, join_room, leave_room
from datetime import datetime
import random
import logging

logger = logging.getLogger(__name__)
logging.disable(logging.CRITICAL)

active_users = {}

def generate_guest_username():
    timestamp = datetime.now().strftime('%H%M')
    return f'Guest{timestamp}{random.randint(1000,9999)}'

def register_socketio_events(app, socketio):
    
    @socketio.event
    def connect():
        if 'username' not in session:
            session['username'] = generate_guest_username()

        active_users[request.sid] = {
            'username': session['username'],
            'connected_at': datetime.now().isoformat()
        }

        emit('active_users', {
            'users': [user['username'] for user in active_users.values()]
        }, broadcast=True)

        logger.info(f"User connected: {session['username']}")

    @socketio.event
    def disconnect():
        if request.sid in active_users:
            username = active_users[request.sid]['username']
            del active_users[request.sid]
            emit('active_users', {
                'users': [user['username'] for user in active_users.values()]
            }, broadcast=True)
            logger.info(f"User disconnected: {username}")

    @socketio.on('join')
    def on_join(data):
        username = session['username']
        room = data['room']

        if room not in current_app.config['CHAT_ROOMS']:
            logger.warning(f"Invalid room join attempt: {room}")
            return

        join_room(room)
        active_users[request.sid]['room'] = room

        emit('status', {
            'msg': f'{username} has joined the room.',
            'type': 'join',
            'timestamp': datetime.now().isoformat()
        }, room=room)

        logger.info(f"{username} joined {room}")

    @socketio.on('leave')
    def on_leave(data):
        username = session['username']
        room = data['room']
        leave_room(room)
        if request.sid in active_users:
            active_users[request.sid].pop('room', None)

        emit('status', {
            'msg': f'{username} has left the room.',
            'type': 'leave',
            'timestamp': datetime.now().isoformat()
        }, room=room)

        logger.info(f"{username} left {room}")

    @socketio.on('message')
    def handle_message(data):
        username = session['username']
        room = data.get('room', 'General')
        msg_type = data.get('type', 'message')
        message = data.get('msg', '').strip()
        timestamp = datetime.now().isoformat()

        if not message:
            return

        if msg_type == 'private':
            target_user = data.get('target')
            for sid, user_data in active_users.items():
                if user_data['username'] == target_user:
                    emit('private_message', {
                        'msg': message,
                        'from': username,
                        'to': target_user,
                        'timestamp': timestamp
                    }, room=sid)
                    logger.info(f"Private message: {username} -> {target_user}")
                    return
            logger.warning(f"Private message failed: user {target_user} not found")
        else:
            if room not in current_app.config['CHAT_ROOMS']:
                logger.warning(f"Message to invalid room: {room}")
                return

            emit('message', {
                'msg': message,
                'username': username,
                'room': room,
                'timestamp': timestamp
            }, room=room)

            logger.info(f"Message sent in {room} by {username}")
