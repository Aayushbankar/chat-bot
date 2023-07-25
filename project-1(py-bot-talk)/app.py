from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = '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'
openai.api_key = api_key
engine = 'text-davinci-003'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    response = openai.Completion.create(
        engine=engine,
        prompt=user_input,
        max_tokens=100  # Adjust as needed
    )
    bot_response = response['choices'][0]['text'].strip()
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
