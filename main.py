#from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import argparse
import time


server="LAPTOP-Q8CKU4E0"
database="url_db" 
driver="ODBC Driver 17 for SQL Server"

conn = pyodbc.connect(f'Driver={driver};'
                      f'Server={server};'
                      f'Database={database};'
                      'Trusted_Connection=yes;')

# Database_Con = f"mssql://@{server}/{database}?driver={driver}"

# engine = create_engine(Database_Con)
# con = engine.connect()
# con.execute("SELECT * FROM urls")
# df=pd.read_sql_query("SELECT * FROM urls;", con)
# print(df)

cursor = conn.cursor()
def create_table() -> None:
    cursor.execute("""\
        IF OBJECT_ID('urls', 'U') IS NOT NULL
        BEGIN
            DROP TABLE urls
        END;

        create table urls(
        short_url char(6) primary key,
        original_url varchar(255), 
        num_referrals int,
        created_at datetime,
        last_referenced_at datetime,
        expires_at datetime
    );
    """)
    cursor.execute("select * from urls")
    cursor.commit()


def set_url(original_url: str) -> None:
    cursor.execute("""\
        DECLARE @original_url VARCHAR(255) = ?;
        DECLARE @short_url CHAR(6);
        EXECUTE set_url @original_url, @short_url OUTPUT;
    """, original_url)

    cursor.execute("""\
        SELECT short_url FROM URLS WHERE original_url = ?
    """, original_url)
    cursor.commit()

    print(f"shorted url:  {cursor.fetchone()[0]}")

def get_url(short_url: str) -> None:
    cursor.execute("""\
        DECLARE @result VARCHAR(255)
        EXEC get_url ?, @result OUTPUT
        SELECT @result
    """, short_url)

    cursor.execute("""\
        SELECT original_url FROM URLS WHERE short_url = ?
    """, short_url)
    cursor.commit()

    print(f"original url:  {cursor.fetchone()[0]}")



    

# create_table()
# time.sleep(3)
# set_url("www.google.com")

# cursor.commit()




def get_list():
    pass


