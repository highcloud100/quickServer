from flask import Flask, jsonify, redirect, render_template, request, session, url_for


def create_app():
    app = Flask(__name__)

    @app.route('/hi', methods=['POST'])
    def hello():
        return jsonify({'reply' : "welcome"}), 200
    
    @app.route('/')
    def home():
        return render_template('main.html')
    
    return app

