# Formula for maximum/failure pressure for thin wall cylinder
# Reference:    Roark's Formulas for Stress & Strain 6E, Table 28 
#               Case 1c, p519
#               Roark's Formulas for Stress & Strain 8E, Table 13.1 
#               Case 1c, p609
# Conditions:
#   Thin-walled
#   Uniform external pressure
#   Ends capped
# Note:
#   Failure pressures derived by reversing formulas from above reference

# Inputs: 
#   Material yield stress, Q  [Pa]
#   Inner radius, r [m]
#   Thickness, t_cyl [m]
# Outputs: 
#   Maximum/failure pressure of thin wall hoop stress, q_hoop_thin (Pa)

q_hoop_thin = Q .* t_cyl ./ r;
