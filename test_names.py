from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
   assert make_full_name("Gleyson", "Lopes") ==  "Lopes;Gleyson"
   assert make_full_name("Stephany", "Lopes") ==  "Lopes;Stephany"
   assert make_full_name("Stephany", "Rocha") ==  "Rocha;Stephany"
   assert make_full_name("", "") ==  ";"

def test_extract_family_name():
   assert extract_family_name("Gleyson", "Lopes") ==  "Lopes;Gleyson"
   assert extract_family_name("Stephany", "Lopes") ==  "Lopes;Stephany"
   assert extract_family_name("Stephany", "Rocha") ==  "Rocha;Stephany"
   assert extract_family_name("", "") ==  ";"

def test_extract_given_name():
   assert extract_given_name("Gleyson", "Lopes") ==  "Lopes;Gleyson"
   assert extract_given_name("Stephany", "Lopes") ==  "Lopes;Stephany"
   assert extract_given_name("Stephany", "Rocha") ==  "Rocha;Stephany"
   assert extract_given_name("", "") ==  ";"


pytest.main(["-v", "--tb=line", "-rN", __file__])