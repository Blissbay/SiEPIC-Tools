"""Tests visualization operations."""

from tidy3d.components.viz import Polygon


def test_make_polygon_dict():
    p = Polygon(context={"coordinates": [(1, 0), (0, 1), (0, 0)]})
    p.interiors
