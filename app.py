from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'

def get_chat_response(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    if len(response.choices) > 0:
        return response.choices[0].text.strip()
    else:
        raise Exception("Modelden yanıt alınamadı.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    question = request.form['question']
    try:
        response = get_chat_response(question)
        return response
    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
