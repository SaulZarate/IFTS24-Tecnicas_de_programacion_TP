import mariadb 

mydb = mariadb.connect(
    host="127.0.0.1",
    user="root",      
    database = "VIDEOCLUB",
    autocommit=True
)