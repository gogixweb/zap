import re
BR_CODE = '55'

class Zap:
    def __init__(self, number=None):
        self.number = None
        if type(number) == str:
            self.number = number
            self.converted_number = self.convert()

    def convert(self) -> str:
        number_to_be_converted = self.number
        print(number_to_be_converted)
        # undesirable_chars = ['(',')','-',' ']

        digits = re.findall(r'\d+', number_to_be_converted)
        final_result = ''.join(digits)

        if not final_result.startswith('55'):
            final_result = BR_CODE+final_result
        print('>>>>')
        print(final_result)

        return final_result
