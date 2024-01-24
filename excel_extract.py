import pandas as pd
from BusinessTravel.get_travel import get_travel
from Chemicals.get_chemicals import get_chemicals
from RawMaterials.get_materials import get_materials
from companyTransport.get_transport import get_transport
from companyVehicles.get_vehicles import get_vehicles
from plants.get_plants import get_plants
import warnings

from stationaryCombustion.get_combustion import get_combustion

# Filter out UserWarning from openpyxl
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl.worksheet._reader")


def extract_and_display(get_func):
    data = get_func()
    df = pd.DataFrame.from_dict(data)
    print(df.to_string(index=False))
    
def main():
    try:
        extract_and_display(get_plants)
        # extract_and_display(get_vehicles)
        # extract_and_display(get_transport)
        # extract_and_display(get_travel)
        # extract_and_display(get_combustion)
        # extract_and_display(get_materials)
        # extract_and_display(get_chemicals)
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()