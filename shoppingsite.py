"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session
import jinja2

import melons


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'sdjhfajsdf-2-35345djfgsdfjf'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    return render_template("all_melons.html",
                           melon_list=melon_list)


@app.route("/melon/<int:melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = melons.get_by_id(melon_id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""


    # melons = session["cart"].get()
    # # melon_details = {}
    # #key is id, value should have pri
    # # cart = ["honeydew", "honeydew" "watermelon"]
    # for melon in melons:
    #     if melon not in melon_count:
    #         melon_count[melon] = 1
    #     else:
    #         melon_count[melon] += 1


    #***********************Our pseudocode**********************
    melon_ids = session["cart"]
    cart = {} #(id is the key and the value is the name, quantity, price and total )
    for melon_id in melon_ids:

        current_melon = melons.get_by_id(melon_id)
        price = current_melon.price
        common_name = current_melon.common_name
        # quantity = 1

        if melon_id not in cart:
            quantity = 1
            total = quantity * price 
            cart[melon_id] = [common_name, price, quantity, total]
        else:
          quantity += 1 
          total = quantity * price 
          cart[melon_id] = [common_name, price, quantity, total]

          

    print cart 


    # for current_melon in cart:
    #     common_name = cart[current_melon][0]
    #     price = cart[current_melon][1]
    #     quantity = cart[current_melon][2]
    #     total = cart[current_melon][3]    
    # common_name = cart[melon_id][0]
    # price = cart[melon_id][1]
    # quantity = cart[melon_id][2]
    # total = cart[melon_id][3]

    # # TODO: Display the contents of the shopping cart.

    # # The logic here will be something like:
    # #
    # # - get the list-of-ids-of-melons from the session cart
    # # - loop over this list:
    # #   - keep track of information about melon types in the cart
    # #   - keep track of the total amt ordered for a melon-typels

    # #   - keep track of the total amt of the entire order
    # # - hand to the template the total order cost and the list of melon types

    return render_template("cart.html", cart = cart)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """

    if "cart" not in session:
        session["cart"] = []
    else:
        session["cart"].append(id)
        

    flash("Melon successfully added to cart!")
    return redirect("/cart")


    # TODO: Finish shopping cart functionality

    # The logic here should be something like:
    #
    # - add the id of the melon they bought to the cart in the session

    # return render_template("cart.html")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
