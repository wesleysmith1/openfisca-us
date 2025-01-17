from openfisca_us.model_api import *


class taxsim_state(Variable):
    value_type = float
    entity = TaxUnit
    label = "State code"
    documentation = 'SOI codes. These run from 1 for Alabama to 51 for Wyoming and are not the Census or PSID codes. See state list,and also item two above.). Use zero for "no state tax calculation"'
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        return 0
