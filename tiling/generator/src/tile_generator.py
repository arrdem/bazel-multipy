import json
from pathlib import Path
from typing import List

from shapely.geometry import Polygon
from geojson import Feature, FeatureCollection

PACKAGE_PREFIX = "coding"
OUTPUT_DIR = "tiles"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def dummy_polygon(center_lon: float, center_lat: float, size: float = 0.01) -> Polygon:
    """Creates a simple square polygon centered at the given coordinates."""
    half_size = size / 2
    return Polygon([
        (center_lon - half_size, center_lat - half_size),
        (center_lon + half_size, center_lat - half_size),
        (center_lon + half_size, center_lat + half_size),
        (center_lon - half_size, center_lat + half_size),
    ])

def generate_tiles(output_directory: str = OUTPUT_DIR, num_features: int = 3) -> None:
    """Generates dummy vector tiles for demonstration."""
    features: List[Feature] = []
    for i in range(num_features):
        lon = -105.0 + (i * 0.05)  # Example longitudes around Denver
        lat = 39.75 + (i * 0.03)   # Example latitudes around Denver
        polygon = dummy_polygon(lon, lat)
        feature = Feature(geometry=polygon, properties={"id": i, "name": f"Area {i+1}"})
        features.append(feature)

    feature_collection = FeatureCollection(features)

    # For simplicity, we'll just save the GeoJSON as if it were a single "tile"
    # In a real application, this would involve tiling logic.
    output_path = Path(output_directory) / "0_0_0.geojson"
    with open(output_path, "w") as f:
        json.dump(feature_collection, f)
    print(f"Dummy tile data generated at: {output_path}")


if __name__ == "__main__":
    generate_tiles()
