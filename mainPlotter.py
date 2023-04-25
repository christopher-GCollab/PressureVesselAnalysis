# Main plotter script

# Inputs: 
# gravity, m/s/s
# density, kg/m3
# 
# mat_prop [material, yeildStress, youngsModulus, poissons], [string, MPa, GPa, nonDimensional]
# 
# cyl [rad_inner, wt_min, wt_max, length], [mm, mm, mm, mm]

from get_max_cyl_depth import *

gravity = 9.81      # m/s/s Assumed constant
density = 1025      # kg/m3 Assumed constant

