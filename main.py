from flask import Flask, render_template, request, redirect
from database import load_job_from_db, load_jobs_from_db, add_application_to_db, add_information_to_db

app = Flask(__name__)
app.secret_key = '7a3f7e3dd2d7bd8c19dc1d9d11c3d3d027bfd8ce0ee5f49e1aad65839de2e04f'

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

@app.route("/login")
def login():
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
        return redirect('/')
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
    return render_template('application_submitted.html', application=data, job=job)

if __name__ == '__main__':
    app.run(debug=True)
