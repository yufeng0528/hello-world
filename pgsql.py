#!/usr/bin/python#-*- coding:utf-8 -*-
import pgdb,sys

settings={
	#"PGDB_SERVER":"100.98.27.139",
	"PGDB_SERVER":"121.40.226.188",
	#"PGDB_SERVER":"10.117.21.179",
	"PGDB_PORT":"5432",
	"PGDB_DB":"trymore",
	"PGDB_USER":"postgre",
	"PGDB_PASSWORD":"postgre"
}

def get_conn():
	try:
		return pgdb.connect(database=settings['PGDB_DB'], host=settings['PGDB_SERVER']+':'+str(settings['PGDB_PORT']), user=settings['PGDB_USER'], password=settings['PGDB_PASSWORD'])
	except Exception, e:
		raise e

def insert(sql):
	try:
		conn = get_conn()
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except Exception,ex:  
		print Exception,":",ex 
	finally:
		cur.close()
		conn.close()

def update(sql):
	try:
		conn = get_conn()
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except Exception,ex:  
		print Exception,":",ex 
	finally:
		cur.close()
		conn.close()

def get_row(sql):
	try:
		conn = get_conn()
		cur = conn.cursor()
		cur.execute(sql)
		return cur.fetchone()
	except Exception,ex:  
		print Exception,":",ex 
	finally:
		cur.close()
		conn.close()

#得到有多少结果        
def dml(sql):
	try:
		conn = get_conn()
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except Exception,ex:  
		print Exception,":",ex 
	finally:
		cur.close()
		conn.close()

	return rowcount

def test():
	pass

if __name__ == "__main__":test()

  