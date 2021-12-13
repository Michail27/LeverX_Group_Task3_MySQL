class SelectDb:
    @staticmethod
    def get_result_select():
        rez = {'number_of_students_rooms': '''SELECT rooms.id, rooms.name, COUNT(students.id) as number_of_students 
                                               FROM rooms JOIN students ON rooms.id = students.room
                                               GROUP BY rooms.id''',

               'top5_rooms_where_min_avg_age': '''SELECT rooms.id, rooms.name, 
                                               cast(avg(year(current_timestamp)-year(students.birthday)) AS UNSIGNED) 
                                               as avg_age
                                               FROM rooms JOIN students ON rooms.id = students.room
                                               GROUP BY rooms.id
                                               ORDER BY avg_age
                                               LIMIT 5''',

               'top5_rooms_with_max_dif_age': '''SELECT rooms.id, rooms.name, 
                                                (max(year(current_timestamp)-year(students.birthday)) - 
                                                min(year(current_timestamp)-year(students.birthday))) as dif_age
                                                FROM rooms JOIN students ON rooms.id = students.room
                                                GROUP BY rooms.id
                                                ORDER BY dif_age desc
                                                LIMIT 20''',

               'rooms_where_sex_M_F': '''SELECT rooms.id, rooms.name
                                        FROM rooms JOIN students ON rooms.id = students.room
                                        GROUP BY rooms.id
                                        HAVING COUNT(DISTINCT students.sex) > 1'''}

        return rez
