import csv
import xml.etree.ElementTree as xmlTree
import numpy as np


# Function that reads in the node names for table column names
def read_columns_from_xml(file_name):
    tree = xmlTree.parse(file_name)
    root = tree.getroot()

    # column Names
    temp_columns = np.array([])
    for n in range(len(root[0])):
        temp_columns = np.append(temp_columns, root[0][n].tag)
    return temp_columns


# function that reads in the node data for table rows
def read_row_from_xml(file_name):
    tree = xmlTree.parse(file_name)
    root = tree.getroot()

    # column Names
    temp_rows = np.array([])
    for x in range(len(root)):
        temp_row = np.array([])
        for n in range(len(root[x])):
            temp_row = np.append(temp_row, root[x][n].text)
        temp_rows = np.append(temp_rows, temp_row)
    temp_rows = temp_rows.reshape(2, 4)
    return temp_rows


# Function to write the column names and rows to a CSV file
def write_csv(file_name, columns_array, rows_array):
    # writing to csv file
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file)

        # writing the fields
        csv_writer.writerow(columns_array)

        # writing the data rows
        csv_writer.writerows(rows_array)

    print(f"Data has been written to {file_name}")


# main code to read XML, create columns, create rows, and write CSV
xml_FileName = "xml_file.xml"
columns = read_columns_from_xml(xml_FileName)
print(columns)
rows = read_row_from_xml(xml_FileName)
print(rows)

csv_filename = "csv_file.csv"
write_csv(csv_filename, columns, rows)
