from policyengine_us.model_api import *


class ok_withheld_income_tax(Variable):
    value_type = float
    entity = Person
    label = "Oklahoma withheld income tax"
    defined_for = StateCode.OK
    unit = USD
    definition_period = YEAR

    def formula(person, period, parameters):
        agi = person("adjusted_gross_income_person", period)
        p = parameters(period).gov.states.ok.tax.income
        standard_deduction = p.deductions.standard.amount["SINGLE"]
        reduced_agi = max_(agi - standard_deduction, 0)
        return p.rates.single.calc(reduced_agi)
