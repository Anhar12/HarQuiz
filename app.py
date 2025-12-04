from flask import Flask, render_template, request, jsonify, session, redirect
from flask_login import current_user, LoginManager, login_user, logout_user, login_required
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, case
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from extensions import db
from models import *
import random
import requests
import urllib.parse
import os
import re

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

parsed_url = urllib.parse.urlparse(DATABASE_URL)
users = parsed_url.username
password = parsed_url.password
host = parsed_url.hostname
port = parsed_url.port
dbname = parsed_url.path[1:]

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{users}:{password}@{host}:{port}/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager.session_protection = "strong"
login_manager.login_view = "/"
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(minutes=30)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city")

    if not city:
        return jsonify({"error": "Nama kota wajib diisi!"}), 400

    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=no&alerts=no"
        res = requests.get(url).json()

        if "error" in res:
            return jsonify({"error": res["error"]["message"]}), 400

        forecast_data = []
        for item in res["forecast"]["forecastday"]:
            date_obj = datetime.strptime(item["date"], "%Y-%m-%d")
            forecast_data.append({
                "date": item["date"],
                "day_name": date_obj.strftime("%A"),
                "temp_day": item["day"]["maxtemp_c"],
                "temp_night": item["day"]["mintemp_c"],
                "condition": item["day"]["condition"]["text"]
            })

        return jsonify({
            "city": city,
            "forecast": forecast_data
        }), 200

    except Exception as e:
        return jsonify({"error": "Terjadi kesalahan ketika mengambil data cuaca."}), 500

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not username or not password or not confirm_password:
        return jsonify({'error': 'Semua field harus diisi!'}), 400

    if " " in username:
        return jsonify({'error': 'Username tidak boleh mengandung spasi!'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Password dan konfirmasi tidak sama!'}), 400

    if Users.query.filter_by(username=username).first():
        return jsonify({'error': 'Username sudah digunakan!'}), 400

    if not re.search(r"[a-z]", password):
        return jsonify({'error': 'Password harus mengandung huruf kecil, huruf besar, angka, dan simbol!'}), 400
    if not re.search(r"[A-Z]", password):
        return jsonify({'error': 'Password harus mengandung huruf kecil, huruf besar, angka, dan simbol!'}), 400
    if not re.search(r"\d", password):
        return jsonify({'error': 'Password harus mengandung huruf kecil, huruf besar, angka, dan simbol!'}), 400
    if not re.search(r"[^\w]", password):
        return jsonify({'error': 'Password harus mengandung huruf kecil, huruf besar, angka, dan simbol!'}), 400

    new_user = Users(
        username=username,
        password_hash=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registrasi berhasil!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username dan password wajib diisi!'}), 400

    user = Users.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Username atau password salah!'}), 401

    login_user(user)
    session['total_score'] = user.total_score or 0

    return jsonify({
        'message': 'Login berhasil!',
        'user': {
            'id': user.id,
            'username': user.username
        }
    }), 200

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route("/quiz", methods=["GET"])
@login_required
def quiz():
    question = Questions.query.order_by(db.func.random()).first()

    if not question:
        return "Belum ada data pertanyaan", 500

    options = [
        {
            "id": opt.id,
            "text": opt.option_text
        }
        for opt in question.options
    ]

    random.shuffle(options)

    quiz_data = {
        "id": question.id,
        "question": question.question_text,
        "topic": question.topic.name,
        "options": options
    }

    return render_template("quiz.html", quiz=quiz_data)

@app.route("/quiz/check", methods=["POST"])
@login_required
def check_answer():
    selected_option_id = request.form.get("answer")
    question_id = request.form.get("question_id")

    if not selected_option_id or not question_id:
        return jsonify({"success": False, "message": "Tidak ada jawaban."})

    option = QuestionOptions.query.filter_by(id=selected_option_id).first()
    if not option:
        return jsonify({"success": False, "message": "Jawaban tidak valid."})

    is_correct = option.is_correct

    attempt = AnswerAttempts(
        user_id=current_user.id,
        question_id=question_id,
        is_correct=is_correct
    )
    db.session.add(attempt)

    if is_correct:
        user = current_user
        user.total_score = (user.total_score or 0) + 10
        db.session.add(user)
        session['total_score'] = current_user.total_score

    db.session.commit()

    return jsonify({
        "success": True,
        "correct": is_correct,
        "message": "Benar!" if is_correct else "Salah."
    })


@app.route("/leaderboard")
def leaderboard():
    page = request.args.get("page", 1, type=int)
    per_page = 20
    offset_data = (page - 1) * per_page

    score_case = case(
        (AnswerAttempts.is_correct == True, 10),
        else_=0
    )

    total_users = db.session.query(func.count(Users.id)).scalar()
    total_pages = (total_users + per_page - 1) // per_page

    results = (
        db.session.query(
            Users.username,
            func.sum(score_case).label("score"),
            func.count(AnswerAttempts.id).label("attempts")
        )
        .join(AnswerAttempts, Users.id == AnswerAttempts.user_id)
        .group_by(Users.id)
        .order_by(func.sum(score_case).desc())
        .limit(per_page)
        .offset(offset_data)
        .all()
    )

    leaderboard_data = [
        {
            "username": r.username,
            "score": r.score or 0,
            "attempts": r.attempts
        }
        for r in results
    ]

    return render_template(
        "leaderboard.html",
        leaderboard=leaderboard_data,
        current_page=page,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=True)
