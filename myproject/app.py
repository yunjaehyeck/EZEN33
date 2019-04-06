from flask import Flask

app = Flask(__name__)



@app.route('/move/<path>', method=['GET'])
def move():
    print('{}로 이동'.format(path))
    return render_template('{}.html'.format(path))

@app.route('/blood', methods=['POST'])
def blood():
    weight = request.form['weight']



if __name__ == '__main__':
    app.run()
