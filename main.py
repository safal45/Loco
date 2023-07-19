
from flask import Flask, render_template, request, redirect, flash
from database import load_job_from_db, load_jobs_from_db, add_application_to_db, add_information_to_db, get_iapplication_by_email
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
csrf = CSRFProtect(app)

@app.route("/")
def hello_Loco():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/view_all", methods=['POST'])
def view_all():
    jobs = load_jobs_from_db()
    return render_template('all_job.html', jobs=jobs)

@app.route("/events", methods=['POST'])
def events():
    return render_template('event.html')

@app.route("/stories")
def stories():
    return render_template('stories.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate login credentials
        if validate_login(email, password):
            # Successful login
            flash("You have successfully logged in!", "success")
            return redirect('/')
        else:
            # Incorrect login credentials
            flash("Invalid email or password. Please try again.", "error")

    return render_template('login_page.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        data = {
            'full_name': full_name,
            'username': username,
            'email': email,
            'password': password
        }
        add_information_to_db(data)
        flash("You have successfully signed up!", "success")
        return redirect('/')  # Redirect to login page after signing up

    return render_template('signup.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found!!, 404"
    else:
        return render_template('job_page.html', job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form

    job = load_job_from_db(id)
    add_application_to_db(id, data)
    flash("Your application has been submitted successfully!", "success")
    return render_template('application_submitted.html', application=data, job=job)

def validate_login(email, password):
    # Retrieve the information from the database based on the given email
    information = get_iapplication_by_email(email)

    # Check if the information exists and if the provided password matches the stored password
    if information and information['password'] == password:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True)
