from typing import List


def list_files(parent_directory, current_filepath="") -> List:
    file_list = []

    for key, value in parent_directory.items():
        new_filepath = current_filepath + "/" + key
        if not value:
            file_list.append(new_filepath)
        else:
            file_list.extend(list_files(value, new_filepath))

    return sorted(file_list)
