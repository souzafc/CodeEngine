from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Rota para processar a string
@app.route("/process", methods=["POST"])
def process_string():
    data = request.get_json()
    input_text = data.get("text", "")  # Obtém a string do JSON
    result = input_text + "abc"  # Adiciona "abc" à string
    
    response = {
        "original": input_text,
        "modified": result
    }
    print('acionado process')
    return jsonify(response)

# Rota para obter o nome modificado
@app.route("/get_name", methods=["GET"])
def get_name():
    name = request.args.get("name", "") 
    result = name + "_abc" 
    
    response = {
        "original": name,
        "modified": result
    }
    print('acionado get')
    return jsonify(response)

# Rota padrão
@app.route("/")
def hello_world():
    print('acionado raiz')
    return jsonify({"message": "Hello World", "status": 200})

# Obtém a porta do ambiente
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    print('init')
    app.run(host='0.0.0.0', port=int(port))
