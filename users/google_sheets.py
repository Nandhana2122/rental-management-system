# users/google_sheet.py
import gspread
from google.oauth2.service_account import Credentials
import os

def append_to_sheet(row_data):
    """
    Append a row to your Google Sheet.
    row_data: list of values, e.g. ["Name", "Email", "Message"]
    """

    # Path to credentials.json (project root)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # RentEase/
    creds_path = os.path.join(BASE_DIR, "credentials.json")                  # RentEase/credentials.json

    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(creds_path, scopes=scope)
    client = gspread.authorize(creds)

    # Your Google Sheet ID
    sheet = client.open_by_key("1VWcccYd0a343Fg0GHFtfaCnxMel0VildT-XvB_glVmw").sheet1

    sheet.append_row(row_data)


# users/google_sheets.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def save_to_sheet(data):
    try:
        print("Saving:", data)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        creds_path = os.path.join(BASE_DIR, "credentials.json")

        scope = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)

        SHEET_ID = "1VWcccYd0a343Fg0GHFtfaCnxMel0VildT-XvB_glVmw"
        sheet = client.open_by_key(SHEET_ID).sheet1

        sheet.append_row(data)

        print("Saved to Google Sheet ✅")
    except Exception as e:
        print("Google Sheet Error ❌:", e)
