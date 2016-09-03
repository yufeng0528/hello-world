#!/usr/bin/python
#-*- coding:utf-8 -*-
import pgdb,sys
import xlrd

settings={
          "PGDB_SERVER":"10.117.21.179",
          "PGDB_PORT":"9999",
          "PGDB_DB":"trymore",
          "PGDB_USER":"postgre",
          "PGDB_PASSWORD":"postgre"
          }

fname = "user.xls"

def excel():
        bk = xlrd.open_workbook(fname)
        shxrange = range(bk.nsheets)
        try:
                sh = bk.sheet_by_name("Sheet1")
        except:
                print "no sheet in %s named Sheet1" % fname
                return None

        nrows = sh.nrows
        ncols = sh.ncols

        print "nrows %d, ncols %d" % (nrows,ncols)
        cell_value = sh.cell_value(1,1)

	item_list = []
	for x in range(nrows):
		item = []
		for i in range(9):
			item.append(sh.cell_value(x, i))	
		item_list.append(item)
	return item_list

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
		
		WITH UPSERT AS
  	(
  		UPDATE yisou.user_match_factor_vector
  		SET vector=%s,
  			total=%s,
  			size=%s,
  			upd_time=now()
  		WHERE uid=%s and type=%s
  		RETURNING *
  	)
  	  
    INSERT INTO  yisou.user_match_factor_vector (uid, type, 
      vector, total, size  
      )
    SELECT %s, %s, 
	%s,
	%s,
	%s
    
     WHERE NOT EXISTS(SELECT * FROM UPSERT); 
		"""


		teacher_sql = """
		SELECT tid,name FROM yisou.teacher
		WHERE name=%s

	"""
		
		item_list = excel()
		size = '{1,1,1,1,1,1,1,1}'

		print item_list
		for item in item_list:
			vector = "{" + ','.join(["\"" + str(v) + "\"" for v in item[1:]]) + "}"
			total = "{" + ','.join(["\"" + str(int(v)) + "\"" for v in item[1:]]) + "}"

			name = item[0].encode('utf-8')
			print name
			cur.execute(teacher_sql, (name,))
			result=cur.fetchone()
			if result:
				uid = result[0]
				print uid, result[1]
				cur.execute(sql, (vector, total, size, uid, '1', uid, '1', vector, total, size))
				conn.commit()

        except Exception,ex:
                print Exception,":",ex
        finally:
                cur.close()
                conn.close()


if __name__ == "__main__":
    test()

