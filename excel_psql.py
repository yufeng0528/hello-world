#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
import pgsql 

def read_execl(file_name):
	bk = xlrd.open_workbook(file_name) 
	shxrange = range(bk.nsheets) 
	try: 
		sh = bk.sheet_by_name("Sheet1") 
	except: 
		print "no sheet in %s named Sheet1" % fname 
		return None 
	nrows = sh.nrows 
	ncols = sh.ncols

	cell_value = sh.cell_value(1,1) 
	print cell_value 

	row_list = [] 

	for i in range(1,nrows): 
		row_data = sh.row_values(i)
		row_list.append(row_data)

	return row_list

def save_to_psql(zone,maker_name,address,name,phone,min_amount,product_type):
	pgsql.insert("""
			insert into pifa.maker (maker_name, maker_phone, 
      maker_address, maker_manager, manager_phone, 
      add_pro, add_city, 
      add_zone, crt_time, upd_time, limit_fee, product_type,status
      )
    values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', now(), now(), '%s', '%s', 0)"""
		% (maker_name, phone, address, name, phone, '重庆', '重庆', zone, min_amount, product_type))

def get_product_type(product_type):
	sql = "SELECT ptid FROM pifa.product_type WHERE name='%s'" % product_type
	row_product_type = pgsql.get_row(sql)
	if row_product_type:
		return row_product_type[0]
	else:
		raise Exception(product_type.encode('utf-8') + "找不到产品类型")

def test():
	maker_list = read_execl("maker.xls")
	if maker_list:
		for maker in maker_list:
			zone,maker_name,address,name,phone,min_amount,product_type = maker[0],maker[1].encode('utf-8'),maker[2].encode('utf-8'),maker[3].encode('utf-8'),maker[4].encode('utf-8'),maker[5],maker[6].encode('utf-8')
			zone = zone[2:].encode('utf-8')
			product_type = get_product_type(product_type)
			print zone, product_type
			save_to_psql(zone, maker_name, address, name, phone, min_amount, product_type)


if __name__ == "__main__":
	test()