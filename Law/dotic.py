import requests
from selenium import webdriver
from requests_html import HTMLSession
from requests_html import HTML
import requests
import sqlite3
#---------------------InitializeValue--------------------------
#
#********************************************Parsing
#*******************************************
'''def _multiple_replace(mapping, text):
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))'''

def linkSplit(string):
    return int((string.split('/'))[5])

'''def convert_fa_numbers(input_str):
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
    return _multiple_replace(mapping, input_str)'''

def detailParse(det):
    return (det.full_text.strip().split(':'))[1].strip()

#********************************************
#****************************************
i = 0
page = 1
rullList = []
conn = sqlite3.connect('Update.db')
c= conn.cursor()
url = 'http://qavanin.ir'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
#*************fill search form with dates
morebtn = driver.find_element_by_id("btnAdvanceSearch")
morebtn.click()
fromApproveDate = driver.find_element_by_name('fromApproveDate')
fromApproveDate.clear()
fromApproveDate.send_keys('1393/01/01')
APPROVEDATE = driver.find_element_by_name('APPROVEDATE')
APPROVEDATE.clear()
APPROVEDATE.send_keys('1398/12/06')
driver.find_element_by_xpath('//input[@name="_isLaw"]').click()
driver.find_element_by_xpath('//button[@type="submit" and @class="btn btn-info btn-lg"]').click()
#***************************************
driver.find_element_by_xpath("//select[@name='PageSize']/option[text()='1000']").click()
lastPage = int((driver.find_element_by_xpath("//select[@name='PageNumber']/option[text()='آخر']")).get_attribute('value'))
while lastPage >= page:
    try:
        driver.find_element_by_xpath("//select[@name='PageNumber']/option[text()="+str(page)+"]").click()
    except:
        driver.find_element_by_xpath("//select[@name='PageNumber']/option[text()='آخر']").click()
    text = (driver.find_elements_by_xpath("//table[@class='slwTable']/tbody/tr/td[2]"))[1:]
    for each in text:
        rullObj = {'id':'','title':''}
        rullObj['id'] = linkSplit(each.find_element_by_css_selector('a').get_attribute('href'))
        rullObj['title'] = each.text.strip()
        rullList.append(tuple(rullObj.values()))
        i+=1
        if i % 50 == 0:
            print(i)
    c.executemany("INSERT INTO Rules VALUES(?,?)",rullList)
    conn.commit()
    rullList = []
    print('Page : '+str(page))
    page += 1
conn.close()