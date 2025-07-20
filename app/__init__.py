import os
from flask import Flask
from flask_socketio import SocketIO
from werkzeug.middleware.proxy_fix import ProxyFix
from .config import Config
from .routes import bp as routes_bp
from .socket_events import register_socketio_events
from .utils.logger import configure_logger

socketio = SocketIO(cors_allowed_origins=Config.CORS_ORIGINS, logger=True, engineio_logger=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    
    configure_logger()

    app.register_blueprint(routes_bp)
    socketio.init_app(app)

    register_socketio_events(app, socketio)

    return app
