import sqlite3 as sq
import tableUtils as tb

print("sql version ",sq.version_info[0],".",sq.version_info[1],".",sq.version_info[2])

[curs,conn]=tb.GetCursor('movie.db')
tb.deleteTable(curs,"movie_list")
tb.CreateTable(curs,"movie_list",["name","year"])

tb.InsertData(curs,"movie_list",["\"shak\"","\"1998-9-2\""])

tb.InsertMany(curs,"movie_list",[("\"shakw\"","\"1938-9-2\""),("\"6hakw\"","\"4938-9-2\""),("\"s3akw\"","\"1938-9-6\""),("\"shkw\"","\"1938-1-2\"")])

tb.tableSelectAll(curs,"movie_list")
tb.selectTableWhere(curs,"movie_list",['''name="shak"'''])

conn.commit()



conn.close()