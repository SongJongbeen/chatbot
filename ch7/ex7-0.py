import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1041489LM', charset='utf8')
cursor = conn.cursor()

sql = 'CREATE DATABASE homestead'


cursor.execute(sql)

conn.commit()
conn.close()