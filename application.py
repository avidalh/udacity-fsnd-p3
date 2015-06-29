

from flask import Flask, render_template, request, redirect, jsonify, url_for,\
flash, json

DEBUG = True

app = Flask(__name__)

# import populate

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Categories, Items

from flask import session as login_session
import random, string


# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
from flask import make_response
import requests

import time

from BeautifulSoup import BeautifulStoneSoup
import dicttoxml

# Log to strderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)


engine = create_engine('postgresql:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# print "populating the DB..."
# populate.populate()


# Home page:
# Show latest added categories and items.
@app.route('/')
@app.route('/itemCatalog/')
def showItems():

    latestCategories = session.query(Categories).order_by(Categories.id.\
        desc()).limit(5).all()
    latestItems = session.query(Items).order_by(Items.id.desc()).limit(7).\
        all()
    
    for item in latestItems:
        item.category = getCategoryInfo(item.category_id)
    
    return render_template('home.html', latestCategories=latestCategories,
                           latestItems=latestItems)


# Show categories
@app.route('/itemCatalog/categories/', methods=['GET','POST'])
def showCategories():
    
    # return "This page will be for showing all categories"
    
    categories = session.query(Categories).order_by(Categories.id.asc()).\
        all()
    for category in categories:
        category.empty = isCategoryEmpty(category.id)
        category.creator = session.query(Users).filter_by(id=category.user_id).one()

    return render_template('showCategories.html', categories=categories)

# JSON 
@app.route('/itemCatalog/categories/endPoint/<endPoint>/')
def showCategoriesEndPoint(endPoint='XML'):
    categories = session.query(Categories).order_by(Categories.id.asc()).\
        all()
        
    # return jsonify(Categories=[c.serialize for c in categories])

    serial_data = {'Categories': [c.serialize for c in categories]}
    
    if endPoint == 'JSON':
        JSON_data = json.dumps(serial_data, indent=4)
        endPoint_type = "JSON endpoint data"
        return render_template('endPoint.html', 
                               endPoint_type=endPoint_type,
                               endPointData=JSON_data)

    if endPoint == 'XML':
        xml_string = BeautifulStoneSoup(dicttoxml.dicttoxml(serial_data)).prettify()
        endPoint_type = "XML endpoint data"
        return render_template('endPoint.html',
                               endPoint_type=endPoint_type,
                               endPointData=xml_string)


# Create a new category
@app.route('/itemCatalog/category/new/', methods=['GET','POST'])
def newCategory():

    if 'username' not in login_session:
        return redirect('/itemCatalog/login')

    if request.method == 'POST':
        if request.form['btn'] == 'save':
            newCategory = Categories(
                vehicle_type=request.form['vehicle_type'],
                description=request.form['description'],
                user_id=login_session['user_id'])

            session.add(newCategory)
            session.commit()
            flash('New category %s successfully added!' % newCategory.vehicle_type)
            return redirect(url_for('showCategories'))
        else:
            return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')
    # return "This page will be for making a new restaurant"


# Edit a category
@app.route('/itemCatalog/category/<int:category_id>/edit/',
           methods=['GET', 'POST'])

def editCategory(category_id):
    editedCategory = session.query(Categories).filter_by(id=category_id).one()
    
    if 'username' not in login_session:
        return redirect('/itemCatalog/login')
    if editedCategory.user_id != login_session['user_id']:
        return render_template('warning.html')

    if request.method == 'POST':
        if request.form['btn'] == 'save':
            editedCategory.vehicle_type = request.form['vehicle_type']
            editedCategory.description = request.form['description']
            session.add(editedCategory)
            session.commit() 
            flash('Changes in %s saved!' % editedCategory.vehicle_type)
            return redirect(url_for('showCategories'))
        else:
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category = editedCategory)

    # return 'This page will be for editing category %s' % category_id


# Delete a category
@app.route('/itemCatalog/category/<int:category_id>/delete/',
           methods=['GET','POST'])

def deleteCategory(category_id):
    categoryToDelete = session.query(Categories).filter_by(id=category_id).one()

    if 'username' not in login_session:
        return redirect('/itemCatalog/login')
    if categoryToDelete.user_id != login_session['user_id']:
        return render_template('warning.html')
    if not isCategoryEmpty(categoryToDelete.id):
        return render_template('warning.html')

    if request.method == 'POST':
        if request.form['btn'] == 'delete':
            session.delete(categoryToDelete)
            session.commit()
            flash('Category %s successfully deleted!' % categoryToDelete.vehicle_type)
            return redirect(url_for('showCategories'))
        else:
            return redirect(url_for('showCategories'))
    else:
        return render_template('deleteCategory.html',
                               category=categoryToDelete)
    
    # return 'This page will be for deleting restaurant %s' % restaurant_id


# Show a category items
@app.route('/itemCatalog/category/<int:category_id>/')
@app.route('/itemCatalog/category/<int:category_id>/items/')
def showCategoryItems(category_id):

    #category = session.query(Categories).filter_by(id = category_id).one()
    
    categories = session.query(Categories).order_by(Categories.id.desc()).\
        all()
    items = session.query(Items).order_by(Items.id.desc()).\
        filter_by(category_id=category_id).all()
    selectedCategory = session.query(Categories).filter_by(id=category_id).\
        all()
    for category in categories:
        category.empty = isCategoryEmpty(category.id)

    return render_template('showItems.html',
                           items = items,
                           itemsLen = len(items),
                           categories = categories,
                           selectedCategory = selectedCategory)


# # JSON 
# @app.route('/itemCatalog/category/<int:category_id>/JSON/')
# @app.route('/itemCatalog/category/<int:category_id>/items/JSON/')
# def showCategoryItemsJSON(category_id):
#     items = session.query(Items).order_by(Items.id.desc()).\
#         filter_by(category_id=category_id).all()
        
# End point JSON / XML
@app.route('/itemCatalog/category/<int:category_id>/endPoint/<endPoint>/')
def showCategoryItemsEndPoint(category_id, endPoint='XML'):
    
    items = session.query(Items).order_by(Items.id.desc()).\
        filter_by(category_id=category_id).all()
    
    category = session.query(Categories).filter_by(id=category_id).\
        all()
    
    # return jsonify(Categories=[c.serialize for c in categories])
    # print category[0].vehicle_type
    serial_data = {category[0].vehicle_type: [i.serialize for i in items]}
    
    if endPoint == 'JSON':
        JSON_data = json.dumps(serial_data, indent=4)
        endPoint_type = "JSON endpoint data"
        return render_template('endPoint.html', 
                               endPoint_type=endPoint_type,
                               endPointData=JSON_data)

    if endPoint == 'XML':
        xml_string = BeautifulStoneSoup(dicttoxml.dicttoxml(serial_data)).prettify()
        endPoint_type = "XML endpoint data"
        return render_template('endPoint.html',
                               endPoint_type=endPoint_type,
                               endPointData=xml_string)



# Show an item
@app.route('/itemCatalog/category/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    #categories = session.query(Categories).order_by(Categories.id.desc()).all()
    item = session.query(Items).filter_by(id=item_id).one()

    itemCreator = session.query(Users).filter_by(id=item.user_id).one()

    return render_template('showItem.html', item=item, itemCreator=itemCreator)
    
# @app.route('/itemCatalog/category/<int:category_id>/item/<int:item_id>/JSON/')
# def showItemJSON(category_id, item_id):
#     item = session.query(Items).filter_by(id = item_id).one()

#     return jsonify(Items=item.serialize)

# End point JSON / XML
@app.route('/itemCatalog/category/<int:category_id>/item/<int:item_id>/endPoint/<endPoint>/')
def showItemEndPoint(category_id, item_id, endPoint='XML'):
    
    item = session.query(Items).filter_by(id=item_id).all()
    
    # category = session.query(Categories).filter_by(id=category_id).\
    #     all()
    
    # return jsonify(Categories=[c.serialize for c in categories])
    # print category[0].vehicle_type
    serial_data = {item[0].model: [i.serialize for i in item]}
    
    if endPoint == 'JSON':
        JSON_data = json.dumps(serial_data, indent=4)
        endPoint_type = "JSON endpoint data"
        return render_template('endPoint.html', 
                               endPoint_type=endPoint_type,
                               endPointData=JSON_data)

    if endPoint == 'XML':
        xml_string = BeautifulStoneSoup(dicttoxml.dicttoxml(serial_data)).prettify()
        endPoint_type = "XML endpoint data"
        return render_template('endPoint.html',
                               endPoint_type=endPoint_type,
                               endPointData=xml_string)



# Create a new item
@app.route('/itemCatalog/category/<int:category_id>/items/new/',
           methods=['GET','POST'])

def newItem(category_id):

    if 'username' not in login_session:
        return redirect('/itemCatalog/login')
    
    if request.method == 'POST':
        # print request.form['btn']
        if request.form['btn'] == 'save':
            newItem = Items(
                make = request.form['make'],
                model = request.form['model'],
                description = request.form['description'],
                picture1 = request.form['picture1'],
                picture2 = request.form['picture2'],
                picture3 = request.form['picture3'],
                displacement = request.form['displacement'],
                engine = request.form['engine'],
                cylinders = request.form['cylinders'],
                power = request.form['power'],
                speed = request.form['speed'],
                seats = request.form['seats'],
                weight = request.form['weight'],
                year = request.form['year'],
                price = request.form['price'],
                category_id = category_id,
                user_id = login_session['user_id'])

            session.add(newItem)
            session.commit()
            flash('New item %s %s successfully added!' % (newItem.make, newItem.model))
            
            return redirect(url_for('showCategoryItems',
                            category_id=category_id))
        else:
            return redirect(url_for('showCategoryItems',
                            category_id=category_id))
    else:
        return render_template('newItem.html', category_id = category_id)

    # return render_template('newItem.html', restaurant = restaurant)
    

#Edit an item
@app.route('/itemCatalog/category/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET','POST'])
def editItem(category_id, item_id):
    editedItem = session.query(Items).filter_by(id = item_id).one()

    if 'username' not in login_session:
        return redirect('/itemCatalog/login')
    if editedItem.user_id != login_session['user_id']:
        return render_template('warning.html')

    if request.method == 'POST':
        if request.form['btn'] == 'save':
            editedItem.make =request.form['make']
            editedItem.model = request.form['model']
            editedItem.description = request.form['description']
            editedItem.picture1 = request.form['picture1']
            editedItem.picture2 = request.form['picture2']
            editedItem.picture3 = request.form['picture3']
            editedItem.displacement = request.form['displacement']
            editedItem.engine = request.form['engine']
            editedItem.cylinders = request.form['cylinders']
            editedItem.power = request.form['power']
            editedItem.speed = request.form['speed']
            editedItem.seats = request.form['seats']
            editedItem. weight = request.form['weight']
            editedItem. year = request.form['year']
            editedItem.price = request.form['price']
            #category_id = category_id)

            session.add(editedItem)
            session.commit()
            flash('Changes in %s %s saved!' % (editedItem.make, editedItem.model))
            return redirect(url_for('showItem',
                            category_id=category_id, item_id=item_id))

        else:
            return redirect(url_for('showItem',
                            category_id=category_id, item_id=item_id))
    else:
        return render_template('editItem.html', item=editedItem)

    
# Delete an item
@app.route('/itemCatalog/category/<int:category_id>/items/<int:item_id>/delete',
           methods = ['GET','POST'])
def deleteItem(category_id, item_id):
    itemToDelete = session.query(Items).filter_by(id = item_id).one() 

    if 'username' not in login_session:
        return redirect('/itemCatalog/login')
    if itemToDelete.user_id != login_session['user_id']:
        return render_template('warning.html')

    if request.method == 'POST':
        if request.form['btn'] == 'delete':
            session.delete(itemToDelete)
            session.commit()
            flash('Item %s %s deleted!' % (itemToDelete.make, itemToDelete.model))
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
        else:
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete,
                               category_id = category_id)
    

def getCategoryInfo(category_id):
    categoryName = session.query(Categories).filter_by(id = category_id).one()
    return categoryName.vehicle_type


def isCategoryEmpty(category_id):
    if session.query(Items).filter_by(category_id = category_id).all():
        return False
    else:
        return True

    
def getUserInfo(user_id):
    user = session.query(Users).filter_by(id = user_id).one()
    return user


#_______________________________oauth_______________________________________

CLIENT_ID = json.loads(
    open('g_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"


# Create a state token to prevent request forgery.
# Store it in the session for later validation.
@app.route('/itemCatalog/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

# G+ login coden
@app.route('/itemCatalog/gconnect', methods=['POST'])
def gconnect():
  
  # print 'received state of %s' %request.args.get('state')
  # print 'login_sesion["state"] = %s' %login_session['state']
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  
  # gplus_id = request.args.get('gplus_id')
  # print "request.args.get('gplus_id') = %s" %request.args.get('gplus_id')
  code = request.data
  # print "received code of %s " % code

  try:
    # Upgrade the authorization code into a credentials object
    oauth_flow = flow_from_clientsecrets('g_client_secrets.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)
  except FlowExchangeError:
    response = make_response(
        json.dumps('Failed to upgrade the authorization code.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  
  # Check that the access token is valid.
  access_token = credentials.access_token
  url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
         % access_token)
  h = httplib2.Http()
  result = json.loads(h.request(url, 'GET')[1])
  # If there was an error in the access token info, abort.
  if result.get('error') is not None:
    response = make_response(json.dumps(result.get('error')), 500)
    response.headers['Content-Type'] = 'application/json'

    
  # Verify that the access token is used for the intended user.
  gplus_id = credentials.id_token['sub']
  if result['user_id'] != gplus_id:
    response = make_response(
        json.dumps("Token's user ID doesn't match given user ID."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  # Verify that the access token is valid for this app.


  if result['issued_to'] != CLIENT_ID:
    response = make_response(
        json.dumps("Token's client ID does not match app's."), 401)
    print "Token's client ID does not match app's."
    response.headers['Content-Type'] = 'application/json'
    return response

  
  stored_credentials = login_session.get('credentials')
  stored_gplus_id = login_session.get('gplus_id')
  if stored_credentials is not None and gplus_id == stored_gplus_id:
    response = make_response(
        json.dumps('Current user is already connected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    
  # Store the access token in the session for later use.
  login_session['provider'] = 'google'
  login_session['credentials'] = credentials
  login_session['gplus_id'] = gplus_id
  response = make_response(json.dumps('Successfully connected user.', 200))
  
  print "#Get user info"
  userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
  params = {'access_token': credentials.access_token, 'alt':'json'}
  answer = requests.get(userinfo_url, params=params)
  data = json.loads(answer.text)
  
  
  # login_session['credentials'] = credentials
  # login_session['gplus_id'] = gplus_id
  login_session['username'] = data["name"]
  login_session['picture'] = data["picture"]
  login_session['email'] = data["email"]
  # print login_session['email']

  # see if user exists, if it doesn't make a new one
  user_id = getUserID(data["email"])
  # print user_id
  if not user_id:
      user_id = createUser(login_session)
  login_session['user_id'] = user_id


  output = ''
  output +='<h1>Welcome, '
  output += login_session['username']

  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output +=' " style = "width: 150px; height: 150px; border-radius: 150px;\
      -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
  flash("you are now logged in as %s"%login_session['username'])

  login_session['timeStamp'] = time.time()
  
  return output

# Revoke current user's token and reset their login_session.
@app.route("/itemCatalog/gdisconnect")
def gdisconnect():
  # Only disconnect a connected user.
  credentials = login_session.get('credentials')
  if credentials is None:
    response = make_response(json.dumps('Current user not connected.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Execute HTTP GET request to revoke current token.
  access_token = credentials.access_token
  
  print access_token
  
  url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
  h = httplib2.Http()
  result = h.request(url, 'GET')[0]

  if result['status'] == '200':
    # Reset the user's session.
    response = make_response(json.dumps('Successfully disconnected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
  else:
    # For whatever reason, the given token was invalid.
    response = make_response(
        json.dumps('Failed to revoke token for given user.', 400))
    response.headers['Content-Type'] = 'application/json'
    return response


# FB login code
@app.route('/itemCatalog/fbconnect', methods=['POST'])
def fbconnect():
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  access_token = request.data
  print "access token received %s "% access_token

  # Exchange client token for long-lived server-side token
 ## GET /oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token} 
  app_id = json.loads(
      open('fb_client_secrets.json', 'r').read())['web']['app_id']
  app_secret = json.loads(
      open('fb_client_secrets.json', 'r').read())['web']['app_secret']
  url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id,app_secret,access_token)
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]

  # Use token to get user info from API 
  userinfo_url =  "https://graph.facebook.com/v2.2/me"
  # strip expire tag from access token
  token = result.split("&")[0]
  
  url = 'https://graph.facebook.com/v2.2/me?%s' % token
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  #print "url sent for API access:%s"% url
  #print "API JSON result: %s" % result
  data = json.loads(result)
  login_session['provider'] = 'facebook'
  login_session['username'] = data["name"]
  login_session['email'] = data["email"]
  login_session['facebook_id'] = data["id"]
  
  

  # Get user picture
  url = 'https://graph.facebook.com/v2.2/me/picture?%s&redirect=0&height=200&width=200' % token
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  data = json.loads(result)

  login_session['picture'] = data["data"]["url"]
  
  # see if user exists
  user_id = getUserID(login_session['email'])
  if not user_id:
    user_id = createUser(login_session)
  login_session['user_id'] = user_id
    
  output = ''
  output +='<h1>Welcome, '
  output += login_session['username']

  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output +=' " style = "width: 150px; height: 150px;border-radius: 150px;\
      -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

  flash ("Now logged in as %s" % login_session['username'])
  login_session['timeStamp'] = time.time()
  return output


@app.route('/itemCatalog/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    url = 'https://graph.facebook.com/%s/permissions' % facebook_id
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1] 
    return "you have been logged out"


def getUserID(email):
    # print email
    try:
        user = session.query(Users).filter_by(email=email).one()
        # print user.id
        return user.id
    except:
        # print "None"
        return None


def createUser(login_session):
    # print 'createUser()'
    newUser = Users(name=login_session['username'],
                    email = login_session['email'],
                    picture = login_session['picture'])

    session.add(newUser)
    session.commit()
    user = session.query(Users).filter_by(email=login_session['email']).one()
    # print 'user_id: ', user.id
    return user.id

@app.route('/itemCatalog/disconnect')
def disconnect(byTimedOut=False):
  if 'provider' in login_session:
    if login_session['provider'] == 'google':
      gdisconnect()
      del login_session['gplus_id']
      del login_session['credentials']
    if login_session['provider'] == 'facebook':
      fbdisconnect()
      del login_session['facebook_id']

    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['provider']

    del login_session['timeStamp']

    if not byTimedOut:
        flash("You have successfully been logged out.")
    return redirect(url_for('showItems'))
  else:
    flash("You were not logged in")
    redirect(url_for('showItems'))

#______________________oauth_______________________


@app.context_processor
def inject_user():
    debug = False
    return dict(debug=debug)


@app.before_request
def make_session_permanent():
    # auto log off code
    if 'timeStamp' in login_session:
        if time.time() - login_session['timeStamp'] > 300:  # 5 minutes
            disconnect(byTimedOut=True)
            flash("Your session has expired!")
            return redirect(url_for('showItems'))
        # refresh timer
        login_session['timeStamp'] = time.time()
    

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)

