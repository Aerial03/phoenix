from data.mois import *

get_mois_population_all(admin_div_code_list)
get_mois_population_resident(admin_div_code_list)
get_mois_population_unknown(admin_div_code_list)
get_mois_population_overseas(admin_div_code_list)

get_mois_birth(admin_div_code_list)
get_mois_death(admin_div_code_list)
get_mois_household_all(admin_div_code_list)
get_mois_household_resident(admin_div_code_list)

get_mois_population_all(list(jr_admin_div_code_dict.keys()))
get_mois_population_resident(list(jr_admin_div_code_dict.keys()))
get_mois_population_unknown(list(jr_admin_div_code_dict.keys()))
get_mois_population_overseas(list(jr_admin_div_code_dict.keys()))
