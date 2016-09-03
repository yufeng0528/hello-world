#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd

fname = "user.xls"

def test():
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


if __name__ == "__main__":
    test()
