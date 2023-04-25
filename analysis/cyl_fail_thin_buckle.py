# Formula for unit external pressure at which buckling occurs
# Reference:    Roark's Formulas for Stress & Strain 6E, Table 35 
#               Case 20a, p690
#               Roark's Formulas for Stress & Strain 7E, Table 15.2 
#               Case 20a, p736
#               Roark's Formulas for Stress & Strain 8E, Table 15.2
#               Case 20a, p750
# Conditions:
#   thin-walled
#   closed ends, held circular
#   uniform external pressure, longitudinal and lateral

# Inputs: 
#   inner radius, r [m]
#   thickness, t_cyl [m]
#   number of lobes, n
#   length of cylinder, l [m]
#   Young's modulus, E [Pa]
#   Poisson's ratio, nu
# Outputs: 
#   buckling pressure, q_buckling [Pa]

q_buckling = (E .* t_cyl./r)./(1.+0.5.*(pi.*r./(n.*l)).^2).*(1./(n.^2.*(1.+(n.*l./(pi.*r)).^2).^2)+n.^2.*t_cyl.^2./(12.*r.^2.*(1.-nu.^2)).*(1.+(pi.*r./(n.*l)).^2).^2);