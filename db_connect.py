
import mysql.connector as mc
class mysql():
    def __init__(self):
        self.mydb = mc.connect(
            host="localhost",
            user="root",
            password="rushabh@75",
            auth_plugin='mysql_native_password',
            db='project'
        )
        self.mycursor = self.mydb.cursor()

