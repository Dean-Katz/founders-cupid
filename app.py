from flask import Flask, render_template


app = Flask(__name__,template_folder='templates',static_folder='static')
app.debug = True


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=2500)