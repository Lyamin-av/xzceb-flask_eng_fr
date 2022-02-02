from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishtext = english_to_french(textToTranslate)
    return englishtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchtext = french_to_english(textToTranslate)
    return frenchtext

@app.route("/")
def renderIndexPage():
    # Write the code to render template
     return render_template('index.html', title='Welcome')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
