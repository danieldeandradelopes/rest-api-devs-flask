from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

devs = [
    {"id": 1, "name": "Daniel Lopes", "lang": "Python"},
    {"id": 2, "name": " Pedro", "lang": "Java"},
    {"id": 3, "name": " João", "lang": "Java"},
    {"id": 4, "name": " Carlos", "lang": "Javascript"},
    {"id": 5, "name": " Milena", "lang": "Javascript"},
    {"id": 6, "name": " Sainara", "lang": "Python"},
]

# LIST ALL DEVS


@app.route('/devs', methods=['GET'])
def home():
    return jsonify(devs), 200

# LIST DEV BY LANG


@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200

# LIST DEV BY ID


@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200

    return jsonify({"error": "user not found"}), 404


# INSERT A NEW DEV
@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)

    return jsonify(data), 201

# UPDATE A DEV


@app.route('/devs/<int:id>', methods=['PUT'])
def update_dev(id):
    lang = request.get_json().get('lang')
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = lang

        return jsonify(dev), 201
    return jsonify({"error": "Dev is not found"}), 404


# DELETE A DEV
@app.route('/devs/<int:id>', methods=['DELETE'])
def delete_dev(id):
    index = id - 1
    del devs[index]

    return jsonify({"message": "Devs is deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
