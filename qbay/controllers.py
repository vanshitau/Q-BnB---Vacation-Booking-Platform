from flask import render_template, request, session, redirect
from qbay.models import login, User, register, listing, update_listing, Listing
import datetime as dt


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
            #print("logged in: ", email)
            try:
                #print("email", email)
                user = User.query.filter_by(email=email).one_or_none()
                
                if user:
                    print("user ", user)
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                return redirect('/login')
            else:
                return redirect('/')
        else:
            # else, redirect to the login page
            #print("loggin in")
            return redirect('/login')
    #print("returnning wrapped inner")
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
    # some fake product data
    # listings = [
    #     {listing.title: 'product 1', 'price': 10},
    #     {'name': 'product 2', 'price': 20}
    return render_template('index.html', user=user)


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
    print("date", date_mod)
    email = session['logged_in']
    user = User.query.filter_by(email=email).first()

    if int(price) < 10:
        error_message = "The price cannot be less than 10."
    else:
        # use backend api to register the user
        success = listing(None, title, desc, int(price), user.id, date_mod)
        print(
            "listing id:", success.id, ", title:", success.title, ", desc:",
            success.description, ", price:", success.price, ", owner id:", 
            success.owner_id, ", date:", success.last_modified_date)
        if not success:
            error_message = "Listing creation failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('create_listing.html', message=error_message)
    else:
        return redirect('/')

@app.route('/update_listing', methods=['GET'])
def update_listing_get():
    #templates are stored in the templates folder
    # email = session['logged_in']
    # listing = Listing.query.filter_by(id=listing_id).first()
    return render_template('update_listing.html', message='')


@app.route('/update_listing', methods=['POST'])
def update_listing_post():
    listing_id = request.form.get('listing_id')
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    error_message = None

    if int(price) < 10:
        error_message = "The price cannot be less than 10."
    else:
        # use backend api to register the user
        success = update_listing(1, title, description, price)
        if not success:
            error_message = "Listing update failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('update_listing.html', message=error_message)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')