#!/usr/bin/python
#-*- coding:utf-8 -*-
# import xlrd
#
# fname = "user.xls"
#
# def test():
# 	bk = xlrd.open_workbook(fname)
# 	shxrange = range(bk.nsheets)
# 	try:
# 		sh = bk.sheet_by_name("Sheet1")
# 	except:
# 		print "no sheet in %s named Sheet1" % fname
# 		return None
#
# 	nrows = sh.nrows
# 	ncols = sh.ncols
#
# 	print "nrows %d, ncols %d" % (nrows,ncols)
# 	cell_value = sh.cell_value(1,1)


def rep(file_name, w_name):
    try:
        file_a = open(file_name, 'r')
        fileList = file_a.readlines()
        file_b = open(w_name, 'w')
        for fileLine in fileList:
            new_l = fileLine.replace("\"articles\"", "\"articles_new\"")
            print new_l
            file_b.write(new_l)
    except Exception as e:
		print e
    file_b.close()
    file_a.close()


if __name__ == "__main__":
    rep("D:/data/backup/aaa_4.sql", "D:/data/backup/bbb_4.sql")
