#просто черновик, нигде не участвует


from flask import *
app = Flask(__name__)
@app.route('/') #app.add_url_rule('/', 'index', index)
def index():
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    return 'Feedback Page'
@app.route('/user/<id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)
if __name__ == "__main__":
    app.run()
