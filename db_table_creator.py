
class DbTables:

    @staticmethod
    def create_db():
        return '''CREATE DATABASE IF NOT EXISTS  test_db'''

    @staticmethod
    def create_table_room():
        return '''CREATE TABLE IF NOT EXISTS rooms (id INTEGER NOT NULL,
                                                    name VARCHAR(250) NOT NULL,
                                                    PRIMARY KEY(id))'''

    @staticmethod
    def create_table_students():
        return ''' CREATE TABLE IF NOT EXISTS students (id INTEGER NOT NULL,
                                          name VARCHAR(250) NOT NULL,
                                          birthday DATETIME,
                                          room INTEGER NOT NULL,
                                          sex CHAR(10) NOT NULL,
                                          PRIMARY KEY(id),
                                          FOREIGN KEY(room) REFERENCES Rooms(id) ON DELETE CASCADE)'''

    @staticmethod
    def drop_tables():
        return ['DROP TABLE Rooms', 'DROP TABLE Students']
