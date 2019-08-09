import sqlite3 as sq

def GetCursor(dbName):
    conn=sq.connect(''+dbName)
    curs=conn.cursor()
    return curs,conn


def CreateTable(curs,table_name,attr_names):
    p="create table "+table_name+" ("
    for m in attr_names:
        if m!=attr_names[-1]:
            p=p+" "+m+","
        else :
            p=p+" "+m
    p=p+")"

    curs.execute(p)

def InsertData(curs,table_name,attr_values):
    try:
        p="insert into "+table_name+" values ("
        for m in attr_values:
            if m!=attr_values[-1]:
                p=p+" "+m+","
            else :
                p=p+" "+m
        p=p+")"

        curs.execute(p)
    except ValueError :
        print("ERROR CHECK VALUE TYPES")    

def deleteTable(curs,table_name):
    curs.execute('drop table '+table_name)

def InsertMany(curs,table_name,value_list):
    count=len(value_list[0])
    p='('
    for i in range(count):
        if(i<count-1):
            p=p+'?,'
        else:
            p=p+'?)'
    curs.executemany('INSERT INTO '+table_name+' Values '+p,value_list)

def tableSelectAll(curs,table_name):
    for p in curs.execute('Select * from '+table_name):
        print (p)
def selectTableWhere(curs,table_name,conditions):
    k='Select * from '+table_name+" where "
    for stri in conditions:
        if stri != conditions[-1]:
            k=k+stri+","
        else:
            k=k+stri
    for p in curs.execute(k):
        print (p)