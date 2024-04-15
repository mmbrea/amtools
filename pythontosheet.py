from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Spreadsheet id
SPREADSHEET_ID = "1SLBBaYnyNJEYLRec0gmjtipa6lx1Ls09mqCSOm_j3JY"

# Sheet Name and Range to Read
READ_RANGE = "Test!A1:B11"
WRITE_RANGE = "Write!A1:B11"

# The boundary of script
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# Configuration for python to sheet link
credentials = service_account.Credentials.from_service_account_file(
    "credentials.json", scopes=SCOPES
)
spreadsheet_service = build("sheets", "v4", credentials=credentials)
drive_service = build("drive", "v3", credentials=credentials)


# Module to read from specific range from google sheet
def read_range():
    range_name = READ_RANGE
    spreadsheet_id = SPREADSHEET_ID
    result = (
        spreadsheet_service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    rows = result.get("values", [])
    print("--- Reading from Google Sheets------")
    print("------------------------------------")
    print("\t{0} cells retrieved.".format(len(rows)))
    print("------------------------------------")
    print("{0} rows retrieved.".format(rows))
    return rows


# Module to write to the specified range of columns in google sheet


def write_range():
    spreadsheet_id = SPREADSHEET_ID
    range_name = WRITE_RANGE
    values = read_range()
    value_input_option = "USER_ENTERED"
    body = {"values": values}
    result = (
        spreadsheet_service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body,
        )
        .execute()
    )
    print("--- Writing from Google Sheets------")
    print("------------------------------------")
    print("\t{0} cells updated.".format(result.get("updatedCells")))
    print("------------------------------------")


read_range()
# write_range()
