""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    ALIGN_PADDING = 4
    col_num = len(title_list)
    row_num = len(table)
    len_list = []
    max_lens = [len(title) + ALIGN_PADDING for title in title_list]
    # Counting longest string in every column
    for i in range(col_num):
        for j in range(row_num):
            len_list.append(len(table[j][i]) + ALIGN_PADDING)
        if max_lens[i] < max(len_list):
            max_lens[i] = max(len_list)
        len_list = []
    # Top
    draw_the_line(max_lens)
    # Headers
    fill_row_with(title_list, max_lens)
    # Body
    for i in range(row_num):
        for val in max_lens:
            print("|" + ("-" * val), end='')
        print(" |")
        fill_row_with(table[i], max_lens)
    # Bottom
    draw_the_line(max_lens)
    # your goes code


def fill_row_with(row, max_lens):
    for i in range(len(row)):
        print("|{0:^{1}}".format(row[i], max_lens[i]), end='')
    print(" |")


def draw_the_line(max_lens, char1='#', char2='-'):
    print(char1, end='')
    for val in max_lens:
        print(char2 * val + char2, end='')
    print(char1)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print('{}:'.format(label))

    if type(result) is str:
        print(result)
    elif type(result) is list:
        for i in result:
            print(i,  end=" ")
            print(", ",  end=" ")
        print(" ")
    elif type(result) is dict:
        for i in result:
            print('{}: {}'.format(i, result[i]))


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    print("\n" + title + ":")

    for i in range(len(list_options)):
        formatted_options = ("({}) {}".format(i + 1, list_options[i]))
        print("{:>{}}".format(formatted_options, len(formatted_options) + 1))

    formatted_exit_option = ("({}) {}".format(0,exit_message))
    print("{:>{}}".format(formatted_exit_option, len(formatted_exit_option) + 1))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    # your code
    inputs = []
    print(title)
    for prompt in list_labels:
        inputs.append(input(prompt))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """


    # your code
    print("ERROR: " + message)
    print('')
