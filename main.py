from sqlalchemy import create_engine
import pandas as pd

server="LAPTOP-Q8CKU4E0"
database="db1"
driver="ODBC Driver 17 for SQL Server"

Database_Con = f"mssql://@{server}/{database}?driver={driver}"

engine = create_engine(Database_Con)
con = engine.connect()

df=pd.read_sql_query("select * from test", con)
print(df)