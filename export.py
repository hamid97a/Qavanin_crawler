import sqlite3
from persiantools.jdatetime import JalaliDate


conn1 = sqlite3.connect('قانون/Final.db')
c1= conn1.cursor()
c1.execute("SELECT * FROM Rules")
rules = c1.fetchall()
conn1.close()

conn2 = sqlite3.connect('مقرره/Final.db')
c2= conn2.cursor()
c2.execute("SELECT * FROM Regulations")
regulations = c2.fetchall()
conn2.close()

conn3 = sqlite3.connect('رای/Final.db')
c3= conn3.cursor()
c3.execute("SELECT * FROM Votes")
votes = c3.fetchall()
conn3.close()

conn4 = sqlite3.connect('organ.db')
c4 = conn4.cursor()
c4.execute('SELECT field1,field3 FROM organs')
organs = c4.fetchall()
conn4.close()

conn = sqlite3.connect("Law.db")
c = conn.cursor()
c.execute('''CREATE TABLE lwlaw(
	"ID" decimal(18, 0) NOT NULL,
	"OLDID" decimal(18, 0) ,
	"CAPTION" nvarchar(4000) ,
	"F_LWBASETABLEID_LAWTYPE" decimal(18, 0) ,
	"F_LWBASETABLEID_CLASSIFICATION" decimal(18, 0) ,
	"RULENO" decimal(18, 0) ,
	"LAWNO" decimal(18, 0) ,
	"APPROVEDATE" nvarchar(10) ,
	"F_CMBASETABLEID_LASTSTATUS" decimal(18, 0) ,
	"HASEXCEPTION" decimal(18, 0) ,
	"ISLAW" decimal(18, 0) ,
	"ISREGULATION" decimal(18, 0) ,
	"ISCORRECTIONLETTER" decimal(18, 0) ,
	"ISOPINION" decimal(18, 0) ,
	"OPINIONNO" decimal(18, 0) ,
	"CONGRESSNO" decimal(18, 0) ,
	"ISCONGRESS" decimal(18, 0) ,
	"F_LWBASETABLEID_REGULATIONTYPE" decimal(18, 0) ,
	"HASNOTE" decimal(18, 0) ,
	"EXPIREDATE" nvarchar(10) ,
	"CONTENTTEXT" ntext ,
	"OLDLAWTYPEID" decimal(18, 0) ,
	"OLDREGULATIONTYPEID" decimal(18, 0) ,
	"OLDLAWNO" decimal(18, 0) ,
	"OLDRULENO" decimal(18, 0) ,
	"LASTEXPIREDATE" decimal(18, 0) ,
	"ISBASEINFOCONFIRMED" decimal(18, 0) ,
	"ISSTRUCTURECONFIRMED" decimal(18, 0) ,
	"ISTOPICCONFIRMED" decimal(18, 0) ,
	"ISEXECUTORCONFIRMED" decimal(18, 0) ,
	"ISREFERCONFIRMED" decimal(18, 0) ,
	"ISCHANGECONFIRMED" decimal(18, 0) ,
	"ISDOCSCONFIRMED" decimal(18, 0) ,
	"ISKEYWORDCONFIRMED" decimal(18, 0) ,
	"ISDOCSCONFIRMEDFIRST" decimal(18, 0) ,
	"ISDOCSCONFIRMEDSECOND" decimal(18, 0) ,
	"ISORGREGULATIONDRAFT" decimal(18, 0) ,
	"ISORGREGULATIONDRAFTCONFIRM" decimal(18, 0) ,
	"ORGREGULATIONDRAFTCONFIRMDATE" nvarchar(10) ,
	"OLDID_LOH"  decimal(18, 0),
	"OLDSHNO"  decimal(18, 0),
    PRIMARY KEY("ID")
)''')

c.execute('''CREATE TABLE lwphase(
	"ID" decimal(18, 0) NOT NULL,
	"OLDID" decimal(18, 0) ,
	"F_LWLAWID" decimal(18, 0) NOT NULL,
	"NO" decimal(18, 0) NOT NULL,
	"COMMANDNO" nvarchar(52) ,
	"COMMANDDATE" nvarchar(10) ,
	"F_CMORGANIZATIONID" decimal(18, 0) ,
	"NEWSPAPERNO" nvarchar(50) ,
	"NEWSPAPERDATE" nvarchar(10) ,
	"LAWTEXT" ntext ,
	"DISTRIBUTETEXT" ntext ,
	"COMMANDTEXT" ntext ,
	"OLDEBLAGHID" decimal(18, 0) ,
	"OLDRULGHENTESHARTEXTID" decimal(18, 0) ,
	"OLDRULGHEBLAGHTEXTID" decimal(18, 0) ,
	"OLDRULGHROZNAMEHID" decimal(18, 0) ,
	"APPROVEDATE" nvarchar(10) ,
	"HASNOTE" decimal(18, 0) ,
	"COMMANPLACE" decimal(18, 0) ,
	"COMMANDPLACE" nvarchar(80) ,
	"APPROVEDOCDATE" nvarchar(10) ,
	"APPROVEDOCNO" nvarchar(20) ,
	"DESC1" nvarchar(500) ,
	"DESC2" nvarchar(60) ,
    PRIMARY KEY("ID")
)''')

c.execute('''CREATE TABLE lwapprover(
	"ID"  decimal(18, 0) NOT NULL,
	"F_LWPHASEID" decimal(18, 0) NOT NULL,
	"F_CMORGANIZATIONID" decimal(18, 0),
	"APPROVEDATE" nvarchar(10),
	"DESCRIPTION" nvarchar(1000),
	"OLDID" decimal(18, 0),
    PRIMARY KEY("ID")
)''')

c.execute('''CREATE TABLE lwexecutor(
	"ID" decimal(18, 0) NOT NULL,
	"OLDID" decimal(18, 0) ,
	"F_LWLAWID" decimal(18, 0) NOT NULL,
	"F_CMORGANIZATIONID" decimal(18, 0) NOT NULL,
    PRIMARY KEY("ID")
)''')

c.execute('''CREATE TABLE lwreceiver(
	"ID" decimal(18, 0) NOT NULL,
	"F_LWLAWID" decimal(18, 0) NOT NULL,
	"F_CMORGANIZATIONID" decimal(18, 0) NOT NULL,
    "OLDID" decimal(18, 0) ,
    PRIMARY KEY("ID")
)''')

c.execute('''CREATE TABLE lwsection(
	"ID" decimal(18, 0) NOT NULL,
	"CAPTION" nvarchar(200) ,
	"F_PARENTID" decimal(18, 0) ,
	"F_CMBASETABLEID_SECTIONSTATUS" decimal(18, 0) ,
	"F_LWLAWSTRUCTUREID" decimal(18, 0) ,
	"SECTIONTEXT" ntext ,
	"SECTIONLEVEL" decimal(18, 0) ,
	"TEXTORDER" decimal(18, 0) ,
	"STATENO" decimal(18, 0) NOT NULL,
	"SECTIONTYPENO" decimal(18, 0) ,
	"F_LWLAWID" decimal(18, 0) NOT NULL,
	"F_LWPHASEID" decimal(18, 0) NOT NULL,
	"OLDID" decimal(18, 0) ,
	"FULLPATH" nvarchar(600) NOT NULL,
	"SECTIONTYPENOTEXT" nvarchar(100) ,
	"FIRSTSATENO" decimal(18, 0) ,
	"LASTSTATENO" decimal(18, 0) ,
	"F_LWSECTIONID_REPLACED" decimal(18, 0) ,
	"HIERARCHY" nvarchar(500) ,
	"DISPLAYINCONTENTS" decimal(18, 0) ,
	"F_LWLAWCHANGEID" decimal(18, 0) ,
	"TMP" decimal(18, 0) ,
	"F_LWLAWCHANGEID_FIRST" decimal(18, 0) ,
	"F_LWLAWCHANGEID_LAST" decimal(18, 0) ,
	"ISINTERPRETATION" decimal(18, 0) ,
    PRIMARY KEY("ID")
)''')

c.execute('''CREATE TABLE prdoc(
	"ID" decimal(18, 0) NOT NULL,
	"DOCTEXT" ntext,
	"OLDID_MAJLES" decimal(18, 0),
	"OLDID_MAJLES_FINALDEC_FLOWDTL" decimal(18, 0),
	"OLDID_RULMAJLESMATNID" decimal(18, 0),
	"OLDID_NAZARAT" decimal(18, 0),
	"F_RULNAZARID" decimal(18, 0),
    PRIMARY KEY("ID") 
)''')

c.execute('''CREATE TABLE opopinion(
	"ID" decimal(18, 0) NOT NULL,
	"subject" nvarchar(4000) ,
	"OPINIONLETTERNO" nvarchar(60) ,
	"OPINIONDATE" nvarchar(10) ,
	"REGISTRATIONNO" nvarchar(100) ,
	"ARCHIVENO" nvarchar(100) ,
	"F_CMBASETABLEID_CLASSIFICATION" decimal(18, 0) ,
	"F_OPOPINIONGIVERID" decimal(18, 0) ,
	"F_OPOPINIONGIVERPERSONID" decimal(18, 0) ,
	"F_LWLAWID" decimal(18, 0) NOT NULL,
	"ISELEMENTARY" decimal(18, 0) ,
	"DISTRIBUTENO" nvarchar(100) ,
	"DISTRIBUTEDATE" nvarchar(10) ,
	"F_PRDOCID" decimal(18, 0) ,
	"REALPERSONRECEIVE" decimal(18, 0) ,
	"HASNOTE" decimal(18, 0) ,
	"THECOMMENT" ntext ,
	"OLDID" decimal(18, 0) ,
	"ISBASEINFOCONFIRMED" decimal(18, 0) ,
	"ISBASEDOCCONFIRMED" decimal(18, 0) ,
	"ISTOPICCONFIRMED" decimal(18, 0) ,
	"ISKEYWORDCONFIRMED" decimal(18, 0) ,
	"ISHISTORYCONFIRMED" decimal(18, 0) ,
	"DOSSIERCLASS" nvarchar(400) ,
	"TOTALIMAGE" decimal(18, 0) ,
    PRIMARY KEY("ID") 
)''')

c.execute('''CREATE TABLE lwlawstructure(
	"ID" decimal(18, 0) NOT NULL,
	"OLDID" decimal(18, 0) ,
	"F_LWLAWID" decimal(18, 0) NOT NULL,
	"F_PARENTID" decimal(18, 0) ,
	"LEVELNO" decimal(18, 0) NOT NULL,
	"F_BASETABLEID_SECTIONTYPE" decimal(18, 0) NOT NULL,
	"NUMBERINGMETHOD" decimal(18, 0) ,
	"HIERARCHY" nvarchar(600) ,
    PRIMARY KEY("ID")
)''')

def selectorgan(string):
    for each in organs:
        if each[1] in string:
            return each[0]

def lawType(string):
    if 'عادي  – حكومتي' in string:
        return 5
    if 'حكومتي' in string:
        return 1
    if 'اساسی' in string:
        return 2
    if 'ولائي' in string:
        return 3
    if 'عادي' in string:
        return 4
    if 'آيين نامه' in string:
        return 6
    if 'اساسنامه' in string:
        return 7
    if 'ندارد' in string:
        return 8
    if 'خيلي' in string:
        return 10
    if 'محرمانه' in string:
        return 9
    if 'بكلي' in string:
        return 12
    if 'سري' in string:
        return 11
    if 'وزارتخانه' in string:
        return 13
    if 'مستقل' in string:
        return 14
    if 'نهاد' in string:
        return 15
    if 'مراجع' in string:
        return 16
    if 'ستادي' in string:
        return 17

def dateParser(string):
    if string != '':
        s = string.split('-')
        tarikh = str(JalaliDate.to_jalali(int(s[0]), int(s[1]), int(s[2])))
        v = tarikh.split('-')
        shamsi = str(v[0])+'/'+str(v[1])+'/'+str(v[2])
        return shamsi
    else:
        return ('')

def opGiver(string):
    if 'رییس مجلس' in string:
        return 4
    if 'دیوان عدالت اداری' in string:
        return 11
    if 'دیوان عالی کشور' in string:
        return 10
    if 'اداره کل حقوقی قوه قضائیه' in string:
        return 12
    
def enterSpliter(string):
    splitList = string.split('\n')
    return splitList

sectionId = 1733482
lawno = 48948
ruleno = 87709
phaseId = 165500
approverId = 105920
execId = 104619
reciveId = 225454
opinionno = 43608
prodocId = 44711
opinionId = 40618
strucId = 346743
sectionList = []
lawList = []
phaseList = []
approveList = []
execList = []
reciveList = []
opinionList = []
prodocList = []
strucList = []
#----------------------------add laws-------------------
for row in rules:
    if row[2]!='':
        execDivs = enterSpliter(row[2])
        for each in execDivs:
            if isinstance(selectorgan(each),int):
                execObj={'ID':'','OLDID':'','F_LWLAWID':'','F_CMORGANIZATIONID':''}
                execObj['ID'] = execId
                execObj['OLDID'] = ''
                execObj['F_LWLAWID'] = row[0]
                execObj['F_CMORGANIZATIONID'] = selectorgan(each)
                execList.append(tuple(execObj.values()))
                execId += 1
    if row[3]!='':
        recivers = enterSpliter(row[3])
        for each in recivers:
            if isinstance(selectorgan(each),int):
                reciveObj={'ID':'','F_LWLAWID':'','F_CMORGANIZATIONID':'','OLDID':''}
                reciveObj['ID'] = reciveId
                reciveObj['OLDID'] = ''
                reciveObj['F_LWLAWID'] = row[0]
                reciveObj['F_CMORGANIZATIONID'] = selectorgan(each)
                reciveList.append(tuple(reciveObj.values()))
                reciveId += 1

    lawObj={'ID':'','OLDID':'','CAPTION':'','F_LWBASETABLEID_LAWTYPE':'','F_LWBASETABLEID_CLASSIFICATION':'',
            'RULENO':'','LAWNO':'','APPROVEDATE':'','F_CMBASETABLEID_LASTSTATUS':'','HASEXCEPTION':'','ISLAW':'',
            'ISREGULATION':'','ISCORRECTIONLETTER':'','ISOPINION':'','OPINIONNO':'','CONGRESSNO':'','ISCONGRESS':'',
            'F_LWBASETABLEID_REGULATIONTYPE':'','HASNOTE':'','EXPIREDATE':'','CONTENTTEXT':'','OLDLAWTYPEID':'',
            'OLDREGULATIONTYPEID':'','OLDLAWNO':'','OLDRULENO':'','LASTEXPIREDATE':'','ISBASEINFOCONFIRMED':'',
            'ISSTRUCTURECONFIRMED':'','ISTOPICCONFIRMED':'','ISEXECUTORCONFIRMED':'','ISREFERCONFIRMED':'',
            'ISCHANGECONFIRMED':'','ISDOCSCONFIRMED':'','ISKEYWORDCONFIRMED':'','ISDOCSCONFIRMEDFIRST':'',
            'ISDOCSCONFIRMEDSECOND':'','ISORGREGULATIONDRAFT':'','ISORGREGULATIONDRAFTCONFIRM':'',
            'ORGREGULATIONDRAFTCONFIRMDATE':'','OLDID_LOH':'','OLDSHNO':''
            }

    lawObj['ID'] = row[0]
    lawObj['OLDID'] = row[0]
    lawObj['CAPTION'] = row[1]
    lawObj['F_LWBASETABLEID_LAWTYPE'] = lawType(row[5])
    lawObj['F_LWBASETABLEID_CLASSIFICATION']  = lawType(row[6])
    lawObj['RULENO'] = ''
    lawObj['LAWNO'] = lawno
    lawObj['APPROVEDATE'] = dateParser(row[8])
    lawObj['F_CMBASETABLEID_LASTSTATUS'] = lawType(row[17])
    lawObj['HASEXCEPTION'] = ''
    lawObj['ISLAW'] = 1
    lawObj['ISREGULATION'] = 0
    lawObj['ISCORRECTIONLETTER'] = ''
    lawObj['ISOPINION'] = 0
    lawObj['HASNOTE'] = '0'

    lawList.append(tuple(lawObj.values()))

    phaseObj={'ID':'','OLDID':'','F_LWLAWID':'','NO':'','COMMANDNO':'','COMMANDDATE':'','F_CMORGANIZATIONID':'',
              'NEWSPAPERNO':'','NEWSPAPERDATE':'','LAWTEXT':'','DISTRIBUTETEXT':'','COMMANDTEXT':'',
              'OLDEBLAGHID':'','OLDRULGHENTESHARTEXTID':'','OLDRULGHEBLAGHTEXTID':'','OLDRULGHROZNAMEHID':'',
              'APPROVEDATE':'','HASNOTE':'','COMMANPLACE':'','COMMANDPLACE':'','APPROVEDOCDATE':'',
              'APPROVEDOCNO':'','DESC1':'','DESC2':''
             }
    phaseObj['ID'] = phaseId
    phaseObj['OLDID'] = ''
    phaseObj['F_LWLAWID'] = row[0]
    phaseObj['NO'] = 1
    phaseObj['COMMANDNO']  = row[11]
    phaseObj['COMMANDDATE'] = dateParser(row[12])
    phaseObj['F_CMORGANIZATIONID'] = selectorgan(row[13])
    phaseObj['NEWSPAPERNO'] = row[15]
    phaseObj['NEWSPAPERDATE'] = dateParser(row[16])
    phaseObj['LAWTEXT'] = ''
    phaseObj['DISTRIBUTETEXT'] = ''
    phaseObj['COMMANDTEXT'] = ''
    phaseObj['OLDEBLAGHID'] = ''
    phaseObj['OLDRULGHENTESHARTEXTID'] = ''
    phaseObj['OLDRULGHEBLAGHTEXTID'] = ''
    phaseObj['OLDRULGHROZNAMEHID'] = ''
    phaseObj['APPROVEDATE'] = dateParser(row[8])
    phaseObj['HASNOTE'] = '0'
    phaseObj['COMMANPLACE'] = ''
    phaseObj['COMMANDPLACE'] = ''
    phaseObj['APPROVEDOCDATE'] = ''
    phaseObj['APPROVEDOCNO'] = ''
    phaseObj['DESC1'] = ''
    phaseObj['DESC2'] = ''
    phaseList.append(tuple(phaseObj.values()))

    approveObj={'ID':'','F_LWPHASEID':'','F_CMORGANIZATIONID':'','APPROVEDATE':'','DESCRIPTION':'','OLDID':''}
    approveObj['ID'] = approverId
    approveObj['F_LWPHASEID'] = phaseId
    approveObj['F_CMORGANIZATIONID'] = selectorgan(row[7])
    approveObj['APPROVEDATE'] = dateParser(row[8])
    approveObj['DESCRIPTION'] = ''
    approveObj['OLDID'] = ''
    approveList.append(tuple(approveObj.values()))

    sectionObj1={'ID':'','CAPTION':'','F_PARENTID':'','F_CMBASETABLEID_SECTIONSTATUS':'','F_LWLAWSTRUCTUREID':'',
            'SECTIONTEXT':'','SECTIONLEVEL':'','TEXTORDER':'','STATENO':'','SECTIONTYPENO':'',
            'F_LWLAWID':'','F_LWPHASEID':'','OLDID':'','FULLPATH':'','SECTIONTYPENOTEXT':'',
            'FIRSTSATENO':'','LASTSTATENO':'','F_LWSECTIONID_REPLACED':'','HIERARCHY':'',
            'DISPLAYINCONTENTS':'','F_LWLAWCHANGEID':'','TMP':'','F_LWLAWCHANGEID_FIRST':'',
            'F_LWLAWCHANGEID_LAST':'','ISINTERPRETATION':''
           }
    sectionObj1['ID'] = sectionId
    sectionObj1['CAPTION'] = ''
    sectionObj1['F_PARENTID'] = ''
    sectionObj1['F_CMBASETABLEID_SECTIONSTATUS'] = lawType(row[17])
    sectionObj1['F_LWLAWSTRUCTUREID'] = strucId
    sectionObj1['SECTIONTEXT'] = row[1]
    sectionObj1['SECTIONLEVEL'] = 1
    sectionObj1['TEXTORDER'] = 1
    sectionObj1['STATENO'] = 1
    sectionObj1['SECTIONTYPENO'] = ''
    sectionObj1['F_LWLAWID'] = row[0]
    sectionObj1['F_LWPHASEID'] = phaseId
    sectionObj1['OLDID'] = ''
    sectionObj1['FULLPATH'] = 'عنوان'
    sectionObj1['SECTIONTYPENOTEXT']=''
    sectionObj1['FIRSTSATENO'] = 1
    sectionObj1['LASTSTATENO'] = 0
    sectionObj1['F_LWSECTIONID_REPLACED']=''
    sectionObj1['HIERARCHY'] = '.'+str(sectionId)+'.'
    sectionObj1['DISPLAYINCONTENTS']=''
    sectionObj1['F_LWLAWCHANGEID']=''
    sectionObj1['TMP']=''
    sectionObj1['F_LWLAWCHANGEID_FIRST']=''
    sectionObj1['F_LWLAWCHANGEID_LAST']=''
    sectionObj1['ISINTERPRETATION']=''
    sectionList.append(tuple(sectionObj1.values()))

    strucObj1={'ID':'','OLDID':'','F_LWLAWID':'','F_PARENTID':'','LEVELNO':1,
              'F_BASETABLEID_SECTIONTYPE':'','NUMBERINGMETHOD':2,'HIERARCHY':''
              }
    strucObj1['ID'] = strucId
    strucObj1['F_LWLAWID'] = row[0]
    strucObj1['F_BASETABLEID_SECTIONTYPE'] = 39
    strucObj1['HIERARCHY'] = '.'+str(strucId)+'.'
    strucList.append(tuple(strucObj1.values()))

    strucId += 1
    sectionId += 1
    

    sectionObj2={'ID':'','CAPTION':'','F_PARENTID':'','F_CMBASETABLEID_SECTIONSTATUS':'','F_LWLAWSTRUCTUREID':'',
                'SECTIONTEXT':'','SECTIONLEVEL':'','TEXTORDER':'','STATENO':'','SECTIONTYPENO':'',
                'F_LWLAWID':'','F_LWPHASEID':'','OLDID':'','FULLPATH':'','SECTIONTYPENOTEXT':'',
                'FIRSTSATENO':'','LASTSTATENO':'','F_LWSECTIONID_REPLACED':'','HIERARCHY':'',
                'DISPLAYINCONTENTS':'','F_LWLAWCHANGEID':'','TMP':'','F_LWLAWCHANGEID_FIRST':'',
                'F_LWLAWCHANGEID_LAST':'','ISINTERPRETATION':''
                }
    sectionObj2['ID'] = sectionId
    sectionObj2['CAPTION'] = ''
    sectionObj2['F_PARENTID'] = ''
    sectionObj2['F_CMBASETABLEID_SECTIONSTATUS'] = lawType(row[17])
    sectionObj2['F_LWLAWSTRUCTUREID'] = strucId
    sectionObj2['SECTIONTEXT'] = row[4]
    sectionObj2['SECTIONLEVEL'] = 1
    sectionObj2['TEXTORDER'] = 2
    sectionObj2['STATENO'] = 1
    sectionObj2['SECTIONTYPENO']=''
    sectionObj2['F_LWLAWID'] = row[0]
    sectionObj2['F_LWPHASEID'] = phaseId
    sectionObj2['OLDID'] = ''
    sectionObj2['FULLPATH'] = 'متن'
    sectionObj2['SECTIONTYPENOTEXT']=''
    sectionObj2['FIRSTSATENO'] = 1
    sectionObj2['LASTSTATENO'] = 0
    sectionObj2['F_LWSECTIONID_REPLACED']=''
    sectionObj2['HIERARCHY'] = '.'+str(sectionId)+'.'
    sectionObj2['DISPLAYINCONTENTS']=''
    sectionObj2['F_LWLAWCHANGEID']=''
    sectionObj2['TMP']=''
    sectionObj2['F_LWLAWCHANGEID_FIRST']=''
    sectionObj2['F_LWLAWCHANGEID_LAST']=''
    sectionObj2['ISINTERPRETATION']=''
    sectionList.append(tuple(sectionObj2.values()))

    strucObj2={'ID':'','OLDID':'','F_LWLAWID':'','F_PARENTID':'','LEVELNO':1,
              'F_BASETABLEID_SECTIONTYPE':'','NUMBERINGMETHOD':2,'HIERARCHY':''
              }
    strucObj2['ID'] = strucId
    strucObj2['F_LWLAWID'] = row[0]
    strucObj2['F_BASETABLEID_SECTIONTYPE'] = 35
    strucObj2['HIERARCHY'] = '.'+str(strucId)+'.'
    strucList.append(tuple(strucObj2.values()))

    strucId += 1
    sectionId += 1
    lawno += 1
    phaseId += 1
    approverId +=1
#--------------------------------add Regulations-----------------
for row in regulations:
    if row[2]!='':
        execDivs = enterSpliter(row[2])
        for each in execDivs:
            if isinstance(selectorgan(each),int):
                execObj={'ID':'','OLDID':'','F_LWLAWID':'','F_CMORGANIZATIONID':''}
                execObj['ID'] = execId
                execObj['OLDID'] = ''
                execObj['F_LWLAWID'] = row[0]
                execObj['F_CMORGANIZATIONID'] = selectorgan(each)
                execList.append(tuple(execObj.values()))
                execId += 1
    if row[3]!='':
        recivers = enterSpliter(row[3])
        for each in recivers:
            if isinstance(selectorgan(each),int):
                reciveObj={'ID':'','F_LWLAWID':'','F_CMORGANIZATIONID':'','OLDID':''}
                reciveObj['ID'] = reciveId
                reciveObj['OLDID'] = ''
                reciveObj['F_LWLAWID'] = row[0]
                reciveObj['F_CMORGANIZATIONID'] = selectorgan(each)
                reciveList.append(tuple(reciveObj.values()))
                reciveId += 1

    lawObj={'ID':'','OLDID':'','CAPTION':'','F_LWBASETABLEID_LAWTYPE':'','F_LWBASETABLEID_CLASSIFICATION':'',
            'RULENO':'','LAWNO':'','APPROVEDATE':'','F_CMBASETABLEID_LASTSTATUS':'','HASEXCEPTION':'','ISLAW':'',
            'ISREGULATION':'','ISCORRECTIONLETTER':'','ISOPINION':'','OPINIONNO':'','CONGRESSNO':'','ISCONGRESS':'',
            'F_LWBASETABLEID_REGULATIONTYPE':'','HASNOTE':'','EXPIREDATE':'','CONTENTTEXT':'','OLDLAWTYPEID':'',
            'OLDREGULATIONTYPEID':'','OLDLAWNO':'','OLDRULENO':'','LASTEXPIREDATE':'','ISBASEINFOCONFIRMED':'',
            'ISSTRUCTURECONFIRMED':'','ISTOPICCONFIRMED':'','ISEXECUTORCONFIRMED':'','ISREFERCONFIRMED':'',
            'ISCHANGECONFIRMED':'','ISDOCSCONFIRMED':'','ISKEYWORDCONFIRMED':'','ISDOCSCONFIRMEDFIRST':'',
            'ISDOCSCONFIRMEDSECOND':'','ISORGREGULATIONDRAFT':'','ISORGREGULATIONDRAFTCONFIRM':'',
            'ORGREGULATIONDRAFTCONFIRMDATE':'','OLDID_LOH':'','OLDSHNO':''
            }

    lawObj['ID'] = row[0]
    lawObj['OLDID'] = row[0]
    lawObj['CAPTION'] = row[1]
    lawObj['F_LWBASETABLEID_LAWTYPE'] = ''
    lawObj['F_LWBASETABLEID_CLASSIFICATION']  = lawType(row[6])
    lawObj['RULENO'] = ruleno
    lawObj['LAWNO'] = ''
    lawObj['APPROVEDATE'] = dateParser(row[8])
    lawObj['F_CMBASETABLEID_LASTSTATUS'] = lawType(row[17])
    lawObj['HASEXCEPTION'] = ''
    lawObj['ISLAW'] = 0
    lawObj['ISREGULATION'] = 1
    lawObj['ISCORRECTIONLETTER'] = ''
    lawObj['ISOPINION'] = 0
    lawObj['HASNOTE'] = 0

    lawList.append(tuple(lawObj.values()))
    ruleno += 1

    phaseObj={'ID':'','OLDID':'','F_LWLAWID':'','NO':'','COMMANDNO':'','COMMANDDATE':'','F_CMORGANIZATIONID':'',
              'NEWSPAPERNO':'','NEWSPAPERDATE':'','LAWTEXT':'','DISTRIBUTETEXT':'','COMMANDTEXT':'',
              'OLDEBLAGHID':'','OLDRULGHENTESHARTEXTID':'','OLDRULGHEBLAGHTEXTID':'','OLDRULGHROZNAMEHID':'',
              'APPROVEDATE':'','HASNOTE':'','COMMANPLACE':'','COMMANDPLACE':'','APPROVEDOCDATE':'',
              'APPROVEDOCNO':'','DESC1':'','DESC2':''
             }
    phaseObj['ID'] = phaseId
    phaseObj['OLDID'] = ''
    phaseObj['F_LWLAWID'] = row[0]
    phaseObj['NO'] = 1
    phaseObj['COMMANDNO']  = row[11]
    phaseObj['COMMANDDATE'] = dateParser(row[12])
    phaseObj['F_CMORGANIZATIONID'] = selectorgan(row[13])
    phaseObj['NEWSPAPERNO'] = row[15]
    phaseObj['NEWSPAPERDATE'] = dateParser(row[16])
    phaseObj['APPROVEDATE'] = dateParser(row[8])
    phaseObj['HASNOTE'] = '0'
    phaseList.append(tuple(phaseObj.values()))

    approveObj={'ID':'','F_LWPHASEID':'','F_CMORGANIZATIONID':'','APPROVEDATE':'','DESCRIPTION':'','OLDID':''}
    approveObj['ID'] = approverId
    approveObj['F_LWPHASEID'] = phaseId
    approveObj['F_CMORGANIZATIONID'] = selectorgan(row[7])
    approveObj['APPROVEDATE'] = dateParser(row[8])
    approveObj['DESCRIPTION'] = ''
    approveObj['OLDID'] = ''
    approveList.append(tuple(approveObj.values()))

    sectionObj1={'ID':'','CAPTION':'','F_PARENTID':'','F_CMBASETABLEID_SECTIONSTATUS':'','F_LWLAWSTRUCTUREID':'',
            'SECTIONTEXT':'','SECTIONLEVEL':'','TEXTORDER':'','STATENO':'','SECTIONTYPENO':'',
            'F_LWLAWID':'','F_LWPHASEID':'','OLDID':'','FULLPATH':'','SECTIONTYPENOTEXT':'',
            'FIRSTSATENO':'','LASTSTATENO':'','F_LWSECTIONID_REPLACED':'','HIERARCHY':'',
            'DISPLAYINCONTENTS':'','F_LWLAWCHANGEID':'','TMP':'','F_LWLAWCHANGEID_FIRST':'',
            'F_LWLAWCHANGEID_LAST':'','ISINTERPRETATION':''
           }
    sectionObj1['ID'] = sectionId
    sectionObj1['CAPTION'] = ''
    sectionObj1['F_PARENTID'] = ''
    sectionObj1['F_CMBASETABLEID_SECTIONSTATUS'] = lawType(row[17])
    sectionObj1['F_LWLAWSTRUCTUREID'] = strucId
    sectionObj1['SECTIONTEXT'] = row[1]
    sectionObj1['SECTIONLEVEL'] = 1
    sectionObj1['TEXTORDER'] = 1
    sectionObj1['STATENO'] = 1
    sectionObj1['SECTIONTYPENO'] = ''
    sectionObj1['F_LWLAWID'] = row[0]
    sectionObj1['F_LWPHASEID'] = phaseId
    sectionObj1['OLDID'] = ''
    sectionObj1['FULLPATH'] = 'عنوان'
    sectionObj1['SECTIONTYPENOTEXT']=''
    sectionObj1['FIRSTSATENO'] = 1
    sectionObj1['LASTSTATENO'] = 0
    sectionObj1['F_LWSECTIONID_REPLACED']=''
    sectionObj1['HIERARCHY'] = '.'+str(sectionId)+'.'
    sectionList.append(tuple(sectionObj1.values()))

    strucObj1={'ID':'','OLDID':'','F_LWLAWID':'','F_PARENTID':'','LEVELNO':1,
              'F_BASETABLEID_SECTIONTYPE':'','NUMBERINGMETHOD':2,'HIERARCHY':''
              }
    strucObj1['ID'] = strucId
    strucObj1['F_LWLAWID'] = row[0]
    strucObj1['F_BASETABLEID_SECTIONTYPE'] = 39
    strucObj1['HIERARCHY'] = '.'+str(strucId)+'.'
    strucList.append(tuple(strucObj1.values()))

    strucId += 1
    sectionId += 1

    sectionObj2={'ID':'','CAPTION':'','F_PARENTID':'','F_CMBASETABLEID_SECTIONSTATUS':'','F_LWLAWSTRUCTUREID':'',
                'SECTIONTEXT':'','SECTIONLEVEL':'','TEXTORDER':'','STATENO':'','SECTIONTYPENO':'',
                'F_LWLAWID':'','F_LWPHASEID':'','OLDID':'','FULLPATH':'','SECTIONTYPENOTEXT':'',
                'FIRSTSATENO':'','LASTSTATENO':'','F_LWSECTIONID_REPLACED':'','HIERARCHY':'',
                'DISPLAYINCONTENTS':'','F_LWLAWCHANGEID':'','TMP':'','F_LWLAWCHANGEID_FIRST':'',
                'F_LWLAWCHANGEID_LAST':'','ISINTERPRETATION':''
                }
    sectionObj2['ID'] = sectionId
    sectionObj2['CAPTION'] = ''
    sectionObj2['F_PARENTID'] = ''
    sectionObj2['F_CMBASETABLEID_SECTIONSTATUS'] = lawType(row[17])
    sectionObj2['F_LWLAWSTRUCTUREID'] = strucId
    sectionObj2['SECTIONTEXT'] = row[4]
    sectionObj2['SECTIONLEVEL'] = 1
    sectionObj2['TEXTORDER'] = 2
    sectionObj2['STATENO'] = 1
    sectionObj2['SECTIONTYPENO']=''
    sectionObj2['F_LWLAWID'] = row[0]
    sectionObj2['F_LWPHASEID'] = phaseId
    sectionObj2['OLDID'] = ''
    sectionObj2['FULLPATH'] = 'متن'
    sectionObj2['SECTIONTYPENOTEXT']=''
    sectionObj2['FIRSTSATENO'] = 1
    sectionObj2['LASTSTATENO'] = 0
    sectionObj2['F_LWSECTIONID_REPLACED']=''
    sectionObj2['HIERARCHY']= '.'+str(sectionId)+'.'
    sectionList.append(tuple(sectionObj2.values()))

    strucObj2={'ID':'','OLDID':'','F_LWLAWID':'','F_PARENTID':'','LEVELNO':1,
              'F_BASETABLEID_SECTIONTYPE':'','NUMBERINGMETHOD':2,'HIERARCHY':''
              }
    strucObj2['ID'] = strucId
    strucObj2['F_LWLAWID'] = row[0]
    strucObj2['F_BASETABLEID_SECTIONTYPE'] = 35
    strucObj2['HIERARCHY'] = '.'+str(strucId)+'.'
    strucList.append(tuple(strucObj2.values()))

    strucId += 1
    sectionId += 1
    phaseId += 1
    approverId +=1
#---------------------------------add votes-------------------

for row in votes:
    lawObj={'ID':'','OLDID':'','CAPTION':'','F_LWBASETABLEID_LAWTYPE':'','F_LWBASETABLEID_CLASSIFICATION':'',
            'RULENO':'','LAWNO':'','APPROVEDATE':'','F_CMBASETABLEID_LASTSTATUS':'','HASEXCEPTION':'','ISLAW':'',
            'ISREGULATION':'','ISCORRECTIONLETTER':'','ISOPINION':'','OPINIONNO':'','CONGRESSNO':'','ISCONGRESS':'',
            'F_LWBASETABLEID_REGULATIONTYPE':'','HASNOTE':'0','EXPIREDATE':'','CONTENTTEXT':'','OLDLAWTYPEID':'',
            'OLDREGULATIONTYPEID':'','OLDLAWNO':'','OLDRULENO':'','LASTEXPIREDATE':'','ISBASEINFOCONFIRMED':'',
            'ISSTRUCTURECONFIRMED':'','ISTOPICCONFIRMED':'','ISEXECUTORCONFIRMED':'','ISREFERCONFIRMED':'',
            'ISCHANGECONFIRMED':'','ISDOCSCONFIRMED':'','ISKEYWORDCONFIRMED':'','ISDOCSCONFIRMEDFIRST':'',
            'ISDOCSCONFIRMEDSECOND':'','ISORGREGULATIONDRAFT':'','ISORGREGULATIONDRAFTCONFIRM':'',
            'ORGREGULATIONDRAFTCONFIRMDATE':'','OLDID_LOH':'','OLDSHNO':''
            }

    lawObj['ID'] = row[0]
    lawObj['OLDID'] = row[0]
    lawObj['CAPTION'] = row[1]
    lawObj['APPROVEDATE'] = dateParser(row[8])
    lawObj['ISLAW'] = 0
    lawObj['ISREGULATION'] = 0
    lawObj['ISOPINION'] = 1
    lawObj['OPINIONNO'] = opinionno
    
    lawList.append(tuple(lawObj.values()))
    opinionno = +1

    prdocObj={'ID':'','DOCTEXT':'','OLDID_MAJLES':'','OLDID_MAJLES_FINALDEC_FLOWDTL':'',
              'OLDID_RULMAJLESMATNID':'','OLDID_NAZARAT':'','F_RULNAZARID':''
             }
    prdocObj['ID'] = prodocId
    prdocObj['DOCTEXT'] = row[4]
    prodocList.append(tuple(prdocObj.values()))

    opinionObj={'ID':'','subject':'','OPINIONLETTERNO':'','OPINIONDATE':'','REGISTRATIONNO':'','ARCHIVENO':'',
            'F_CMBASETABLEID_CLASSIFICATION':'','F_OPOPINIONGIVERID':'','F_OPOPINIONGIVERPERSONID':'',
            'F_LWLAWID':'','ISELEMENTARY':'','DISTRIBUTENO':'','DISTRIBUTEDATE':'','F_PRDOCID':'',
            'REALPERSONRECEIVE':'','HASNOTE':'','THECOMMENT':'','OLDID':'','ISBASEINFOCONFIRMED':'',
            'ISBASEDOCCONFIRMED':'','ISTOPICCONFIRMED':'','ISKEYWORDCONFIRMED':'','ISHISTORYCONFIRMED':'',
            'DOSSIERCLASS':'','TOTALIMAGE':''
            }
    opinionObj['ID'] = opinionId
    opinionObj['subject'] = row[1]
    opinionObj['OPINIONLETTERNO'] = ''
    opinionObj['OPINIONDATE'] = dateParser(row[8])
    opinionObj['F_OPOPINIONGIVERID'] = opGiver(row[7])
    opinionObj['F_OPOPINIONGIVERPERSONID'] = ''
    opinionObj['F_LWLAWID'] = row[0]
    opinionObj['F_PRDOCID'] = prodocId
    opinionObj['REALPERSONRECEIVE'] = 0
    opinionObj['HASNOTE'] = 0
    opinionList.append(tuple(opinionObj.values()))

    opinionId += 1
    prodocId += 1

c.executemany("INSERT INTO lwlaw VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",lawList)
conn.commit()
c.executemany("INSERT INTO lwphase VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",phaseList)
conn.commit()
c.executemany("INSERT INTO lwapprover VALUES(?,?,?,?,?,?)",approveList)
conn.commit()
c.executemany("INSERT INTO lwsection VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",sectionList)
conn.commit()
c.executemany("INSERT INTO lwexecutor VALUES(?,?,?,?)",execList)
conn.commit()
c.executemany("INSERT INTO lwreceiver VALUES(?,?,?,?)",reciveList)
conn.commit()
c.executemany("INSERT INTO prdoc VALUES(?,?,?,?,?,?,?)",prodocList)
conn.commit()
c.executemany("INSERT INTO opopinion VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",opinionList)
conn.commit()
c.executemany("INSERT INTO lwlawstructure VALUES(?,?,?,?,?,?,?,?)",strucList)
conn.commit()