from Chemicals.chemical_constants import *
from excel_utils import get_data_from_sheet


def get_chemicals():
    chemicals_1 = get_data_from_sheet(CHEMICAL_SHEET_NAME, CHEMICAL_SHEET_DIMENSIONS_1, GAS_HEADER_STRINGS)
    chemicals_2 = get_data_from_sheet(CHEMICAL_SHEET_NAME, CHEMICAL_SHEET_DIMENSIONS_2, REFRIGERANT_HEADER_STRINGS)
    chemicals_3 = get_data_from_sheet(CHEMICAL_SHEET_NAME, CHEMICAL_SHEET_DIMENSIONS_3, HYDROCARBON_HEADER_STRINGS)

    return chemicals_1 + chemicals_2 + chemicals_3 # combine both known and unknown materials