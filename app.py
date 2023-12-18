from flask import Flask, jsonify, request
from Hackaton import check_hate_speech, cur, conn

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    data = request.get_json()
    user_input = data.get('user_input')

    if user_input.lower() == 'exit':
        response = {"response": "Bye! See you next time."}
    else:
        is_hate, non_hateful_response = check_hate_speech(user_input)
        if is_hate:
            response = {
                "response": "This content is hateful.",
                "non_hateful_content": non_hateful_response if non_hateful_response else None
            }
        else:
            response = {"response": "This content is appropriate."}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
