import sqlite3

#---------------------InitializeValue--------------------------
conn = sqlite3.connect("Update.db")
c = conn.cursor()
c.execute("""CREATE TABLE "Votes" (
	"Id"	INTEGER NOT NULL,
	"Title"	TEXT,
	"approvalRef"	TEXT
)""")
conn.commit()
conn.close()

conn = sqlite3.connect("Final.db")
c = conn.cursor()
c.execute('''CREATE TABLE "Votes" (
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
conn.close()