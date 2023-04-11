from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST', 'GET'])
def handle_data():

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        # do something with the data
        response = {'success': True}
        return jsonify(response)
    else: 
        return "not allowed"
    

if __name__== "__main__":
    app.run(debug = True)
