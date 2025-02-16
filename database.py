from sqlalchemy import create_engine, text
import os
# syntax for connecting sqlalchemy to mysql
# engine = create_engine( "mysql+pymysql://user:pass@host/dbname?charset=utf8mb4")
db_connection_string = os.environ["DB_CONNECTION_STRING"]
engine = create_engine(db_connection_string)

# more secure way to connect with SSL



# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(type(result))
#     # here result is like a file stream, means if we go through it one time then we can not read it again.
#     printResult = result.all()
#     print(printResult)
#     print("type of returning object from all():", type(printResult))
#     print("type of every index of that list:", type(printResult[0])) 

#     for _ in range(50):  print(end="-")
#     print()

#     # now we convert each row into dictionary type because we don't know how to deal with that type
#     # so now we will make list of dictionary

    
#     result_all = [dict(row._mapping) for row in printResult]
#     # for row in printResult:
#     #     result_all.append(dict(row))

#     print(result_all)

# # print(result_all)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [dict(row._mapping) for row in result.all()]
        return jobs
