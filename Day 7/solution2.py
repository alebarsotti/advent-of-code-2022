from Utils.Color import print_color, Color


class File:
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def __str__(self):
        return f'File name: {self.get_name()} - Size: {self.get_size()}'


class Directory:
    def __init__(self, name, parent):
        self.__name = name
        self.__parent = parent
        self.__children = []

    def get_name(self):
        return self.__name

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def get_size(self):
        return sum([child.get_size() for child in self.__children])

    def add_child(self, child):
        self.__children.append(child)

    def __str__(self):
        return f'Dir name: {self.get_name()} - Parent: {self.get_parent()} - Children: {len(self.get_children())}'

    def __repr__(self):
        return self.__str__()


def is_cd(line):
    return is_command(line) and line[1] == "cd"


def is_cd_back(line):
    return line[2] == ".."


def is_ls(line):
    return is_command(line) and line[1] == "ls"


def is_command(line):
    return line[0] == '$'


def is_directory(line):
    return line[0] == "dir"


def get_file_size(line):
    return int(line[0])


TOTAL_SPACE = 70_000_000
SPACE_AVAILABLE_NEEDED = 30_000_000
MAX_DIRECTORY_SIZE = 100_000
directories = []
current_directory = None
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        if is_cd(line):
            if is_cd_back(line):
                current_directory = current_directory.get_parent()
            else:
                new_directory_name = line[2]
                directory_children = current_directory.get_children() if current_directory is not None else []
                new_directory = next(
                    filter(lambda directory: directory.get_name() == new_directory_name, directory_children), None)

                if new_directory is None:
                    current_directory = Directory(name=new_directory_name, parent=current_directory)
                else:
                    current_directory = new_directory

                directories.append(current_directory)
        elif not is_ls(line):
            if is_directory(line):
                current_directory.add_child(Directory(name=line[1], parent=current_directory))
            else:
                current_directory.add_child(File(name=line[1], size=get_file_size(line)))

parent_directory = next(filter(lambda directory: directory.get_name() == "/", directories), None)
space_to_delete = SPACE_AVAILABLE_NEEDED - (TOTAL_SPACE - parent_directory.get_size())
print(f'\nEspacio que necesita ser eliminado: {space_to_delete}')

to_delete = filter(lambda directory: directory.get_size() >= space_to_delete, directories)

directory_to_delete = min(to_delete, key=lambda x: x.get_size())

total_size = 0
print(f'\nEl directorio más chico a ser eliminado es: {print_color(f"{directory_to_delete.get_name()} - Size: {directory_to_delete.get_size()}", Color.RED)}')
