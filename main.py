import argparse
from json_read_file import JsonLoad
from connect_db import ConnectorDb
from writer_fIle import JsonWriter, XmlWriter
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
    format_out = {'json': JsonWriter(), 'xml': XmlWriter()}
    db = ConnectorDb()
    db.create_db()
    db.create_table_rooms()
    db.create_table_students()
    db.insert_rooms(JsonLoad.read_json(args.rooms_path))
    db.insert_students(JsonLoad.read_json(args.students_path))
    db.create_index_roomid_in_students()
    db.commit()
    try:
        for name, qry in SelectDb.get_result_select().items():
            format_out[args.out_format].write(result_list=db.get_select(qry), name=name)
    except KeyError:
        raise ValueError('This format is not supported')
    db.drop_tables()


if __name__ == '__main__':
    main()
