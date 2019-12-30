from flask import Flask
from .route import router

app = Flask('Twitter Sentiment Analysist')
app.register_blueprint(router)
