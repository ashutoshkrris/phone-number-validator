import pytest
from phone_number_validator.validator import PhoneNumberValidator


VALID_PHONE_NUMBER="+12069220880"
INVALID_PHONE_NUMBER="+15551234"
PHONE_NUMBER_WITHOUT_COUNTRY_CODE="2069220880"


@pytest.fixture
def validator():
    return PhoneNumberValidator(api_key="test_api_key")


def test_valid_phone_number(validator, requests_mock):
    requests_mock.get(validator.api_url + VALID_PHONE_NUMBER, json={"valid": True})
    assert validator.validate(VALID_PHONE_NUMBER) == True


def test_invalid_phone_number(validator, requests_mock):
    requests_mock.get(validator.api_url + INVALID_PHONE_NUMBER, json={"valid": False})
    assert validator.validate(INVALID_PHONE_NUMBER) == False


def test_api_call_failure(validator, requests_mock):
    requests_mock.get(validator.api_url, status_code=500)
    with pytest.raises(Exception):
        validator.validate(INVALID_PHONE_NUMBER)


def test_phone_number_without_country_code(validator, requests_mock):
    requests_mock.get(
        validator.api_url + PHONE_NUMBER_WITHOUT_COUNTRY_CODE, json={"valid": True, "country_code": "US"}
    )
    assert validator.validate(PHONE_NUMBER_WITHOUT_COUNTRY_CODE, country_code="US") == True


def test_phone_number_with_unsupported_country_code(validator, requests_mock):
    requests_mock.get(validator.api_url, status_code=400)
    with pytest.raises(Exception):
        validator.validate(VALID_PHONE_NUMBER, country_code="ZZ")


def test_invalid_api_key(validator, requests_mock):
    requests_mock.get(validator.api_url, status_code=401)
    with pytest.raises(Exception):
        validator.validate(VALID_PHONE_NUMBER)


def test_invalid_phone_number_type(validator):
    with pytest.raises(TypeError):
        validator.validate(5551234)


def test_empty_phone_number(validator):
    with pytest.raises(ValueError):
        validator.validate("")
