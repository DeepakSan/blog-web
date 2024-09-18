from flask import Flask, render_template
from .extensions import db  
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('blog_web.config.Config')

    db.init_app(app)  

    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)

    from .models import Count  


    @app.route('/index')
    def index():
        new_count = Count(count=0)
        db.session.add(new_count)
        db.session.commit()
        return render_template('index.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/home')
    def home():
        return render_template('home.html')

    return app
