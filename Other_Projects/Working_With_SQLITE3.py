import sqlite3


class WrongDataInputError(BaseException):
    pass

class sqlite_database:

    def __init__(self, name):
        self.name = name

    def create_db(self):

        self.conn = sqlite3.connect("{}.db".format(self.name))
        self.cur = self.conn.cursor()
        print("Connected to:", self.name)

    def create_table(self, tablename):

        self.tablename = tablename

        if self.db_item_exists("table", self.tablename):
            print('!!!!!! Table already exists!')

        else:

            __statement = """ CREATE TABLE {}(
                                id INT PRIMARY KEY,
                                headline CHAR(255),
                                posted_date DATE
                            );
                            """.format(tablename)

            self.cur.execute(__statement)

            print("Table created named: " + tablename)

    def db_item_exists(self, data_type, data_name):

        if data_type == "table":

            self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''', (data_name, ))

            if self.cur.fetchone():
                return True
            else:
                return False

        ## only works with Headlines table
        elif data_type == "data_entry":

            __statement = """SELECT id FROM Headlines WHERE id=""" + str(data_name)
            self.cur.execute(__statement)

            if self.cur.fetchone():
                return True
            else:
                return False

        else:
            print("Unrecognized data type!")

    def insert_into_db(self, headline_id, headline, posted_date):

        ## only works with Headlines table

        if Headlines.db_item_exists("data_entry", headline_id) != True:

            self.cur.execute('INSERT INTO Headlines (id, headline, posted_date) VALUES (?,?,?)', (headline_id, headline, posted_date))
            self.conn.commit()

        else:

            print("!!!!!! Data insertion failed, you need a unique data item")

    def return_from_db(self, value):

        id_from_input = ""
        headline_from_input = ""
        posted_date_from_input = ""

        try:
            if value == "all":

                id_from_input = "id,"
                headline_from_input = "headline,"
                posted_date_from_input = "posted_date"

            elif value == "id":

                id_from_input = "id,"

            elif value == "headline":

                headline_from_input = "headline,"

            elif value == "date":

                posted_date_from_input = "posted_date"

            else:
                raise WrongDataInputError

            statement = "SELECT " + id_from_input + headline_from_input + posted_date_from_input + " FROM Headlines"
            self.cur.execute(statement)

            table = self.cur.fetchall()
            for i in table:
                print(i)

        except WrongDataInputError:
            print("Wrong input data!")

    def closedb(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

Headlines = sqlite_database("database")
Headlines.create_db()
Headlines.create_table("Headlines")
Headlines.insert_into_db(2, "Gaint zebra breaks out of zoo!", "03-23-20")
Headlines.return_from_db("all")
Headlines.closedb()



