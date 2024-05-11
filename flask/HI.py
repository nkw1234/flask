from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

@app.route('/<user>')
def hi(user):
    return render_template('index.html', name=user)

app.run(debug=True)