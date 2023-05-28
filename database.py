from sqlalchemy import create_engine, text
import os

#db_connection_string = os.environ['DB_CONNECTION_STRING']
db_connection_string = "mysql+pymysql://nwmmxk7iaour2650idac:pscale_pw_gIpW8uBNJGQnklspWNjlYSNIumHjcSV7jvBCwxmd7s8@aws.connect.psdb.cloud/adecareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    result_all = result.all()
    for row in result_all:
      jobs.append(row)
    return jobs
