import pytest
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

@pytest.mark.parametrize(
    'number,converted_number',[
        ('(75) 99988 - 7654', '5575999887654'),
        ('(75) 90000 - 0000', '5575900000000'),
        ('123(**@#(!12930!', '5512312930'),
        ('+55(75)3655-0000', '557536550000'),
        ('asdf(75)981230000ert', '5575981230000')
    ])
def test_convert(number, converted_number):
    zap = Zap(number)
    assert zap.converted_number == converted_number

if __name__ == '__main__':
    pytest.main(["-x", __file__])
