#simple flask program
from flask import Flask  #imports flask
app=Flask(__name__) #instatiates flask class

@app.route('/') #tells flask which url to trigger function
def hello_world(): #the function to be trigered
  return "Hello World!"  #returns the message to be displayed