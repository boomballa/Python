#!/usr/bin/python
import MySQLdb

conn = MySQLdb.Connect(
                       host = '172.16.3.88',
                       port = 3306,
                       user = 'root',
                       passwd = 'pwd4mysql',
                       db = 'crm',
                       charset = 'utf8'
                      )
cursor=conn.cursor()

sql = "select * from dish where id in (807119,807130,807149,807163,807177,807184)"

cursor.execute(sql)
print '000'

print cursor.rowcount
print '111'


rs = cursor.fetchone()
print rs
print '222'

rs = cursor.fetchmany(2)
print rs
print '333'

rs = cursor.fetchall()
print rs
print '444'

#print conn
#print cursor

cursor.close()
conn.close()