import os
import pymysql

# get username from workspace

username = os.getenv('C9_USER')

# connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # delete many rows with WHERE IN command:
    with connection.cursor() as cursor:
        names = ['jum', 'bob']
        cursor.execute("DELETE FROM Friend WHERE name in (%s, %s)", names )
        connection.commit()



    # to delete many
    # with connection.cursor() as cursor:
    #     row = cursor.executemany("Delete From Friends Where name = %s ;", ['bob', 'Stan'])
    #     connection.commit()

        # to delete:
        # rows =  cursor.execute("DELETE FROM Friends WHERE name ='Bob';")
        # connection.commit()
    
    # update many
    # with connection.cursor() as cursor:
    #     rows = [(23, 'Bob'),
    #             (27, 'Stan'),
    #             (74, 'Jim')]
    #     cursor.executemany("UPDATE Friends SET age = %s WHERE name= %s;", rows)
    #     connection.commit()
  
  
    # # Run a query
    # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #     row = [("Bob", 30, "1990-09-06 21:21:21"),
    #           ("Stan", 28, "1991-11-23 17:16:15"),
    #           ("Jim", 56, "1958-10-10 12:12:25")]
    #     cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", row)
    #     connection.commit()

        # result = cursor.fetchall()
        # print(result)
        # for row in cursor:
        #     print(row)
finally:
    # Close the connection to sql
    connection.close()
