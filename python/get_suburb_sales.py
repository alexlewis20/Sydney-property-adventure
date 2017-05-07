import urllib
import os
import csv

CWD = os.getcwd()


def prep_name(suburb_human):
    """Convert human readable suburb name and convert for url."""
    s = suburb_human.upper()
    s = str.split(s)
    s = '%20'.join(s)
    return s


def save_csv(suburb, postcode):
    """Download and save the csv.

    Save from NSW government website based on list of
    suburbs file.
    """
    base_url = "http://maps.six.nsw.gov.au/csv/current/suburb/"
    full_url = base_url + prep_name(suburb) + "_" + str(postcode) + ".csv"

    save_path = CWD + "/data/" + suburb + ".csv"
    save = urllib.URLopener()
    save.retrieve(full_url, save_path)
    return save_path


with open("reference/suburbs_list.csv") as csvfile:
    suburb_list = csv.reader(csvfile, delimiter=",")
    for row in suburb_list:
        print save_csv(row[0], row[1])
print("Complete")
csvfile.close()
