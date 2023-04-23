from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "label": "My first task", "done": False
    },
    {
        "label": "My second task", "done": False
    }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text

@app.route('/todos', methods=['GET'])
def returning_todos():
    json_todo = jsonify(todos)
    return json_todo

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print(f"The toDo in the position num {position}, has been deleted")
    todos.pop(position)
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)