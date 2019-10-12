import sqlite3

class Database:
    
    def __init__(self, csv_url, db_url):
        self.csv_url = csv_url
        self.db_url = db_url
        self.conn = None

    def connect_to_db(self):
        """
        Connects to a db if that db doesn't exist it creates a new one
        """
        self.conn = sqlite3.connect(self.db_url)
        return self.conn
    
    def create_words_table(self):

        cursor = self.conn.cursor()
        sql_command = "DROP TABLE IF EXISTS data; CREATE TABLE data (id INTEGER, deutsch VARCHAR, english VARCHAR, PRIMARY KEY(id))"
        cursor.executescript(sql_command)
    
    def insert_csv(self):
        sql_command = "INSERT INTO data (deutsch, english) values (?,?)"

        file = open(csv_url)
        csv_reader = csv.reader(file, delimiter=",")
        cursor = self.conn.cursor()
        data = list()

        #retrieve from csv
        for row in csv_reader:
            data.append(row)

        #add to db
        for row in range(len(data)):
            cursor.execute(sql_command,(str(data[row][0]),str(data[row][1])))
        self.conn.commit()
        

    def read_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM data")
        return cursor.fetchall()

    def length_db(self):
        cursor = self.conn.cursor()
        data = self.read_all()
        return len(data)

    def get_row(self,row_num):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM data WHERE id={str(row_num+1)}")
        return cursor.fetchone()
    
    
            


        

