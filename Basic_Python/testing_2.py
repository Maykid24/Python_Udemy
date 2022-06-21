from datetime import datetime

file_name_list = []


def file_name():
    file_name_format = datetime.now().strftime('%Y%m%d_%H-%M-%S')
    file_name_list.append(file_name_format)
    print(file_name_list)

