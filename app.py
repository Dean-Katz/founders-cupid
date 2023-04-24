from flask import Flask, render_template


app = Flask(__name__,template_folder='templates',static_folder='static')
app.debug = True


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
   pass
@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
   pass

@app.route('/oppurtunites',methods=['GET','POST'])
def explore():
    pass










if __name__ == '__main__':
    app.run(port=2500)