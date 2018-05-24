question_table = ['','','','','','','']
answer_table = ['','','','','','']


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table

def write_table_to_file(file_name, table):
    with open(file_name, "a") as file: 
        row = ';'.join(table)
        file.write("\n" + row)
    return table