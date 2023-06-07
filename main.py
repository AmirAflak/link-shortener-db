#from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import argparse
from time import sleep
import warnings

warnings.filterwarnings('ignore')

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
    cursor.commit()
    # cursor.execute("select * from urls")


def set_url(original_url: str) -> None:
    cursor.execute("""\
        DECLARE @original_url VARCHAR(255) = ?;
        DECLARE @short_url CHAR(6);
        EXECUTE set_url @original_url, @short_url OUTPUT;
    """, original_url)
    cursor.commit()

    cursor.execute("""\
        SELECT short_url FROM URLS WHERE original_url = ?
    """, original_url)

    print(f"shorted url:  {cursor.fetchone()[0]}")
   

def get_url(short_url: str) -> None:
    cursor.execute("""\
        DECLARE @result VARCHAR(255)
        EXEC get_url ?, @result OUTPUT
        SELECT @result
    """, short_url)
    cursor.commit()

    cursor.execute("""\
        SELECT original_url FROM URLS WHERE short_url = ?
    """, short_url)
    

    print(f"original url:  {cursor.fetchone()[0]}")
    
def get_list() -> None:
    # cursor.execute("""\
    #     SELECT * FROM URLS
    # """)
    df=pd.read_sql_query("SELECT * FROM URLS;", conn)
    print(df)
    # for row in cursor.fetchall():
    #     print(row)


    

# create_table()
# time.sleep(3)
# set_url("www.google.com")

# cursor.commit()





    

# # if __name__ == '__main__':
parser = argparse.ArgumentParser(description='URL shortener CLI')
subparsers = parser.add_subparsers(title='subcommands')

# create table
create_parser = subparsers.add_parser('init', help='create a new  table')
create_parser.set_defaults(func=lambda args: create_table())

# create url
create_parser = subparsers.add_parser('create', help='create a new short URL')
create_parser.add_argument('seturl', type=str, help='short the URL')
create_parser.set_defaults(func=lambda args: set_url(args.seturl))
# get url
get_parser = subparsers.add_parser('get', help='retrieve the original URL for a short URL')
get_parser.add_argument('geturl', type=str, help='get original url from shorted url')
get_parser.set_defaults(func=lambda args: get_url(args.geturl))
# list table
create_parser = subparsers.add_parser('list', help='get active urls')
create_parser.set_defaults(func=lambda args: get_list())
# Parse arguments and execute command
args = parser.parse_args()
args.func(args)
