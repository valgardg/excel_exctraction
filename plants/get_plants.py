from excel_utils import get_data_from_sheet
from plants.plant_constants import *

def get_plants():
    return get_data_from_sheet(PLANT_SHEET_NAME, PLANT_SHEET_DIMENSIONS, PLANT_HEADER_STRINGS)