# REST API (CRUD DEVS)

This is my First API With Flask Framework


##ROUTES

# LIST ALL DEVS
@app.route('/devs', methods=['GET'])

# LIST DEV BY LANG
@app.route('/devs/<string:lang>', methods=['GET'])

# LIST DEV BY ID
@app.route('/devs/<int:id>', methods=['GET'])

# INSERT A NEW DEV
@app.route('/devs', methods=['POST'])

# UPDATE A DEV
@app.route('/devs/<int:id>', methods=['PUT'])

# DELETE A DEV
@app.route('/devs/<int:id>', methods=['DELETE'])


;)
