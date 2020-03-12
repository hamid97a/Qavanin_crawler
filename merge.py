import sqlite3

#---------------------InitializeValue--------------------------

rules = []
regulations = []
votes = []

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

conn = sqlite3.connect("Final.db")
c = conn.cursor()
c.execute('''CREATE TABLE "Rules" (
	"Id"	INTEGER NOT NULL,
	"Title"	    TEXT,
	"executingDevices"	TEXT,
	"transcriptRecipients"	TEXT,
	"text"      TEXT,
	"lawType"	TEXT,
	"classification"	TEXT,
	"approvalRef"	TEXT,
	"approvalDate"	DATE,
	"documentDate"	DATE,
	"documentNumber"	TEXT,
	"announcementNumber"	TEXT,
	"announcementDate"	DATE,
	"announcementRef"	TEXT,
	"executionDate"	DATE,
	"newspaperNum"	TEXT,
	"newspaperDate"	DATE,
	"lastStatus"	TEXT,
	"firstStatus"	TEXT
)''')

conn.commit()
c.executemany("INSERT INTO Rules VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rules)
c.executemany("INSERT INTO Rules VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",regulations)
c.executemany("INSERT INTO Rules VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",votes)
conn.commit()
conn.close()