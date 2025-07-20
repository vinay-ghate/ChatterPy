from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(
        app,
        host='0.0.0.0',
        port=5000,
        # debug=app.config['DEBUG'],
        # use_reloader=app.config['DEBUG'],
        allow_unsafe_werkzeug=True
    )

# port = 5000
# debug = app.config['DEBUG']
