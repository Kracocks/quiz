from flask import jsonify, abort, make_response, request, url_for
from .app import app
from .models import *

# get all questionnaires
@app.route('/quiz/api/v1.0/questionnaires', methods = ['GET'])
def get_questinnaires():
    quetionnaires = get_questionnaires_db()
    res = []
    for qaire in quetionnaires:
        res.append(qaire.to_json())
    return jsonify(res)

# get questionnaire with id
@app.route('/quiz/api/v1.0/questionnaires/<int:id>', methods = ['GET'])
def get_questinnaire(id):
    return get_questionnaire_db(id).to_json()

# get all questions from questionnaires
@app.route('/quiz/api/v1.0/questionnaires/<int:id_qaire>/questions', methods = ['GET'])
def get_questions_by_questionnaire(id_qaire):
    questions = get_questions_by_questionnaire_db(id_qaire)
    res = []
    for q in questions:
        res.append(q.to_json())
    return jsonify(res)

# get question with id from questionnaires
@app.route('/quiz/api/v1.0/questionnaires/<int:id_qaire>/questions/<int:id_q>', methods = ['GET'])
def get_question(id_qaire, id_q):
    question = get_question_db(id_q)
    return question.to_json()

# add questionnaire
@app.route('/quiz/api/v1.0/questionnaires', methods = ['POST'])
def create_questionnaire():
    if not request.json:
        abort(400)
    if 'nom' in request.json and type(request.json['nom']) is not str:
        abort(400)

    questionnaire = add_questionnaire_db(request.json['nom'])
    
    return questionnaire.to_json(), 201
    
# add question
@app.route('/quiz/api/v1.0/questionnaires/<int:id>/questions', methods = ['POST'])
def create_question(id):
    if not request.json:
        abort(400)
    if 'titre' in request.json and type(request.json['titre']) is not str:
        abort(400)
    if 'type' in request.json and type(request.json['type']) is not str:
        abort(400)
    
    question = add_question_db(request.json['titre'], request.json['type'], id)

    return question.to_json(), 201
    
# update questionnaire
@app.route('/quiz/api/v1.0/questionnaires/<int:id>', methods = ['PUT'])
def update_questionnaire(id):    
    if not request.json:
        abort(400)
    # Get the body
    if 'nom' in request.json and type(request.json['nom']) is not str:
        abort(400)
    
    update_questionnaire_db(id, request.json['nom'])

    return get_questionnaire_db(id).to_json()

# update question
@app.route('/quiz/api/v1.0/questionnaires/<int:id_qaire>/questions/<int:id_q>', methods=['PUT'])
def update_or_change_question(id_qaire, id_q):
    if not request.json:
        abort(400)

    # Changement de type de question
    if 'type' in request.json:
        if type(request.json['type']) is not str:
            abort(400)
        changed_question = change_type_question_bd(id_q, request.json['type'])
        return changed_question.to_json()

    # Mise à jour de la question
    if 'titre' in request.json and type(request.json['titre']) is not str:
        abort(400)

    titre = request.json['titre']

    kwargs = {}
    if 'proposition1' in request.json and type(request.json['proposition1']) is str:
        kwargs['proposition1'] = request.json['proposition1']
    if 'proposition2' in request.json and type(request.json['proposition2']) is str:
        kwargs['proposition2'] = request.json['proposition2']
    if 'reponse' in request.json:
        kwargs['reponse'] = request.json['reponse']

    update_question_db(id_q, titre, **kwargs)

    return get_question_db(id_q).to_json()
    
# delete questionnaire
@app.route('/quiz/api/v1.0/questionnaires/<int:id>', methods = ['DELETE'])
def delete_questionnaire(id):
    remove_questionnaire_db(id)
    return "True", 204

# delete question
@app.route('/quiz/api/v1.0/questionnaires/<int:id_qaire>/questions/<int:id_q>', methods = ['DELETE'])
def delete_question(id_qaire, id_q):
    remove_question_db(id_q)
    return "True", 204

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error':'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error) :
    return make_response(jsonify({'error':'Not found'}), 404)

@app.errorhandler(418)
def not_found(error) :
    return make_response(jsonify({'error':'I\'m not a teapot'}), 418)