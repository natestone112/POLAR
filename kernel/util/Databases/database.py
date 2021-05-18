# API for creating, storing and reading with regards to the measurement database

import os
import csv
from time import asctime

#   Constants
field_names = ["time", "serial", "M1", "M2", "M3", "M4", "M5", "M6", "GO/NOGO",
               "DEV1", "DEV2", "DEV3", "DEV4", "DEV5", "DEV6", "FailFlag"]
test_row = {"serial": "N/A", "M1": "1", "M2": "2", "M3": "3", "M4": "4", "M5": "5", "M6": "6", "GO/NOGO": "NOGO",
            "DEV1": "0", "DEV2": "0", "DEV3": "0", "DEV4": "0", "DEV5": "0", "DEV6": "0", "FailFlag": "0"}


#   databaseWrite()
#   Writes single entry into the measurement csv, creating a new csv if none exists
#   The current delimiter is TAB, or "\t"
#   data is a dictionary with values mapped to the desired column name
#   database is a string corresponding to the database folder name
#   serial is an optional parameter, corresponding to the id for a specific set of measurements

def databaseWrite(data, database, serial=None):
    #   Current time
    time = asctime()
    row = data
    #   Update row with time
    row.update({"time": time})
    #   Add serial number
    if serial is not None:
        row.update({"serial": serial})

    #   Create folder if necessary
    path = "./measurements/" + database + "/"
    try:
        (os.makedirs(path))
        print("Measurement storage folder generated: " + path)
    except FileExistsError:
        print("Measurement storage folder opened: " + path)

    #   Check for header
    try:
        has_header = False
        is_corrupt = False
        with open((path + "measurements.csv"), "r", newline="") as csv_file:
            print("Opened current CSV file")
            try:
                if csv.Sniffer().has_header(csv_file.read(1024)):
                    has_header = True
            except:
                print("file is corrupt")
        if is_corrupt:
            with open((path + "measurements.csv"), "w", newline="") as csv_file:
                print("created new CSV file, writing header ")
                csv_writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=field_names)
                csv_writer.writeheader()
        else:
            if not has_header:
                with open((path + "measurements.csv"), "w", newline="") as csv_file:
                    print("writing header to existing CSV file")
                    csv_writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=field_names)
                    csv_writer.writeheader()

    #   If file does not exist
    except FileNotFoundError:
        with open((path + "measurements.csv"), "w", newline="") as csv_file:
            print("created new CSV file")
            csv_writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=field_names)
            csv_writer.writeheader()
    #   Write new row
    with open((path + "measurements.csv"), "a", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=field_names)
        csv_writer.writerow(row)
        print("wrote new row entry")

