from flask import Flask , request , abort
import time 


app = Flask(__name__)
#import controller.user_controller as user_controller
#import controller.product_controller as product_controller
#from controller import user_controller , product_controller
from controller import *

@app.route('/')  # / shows homepage
def hello_world():
    return "<p>Hello , Abhishek  World! is great today </P>"

@app.route('/home')
def info():
    return "<h1> India that is BHARAT </h1>"

#dynamic URL
@app.route('/hello/<name>')
def hello(name):
    return "<h1> This is a webpage for {}</h1>".format(name)


if __name__ == "__main__":
    app.run(debug=True)  # when in production never use debug=True otherwise they can see the whole page instead of internal server error
    