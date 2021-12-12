
class InsertTables:

    @staticmethod
    def insert_rooms():
        return 'INSERT INTO Rooms(id, name) ' \
               'VALUES(%s, %s)'

    @staticmethod
    def insert_students():
        return 'INSERT INTO Students(id, name, birthday, room, sex)' \
               ' VALUES(%s, %s, %s, %s, %s)'