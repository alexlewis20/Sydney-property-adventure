import pandas as pd
import glob


# Functions for processing CSVs


def get_day(x):
    """Get the day from the sale date column."""
    return x["SALE DATE"].day


def get_month(x):
    """Get the month from the sale date column."""
    return x["SALE DATE"].month


def get_year(x):
    """Get the year from the sale date column."""
    return x["SALE DATE"].year


def separate_date(x):
    """Create new columns for day, month and year in loaded data frame."""
    x["SALE DAY"] = x.apply(get_day, axis=1)
    x["SALE MONTH"] = x.apply(get_month, axis=1)
    x["SALE YEAR"] = x.apply(get_year, axis=1)


def get_suburb(filepath):
    """Get the suburb name from the filepath."""
    suburb = filepath.split("/")
    suburb = suburb[1].split(".")
    suburb = suburb[0]
    return suburb


def process_csv(filepath):
    """Return a data frame for prcessed for date and suburb."""
    suburb = get_suburb(filepath)
    read_file = pd.read_csv(filepath,
                            infer_datetime_format=True,
                            parse_dates=["SALE DATE"],
                            dayfirst=True)
    read_file["SUBURB"] = suburb
    separate_date(read_file)
    return read_file


# Load all CSVs in data folder
files = glob.glob("data/*.csv")
print files

# Process and combine loaded CSVs the save to new file
sales_data = pd.concat([process_csv(f) for f in files], ignore_index=True)
sales_data = sales_data.drop_duplicates(subset=["DEALING NUMBER"])
sales_data.to_csv("combined_data/sydney_sales_combined.csv")
