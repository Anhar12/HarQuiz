from app import app
from extensions import db
from seed_questions import seed_data

with app.app_context():
    seed_data()
