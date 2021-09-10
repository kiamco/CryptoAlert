import operator

class Conditions:
    def __init__(self,type,signal):
        self.type = {}
        self.signal = signal
        
    def update_signal(self, new_signal):
        self.signal = new_signal
    
    def static_threshold(self, threshold, option):
        operators = {
            'gt':operator.gt(self.signal, threshold),
            'lt':operator.lt(self.signal, threshold),
            'lte':operator.le(self.signal, threshold),
            'gte':operator.ge(self.signal, threshold)
        }

        try:
            validate = operators[option]

            if option == 'gt':
                return operators[option]

            if option == 'gte':
                return operators[option]

            if option == 'lt':
                return operators[option]

            if option == 'lte':
                return operators[option]

        except:
            print(option,': operator does not exist')
    
# if __name__ == '__main__':
    # condition = Conditions(type = {}, signal = 7)
    # print(condition.static_threshold(threshold = 6, option = 'gte'))
        


    