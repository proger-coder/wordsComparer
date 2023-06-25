import json

from flask import Flask, request, jsonify

from fonetika.distance import PhoneticsInnerLanguageDistance
from fonetika.soundex import RussianSoundex

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_words():
    data = request.get_json()

    given_word = data.get('given')
    answer_word = data.get('answer')

    soundex = RussianSoundex(delete_first_letter=True)
    phon_distance = PhoneticsInnerLanguageDistance(soundex)
    distance = phon_distance.distance(given_word, answer_word)

    response_data = {
        'given word': given_word,
        'answer word': answer_word,
        'distance': distance
    }

    response = app.response_class(
        response=json.dumps(response_data, sort_keys=False),
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)