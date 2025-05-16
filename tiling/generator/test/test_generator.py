#!/usr/bin/env python3

from shapely.geometry import Polygon
import tile_generator

def test_generate():
    assert isinstance(tile_generator.dummy_polygon(), Polygon)
