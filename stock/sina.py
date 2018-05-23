# coding:utf8
import re

from basequotation import BaseQuotation


class Sina(BaseQuotation):
    """新浪免费行情获取"""
    max_num = 800
    grep_detail = re.compile(r'(\d+)=([^\s][^,]+?)%s%s' % (r',([\.\d]+)' * 29, r',([-\.\d:]+)' * 2))
    grep_detail_with_prefix = re.compile(r'(\w{2}\d+)=([^\s][^,]+?)%s%s' % (r',([\.\d]+)' * 29, r',([-\.\d:]+)' * 2))
    stock_api = 'http://hq.sinajs.cn/?format=text&list='

    def format_response_data(self, rep_data, prefix=False):
        stocks_detail = ''.join(rep_data)
        grep_str = self.grep_detail_with_prefix if prefix else self.grep_detail
        result = grep_str.finditer(stocks_detail)
        stock_list = list()
        for stock_match_object in result:
            stock = stock_match_object.groups()
            stock_list.append(dict(
                code=stock[0],
                name=stock[1],
                open=float(stock[2]),
                close=float(stock[3]),
                now=float(stock[4]),
                high=float(stock[5]),
                low=float(stock[6]),
                buy=float(stock[7]),
                sell=float(stock[8]),
                turnover=int(stock[9]),
                volume=float(stock[10]),
                date=stock[31],
            ))
        return stock_list
