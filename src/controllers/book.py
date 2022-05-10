from collections.abc import MutableMapping
from flask import Flask
from flask_restplus  import api, Resource

from src.server.instance import server

app, apis = server.app, server.apis


books_db = [
    {"id":0, "title":"War and Peace"},
    {"id":1, "title":"Clean Code"}
]

@app.route('/books')
class BookList(Resource):

    def get(self, ):
        return books_db

    def post(self, ):
        response = apis.payload
        books_db.append(response)
        return response, 200