from RawMaterials.material_constants import *
from excel_utils import get_data_from_sheet


def get_materials():
    raw_materials_1 = get_data_from_sheet(MATERIAL_SHEET_NAME, MATERIAL_SHEET_DIMENSIONS_1, MATERIAL_HEADER_STRINGS)
    raw_mateirals_2 = get_data_from_sheet(MATERIAL_SHEET_NAME, MATERIAL_SHEET_DIMENSIONS_2, MATERIAL_HEADER_STRINGS)
    return raw_materials_1 + raw_mateirals_2 # combine both known and unknown materials