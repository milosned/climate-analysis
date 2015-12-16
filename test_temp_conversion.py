from temp_conversion import fahr_to_kelvin

#from numpy.testing import assert_raises
from nose.tools import *

def test_zero_celsius():
    assert fahr_to_kelvin(32) == 273.15

def test_zero_kelvin():
    assert round(fahr_to_kelvin(-459.67),2) == 0.0

def test_fahr_greater():
    assert fahr_to_kelvin(-10) > 0

@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin("SomeTemperature")

@raises(TypeError)
def test_null_temp():
    assert fahr_to_kelvin()
