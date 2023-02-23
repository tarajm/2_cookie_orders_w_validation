from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.cookie_order import Cookie_order


# Number of Pages Displayed to User:  3
# /cookies  - displays ALL cookie orders
# /cookies/new  - displays create a new order
# /cookies/edit - displays Change/EDIT order



#Number of Routes that will be used (NOT SEEN):  2
# THis is where post methods will be used?  taking the information in and sending it to the database and then rednering a different page


#########################################################################


#create cookies page using  landing page method  
#create cookies.html

@app.route('/')
@app.route('/cookies')
def index():
    #display all orders listed in the database - reference the method get_all
    orders = Cookie_order.get_all()
    return render_template("cookies.html", orders = orders)

#html page (Cookies) points to cookie/new and cookie/edit
#create cookie/new  then cookie/edit


@app.route('/cookies/new')
def new_cookie():
    return render_template('new_cookie.html')

#go create new_cookie html page
#go create route to take in new information that was just logged in

@app.route('/cookies', methods = ['POST'])
def create_cookie():
    cookie_order = request.form 

    if not Cookie_order.is_valid(cookie_order):
        return redirect("/cookies/new")
    
    Cookie_order.create(cookie_order)
    return redirect('/')

#now create cookie/edit page
#name this edit_page and then the app. route for (Cookies/edit where we pass the data in - name that update_cookie for the function)

@app.route("/cookies/edit/<int:cookie_id>")
def edit_page(cookie_id):
    data = {
        "id" : cookie_id
    }
    order = Cookie_order.get_by_id(data)

    return render_template("edit_order.html", order = order)
    
    # # order = Cookie_order.get_by_id(cookie_id)
    # # return render_template("/edit_order.html", orders = orders)

    # orders = Cookie_order.get_by_id(cookie_id)
    # return render_template("/edit_order.html", orders = orders)

#go create edit_order html page

@app.route("/cookies/edit/<int:cookie_id>", methods = ["POST"])
def update_cookie(cookie_id): 
    # data = {
    #     "id" : id
    # }
    cookie_order = request.form 

    if not Cookie_order.is_valid(cookie_order):
        return redirect(f"/cookies/edit/{cookie_id}")
    
    Cookie_order.update(cookie_order)
    return redirect('/')
