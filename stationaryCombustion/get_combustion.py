from stationaryCombustion.combustion_constants import *
from excel_utils import get_data_from_sheet


def get_combustion():
    return get_data_from_sheet(COMBUSTION_SHEET_NAME, COMBUSTION_SHEET_DIMENSIONS, COMBUSTION_HEADER_STRINGS)