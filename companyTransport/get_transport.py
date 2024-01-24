from companyTransport.transport_constants import *
from excel_utils import get_data_from_sheet


def get_transport():
    return get_data_from_sheet(TRANSPORT_SHEET_NAME, TRANSPORT_SHEET_DIMENSIONS, TRANSPORT_HEADER_STRINGS)