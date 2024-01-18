import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get user portfolio
    portfolio = db.execute(
        "SELECT * FROM portfolio WHERE user_id = ?", session["user_id"]
    )

    # Get user balance
    balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

    # Grand total (stock's value + cash)
    grand_total = balance[0]["cash"]

    # Dictionary to store current price for each stock
    current_prices = {}

    # Loop trough the user portfolio
    for row in portfolio:
        # Ensure you own something from that stock
        if row["shares"] == 0:
            # Deletes from portfolio
            db.execute(
                "DELETE FROM portfolio WHERE user_id = ? AND symbol = ?",
                session["user_id"],
                request.form.get("symbol"),
            )
            portfolio.remove(row)
            break

        # Stock current price
        current_value = lookup(row["symbol"])["price"]

        # Increment the grand total based on the stock's value
        grand_total = grand_total + (row["shares"] * current_value)

        # Put current price in a lsit
        current_prices[row["symbol"]] = current_value

    # Render user home page (portfolio)
    return render_template(
        "index.html",
        portfolio=portfolio,
        balance=balance,
        grand_total=grand_total,
        current_prices=current_prices,
    )


@app.route("/addCash", methods=["GET", "POST"])
@login_required
def addCash():
    """Add Cash"""

    # User reached rout via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure quantity was submitted
        if not request.form.get("quantity"):
            return apology("must provide quantity")

        # Add the quantity into the user balance
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            int(request.form.get("quantity")),
            session["user_id"],
        )

        # Redirect user to home page
        return redirect("/")

    # User reached rout via GET (as by clicking a link  or via redirect)
    else:
        # Render a page to add cash
        return render_template("addCash.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Ensure symbol is valid (exists)
        symbol = lookup(request.form.get("symbol"))
        if symbol == None:
            return apology("must provide valid symbol")

        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares")

        # Ensure shares is a positive integer
        # Ensure shares is a integer
        try:
            int(request.form.get("shares"))
        except ValueError:
            return apology("must provide a positive integer for shares")

        # Ensure shares is positve
        if int(request.form.get("shares")) < 1:
            return apology("must provide a positive integer for shares")

        # Ensure user can afford the shares
        # Get user cash
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )
        cash = user_cash[0]["cash"] if user_cash else 0

        # Calculate the stock's price
        price = int(request.form.get("shares")) * symbol["price"]

        # See if user can afford the stock's
        if price > cash:
            return apology("not enough money")

        # Insert into user history (user_id, the stock bought and the quantity of shares) and
        db.execute(
            "INSERT INTO history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?) ",
            session["user_id"],
            request.form.get("symbol").upper(),
            int(request.form.get("shares")),
            price,
        )

        # Insert into user portfolio
        if not db.execute(
            "UPDATE portfolio SET shares = shares + ? WHERE user_id = ? AND symbol = ?",
            int(request.form.get("shares")),
            session["user_id"],
            request.form.get("symbol").upper(),
        ):
            db.execute(
                "INSERT INTO portfolio (user_id, symbol, shares) VALUES (?, ?, ?)",
                session["user_id"],
                request.form.get("symbol").upper(),
                int(request.form.get("shares")),
            )

        # Change user balance (cash - price)
        db.execute(
            "UPDATE users SET cash = cash - ? WHERE id = ?", price, session["user_id"]
        )

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Render page to buy stock's
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Get user history
    history = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])

    # Render page with user hsitory
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # If user wants to change the password
        if "Change Password" in request.form:
            # Redirect user to change password page
            return redirect("/change_password")

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username provided
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Render login page
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Lookup stock symbol
        stock = lookup(request.form.get("symbol"))

        # Ensure there is a stock with that symbol
        if stock == None:
            return apology("must provide a existing symbol")

        # Render page with the stock information
        return render_template("quoted.html", stock=stock)

    # User reached route via Get(as by clicking a link or via redirect)
    else:
        # Render page to serach stock's
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password")

        # Ensure password confirmation was submitted
        if not request.form.get("confirmation"):
            return apology("must provide confirmation")

        # Ensure password and confirmation match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation must be equal")

        # Ensure username is not already taken
        check_username = db.execute(
            "SELECT COUNT(*) FROM users WHERE username = ?",
            request.form.get("username"),
        )

        # If it is not taken
        if check_username[0]["COUNT(*)"] == 0:
            # Insert the user into the database
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                request.form.get("username"),
                generate_password_hash(request.form.get("password")),
            )

        # If it is taken
        else:
            return apology("Username already taken")

        # Query database to get the id of the new user
        new_user = db.execute(
            "SELECT id FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember wich user has registered
        session["user_id"] = new_user[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via Get(as by clicking a link or via redirect)
    else:
        # Render registration page
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Get user portfolio
    portfolio = db.execute(
        "SELECT symbol, shares FROM portfolio WHERE user_id = ?", session["user_id"]
    )

    # User reached out via POST(as by submitting a form via POST)
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("must provide shares")

        # Ensure shares is a positive integer
        # Ensure shares is a integer
        try:
            int(request.form.get("shares"))
        except ValueError:
            return apology("must provide a positive integer for shares")

        # Ensure shares is positve
        if int(request.form.get("shares")) < 1:
            return apology("must provide a positive integer for shares")

        # Ensure user has that stock and owns enough shares
        # Loop trough stock's in portfolio
        for i, stock in enumerate(portfolio):
            # If the stock to sell is found in the portfolio
            if request.form.get("symbol") == stock["symbol"]:
                # If the number of shares to sell is bigger than the number owned by the user
                if int(request.form.get("shares")) > int(stock["shares"]):
                    return apology("you do not own enough shares")
                break
            else:
                return apology("must have stocks")

        # The money the user got as a result of selling the stocks (number of shares times the current stock price)
        price = lookup(request.form.get("symbol"))["price"] * int(request.form.get("shares"))

        # Insert into history sold shares
        db.execute(
            "INSERT INTO history (user_id, symbol, shares, price, action) VALUES (?, ?, ?, ?, 'sold')",
            session["user_id"],
            request.form.get("symbol").upper(),
            request.form.get("shares"),
            price,
        )

        # Update user portfolio
        db.execute(
            "UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?",
            request.form.get("shares"),
            session["user_id"],
            request.form.get("symbol").upper(),
        )

        # Update user balance
        db.execute("UPDATE users SET cash = cash + ?", price)

        # Redirect user to home page
        return redirect("/")

    # User reached out via GET(as by clicking a link or via redirect)
    else:
        # Render sell page
        return render_template("sell.html", portfolio=portfolio)


@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    """Change user password"""

    # User reached out via POST(as by submitting a form via post)
    if request.method == "POST":
        # Ensure the username was submitted
        if not request.form.get("username"):
            return apology("msut provide username")

        # Ensure the username exists in the database
        users = db.execute("SELECT username FROM users")
        usernames = [user["username"] for user in users]
        print(usernames)
        if request.form.get("username") not in usernames:
            return apology("username do not exist")

        # Ensure the new password was submitted
        if not request.form.get("new_password"):
            return apology("must provide new password")

        # Ensure confirmation was submitted
        if not request.form.get("confirmation"):
            return apology("must confirm password")

        # Ensure the new password and the confirmation are the same
        if request.form.get("new_password") != request.form.get("confirmation"):
            return apology("The new password and the confirmation must be the same")

        # Update new password in the database
        db.execute(
            "UPDATE users SET hash = ? WHERE username = ?",
            generate_password_hash(request.form.get("new_password")),
            request.form.get("username"),
        )

        # Redirect to login
        return redirect("/login")

    # User reached out via GET(as by clicking a link or via redirect)
    else:
        # Render page to change user password
        return render_template("change_password.html")
