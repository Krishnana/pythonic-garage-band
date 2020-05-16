from pythonic_garage_band import __version__
from pythonic_garage_band.garage_band import Band
from pythonic_garage_band.garage_band import Guitarist, Bassist
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_create_bands():
    Band.create_from_data('pythonic_garage_band\\assets\\bands.yaml')
    assert str(Band.to_list()[0]) == "The band Band1"
    assert str(Band.to_list()[1]) == "The band Band2"
    assert repr(Band.to_list()[0]) == "The band instance with name = Band1, members = [Bassist instance. Name: Simon, Guitarist instance. Name: Krishnan]"
    assert repr(Band.to_list()[1]) == "The band instance with name = Band2, members = [drummer instance. Name: Vara, Guitarist instance. Name: JB]"


def test_band_name():
    test_band = Band("test");
    assert test_band.name == "test"

def test_band_members():
    test_band = Band("test",[Guitarist("test1"),Bassist("test2")]);
    assert test_band.members[0].name == "test1"
    assert test_band.members[0].instrument == "Guitar"
    assert test_band.members[1].name == "test2"
    assert test_band.members[1].instrument == "Bass"

def test_band_play_solo():
    test_band = Band("test",[Guitarist("test1"),Bassist("test2")]);
    assert test_band.play_solos() == ["test1 Playing solo guitar","test2 Playing solo bass"]

def test_band_to_list():
    test_band1 = Band("test",[Guitarist("test1")]);
    assert len(test_band1.to_list())>0


def test_musician_get_instrument():
    test_musician1 = Guitarist("test1")
    test_musician2 = Bassist("test1")
    assert test_musician1.get_instrument() == 'Guitar'
    assert test_musician2.get_instrument() == 'Bass'
