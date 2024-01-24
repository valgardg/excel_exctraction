from businessTravel.travel_constants import *
from excel_utils import get_data_from_sheet


def get_travel():
    return get_data_from_sheet(TRAVEL_SHEET_NAME, TRAVEL_SHEET_DIMENSIONS, TRAVEL_HEADER_STRINGS)