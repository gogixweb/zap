import pytest

BR_CODE = '55'

class Zap:
    def __init__(self, number=None):
        self.number = None
        if type(number) == str:
            self.number = number

    def convert(self) -> str:

        number_to_be_converted = str(self.number)

        if ('(' or ')' in number_to_be_converted):
            number_to_be_converted = number_to_be_converted.replace('(', '')
            number_to_be_converted = number_to_be_converted.replace(')', '')
        if '-' in number_to_be_converted:
            number_to_be_converted = number_to_be_converted.replace('-', '')
        if(' ' in number_to_be_converted):
            number_to_be_converted = number_to_be_converted.replace(' ','')

        final_result = BR_CODE+number_to_be_converted
        print('>>>>')
        print(final_result)

        return final_result


def test_instantiate_class():
    zap = Zap()

def test_pass_number():
    number = '9999-0000'
    zap = Zap(number)
    assert zap.number == number

def test_pass_is_not_number():
    number = 9
    zap = Zap(number)
    assert zap.number != number

def test_convert():
    number = '(75) 99988 - 7654'
    zap = Zap(number)
    assert zap.convert() == '5575999887654'
    number = '(75) 90000 - 0000'
    zap = Zap(number)
    assert zap.convert() == '5575900000000'

if __name__ == '__main__':
    pytest.main(["-x", __file__])