import re
import csv

task_data = [
    "Изготовитель системы",
    "Название ОС",
    "Код продукта",
    "Тип системы",
]

name_file = [
    'info_1.txt',
    'info_2.txt',
    'info_3.txt',
]


def get_data(files, data):

    result_list = [data[:]]  # create heading in list
    row = []

    for file in files:
        with open(file, encoding='windows 1251') as f:
            str = f.read()
        for heading in data:
            row.append(re.findall(heading + r".*", str)
                       [0].split('  ')[-1].strip())
        result_list.append(row[:])
        row.clear()

    return result_list


def write_to_csv():
    with open('task1.csv', 'w') as f:
        f_writer = csv.writer(f)
        for row in get_data(name_file, task_data):
            f_writer.writerow(row)


if __name__ == "__main__":

    print(get_data(name_file, task_data))
    write_to_csv()
