import os
import tkinter
from tkinter import filedialog

import pandas

hardcoded_input: bool = True # For debugging purposes. Set to true for actual use
hardcoded_output: bool = False  # True = filename.csv --- filename_parsed.csv

if hardcoded_input:  # same as if hardcoded_input == true
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_name = "MYST_BOM Harpon.csv"
    target = os.path.join(file_path, file_name)

else:  # same as if hardcoded_input == false

    root = tkinter.Tk()
    root.attributes('-alpha', 0.0)  # Hide the window
    root.attributes('-topmost', True)  # always have it on top
    target = filedialog.askopenfilename(title=str.upper("Select source csv file"), defaultextension=".csv",
                                        filetypes=[("Comma Separated Values", ".csv")])
    root.destroy()  # Destroy window when file dialog is finished

print("Now reformating BOM list " + target)
# data = pandas.read_csv(target)


def extract_from_csv() -> list[list]:
    try:
        data1 = pandas.read_csv(target)
        imported_part_qty = data1["QTY"].tolist()
        imported_part_name = data1["PART NUMBER"].tolist()
        return [imported_part_qty, imported_part_name]

        # print(imported_part_name)

    except AttributeError:

        print("Unable to find header in first row, trying second row")

        try:
            data2 = pandas.read_csv(target, header=1)
            imported_part_qty = data2["QTY"].tolist()
            imported_part_name = data2["PART NUMBER"].tolist()
            return [imported_part_qty, imported_part_name]

        except AttributeError:
            print("Could not find QTY or PART NUMBER columns")

    except FileNotFoundError :
            print("Could not locate file " + target)



def part_number_extract() -> list[list]:  # returns [valid_part_qty], [valid_part_number], [valid_part_name]

    valid_part_number: list = []
    valid_part_name: list = []
    valid_part_qty: list = []

    i: int = 0  # index increment

    for item in extract_from_csv()[1]:  # Is imported_part_name

        digit_check = str(item[0]).isdigit()

        if digit_check:  # same as if digit_check == true

            if "_" in str(item):
                split_item = str(item).split("_", 1)

                valid_part_number.append(split_item[0])
                valid_part_name.append(split_item[1])
                valid_part_qty.append(extract_from_csv()[0][i])

                i += 1

            else:

                i += 1

    return [valid_part_qty, valid_part_number, valid_part_name]


def accumulate_duplicates() -> list[list]:
    valid_part_qty: list = part_number_extract()[0]
    valid_part_number: list = part_number_extract()[1]

    pop_index: list[int] = []

    # print(valid_part_number)

    p: int = 0  # parent increment
    t: int = p + 1  # target increment
    for _ in valid_part_number:

        while t < len(valid_part_number):
            if str(valid_part_number[p]) == str(valid_part_number[t]):
                valid_part_qty[p] += valid_part_qty[t]
                valid_part_qty[t] = 0
                pop_index.append(t)
                t += 1

            else:
                t += 1

        p += 1
        t = p + 1

    return [valid_part_qty, pop_index]


def pop_duplicates() -> list[list]:
    qty: list = accumulate_duplicates()[0]
    number: list = part_number_extract()[1]
    name: list = part_number_extract()[2]
    pop_index: list = accumulate_duplicates()[1]

    pop_index.sort()

    i = 0

    for item in pop_index:

        qty.pop(item)
        number.pop(item)
        name.pop(item)

        for _ in pop_index:
            pop_index[i] -= 1
            i += 1
        i = 0

    return [qty, number, name]


def create_data_frame() -> None:
    web = []

    for item in pop_duplicates()[1]:
        web.append("https://www.mcmaster.com/" + item + "/")

    dataframe = pandas.DataFrame(list(zip(pop_duplicates()[0], pop_duplicates()[1], pop_duplicates()[2], web)),
                                 columns=["QTY", "PART NUMBER", "PART NAME", "WEB"])

    if hardcoded_output:

        file_path = os.path.dirname(os.path.abspath(__file__))
        new_file_name = file_name.replace(".csv", "") + "_parsed.csv"
        target = os.path.join(file_path, new_file_name)

        print(dataframe)

        try:
            dataframe.to_csv(target, mode='x')  # open for exclusive creation, failing if the file already exists
            input("Press enter to quit")
        except FileExistsError:
            print("file " + target + " already exists")

            overwrite = str.upper(input("Do you want to overwrite? Y/N"))

            if overwrite == "Y":
                dataframe.to_csv()
                input("File overwritten. Press enter to quit")
            elif overwrite == "N":
                input("File was not overwritten. Press enter to quit")

    if not hardcoded_output:

        save_csv = str.upper(input("Would you like to save date to csv file? Y/N"))

        if save_csv == "Y":

            root = tkinter.Tk()
            root.withdraw() # Hide the window (on linux?)
            root.attributes('-alpha', 0.0)  # Hide the window (on windows?)
            root.attributes('-topmost', True)  # always have it on top
            target = filedialog.asksaveasfilename(title="select destination", defaultextension=".csv",
                                                  confirmoverwrite=True, filetypes=[("Comma Separated Values", ".csv")])
            root.destroy()  # Destroy window when file dialog is finished
            dataframe.to_csv(target)

            print(dataframe)

        elif save_csv == "N":

            print(dataframe)

            # else:
            #     print("An error occurred, please enter Y or N")
            #     SaveToCsv()

        # SaveToCsv()
        input("press enter to quit")


extract_from_csv()
part_number_extract()
accumulate_duplicates()
pop_duplicates()
create_data_frame()