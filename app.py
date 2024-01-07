from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    names = request.args.get('names', '')
    quantity = request.args.get('quantity', '')
    return render_template('index.html', names=names, quantity=quantity)

@app.route('/result_list_name', methods=['POST'])
def result_list_name():
    if request.method == 'POST':
        names = request.form.get('names')
        names_list = names.split('\n')

        quantity = int(request.form.get('quantity'))
        if quantity > len(names_list):
            quantity = len(names_list)

        random_names = random.sample(names_list, quantity)
        return render_template('result_list_name.html', random_names=random_names)

if __name__ == '__main__':
    app.run(debug=True)
