import click
from .app import app, db
from .models import Question, SimpleQuestion, OpenQuestion, Questionnaire

print(Question.__table__)
print(SimpleQuestion.__table__)
print(OpenQuestion.__table__)

@app.cli.command()
def loaddb():
    '''Creates the tables and populates them with data'''
    
    #Création de toute les tables
    db.create_all()
    
    # insertion des données
    qaire1 = Questionnaire('nom1')
    qaire2 = Questionnaire('nom2')
    qaire3 = Questionnaire('nom3')
    
    db.session.add(qaire1)
    db.session.add(qaire2)
    db.session.add(qaire3)
    db.session.flush()
    
    db.session.add(SimpleQuestion('titre1', qaire1, 'Vrai', 'Faux', True))
    db.session.add(SimpleQuestion('titre2', qaire2, 'Vrai', 'Faux', True))
    db.session.add(SimpleQuestion('titre3', qaire2, 'Vrai', 'Faux', True))
    
    db.session.add(OpenQuestion('titre4', qaire1, 'Une bonne réponse'))
    db.session.add(OpenQuestion('titre5', qaire3, 'Une autre bonne réponse'))
    db.session.add(OpenQuestion('titre6', qaire3, 'Une dernière bonne réponse'))
    
    db.session.commit()
    
@app.cli.command()
def syncdb():
    '''Create all missing tables'''
    db.create_all()
