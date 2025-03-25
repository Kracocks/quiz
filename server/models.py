from .app import db
from flask import request

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    uri = db.Column(db.String(255))
    
    def __init__(self, name:str):
        self.name = name
        self.uri = f'/quiz/api/v1.0/questionnaires/{self.id}'
    
    def __repr__(self):
        return "<Questionnaire (%d) %s>" % (self.id, self.name)

    def to_json(self):
        self.uri = f'/quiz/api/v1.0/questionnaires/{self.id}'
        json ={
            'id': self.id,
            'name': self.name,
            'uri' : request.host_url.rstrip('/') + self.uri,
            'questions': [question.to_json() for question in get_questions_by_questionnaire_db(self.id)]
        }
        return json
    
class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    uri = db.Column(db.String(255))
    type = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref=db.backref("questions"))
    
    __mapper_args__ = {
        "polymorphic_identity": "question",
        "polymorphic_on": type,
    }
    
    def __init__(self, title:str, questionnaire:Questionnaire, type:str):
        self.title = title
        self.type = type
        self.questionnaire_id = questionnaire.id
        self.questionnaire = questionnaire
        self.uri = f'/quiz/api/v1.0/questionnaires/{self.questionnaire_id}/questions/{self.id}'
        
    def __repr__(self):
        return "<Question (%d) %s>" % {self.id, self.title}
        
    def to_json(self):
        self.uri = f'/quiz/api/v1.0/questionnaires/{self.questionnaire_id}/questions/{self.id}'
        json = {
            'id': self.id,
            'title': self.title,
            'type': self.type,
            'uri' : request.host_url.rstrip('/') + self.uri
        }
        return json

class SimpleQuestion(Question):
    __tablename__ = "simple_question"

    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    simple_title = db.Column(db.String(120))
    simple_uri = db.Column(db.String(255))
    proposition1 = db.Column(db.String(255))
    proposition2 = db.Column(db.String(255))
    simple_reponse = db.Column(db.Boolean)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref=db.backref("simple_questions"))
    
    __mapper_args__ = {
        "polymorphic_identity": "simple_question",
    }
    
    def __init__(self, title:str, questionnaire:Questionnaire, proposition1:str, proposition2:str, reponse:bool):
        self.simple_title = title
        self.simple_uri = f'/quiz/api/v1.0/questionnaires/{self.questionnaire_id}/questions/{self.id}'
        self.proposition1 = proposition1
        self.proposition2 = proposition2
        self.simple_reponse = reponse
        self.questionnaire_id = questionnaire.id
        self.questionnaire = questionnaire
        
    def __repr__(self):
        return "<SimpleQuestion (%d) %s>" % {self.id, self.title}

    def to_json(self):
        self.simple_uri = f'/quiz/api/v1.0/questionnaires/{self.questionnaire_id}/questions/{self.id}'
        json = {
            'id': self.id,
            'title': self.simple_title,
            'proposition1': self.proposition1,
            'proposition2': self.proposition2,
            'reponse': self.simple_reponse,
            'uri': request.host_url.rstrip('/') + self.simple_uri
        }
        return json

class OpenQuestion(Question):
    __tablename__ = "open_question"

    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    open_title = db.Column(db.String(120))
    open_uri = db.Column(db.String(255))
    open_reponse = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref=db.backref("open_questions"))
    
    __mapper_args__ = {
        "polymorphic_identity": "open_question",
    }
    
    def __init__(self, title:str, questionnaire:Questionnaire, reponse:str):
        self.open_title = title
        self.open_uri = f'/quiz/api/v1.0/questionnaires/{self.questionnaire_id}/questions/{self.id}'
        self.open_reponse = reponse
        self.questionnaire_id = questionnaire.id
        self.questionnaire = questionnaire
        
    def __repr__(self):
        return "<OpenQuestion (%d) %s>" % {self.id, self.title}

    def to_json(self):
        self.open_uri = f'/quiz/api/v1.0/questionnaires/{self.questionnaire_id}/questions/{self.id}'
        json = {
            'id': self.id,
            'title': self.open_title,
            'reponse': self.open_reponse,
            'uri': request.host_url.rstrip('/') + self.open_uri
        }
        return json

# Getters
def get_questionnaires_db() -> list:
    return Questionnaire.query.all()

def get_questionnaire_db(id) -> Questionnaire | None:
    return Questionnaire.query.get_or_404(id)

def get_questions_by_questionnaire_db(id_qaire) -> list:
    return Question.query.join(Questionnaire).filter(Questionnaire.id == id_qaire).order_by(Questionnaire.name).all()

def get_question_db(id_q) -> Question | None:
    return Question.query.join(Questionnaire).filter(Question.id == id_q).first()

# Insert
def add_questionnaire_db(nom: str):
    new_questionnaire = Questionnaire(nom)
    db.session.add(new_questionnaire)
    db.session.commit()
    return new_questionnaire
    
def add_question_db(titre: str, type: str, id_qaire: int):
    questionnaire = get_questionnaire_db(id_qaire)
    if (type == "simple_question"):
        new_question = SimpleQuestion(titre, questionnaire, "", "", False)
        db.session.add(new_question)
    elif (type == "open_question"):
        new_question = OpenQuestion(titre, questionnaire, "")
        db.session.add(new_question)
    db.session.commit()
    return new_question
    
# Update
def update_questionnaire_db(id_qaire: int, new_nom: str):
    questionnaire:Questionnaire = get_questionnaire_db(id_qaire)
    questionnaire.name = new_nom
    db.session.commit()
    return questionnaire
    
def update_question_db(id_q: int, new_titre: str, **kwargs):
    question:Question = get_question_db(id_q)
    
    if isinstance(question, SimpleQuestion):
        question.simple_title = new_titre
        question.proposition1 = kwargs.get('proposition1', question.proposition1)
        question.proposition2 = kwargs.get('proposition2', question.proposition2)
        question.simple_reponse = kwargs.get('reponse', question.simple_reponse)
    elif isinstance(question, OpenQuestion):
        question.open_title = new_titre
        question.open_reponse = kwargs.get('reponse', question.open_reponse)
    db.session.commit()
    return question
    
def change_type_question_bd(id_q: int, new_type: str):
    old_q = get_question_db(id_q)
    
    questionnaire = old_q.questionnaire
    
    db.session.delete(old_q)
    db.session.commit()
    
    if new_type == "simple_question":
        new_question = SimpleQuestion(old_q.title, questionnaire, "", "", True)
    elif new_type == "open_question":
        new_question = OpenQuestion(old_q.title, questionnaire, "")
    
    db.session.add(new_question)
    db.session.commit()
    return new_question

# Delete
def remove_questionnaire_db(id_qaire: int):
    questionnaire= get_questionnaire_db(id_qaire)
    db.session.delete(questionnaire)
    db.session.commit()

def remove_question_db(id_q: int):
    question = get_question_db(id_q)
    db.session.delete(question)
    db.session.commit()