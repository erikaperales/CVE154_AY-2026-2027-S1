"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Supplemental Material No. 01

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Rain L. Niño"

def calc_surface_area(radius, length, end_faces = True):
    lateral_area = 2 * mt.pi * radius * length
    endface_area = mt.pi * (radius ** 2)

    if end_faces:
        return lateral_area + (2 * endface_area)
    else:
        return lateral_area
    # One-line alternative:
    # return lateral_area + (2 * endface_area) if end_faces else lateral_area

# Do not remove this and the following lines
if __name__ == "__main__":
    print(__AUTHOR__)

    radiuses = [1, 2, 3, 4, 5]
    lengths = [1, 2, 3, 4, 5]

    rs = [1, 3.5, 5, 0.5]
    ls = [3, 7, 1]

    for r in rs:
        for l in ls:
            print(f"{r}-m rad., {l}-m long: {calc_surface_area(r, l, end_faces=False) : .5f} m^2")
