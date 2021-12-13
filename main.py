import argparse
from json_read_file import JsonLoad
from connect_db import ConnectorDb
from writer_fIle import JsonWriter
from select_db import SelectDb


def args_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('students_path', type=str, help='Path students file.')
    parser.add_argument('rooms_path', type=str, help='Path rooms file.')
    parser.add_argument('out_format', type=str, help='Source file format(json/xml).')
    args = parser.parse_args()
    return args


def main():
    args = args_parsing()
    format_args = ['xml', 'json']
    if args.out_format not in format_args:
        raise ValueError('Invalid format.')
    db = ConnectorDb()
    db.create_db()
    db.create_table_rooms()
    db.create_table_students()
    db.insert_rooms(JsonLoad.read_json(args.rooms_path))
    db.insert_students(JsonLoad.read_json(args.students_path))
    db.commit()

    if args.out_format == 'json':
        qry = SelectDb.get_number_of_students()
        JsonWriter.write(db.get_select(qry), name='number_of_students')




if __name__ == '__main__':
    # python main.py D:\Tasks_LeverX_Group\Tasks3_parser_json_and_mysql\students.json D:\Tasks_LeverX_Group\Tasks3_parser_json_and_mysql\rooms.json json
    main()
