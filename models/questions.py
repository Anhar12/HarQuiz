from extensions import db
    
class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('quiz_topics.id'), nullable=False)
    question_text = db.Column(db.Text, unique=False, nullable=False)
    options = db.relationship('QuestionOptions', backref='question', cascade="all, delete-orphan")