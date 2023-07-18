from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ.get('DB_CONNECTION_STR', "")

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = [row._asdict() for row in result]
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


def add_information_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO information (full_name, username, email, password) VALUES (:full_name, :username, :email, :password)")

        conn.execute(query, {
            'full_name': data['full_name'],
            'username': data['username'],
            'email': data['email'],
            'password': data['password']
        })
