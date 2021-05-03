from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('drop table if exists labs;')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('create table labs (name text primary key, map text, size integer);')

    map1 = '1#1#1#1#1#1#0#0#0#1#1#3#2#4#1#1#0#0#0#1#1#1#1#1#1'
    map2 = '1#1#1#1#1#1#3#2#0#1#1#0#2#4#1#1#0#0#0#1#1#1#1#1#1'
    map3 = '1#1#1#1#1#1#1#0#0#0#3#1#1#0#1#1#0#1#1#0#1#1#0#1#1#4#0#0#2#1#1#1#1#1#1#1'
    map4 = '3#3#3#3#3#3#3#3#0#0#0#0#0#3#3#0#3#3#3#0#3#3#0#2#0#3#0#3#3#0#3#0#3#0#3#3#0#0#0#3#0#3#3#3#3#3#3#4#3'
    map5 = '0#0#0#1#3#0#1#0#1#0#0#1#0#1#0#0#1#0#2#0#4#1#0#0#0'

    cursor.execute(
        'insert into labs (name, map, size) values (?, ?, ?)',
        ("DEMO1", map1, 5, )
    )

    cursor.execute(
        'insert into labs (name, map, size) values (?, ?, ?)',
        ("DEMO2", map2, 5, )
    )

    cursor.execute(
        'insert into labs (name, map, size) values (?, ?, ?)',
        ("DEMO3", map3, 6, )
    )

    cursor.execute(
        'insert into labs (name, map, size) values (?, ?, ?)',
        ("heaven", map4, 7, )
    )

    cursor.execute(
        'insert into labs (name, map, size) values (?, ?, ?)',
        ("DEMO4", map5, 5, )
    )

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
