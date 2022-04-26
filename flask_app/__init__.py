from flask import Flask

app = Flask(__name__)

app.secret_key = "BLEH"
DB = 'selena_schema'

from flask_app.controllers import controller
