import mysql.connector as mydb
import sys

def mysqlConnector(_host, _port, _user, _passwd, _dbname):
  try:
    resconn = mydb.connect(
      host=_host,
      port=_port,
      user=_user,
      password=_passwd,
      database=_dbname
    )
  except Exception as e:
    print('[DB Connection Error]', e)
    sys.exit(1)

  # 接続が切れた場合に自動的に再接続する
  resconn.ping(reconnect=True)

  return resconn


user = 'pi'
password = 'raspberry'
host = 'localhost'
db = 'sample_db'

conn = mysqlConnector(host, 3306, user, password, db)
cur = conn.cursor()
sql = 'SELECT * FROM sample_tb;'
cur.execute(sql)

rows = cur.fetchall()

for row in rows:
 print(row)

cur.close
conn.close