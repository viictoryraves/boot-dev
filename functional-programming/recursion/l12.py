from typing import List


def list_files(parent_directory, current_filepath="") -> List:
    file_list = []

    for key in parent_directory.keys():
        new_filepath = current_filepath + "/" + key
        if parent_directory[key] is None:
            file_list.append(new_filepath)
        else:
            file_list.extend(list_files(parent_directory[key], new_filepath))

    return sorted(file_list)
