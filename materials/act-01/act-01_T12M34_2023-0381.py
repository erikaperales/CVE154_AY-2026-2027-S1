"""
CVE154 (A.Y. 2026-2027, S1)
Template script for Programming Activity No. 01

Prepared by Christian Cahig

This file belongs to the repository
https://github.com/christian-cahig/CVE154_AY-2026-2027-S1.
"""

import math as mt

__AUTHOR__ = "Erika Perales"

def watvol(radius, h, length):
    """Calculates the volume of water in the trough."""
    area = (radius**2) * math.acos(h / radius) - h * math.sqrt(radius**2 - h**2)
    return area * length

def wetper(diameter, h):
    """Calculates the wetted perimeter of the trough."""
    radius = diameter / 2.0
    return diameter * math.acos(h / radius)

def volper(diameter_in, length_m, h_cm):
    """Returns a list containing [volume in m^3, perimeter in inches]."""
    # 1. Calculate Volume in cubic meters
    radius_m = (diameter_in * 0.0254) / 2.0
    h_m = h_cm / 100.0
    volume_m3 = watvol(radius_m, h_m, length_m)
    
    # 2. Calculate Wetted Perimeter in inches
    h_in = h_cm / 2.54
    perimeter_in = wetper(diameter_in, h_in)
    
    return [volume_m3, perimeter_in]

if __name__ == "__main__":
    pass
