from flask import jsonify


def init_routes(app):
    @app.route('/')
    def index():
        return jsonify({'message': 'Hello, World!'})
