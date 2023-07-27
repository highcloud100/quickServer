from flask import Flask, jsonify, redirect, render_template, request, session, url_for

import openai
openai.api_key = "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"


def generateImage(description):
    """generate image"""
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
        )
    image_url = response['data'][0]['url']
    print(image_url)
    return image_url

def create_app():
    app = Flask(__name__)

    @app.route('/hi', methods=['GET', 'POST'])
    def hello():
        return jsonify({'name' : "baek", "data" : "hi there!"}), 200    
    
    @app.route('/')
    def home():
        return render_template('main.html')
    
    @app.route('/gen/<data>', methods=['GET'])
    def generateIMG(data):
        url = generateImage(data)
        return redirect(url)
        

    return app

