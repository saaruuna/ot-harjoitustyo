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
        lab_map_string = self._generate_lab_map_string(lab_map, size)

        cursor.execute(
            'insert into labs (name, map, size) values (?, ?, ?)',
            (name, lab_map_string, size, )
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

    def _generate_lab_map_string(self, lab_map, size):
        """A method to generate an appropriate string to describe the lab_map
            that can be inserted into the database.

        Args:
            lab_map: The lab_map which we want to generate a string from.

        Returns:
            string lab_map_string, which is built from the lab map.
        """

        lab_map_string = ""

        i=0
        for row in lab_map:
            j=0
            for element in row:
                if i == size - 1 and j == size - 1:
                    lab_map_string += str(element)
                else:
                    lab_map_string += str(element)+"#"
                j+=1
            i+=1

        return lab_map_string

lab_repository = LabRepository(get_database_connection())
