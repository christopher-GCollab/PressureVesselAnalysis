# Formula for maximum/failure pressure for thick wall cylinder
# Reference:    Roark's Formulas for Stress & Strain 6E, Table 32 
#               Case 1d, p639
#               Roark's Formulas for Stress & Strain 8E, Table 13.5 
#               Case 1d, p697
# Conditions:
#   wall thickness > 1/10 radius
#   ends capped
#   uniform external pressure in all directions
# Note:
#   Failure pressures derived by reversing formulas from above reference

# Inputs: 
#   Material yield stress, Q  [Pa]
#   Inner radius, r [m]
#   Thickness, t_cyl [m]
# Outputs: 
#   Maximum/failure pressure of thick wall hoop stress, q_hoop_thick (Pa)

q_hoop_thick = Q .* ((r + t_cyl).^2 - r.^2) ./ (2 .* (r + t_cyl).^2);
