# Phone Number Validator

The Phone Number Validator package provides a simple way to validate phone numbers using the NumLookupAPI.

## Installation
You can install the package using pip:

```bash
pip install phone-number-validator
```

## Usage
To use the package, you must first obtain an API key from NumLookupAPI. Once you have an API key, you can create a PhoneNumberValidator instance and use its validate method to validate a phone number:

```python
from phone_number_validator.validator import PhoneNumberValidator

validator = PhoneNumberValidator(api_key="YOUR_API_KEY")

# Example 1: Valid phone number without country code
is_valid1 = validator.validate("+16502530000")
print(is_valid1)  # Returns True

# Example 2: Valid phone number with country code
is_valid2 = validator.validate("6502530000", "US")
print(is_valid2)  # Returns True

# Example 3: Invalid phone number without country code
is_valid3 = validator.validate("+11234567890")
print(is_valid3)  # Returns False

# Example 4: Invalid phone number with country code
is_valid4 = validator.validate("1234567890", "US")
print(is_valid4)  # Returns False
```
The validate method takes a phone number and an optional country code as arguments. If the phone number is valid, the method returns True. If the phone number is invalid, the method returns False.

If the API call fails for any reason, the method raises an HTTPError exception.