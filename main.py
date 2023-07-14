from flask import Flask,render_template
app = Flask( __name__ )

JOBS = [
{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Benguluru,India',
    'salary':'Rs. 120,00,000'
},
{
    'id':2,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 15,00,000'
},
{
    'id':3,
    'title':'Data Scienctist',
    'location':'Delhi,India',
    'salary':'Rs. 150,00,000'
},
{
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco,USA',
    'salary':'$150,000'
},
]


@app.route("/")
def hello_Loco():
    return render_template('home.html',jobs=JOBS,company_name = 'Loco_Mind')
if __name__ == '__main__':
    app.run(debug = True)
