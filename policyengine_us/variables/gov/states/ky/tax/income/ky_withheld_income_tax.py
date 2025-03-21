from policyengine_us.model_api import *


class ky_withheld_income_tax(Variable):
    value_type = float
    entity = Person
    label = "Kentucky withheld income tax"
    defined_for = StateCode.KY
    unit = USD
    definition_period = YEAR

    def formula(person, period, parameters):
        agi = person("adjusted_gross_income_person", period)
        p = parameters(period).gov.states.ky.tax.income
        # We apply the base standard deduction amount
        standard_deduction = p.deductions.standard
        reduced_agi = max_(agi - standard_deduction, 0)
        return p.rate * reduced_agi
