from flask import Flask,render_template,jsonify
from database import load_job_from_db, load_jobs_from_db
app = Flask( __name__ )


@app.route("/")
def hello_Loco():
    jobs= load_jobs_from_db()
    return render_template('home.html',
                        jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found!!, 404"
    else:
        return render_template('job_page.html', job=job)



if __name__ == '__main__':
    app.run(debug = True)
