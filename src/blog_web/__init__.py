from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object('blog_web.config.Config')


    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/home')
    def home():
        return render_template('home.html')

    return app

