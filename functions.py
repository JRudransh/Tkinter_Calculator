numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e']
operator_list = ['+', '-', '*', '**', '(', ')', '÷']
dot_list = ['.']
got_operator = False
got_point = True
string_fill = "0"

# Function for validation


def get_value(values):
    string = ""
    for value in values:
        if value in numbers_list or value in operator_list or value in dot_list:
            string = string + value
    if values == '0':
        string = ""
    return string
