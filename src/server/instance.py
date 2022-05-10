from collections.abc import MutableMapping
from flask import Flask
from flask_restplus import api

class Server():

    def __init__(self, ):
        self.app = Flask(__name__)
        self.apis = api(self.app,
            version="1.0",
            title="Sample Book Api",
            description="A Simple book Api",
            doc = '/docs'
        )

    def run(self, ):
        self.app.run(
            debug=True
        )


server = Server()