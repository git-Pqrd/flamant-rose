from flask import Flask, render_template, url_for, request, Response, jsonify
from flask_api import status
import json
from flask_json import json_response, FlaskJSON, JsonTestResponse


app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config.Config')

#import models 

from flamantrose import models

#define response codes

@app.route('/')
def index():

  return "Welcome to flamant rose"

@app.route('/menus', methods=['GET'])
def get_menus():
  if request.method == 'GET':
    menus = models.Menu.query.all()

    results=[]

    for menu in menus:

      one_result = { 
        "id":menu.id,
        "name":menu.name, 
        "chosen_by": menu.chosen_by
      }
      
      results.append(one_result)

    count = len(results)

    return json_response(
      count = count, 
      results = results
    )

@app.route('/users', methods=['GET', 'POST'])
def get_users():
  if request.method == 'GET':
      users = models.Users.query.all()
      results=[]
      for user in users:
        one_result = { 
          "id":user.id,
          "name":user.name, 
          "email": user.email, 
          "choices": user.choices
        }
        results.append(one_result)
      count = len(results)
      return json_response(
        count = count, 
        results = results
      ), status.HTTP_302_FOUND

  if request.method == 'POST': 
      user_content = request.json
      models.db.session.add(models.Users(user_content["name"],user_content["mail"],user_content["password"],user_content["choices"]))
      models.db.session.commit()
            
      return json_response(
      Status = "SUCESS", 
      Message = "User successfully created "
    )
    
@app.route('/users/<int:userid>', methods=['GET'])

def get_user_by_id (userid): 

  user = models.Users.query.get(userid)

  return json_response(
    id = user.id, 
    name = user.name, 
    mail = user.email, 
    choices = user.choices 
    )

#if __name__ == "__main__":
  #  app.run()