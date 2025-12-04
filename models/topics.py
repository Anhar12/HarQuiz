from extensions import db

class QuizTopics(db.Model):
    __tablename__ = 'quiz_topics'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    questions = db.relationship('Questions', backref='topic', cascade="all, delete-orphan")