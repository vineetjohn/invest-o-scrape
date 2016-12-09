
def get_file_line_iterator(file_path):
    with open(file_path) as file_object:
        for line in file_object:
            yield line
