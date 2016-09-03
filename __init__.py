#!/usr/bin/python
#-*- coding:utf-8 -*-
import jieba
import jieba.analyse
import re
import os
import pgdb,sys
import hashlib,json
from lxml.html.clean import clean_html,Cleaner
import setting
#1.对内容进行清洗，删除所有的非文本信息
settings={
          "PGDB_SERVER":"42.121.113.40",
          "PGDB_PORT":"5432",
          "PGDB_DB":"zjdw",
          "PGDB_USER":"zhima",
          "PGDB_PASSWORD":"zhima617"
          }

def clean_html(text):
    print 'i am here ----------' 
    try :
        text = re.sub('<[^>]+>', '', text)
#         text = u""+ text +"".encode("utf-8")
        print text,'tem-------------------------------tem-----------------------'
        return text
    except :
        return 'error'


#2.提取每篇文章的关键字，根据文本长度来提取关键词，当关键词
#50-200字 50个，200-500  100个，500-1000 150个
#并且并且存入数据库
def keywords():

    print 'jin ru =========================>'
    insert_sql='''INSERT INTO
    kh_test(aid,title,keywords,count_type,from_web,cat,city,start_time,end_time,status)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
#对y
    select_sql='''SELECT
    A .aid,
    A .title,
    A.content,
    A .status,
    A .from_web,
    b.cat,
    b.city 
    b.start_time,
    b.end_time
FROM
    zhima.article_tags b,
    zhima.articles A
WHERE
b.tag_key='default'
AND 
A .aid = b.aid
AND A .from_web = %s
AND A .crt_time > (
    TIMESTAMP 'now' - INTERVAL '1 hours'
)

 '''
    update_sql='''UPDATE
    kh_test
    SET
    re_aid=%s
    type=%s
    '''
    item=['中演票务通','大麦网']
    try:
        conn = pgdb.connect(database=settings['PGDB_DB'], host=settings['PGDB_SERVER']+':'+str(settings['PGDB_PORT']), user=settings['PGDB_USER'], password=settings['PGDB_PASSWORD'])
        cur = conn.cursor()
        for it in item:
            cur.execute(select_sql, (it,))
            row = commFun.getmulti(cur)
            print  '=====  row = commFun.getmulti(cur)=44444444444444='
            for kh in row:
                print kh['title']
                kh_content=clean_html(kh['content'])
                print  '=====clean_html(',kh_content,')=6666666666666='
                kh_len=len(kh_content)
#判断
                count_type='0'
                topK =1
                if kh_len<300:
                    count_type='1'
                    topK=20
                elif kh_len<600:
                    count_type='2'
                    topK=50
                elif kh_len<1500:
                    count_type='3'
                    topK=100
                else:
                    count_type='4'
                    topK=150
                
                
                print topK,'------词个数-------------------------'
                tags= jieba.analyse.extract_tags(kh_content,topK)
                print  tags,'1111111111111111222222222222222',type(tags)
                words=",".join(tags)
                print words+'======================='
                cur.execute(insert_sql, (kh['aid'],kh['title'],words,count_type,kh['from_web'],kh['cat'],kh['city'],kh['start_time'],kh['end_time'],kh['status'],))
                print'************-----------------------------*************'
        
    except Exception,ex:  
        print Exception,":",ex 
    finally:
        conn.commit()
        cur.close()
        conn.close()
        
#     jieba.analyse.extract_tags(sentence,topK)



#3.根据关键字判断是否重合
def isRepeat():
    pass



class commFun(object):
    '''
    @class: ATC_SQL
            used to store static variable
    '''
    
 #行列转换   
    @staticmethod
    def getone(cursor):
        cols = [t[0] for t in cursor.description]
        row = cursor.fetchone()
        if row:
            info = dict(zip(cols, row))
            return info
        else:
            return row
#行列转换   
    @staticmethod
    def getmulti(cursor):
        cols = [t[0] for t in cursor.description]
        rows = cursor.fetchall()
        if rows:
            return [dict(zip(cols, row)) for row in rows]
        else:
            return rows
#得到有多少结果        
    @staticmethod
    def dml(cursor):
        rowcount = cur.rowcount
        cursor.close()
        return rowcount
    @staticmethod
    def multiple_replace(text,adict):
        rx=re.compile('|'.join(map(re.escape,adict)))
        def one_xlat(match):
            return adict[match.group(0)]
        return rx.sub(one_xlat,text)
    
def main():
    keywords()
if __name__ == "__main__":
    main()