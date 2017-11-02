__author__ = 'hongda'
# coding=utf-8
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
import sys
import os
import re, time
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')
nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

total = os.popen("cat /data/nginx/logs/saas.access.log |grep -v assets|wc -l").read()
hostip = "10.26.84.23"
username = "eskfdata"
password = "MzZBR46t"
database = "user_behavior"

conn = MySQLdb.connect(host=hostip, user=username, passwd=password, db=database, port=3306, charset='utf8')
cur = conn.cursor()
sql = "insert into user_behavior.api_use_statistical(application,date,daily_total_amount,status,created_at,updated_at) VALUE('saas','%s','%s','1','%s','%s');" % (nowtime, total, nowtime, nowtime)
cur.execute(sql)
cur.close()
conn.commit()
conn.close()


