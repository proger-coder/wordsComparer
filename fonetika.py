from flask import Flask, request, make_response, jsonify, render_template
from fonetika.distance import PhoneticsInnerLanguageDistance
from fonetika.soundex import RussianSoundex

app = Flask(__name__)

def calculate_distance(given_word, answer_word):
    try:
        soundex = RussianSoundex(delete_first_letter=True)
        phon_distance = PhoneticsInnerLanguageDistance(soundex)
        return phon_distance.distance(given_word, answer_word)
    except Exception as e:
        print(f"An error occurred while calculating distance: {e}")
        return None


@app.route('/only_boolean', methods=['POST'])
def only_boolean():
    if not request.is_json:
        error_message = "No JSON found in request"
        print(error_message)
        return make_response(jsonify({'error': error_message}), 400)

    data = request.get_json()

    required_fields = ['given', 'answer', 'limit']
    missing_fields = [field for field in required_fields if field not in data]

    if not data or missing_fields:
        error_message = 'Missing data in request: ' + ', '.join(missing_fields)
        print(error_message)
        return make_response(jsonify({'error': error_message}), 400)

    given_word = data['given']
    answer_word = data['answer']
    limit = data['limit']
    distance = calculate_distance(given_word, answer_word)

    if distance is None:
        error_message = 'An error occurred while calculating distance'
        print(error_message)
        return make_response(jsonify({'error': error_message}), 500)

    response_data = {
        'match': distance <= limit
    }
    return make_response(jsonify(response_data), 200)


@app.route('/full_info', methods=['POST'])
def full_info():
    if not request.is_json:
        return make_response(jsonify({'error': 'No JSON found in request'}), 400)

    data = request.get_json()

    required_fields = ['given', 'answer']
    missing_fields = [field for field in required_fields if field not in data]

    if not data or missing_fields:
        error_message = 'Missing data in request: ' + ', '.join(missing_fields)
        print(error_message)
        return make_response(jsonify({'error': error_message}), 400)

    given_word = data['given']
    answer_word = data['answer']
    distance = calculate_distance(given_word, answer_word)

    if distance is None:
        error_message = 'An error occurred while calculating distance'
        print(error_message)
        return make_response(jsonify({'error': error_message}), 500)

    response_data = {
        'given_word': given_word,
        'answer_word': answer_word,
        'distance': distance
    }
    return make_response(jsonify(response_data), 200)


@app.route('/', methods=['GET'])
def get_root():
    return render_template('root.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33)
