from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)   # ✅ Important

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(200))



@app.route("/user", methods=["POST"])
def create_user():
    try:
        data = request.form

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        password = data.get("password")

        if not all([name, email, phone, password]):
            return redirect(url_for("create_user_form", error="All fields are required"))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return redirect(url_for("create_user_form", error="Email already exists"))
        hashed_password = generate_password_hash(password)

        user = User(name=name, email=email, phone=phone, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("thank_you", name=user.name))
    except IntegrityError:
        db.session.rollback()   # 🔥 VERY IMPORTANT
        return redirect(url_for("create_user_form", error="Validation error"))

    except Exception as e:
        db.session.rollback()
        return redirect(url_for("create_user_form", error="Something went wrong"))
@app.route("/register", methods=["GET"])
def create_user_form():
    error = request.args.get("error")
    return render_template("create_user.html", error=error)

@app.route("/thank-you", methods=["GET"])
def thank_you():
    name = request.args.get("name")
    return render_template("thank_you.html", name=name)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("admin"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
@app.route("/")
def home():
    return render_template("home.html", user=current_user)
@app.route("/reading")
def reading():
    aikey="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";
    return render_template("reading.html", user=current_user, aikey=aikey)
@app.route("/cards")
def cards():
    return render_template("cards.html", user=current_user)
@app.route("/guidance")
def guidance():
    return render_template("guidance.html", user=current_user)
if __name__ == "__main__":
    app.run(debug=True)

