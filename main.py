from functions import output_data, input_data, del_data, search_data, blue_text, orange_text, yellow_text, red_text, \
    green_text


def task():
    print(f"\n\n"
          f"{orange_text('******* ACTIONS *******')}\n\n"
          f"Read Existing Data: {yellow_text('R')}\n"
          f"Input New Data: {yellow_text('I')}\n"
          f"Delete Old Data: {yellow_text('D')}\n"
          f"Search Data: {yellow_text('S')}\n"
          f"Exit: {yellow_text('E')}"
          f"")

    n = input(blue_text('\nTask [R/I/D/S/E]: '))
    if n.upper() == 'R':
        output_data()
        task()
    elif n.upper() == 'I':
        input_data()
        task()
    elif n.upper() == 'D':
        del_data()
        task()
    elif n.upper() == 'S':
        search_data()
    elif n.upper() == 'E':
        print(green_text('\nThank You!\n'))
        exit()
    else:
        print(red_text("\nENTER A VALID OPTION!"))
        task()


if __name__ == "__main__":
    while True:
        task()
