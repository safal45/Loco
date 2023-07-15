import email
from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ.get('DB_CONNECTION_STR'," ")


engine = create_engine(
    db_connection_string,
    connect_args = {
        "ssl" : {
            "ssl_ca":"/etc/ssl/cert.pem"
    }
    }    
)
def load_jobs_from_db():

    with engine.connect() as conn:
        result = conn.execute(text("Select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(id):

    with engine.connect() as conn:
        stmt = text("SELECT * FROM jobs WHERE id = :val")
        stmt = stmt.bindparams(val=id)
        result = conn.execute(stmt)
        rows = result.fetchall()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        
        conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })

