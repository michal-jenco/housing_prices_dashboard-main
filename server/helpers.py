from typing import List


def generate_ocean_proximity_list(input_location: str) -> List:
    ocean_proximity_options = ("<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN")

    return [1 if input_location == location else 0 for location in ocean_proximity_options]
