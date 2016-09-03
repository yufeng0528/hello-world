#!/usr/bin/python
#-*- coding:utf-8 -*-
import pgdb,sys
import xlrd
import json,re
import datetime
import random

settings={
          "PGDB_SERVER":"10.117.21.179",
          "PGDB_PORT":"9999",
          "PGDB_DB":"trymore",
          "PGDB_USER":"postgre",
          "PGDB_PASSWORD":"postgre"
          }

time_pattern=re.compile('\d{2}:\d{2}-\d{2}:\d{2}')


#行列转换   
def getmulti(cursor):
        cols = [t[0] for t in cursor.description]
        rows = cursor.fetchall()
        if rows:
            return [dict(zip(cols, row)) for row in rows]
        else:
            return rows

#得到有多少结果        
def dml(cursor):
        rowcount = cur.rowcount
        cursor.close()
        return rowcount

def getMatchVectorFromExcl():
	return

def test():
        try:
                conn = pgdb.connect(database=settings['PGDB_DB'], host=settings['PGDB_SERVER']+':'+str(settings['PGDB_PORT']), user=settings['PGDB_USER'], password=settings['PGDB_PASSWORD'])
                cur = conn.cursor()

		sql = """
			select cid,time,start_time from course where type in (1,3);
		"""


		teacher_sql = """
			UPDATE yisou.course set lesson_rule='%s',time='%s'
			WHERE cid = %s;
		"""
		
		item_list = cur.execute(sql)
		cur = conn.cursor()

		for item in item_list:

			lesson_time_json = to_lesson_rule(item[2])
		
			if lesson_time_json:
				print lesson_time_json
				cur.execute(teacher_sql%(lesson_time_json[0],lesson_time_json[1],item[0]))
				conn.commit()			

		#conn.commit()

        except Exception,ex:
                print Exception,":",ex
        finally:
                cur.close()
                conn.close()

def to_lesson_rule(start_time):
	lesson_id = random.randint(1, 7)
	print start_time
	d = datetime.date(int(str(start_time[:4])), int(str(start_time[5:7])), int(str(start_time[8:10])))
	dayOfWeek = d.weekday()+1
	lesson_time = time_from_id(lesson_id)
	
	lesson_dict={}
	lesson_dict["lessonTimeId"]=lesson_id
	lesson_dict["lessonTime"]=lesson_time
	
	lesson_json={}
	lesson_json[str(dayOfWeek)]=[lesson_dict]
	return (json.dumps(lesson_json),week_from_id(dayOfWeek)+' ' + lesson_time)

	
def time_from_id(id):
	#08:00-09:35,09:45-11:20,12:05-13:40,13:50-15:25,15:35-17:10,18:00-19:35,19:40-21:15
	if id==1:
		return "08:00-09:35"
	elif id==2:
		return "09:45-11:20"
	elif id==3:
		return "12:05-13:40"
	elif id==4:
		return "13:50-15:25"
	elif id==5:
		return "15:35-17:10"
	elif id==6:
		return "18:00-19:35"
	else:
		return "19:40-21:15"

def week_from_id(id):
	if id == 1:
		return "周一"
	elif id == 2:
		return "周二"
	elif id == 3:
		return "周三"
	elif id == 4:
		return "周四"
	elif id == 5:
		return "周五"
	elif id == 6:
		return "周六"
	else:
		return '周日'



if __name__ == "__main__":
	print to_lesson_rule('2015-09-18')
	test() 

