import mysql.connector

from settings import SETTINGS
from db_table_creator import DbTables
from insert_tables import InsertTables


class ConnectorDb:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host=SETTINGS['host'],
            user=SETTINGS['user'],
            passwd=SETTINGS['password'],
            database=SETTINGS['database']
        )
        self.cursor = self.connector.cursor()

    def create_db(self):
        self.cursor.execute(DbTables.create_db())

    def create_table_rooms(self):
        self.cursor.execute(DbTables.create_table_room())

    def create_table_students(self):
        self.cursor.execute(DbTables.create_table_students())

    def drop_tables(self):
        for table in DbTables.drop_tables():
            self.cursor.execute(table)

    def insert_rooms(self, list_rooms):
        for room in list_rooms:
            self.cursor.execute(InsertTables.insert_rooms(), (room['id'],
                                                              room['name']))

    def insert_students(self, students_list):
        for student in students_list:
            self.cursor.execute(InsertTables.insert_students(), (student['id'],
                                                                 student['name'],
                                                                 student['birthday'],
                                                                 student['room'],
                                                                 student['sex']))

    def commit(self):
        self.connector.commit()
