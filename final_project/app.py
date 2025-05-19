from flask import Flask, request, render_template
from translator import english_to_french

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        translated_text = english_to_french(text)
        return render_template('index.html', translated_text=translated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
