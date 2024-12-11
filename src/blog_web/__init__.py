import os
import json
from flask import Flask, render_template, jsonify, redirect, session, url_for
from .extensions import db, migrate  
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth


def create_app():
    app = Flask(__name__)
    app.config.from_object('blog_web.config.Config')
    app.secret_key = app.config.get('API_KEY')


    db.init_app(app)  
    migrate.init_app(app, db)

    # the below not needed since i am using flask-migrate
    # with app.app_context():
    #     db.create_all()


    # from .models import Count  
    oauth = OAuth(app)

    oauth.register(
        "auth0",
        client_id=app.config.get("AUTH0_CLIENT_ID"),
        client_secret=app.config.get("AUTH0_CLIENT_SECRET"),
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=f'https://{app.config.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
    )


    @app.route("/login")
    def login():
        return oauth.auth0.authorize_redirect(
            redirect_uri=url_for("callback", _external=True)
        )

    @app.route("/callback", methods=["GET", "POST"])
    def callback():
        token = oauth.auth0.authorize_access_token()
        access_token = token["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        
        userinfo_url = f'https://{app.config.get("AUTH0_DOMAIN")}/userinfo'
        response = oauth.auth0.get(userinfo_url, headers=headers)
        userinfo = response.json()
        session["user"] = userinfo  
        email = userinfo.get("email")
        print(f"User email: {email}", flush=True) 
        print(token)
        # session["user"] = token
        return redirect("/home")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(
            "https://" + app.config.get("AUTH0_DOMAIN")
            + "/v2/logout?"
            + urlencode(
                {
                    "returnTo": url_for("index", _external=True),
                    "client_id": app.config.get("AUTH0_CLIENT_ID"),
                },
                quote_via=quote_plus,
            )
        )
    # @app.route("/")
    # def home():
    #     return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))


    @app.route('/home')
    def index():
        # new_count = Count(count=0)
        # db.session.add(new_count)
        # db.session.commit()
        return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

    @app.route('/contact')
    def contact():
        return render_template('contact.html',session=session.get('user'))

    # @app.route('/blogs')
    # def contact():
    #     return render_template('contact.html',session=session.get('user'))
    


    # @app.route('/home')
    # def home():
    #     return render_template('home.html',session=session.get('user'))

    return app
