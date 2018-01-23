from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

#engine = create_engine('sqlite:///db_name.db')
#Base.metadata.bind = engine

#DBSession = sessionmaker(bind engine)
#session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    """This will display all of my restaurants"""
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new/')
def newRestaurant():
    """This will create a new restaurant"""
    return render_template('newrestaurant.html', restaurants=restaurants)

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    """This will edit an exisitng restaurant name"""
    return render_template('editrestaurant.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    """This will delete an exisiting restaurant"""
    return render_template('deleterestaurant.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    """This will display a restaurant's menu items"""
    return render_template('menu.html', restaurant_id=restaurant_id, items=items)

@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    """This will create a menu item"""
    return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    """This will edit an exisitng menu item's attributes"""
    return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    """This will delete an exisiting menu item"""
    return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id)




#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
