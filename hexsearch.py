# program to convert strings into hex, and then find the hex strings in a hex grid and return the co-ordinates
import time


def formulate_grid(input_grid):
    """Function that will take the raw input from a provided grid file and transform it into a workable 2D list format

    :param input_grid: Raw data is stored in the input grid variable, assuming each row is on its own line, the file can
    be read line by line. Assuming each valuable data entry is tab delimited, we can use .split("\t") to create a 2D
    list with each row containing "x" number of entries, and number of rows determined by the number of lines in the raw
    file. The number of columns is equal to the number of row entries "x", and in a 2D list any entry can be found using
    slicing, ie. grid[row][column]
    :type: list[str]
    """
    if not isinstance(input_grid, list):
        return "formulate grid is expecting an input in the form of a list! Please check the file containing the grid!"

    # empty lists to contain worked data from the raw grid
    grid_rows = []
    individual_row = []

    # each line in the raw data is read as an entry in a list and corresponds to a row. This configures each row into
    # a 2D list by splitting each valuable piece of data into its own entry, on that row entry, ie. [row][valuable_data]
    # as well as removing the unwanted \t notation from the string
    input_rows = [i.split("\t") for i in input_grid]

    # this now takes each entry in the grid and adds "0x" in front of it so this program can properly read it as a
    # hex-decimal. It also removes the \n notation at the end of each row as this is also unwanted in the output
    for i in range(0, len(input_rows)):
        for j in range(0, len(input_rows[i])):
            individual_row.append(("0x" + input_rows[i][j].lower().replace("\n", "")))

            if j == (len(input_rows[i]) - 1):
                grid_rows.append(individual_row)
                individual_row = []

    completed_grid = grid_rows

    # once each entry on each row is processed, each row is appended to a list creating a 2D list,
    # which is then returned
    return completed_grid


def convert_hex_string_to_hex_decimal():
    """Function that when called, will create a list of hex entries to search for in the grid from the strings
    defined below
    """

    # the strings needed in UTF-8 encoding
    utf8_strings = ["Christmas\n", "Presents", "@iant"]

    # the strings needed in UTF-16-be encoding
    utf16_strings = ["Dstl"]

    # the strings needed in u8,u8,16 encoding
    u8_u8_u16_strings = ["25", "12", "2017"]

    # the strings needed in u32 encoding
    u32_strings = ["1514160000"]

    # the strings needed in u8 encoding
    u8_4_strings = [["127", "0", "0", "10"], ["192", "168", "0", "1"]]

    # the strings needed in u8 encoding - this is already in hex!
    u8_6_strings = ["07", "9D", "72", "8E", "A3", "61"]

    # the strings to find, converted into hex
    strings_in_hex = []

    # convert the UTF-8 strings to hex and append them to a list of hex entries to search
    # store_string is used to group hex codes taken from the same input string
    for entry in range(0, len(utf8_strings)):

        store_string = []

        for character in range(0, len(utf8_strings[entry])):
            string = utf8_strings[entry][character]
            string = string.encode("utf-8")
            store_string.append("0x" + string.hex())

        strings_in_hex.append(store_string)

    # convert the UTF-16-BE strings to hex and append them to a list of hex entries to search
    for entry in range(0, len(utf16_strings)):

        store_string = []

        for character in range(0, len(utf16_strings[entry])):
            string = utf16_strings[entry][character]
            # still encoding in UTF-8 but remembering to add the additional 00 hex entry before each encoded UTF-8
            # entry. this results in an output in the format UTF-16-BE
            string = string.encode("utf-8")
            store_string.append("0x00")
            store_string.append("0x" + string.hex())

        strings_in_hex.append(store_string)

    def convert_integer_to_hex(input_string):
        """Nested function that converts the integer strings into hex

        :param input_string: Should contain a list of integer entries to be converted into hex
        :type: list[str]
        """

        # check to ensure each string entry provided to this function can convert into an integer before proceeding
        for int_entry in range(0, len(input_string)):

            try:
                int(input_string[int_entry])

            # a value error is raised if a string from the input cannot convert into an integer
            except ValueError:
                print("input_string for function: convert_integer_to_hex must be an integer!")
                exit(0)

        # store_int_string is used to group hex codes taken from the same input string
        store_int_string = []

        # the ranges for x follow the rules for unsigned bits, larger unsigned bits are split into individual hex codes
        # as required for the search
        for int_entry in range(0, len(input_string)):

            x = int(input_string[int_entry])

            if x <= 255:

                x = hex(x)
                x = x.replace("0x", "")

                if len(x) < 2:
                    store_int_string.append("0x" + x.zfill(2))

                else:
                    store_int_string.append("0x" + x)

            elif 65535 >= x > 255:

                x = hex(x)
                x = x.replace("0x", "")

                if len(x) < 4:
                    x = x.zfill(4)
                    store_int_string.append("0x" + x[:2])
                    store_int_string.append("0x" + x[2:])

                else:
                    store_int_string.append("0x" + x[:2])
                    store_int_string.append("0x" + x[2:])

            elif 4294967295 >= x > 65535:

                x = hex(x)
                x = x.replace("0x", "")

                if len(x) < 8:
                    x = x.zfill(8)
                    store_int_string.append("0x" + x[:2])
                    store_int_string.append("0x" + x[2:4])
                    store_int_string.append("0x" + x[4:6])
                    store_int_string.append("0x" + x[6:])

                else:
                    store_int_string.append("0x" + x[:2])
                    store_int_string.append("0x" + x[2:4])
                    store_int_string.append("0x" + x[4:6])
                    store_int_string.append("0x" + x[6:])

        strings_in_hex.append(store_int_string)

    # convert the integer strings to hex and append them to a list of hex entries to search using the above function

    convert_integer_to_hex(u8_u8_u16_strings)
    convert_integer_to_hex(u32_strings)

    for entry in range(0, len(u8_4_strings)):
        convert_integer_to_hex(u8_4_strings[entry])

    # we know the final entry in strings is already in hex code, each entry just needs 0x appended to it!

    store_string = []

    for entry in range(0, len(u8_6_strings)):
        store_string.append("0x" + u8_6_strings[entry].lower())

    strings_in_hex.append(store_string)

    return strings_in_hex


def cardinal_point_search(strings_to_search):
    """Function that will run a cardinal point search via its nested functions (see below)

    :param strings_to_search: The list of strings converted into hex to search for in the grid
    :type: list[str]
    """
    if not isinstance(strings_to_search, list):
        return "expecting a list of strings to search, check your strings_to_search variable!"

    try:
        for string in range(0, len(strings_to_search)):
            for entry in range(0, len(strings_to_search[string])):
                if not isinstance(strings_to_search[string][entry], str):
                    return "expecting list to contain string entries, check your strings_to_search variable!"

    except TypeError:
        return "expecting list to contain string entries, check your strings_to_search variable!"

    def search_north():
        """Nested function that will search north of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        # searches the row above the first match to check whether the next hex code in the string is also a match,
        # this continues until all hex codes for that entry have been checked and if all are a match the string is found
        # if at any point in this process a match isn't found - or the index goes out of range (off the grid),
        # the search ends and the program will move on.
        # each search_"x" function is the same but with differing "i" and "j" values dependent on the search direction
        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row - i][column] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", (row - j) + 1, "column", column + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_north_east():
        """Nested function that will search north_east of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row - i][column + i] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", (row - j) + 1, "column", (column + j) + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_east():
        """Nested function that will search east of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row][column + i] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", row + 1, "column", (column + j) + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_south_east():
        """Nested function that will search south_east of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row + i][column + i] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", (row + j) + 1, "column", (column + j) + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_south():
        """Nested function that will search south of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row + i][column] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", (row + j) + 1, "column", column + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_south_west():
        """Nested function that will search south_west of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row + i][column - i] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", (row + j) + 1, "column", (column - j) + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_west():
        """Nested function that will search west of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row][column - i] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", row + 1, "column", (column - j) + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    def search_north_west():
        """Nested function that will search north_west of the matching
        "grid[row][column]" : "strings_to_search[entry][hex_code]" pair for additional pair matches,
        if all pair matches are found for a string, its co-ordinates are printed to the terminal

        :return: True/False
        """

        try:
            for i in range(1, len(strings_to_search[entry])):
                if hex_grid[row - i][column - i] == strings_to_search[entry][hex_code + i]:

                    if i == (len(strings_to_search[entry]) - 1):

                        print("\nString found:", strings[entry], strings_in_hex_to_search[entry])
                        for j in range(0, len(strings_to_search[entry])):
                            print("row", (row - j) + 1, "column", (column - j) + 1, strings_in_hex_to_search[entry][j])
                        return True
                else:
                    return False

        except IndexError:
            return False

    # this will allows us to track any strings the search fails to find, and investigate accordingly
    strings_not_found = []

    # will inform of how long the program takes to complete the search - more at the end of this function
    start_time = time.time()

    # for each entry in the strings we need to search, the search will look for the first hex code that makes up the
    # string in the grid, searching each entry (grid[row][column]). it will look for matches for as long as the
    # conduct_search flag is True. when a word is found this flag is set to false, telling the program to look for the
    # next entry (the flag gets reset to true) until all entries have been searched and hopefully found!

    for entry in range(0, len(strings_to_search)):

        conduct_search = True

        while conduct_search:

            for hex_code in range(0, len(strings_to_search[entry])):

                if not conduct_search:
                    break

                for row in range(0, len(hex_grid)):

                    if not conduct_search:
                        break

                    for column in range(0, len(hex_grid[row])):

                        if not conduct_search:
                            break

                        if hex_grid[row][column] == strings_to_search[entry][hex_code] and hex_code == 0:

                            # the search_"x" functions are set to return True when a word is found or False otherwise

                            if search_north():
                                conduct_search = False
                                break

                            elif search_north_east():
                                conduct_search = False
                                break

                            elif search_east():
                                conduct_search = False
                                break

                            elif search_south_east():
                                conduct_search = False
                                break

                            elif search_south():
                                conduct_search = False
                                break

                            elif search_south_west():
                                conduct_search = False
                                break

                            elif search_west():
                                conduct_search = False
                                break

                            elif search_north_west():
                                conduct_search = False
                                break

                            else:
                                continue

                        # if a string is not found, the code below will make a note of it,
                        # and prevent an endless search for the offending string
                        if row == len(hex_grid) - 1 and column == len(hex_grid[row]) - 1:
                            strings_not_found.append(strings[entry])
                            conduct_search = False
                            break

    # displays the time taken to perform the search
    print("\nThe operation took %s seconds to perform" % (time.time() - start_time))

    # displays which strings could not be found if any
    if strings_not_found:
        print("The following strings were not found.", strings_not_found,
              "Please check the strings conversion output or the hex grid for errors!")

    return "The operation completed successfully"


# opens the provided file that contains the hex grid to search, and stores its contents into the "grid" variable
input_file = open("grid", "r", encoding="utf8")
grid = input_file.readlines()
input_file.close()

# creates the hex grid from file provided using the function above
hex_grid = formulate_grid(grid)

# strings to find in the hex grid
strings = ["Christmas/n", "Presents", "@iant", "Dstl", "25/12/2017", "1514160000 secs", "127.0.0.10", "192.168.0.1",
           "07:9D:72:8E:A3:61"]

# runs the main functions that converts the strings into hex and then conducts a search for them in the grid
strings_in_hex_to_search = convert_hex_string_to_hex_decimal()
cardinal_point_search(strings_in_hex_to_search)
