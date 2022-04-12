from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    to_french = translator.english_to_french(text_to_translate)
    translation = to_french['translations'][0]['translation']
    return translation

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    to_english = translator.french_to_english(text_to_translate)
    translation = to_english['translations'][0]['translation']
    return translation

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
