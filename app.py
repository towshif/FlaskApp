from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/data')
def data():
    import myplots as mp 
    return mp.data()

@app.route('/data2')
def data2():
    import myplots as mp 
    return mp.pd_data()


@app.route('/name/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()