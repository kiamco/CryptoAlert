

from conditions import Conditions

class Alert:
    def __init__(self, alert_name, ticker, conditions = []):
        self.alert_name = alert_name
        self.ticker = ticker
        self.conditions = conditions

    def check_condtion(self):
        status = all(conditions)
        return status

    def add_condition(self, condition:Conditions): 
        self.conditions.append(condition)
        return self.conditions

    def __str__(self):
        return f" alert name: {self.alert_name}\n ticker: {self.ticker} \n conditions: {self.conditions}"
