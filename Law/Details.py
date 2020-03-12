from requests_html import HTMLSession
from requests_html import HTML
import requests
import json
import time
from datetime import datetime
import re
import sqlite3
from persiantools.jdatetime import JalaliDate
#---------------------InitializeValue--------------------------
#
#------------------------Parsing-------------------------------
#--------------------------------------------------------------
def _multiple_replace(mapping, text):
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

def convert_fa_numbers(input_str):
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)

def detailParse(det):
    return (det.full_text.strip().split(':'))[1].strip()

def remove_html_tags(text):
    text = "\n".join(text.split("<br/>"))
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def clean_text(text):
    text = "\r\n".join(text.split("</p>"))
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def dateSplit(string):
    if string != '':
        if (string.split('/')[1] != '00' and '0000') and (string.split('/')[2] != '00' and '0000'):
            s = string.split('/')
            if len(s[0])==4:
                if s[1].startswith('0'):
                    s[1]=s[1][1:]
                if s[2].startswith('0'):
                    s[2]=s[2][1:]
                tarikh =str(JalaliDate(int(s[0]), int(s[1]), int(s[2])).to_gregorian())
                return tarikh
            else:
                return('')
        else:
            return ('')
    else:
        return ('')

def fillDetails(spans):
    v = {'lawType':'',
         'classification':'',
         'approvalRef':'',
         'approvalDate':'',
         'documentDate':'',
         'documentNumber':'',
         'announcementNumber':'',
         'announcementDate':'',
         'announcementRef':'',
         'executionDate':'',
         'newspaperNum':'',
         'newspaperDate':'',
         'lastStatus':'',
         'firstStatus':'',
         }
    for span in spans:
        if 'نوع قانون' in span.full_text:
            v['lawType'] = detailParse(span)
        if 'طبقه بندی' in span.full_text:
            v['classification'] = detailParse(span)
        if 'مرجع تصويب' in span.full_text:
            v['approvalRef'] = detailParse(span)
        if 'تاريخ تصويب' in span.full_text:
            v['approvalDate'] = detailParse(span)
        if 'تاریخ سند تصويب' in span.full_text:
            v['documentDate'] = detailParse(span)
        if 'شماره سند تصویب' in span.full_text:
            v['documentNumber'] = detailParse(span)
        if 'شماره ابلاغ' in span.full_text:
            v['announcementNumber'] = detailParse(span)
        if 'تاریخ ابلاغ' in span.full_text:
            v['announcementDate'] = detailParse(span)
        if 'مرجع ابلاغ' in span.full_text:
            v['announcementRef'] = detailParse(span)
        if 'تاريخ اجرا' in span.full_text:
            v['executionDate'] = detailParse(span)
        if 'شماره روزنامه رسمي' in span.full_text:
            v['newspaperNum'] = detailParse(span)
        if 'تاریخ روزنامه رسمي' in span.full_text:
            v['newspaperDate'] = detailParse(span)
        if 'آخرین وضعیت' in span.full_text:
            v['lastStatus'] = detailParse(span)
        if 'وضعیت اولیه' in span.full_text:
            v['firstStatus'] = detailParse(span)
        else:
            pass
    return v
#--------------------------end parsing---------------------------
#----------------------------------------------------------------
#--------------------------Base data-----------------------------
counter=1
detailsList = []
deleteList = []
conn1 = sqlite3.connect('Update.db')
c1= conn1.cursor()
c1.execute("SELECT * FROM Rules")
ruleList = c1.fetchall()
conn2 = sqlite3.connect('Final.db')
c2= conn2.cursor()
url = 'http://qavanin.ir/Law/'
session = HTMLSession()
for row in ruleList:
    detailObj = {'Id':'','title':'','executingDevices':'','transcriptRecipients':'','text':'',
                 'lawType':'','classification':'','approvalRef':'','approvalDate':'','documentDate':'',
                 'documentNumber':'','announcementNumber':'','announcementDate':'','announcementRef':'',
                 'executionDate':'','newspaperNum':'','newspaperDate':'','lastStatus':'','firstStatus':'',
                }
    ghanoon = session.get(url+'Attribute/'+str(row[0]))
    maindetails = ghanoon.html.find('div[class="tab-content tabs"]',first=True)
    details = maindetails.find('table',first=True).find('td')
    s = fillDetails(details)
    detailObj['Id'] = row[0]
    detailObj['title'] = row[1]
    detailObj['executingDevices'] = remove_html_tags((maindetails.find('div')[2]).find('span',first=True).html)
    detailObj['transcriptRecipients'] = remove_html_tags((maindetails.find('div')[3]).find('span',first=True).html)
    detailObj['lawType'] = s['lawType']
    detailObj['classification'] = s['classification']
    detailObj['approvalRef'] = s['approvalRef']
    detailObj['approvalDate'] = dateSplit(s['approvalDate'])
    detailObj['documentDate'] = dateSplit(s['documentDate'])
    detailObj['documentNumber'] = s['documentNumber']
    detailObj['announcementNumber'] = s['announcementNumber']
    detailObj['announcementDate'] = dateSplit(s['announcementDate'])
    detailObj['announcementRef'] = s['announcementRef']
    detailObj['executionDate'] = dateSplit(s['executionDate'])
    detailObj['newspaperNum'] = s['newspaperNum']
    detailObj['newspaperDate'] = dateSplit(s['newspaperDate'])
    detailObj['lastStatus'] = s['lastStatus']
    detailObj['firstStatus'] = s['firstStatus']
    #matn
    matn = ''
    ghanoonText = session.get(url+'TreeText/'+str(row[0]))
    matndetails = ghanoonText.html.find('div[id="treeText"]',first=True)
    ptags = matndetails.find('p')
    if len(ptags) != 0:
        for each in ptags:
            if 'متن و تصوير قابل مشاهده است.' not in each.full_text:
                matn += convert_fa_numbers(clean_text(each.html))
    if len(ptags) == 0:
        matn = 'متن این مصوبه هنوز وارد سامانه نشده است'
    detailObj['text'] = matn
    detailsList.append(tuple(detailObj.values()))
    deleteList.append(tuple([row[0]]))
    if counter % 20 == 0:
        c2.executemany("INSERT INTO Rules VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",detailsList)
        conn2.commit()
        c1.executemany("DELETE FROM Rules WHERE Id=?",deleteList)
        conn1.commit()
        detailsList = []
        deleteList = []
        print(counter)
        time.sleep(30)
        session = HTMLSession()
    counter+=1
if detailsList != []:
    c2.executemany("INSERT INTO Rules VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",detailsList)
    conn2.commit()
    c1.executemany("DELETE FROM Rules WHERE Id=?",deleteList)
    conn1.commit()   
conn1.close()
conn2.close()