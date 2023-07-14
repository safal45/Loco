from flask import Flask,render_template
from database import load_job_from_db
app = Flask( __name__ )


@app.route("/")
def hello_Loco():

    jobs= load_job_from_db()
    return render_template('home.html',jobs=jobs,company_name = 'Loco_Mind')
if __name__ == '__main__':
    app.run(debug = True)
