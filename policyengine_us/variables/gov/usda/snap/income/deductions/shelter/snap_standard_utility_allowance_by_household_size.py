from policyengine_us.model_api import *


class snap_standard_utility_allowance_by_household_size(Variable):
    value_type = bool
    entity = SPMUnit
    label = "SNAP Standard Utility Allowance by household size"
    unit = USD
    definition_period = MONTH

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.usda.snap.income.deductions.utility.standard
        region = spm_unit.household("snap_utility_region_str", period)
        return is_in(region, p.by_household_size.participating_states)
