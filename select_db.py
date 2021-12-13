class SelectDb:
    @staticmethod
    def get_number_of_students():
        return '''SELECT rooms.id, rooms.name, COUNT(students.id) as number_of_students 
                  FROM Rooms JOIN Students ON Rooms.id = Students.room
                  GROUP BY rooms.id'''
