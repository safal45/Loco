from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ.get('DB_CONNECTION_STR',"no string")


engine = create_engine(
    db_connection_string,
    connect_args = {
        "ssl" : {
            "ssl_ca":"/etc/ssl/cert.pem"
    }
    }    
)
def load_job_from_db():

    with engine.connect() as conn:
        result = conn.execute(text("Select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

