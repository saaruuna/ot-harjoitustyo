from logic.lab import Lab
from database_connection import get_database_connection

def get_lab_by_row(row):
    """The method to transform a given row fetched from the database into
        a Lab object.

    Args:
        row: The row fetched from the database.

    Returns:
        A Lab object.
    """

    new_map = []
    name = row['name']
    lab_map = row['map'].split("#")
    size = row['size']

    map_as_int = []

    for variable in lab_map:
        map_as_int.append(int(variable))

    i = 0
    j = 0

    while i < size:
        new_map.append(map_as_int[j:j+size])
        j += size
        i += 1

    return Lab(name, new_map)

class LabRepository:
    """A class to interface with the lab database.

    Attributes:
        _connection: The connection to the database.
    """

    def __init__(self, connection):
        """The class contructor, which creates a new LabRespository.

        Attributes:
            _connection: The connection to the database.

        Args:
            connection: The connection to the database.
        """

        self._connection = connection

    def find_all(self):
        """The method to fetch all labs from the database.

        Returns:
            A list of Lab objects.
        """

        cursor = self._connection.cursor()

        cursor.execute('select * from labs')

        rows = cursor.fetchall()

        return list(map(get_lab_by_row, rows))

    def find_by_name(self, name):
        """The method to find a lab by a certain name.

        Args:
            name: the name of the lab we want.

        Returns:
            A Lab object.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from labs where name = ?',
            (name,)
        )

        row = cursor.fetchone()

        return get_lab_by_row(row)

    def add_lab(self, name, lab_map, size):
        """The method to insert a lab into the database.

        Args:
            name: The name of the lab we wish to insert.
            lab_map: The lab_map of the lab we wish to insert.
            size: The size of the lab we wish to insert.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into labs (name, map, size) values (?, ?, ?)',
            (name, lab_map, size, )
        )

        self._connection.commit()

    def contains_lab(self, name):
        """The method to check whether the database contains a lab with a
        certain name.

        Args:
            name: The name of the lab we are checking for.

        Returns:
            True, if the database does not contain a lab of the given name.
            False, if the database contains a lab of the given name.
        """

        contains_lab = False

        cursor = self._connection.cursor()

        cursor.execute(
            'select name from labs',
        )

        lab_names = cursor.fetchall()

        for lab_name in lab_names:
            if lab_name[0] == name:
                contains_lab = True

        return contains_lab

lab_repository = LabRepository(get_database_connection())
