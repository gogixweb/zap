from django.test import TestCase
from api.zap import Zap
import pytest

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
