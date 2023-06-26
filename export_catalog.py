from trino import dbapi
import json


NASDAQ_DATA_LINK_API_KEY = os.getenv("NASDAQ_DATA_LINK_API_KEY")

if __name__ == '__main__':
  with dbapi.connect(
    host="huron.app.staging.quandl.corp",
    port=80,
    user=NASDAQ_DATA_LINK_API_KEY,
    catalog="main",
    schema="huron"
  ) as conn:
     cur = conn.cursor()
     show_query = 'SHOW TABLES'
     cur.execute(show_query)
     rows = cur.fetchall()
     data = {}
     for row in rows:
        tbl = row[0]
        describe_sql = f"DESCRIBE {tbl}"
        try:
          cur.execute(describe_sql)
          info = cur.fetchall()
        except Exception:
          pass
        else:
          data[tbl] = info
     with open('sqltables.json', 'w') as fp:
       json.dump(data, fp)
