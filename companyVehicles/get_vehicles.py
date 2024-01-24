from companyVehicles.vehicle_constants import *
from excel_utils import get_data_from_sheet


def get_vehicles():
    return get_data_from_sheet(VEHICLE_SHEET_NAME, VEHICLE_SHEET_DIMENSIONS, VEHICLE_HEADER_STRINGS)