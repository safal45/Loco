
from crypt import methods
from email.mime import application
from flask import Flask,render_template,jsonify,request,redirect,url_for,flash
from database import load_job_from_db, load_jobs_from_db,add_application_to_db

app = Flask( __name__ )
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def hello_Loco():
    jobs= load_jobs_from_db()
    return render_template('home.html',
                        jobs=jobs)

@app.route("/view_all",methods=['post'])
def view_all():
    jobs= load_jobs_from_db()
    return render_template('all_job.html',
                        jobs=jobs)

@app.route("/events",methods=['post'])
def events():
    return render_template('event.html')

@app.route("/stories")
def stories():
    return render_template('stories.html')



@app.route("/login")
def login():
    return render_template('login_page.html')


@app.route("/signup")
def signup():
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

@app.route("/job/<id>/apply",methods=['post'])
def apply_to_job(id):
    data = request.form

    job = load_job_from_db(id)
    add_application_to_db(id,data)
    return render_template('application_submitted.html',application = data,job=job)





if __name__ == '__main__':
    app.run(debug = True)
