import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')
    CHAT_ROOMS = ['General', 'Anime', 'Movie', 'Sports']
