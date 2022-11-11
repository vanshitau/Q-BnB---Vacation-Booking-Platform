from flask import render_template, request, session, redirect
from qbay.models import (
    login, User, register, listing, 
    update_listing, update_user, Listing
)
import datetime as dt
import traceback


from qbay import app


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        print("session: ", session)
        if 'logged_in' in session:
            email = session['logged_in']
            # print("logged in: ", email)
            try:
                # print("email", email)
                user = User.query.filter_by(email=email).one_or_none()
                
                if user:
                    print("user ", user)
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception as e:
                print(e)
                pass
        else:
            # else, redirect to the login page
            print("loggin in")
            return redirect('/login')
    # print("returnning wrapped inner")
    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = login(email, password)

    if user:
        print("the user was created")
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between a user's browser and the end server. 
        Typically it is packed and stored in the browser cookies. 
        They will be past along between every request the browser made 
        to this services. Here we store the user object into the 
        session, so we can tell if the client has already login 
        in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='login failed')


@app.route('/')
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    # the user's listings
    all_listings = Listing.query.filter_by(owner_id=user.id).all()
    if len(all_listings) > 0:
        listings = []
        for listing in all_listings:
            listings.append({
                "id": listing.id,
                "title": listing.title, 
                "description": listing.description, 
                "price": f"${listing.price}",
                "last_modified_date": listing.last_modified_date
            })
    else:
        listings = [{"title": "No listings yet!", "description": "", 
                    "price": ""}]

    return render_template('index.html', user=user, listings=listings)


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = register(None, name, email, password)
        if not success:
            error_message = "Registration failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/create_listing', methods=['GET'])
def create_listing_get():
    # templates are stored in the templates folder
    email = session['logged_in']
    user = User.query.filter_by(email=email).first()
    return render_template('create_listing.html', message='', user=user)


@app.route('/create_listing', methods=['POST'])
def create_listing_post():
    title = request.form.get('title')
    desc = request.form.get('description')
    price = request.form.get('price')
    date_mod = dt.date.today()
    error_message = None
    email = session['logged_in']
    user = User.query.filter_by(email=email).first()

    if int(price) < 10 or int(price) > 10000:
        error_message = "Price is not between 10 and 10000"
    elif title is False:
        error_message = "Title is not valid"
    elif desc is False:
        error_message = "Description is not valid"
    else:
        # use backend api to register the user
        success = listing(None, title, desc, int(price), user.id, date_mod)
        if not success:
            error_message = "Listing creation failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template(
            'create_listing.html', message=error_message, user=user
        )
    else:
        return redirect('/')


@app.route('/update_listing/<int:old_id>', methods=['GET'])
def update_listing_get(old_id):
    # templates are stored in the templates folder
    return render_template('update_listing.html', message='', old_id=old_id)


@app.route('/update_listing/<int:old_id>', methods=['POST'])
def update_listing_post(old_id):
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    error_message = None
  
    success = update_listing(old_id, title, description, int(price))
    if not success:
        error_message = "Listing update failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template(
            'update_listing.html', message=error_message, old_id=old_id
        )
    else:
        return redirect('/')


@app.route('/updateUser', methods=['GET'], endpoint='update_get')
def update_get():
    return render_template('updateUser.html', message='')


@app.route('/updateUser', methods=['POST'])
def update_post():
    # getting info from form
    username = request.form.get('username')
    email_new = request.form.get('email')
    billing_address = request.form.get('billing_address')
    postal_code = request.form.get('postal_code')
    error_message = None
    email = session['logged_in']
    user = User.query.filter_by(email=email).one_or_none()

    # calling update functionx
    user = update_user(
        user.id, username, email_new, billing_address, postal_code
    )
    if user:
        # session['updated_user'] = user.email
        # are we supposed to use success? If so how?
        success = user
        if not success:
            error_message = "Update failed."
        # logic not quite right here
        if error_message:
            return render_template('updateUser.html', message=error_message)
        else:
            session['logged_in'] = user.email
            return redirect('/')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')