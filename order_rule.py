#!/usr/bin/python
#-*- coding:utf-8 -*-
import pgdb,sys
import xlrd
import json,re

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
			select ocdid,lesson_rule,ocdid,tid,lesson_time,lesson_time_id,lesson_type from order_course_detail	
		"""


		teacher_sql = """
			UPDATE yisou.order_course_detail set lesson_rule='%s'
			WHERE ocdid = %s;
		"""
		
		item_list = cur.execute(sql)
		cur = conn.cursor()

		for item in item_list:

			name = item[4].decode('utf-8')
			lesson_time_json = to_lesson_rule(item)
		
			if lesson_time_json:
				#cur.execute("update yisou.order_course_detail set upd_time = now() where ocdid=634")
				cur.execute(teacher_sql%(lesson_time_json,item[0]))
				#print teacher_sql%(lesson_time_json,item[0])
				conn.commit()			

			#cur.execute(teacher_sql, (name,))
			#result=cur.fetchone()
			#if result:
			#	uid = result[0]
			#	print uid, result[1]
			#	cur.execute(sql, (vector, total, size, uid, '1', uid, '1', vector, total, size))
			#	conn.commit()
		#conn.commit()

        except Exception,ex:
                print Exception,":",ex
        finally:
                cur.close()
                conn.close()

def to_lesson_rule(item):
	lesson_time = item[4].decode('utf-8')
	lesson_time_id = item[5]
	time_dict = {}
	time_dict["lessonTimeId"]=lesson_time_id
        week_id = []	
	lesson_time_str = ''
	
	#print lesson_time,len(lesson_time)

	if(lesson_time == ''):
		return None

	if(lesson_time[:2] == u'每天'):
		week_id=[1,2,3,4,5,6,7]
	elif(lesson_time[:2] == u'周一'):
		week_id=[1]
	elif(lesson_time[:2] == u'周二'):
                week_id=[2]
	elif(lesson_time[:2] == u'周三'):
                week_id=[3]
	elif(lesson_time[:2] == u'周四'):
                week_id=[4]
	elif(lesson_time[:2] == u'周五'):
                week_id=[5]
	elif(lesson_time[:2] == u'周六'):
                week_id=[6]
	elif(lesson_time[:2] == u'周日'):
                week_id=[7]
	elif(lesson_time[11:13] == u'周一'):
                week_id=[1]
        elif(lesson_time[11:13] == u'周二'):
                week_id=[2]
        elif(lesson_time[11:13] == u'周三'):
                week_id=[3]
        elif(lesson_time[11:13] == u'周四'):
                week_id=[4]
        elif(lesson_time[11:13] == u'周五'):
                week_id=[5]
        elif(lesson_time[11:13] == u'周六'):
                week_id=[6]
        elif(lesson_time[11:13] == u'周日'):
                week_id=[7]

	lesson_time_str = reg_time(lesson_time)
		
	#print lesson_time,'+++',lesson_time_str,'---',len(week_id),lesson_time[:4]
	
	if(len(week_id) == 0):
		return None


	time_dict["lessonTime"] = lesson_time_str	
	time_dict_json={}
	for week in week_id:
		time_dict_json[str(week)]=[time_dict]
	print json.dumps(time_dict_json)
	return json.dumps(time_dict_json)


#给user_match_factor添加user_match_factor_vector
def reg_time(lesson_time):
	match = time_pattern.search(lesson_time)
	if match:
		return match.group()
	return ""
	 

if __name__ == "__main__":
    test()

