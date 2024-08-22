from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('template.html')

@app.route('/retirada', methods=['GET', 'POST'])
def retirada():
    return render_template('retirada.html')

@app.route('/ajuda', methods=['GET','POST'])
def ajuda():
    return render_template('ajuda.html')

@app.route('/investimentos', methods=['GET','POST'])
def investimentos():
    return render_template('investimentos.html')

@app.route('/depositos')
def depositos():
    return render_template('depositos.html')

if __name__ == '__main__':
    app.run(debug=True)
