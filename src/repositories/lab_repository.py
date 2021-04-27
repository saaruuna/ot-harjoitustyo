from ui.lab import Lab
from database_connection import get_database_connection

def get_lab_by_row(row):
    new_map = []
    name = row['name']
    map = row['map'].split("#")
    size = row['size']

    map_as_int = []

    for variable in map:
        map_as_int.append(int(variable))

    i = 0
    j = 0

    while i < size:
        new_map.append(map_as_int[j:j+size])
        j += size
        i += 1

    return Lab(name, new_map)

class LabRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute('select * from labs')

        rows = cursor.fetchall()

        return list(map(get_lab_by_row, rows))

    def find_by_name(self, name):
        cursor = self._connection.cursor()

        cursor.execute(
            'select * from labs where name = ?',
            (name,)
        )

        row = cursor.fetchone()

        return get_lab_by_row(row)

lab_repository = LabRepository(get_database_connection())
