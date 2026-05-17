# Before running, make sure to run in the terminal:
# pip install bcrypt
# pip install flask

from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from database import get_db
import bcrypt
import re

app = Flask(__name__)
app.secret_key = "supersecretkey"

def if_sorted(entry_importance):
    for x in range(len(entry_importance) - 1):
        if entry_importance[x] > entry_importance[x + 1]:
            return False
    return True

def importance_sorting(entry_importance):
    if len(entry_importance) < 2:
        return entry_importance
    while not if_sorted(entry_importance):
        for x in range(len(entry_importance) - 1):
            if entry_importance[x] > entry_importance[x + 1]:
                entry_importance[x], entry_importance[x + 1] = entry_importance[x + 1], entry_importance[x]
    return entry_importance

# ---------- PASSWORD VALIDATION ----------
def is_valid_password(password):
    return (
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[^A-Za-z0-9]", password)
    )

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Incorrect username or password"

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            error = "Fields cannot be empty"
        elif not is_valid_password(password):
            error = "Password must include uppercase, lowercase, number, and special character"
        else:
            conn = get_db()
            try:
                hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

                conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hashed_pw)
                )
                conn.commit()

                return redirect(url_for("dashboard"))
            except:
                conn.rollback()
            finally:
                conn.close()

    return render_template("register.html", error=error)

# slider
@app.route('/process_slider', methods=['POST'])
def process_slider():
    data = request.get_json()
    slider_val = data.get("slider_value")
    # print("slider value received:", slider_val)
    return jsonify({'status': 'received', 'value': slider_val})

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    entries = conn.execute(
        "SELECT * FROM entries WHERE author=?",
        (session["user"],)
    ).fetchall()

    order_of_showing = [round(a % 1 * 10) for a in importance_sorting([entry['importance'] for entry in entries])]
    correctly_ordered_entries = []
    for x in order_of_showing:
        correctly_ordered_entries += [conn.execute(
            "SELECT * FROM entries WHERE id=?",
            (x,)
        ).fetchone()]

    conn.close()
    return render_template("dashboard.html", entries=correctly_ordered_entries, username=session["user"])


# ---------- CREATE ----------
# TODO: Create a route like /create
# This page should:
# - Show a form (GET)
# - Save data to the database (POST)
# - Redirect back to dashboard
# NOTE: Remove the triple """ before and after each route to 'uncomment'

@app.route("/create", methods=["GET", "POST"])
def create():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        conn = get_db()

        ntries = conn.execute(
            "SELECT * FROM entries"
        ).fetchall()

        a = len(ntries) + 1
        importance = int(request.form.get("importance")) + a / 10 ** len(f'{a}')
        title = request.form["title"].strip()
        content = request.form["content"].strip()

        try:        
                conn.execute(
                    "INSERT INTO entries (author, importance, title, content) VALUES (?, ?, ?, ?)",
                    (session["user"], importance, title, content,)
                )
                conn.commit()

                return redirect(url_for("dashboard"))
        except:
                conn.rollback()
        finally:
                conn.close()

        return redirect(url_for("dashboard"))

    return render_template("create.html")


# ---------- UPDATE ----------
# TODO: Create a route like /edit/<id>
# This page should:
# - Load existing data
# - Show it in a form
# - Update the database on submit


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    entry = conn.execute(
        "SELECT * FROM entries WHERE id=? AND author=?",
        (id, session["user"],)
    ).fetchone()

    if not entry:
        conn.close()
        return "Entry not found"

    if request.method == "POST":
        importance = int(request.form.get("importance")) + id / 10 ** len(f'{id}')

        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:
            error = "Fields cannot be empty"
        else:
            try:
                conn.execute(
                    "UPDATE entries SET importance=?, title=?, content=? WHERE id=? AND author=?",
                    (importance, title, content, id, session["user"],)
                )
                conn.commit()
                conn.close()

                return redirect(url_for("dashboard"))
            except:
                conn.rollback()
                conn.close()
                error =  "Error updating entry"

        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("edit.html", entry=entry)


# ---------- DELETE ----------
# TODO: Create a route like /delete/<id>
# This should:
# - Delete an entry from the database
# - Redirect back to dashboard


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    entry = conn.execute(
        "SELECT * FROM entries WHERE id=? AND author=?",
        (id, session["user"],)
    ).fetchone()
    print(entry)


    if not entry:
        conn.close()
        error =  "Entry not found"
    
    if request.method == "POST":
        try:
            conn.execute(
                "DELETE FROM entries WHERE id=?",
                (id,)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
        return redirect(url_for("dashboard"))
    
    conn.close()
    return render_template("delete.html", entry=entry)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)