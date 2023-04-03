import requests


class PhoneNumberValidator:
    def __init__(self, api_key: str) -> None:
        """
        Initializes the PhoneNumberValidator class with an API key.

        Args:
            api_key (str): Your API key for the NumLookupAPI.
        """
        self.api_key = api_key
        self.api_url = "https://api.numlookupapi.com/v1/validate/"

    def validate(self, phone_number: str, country_code: str = None) -> bool:
        """
        Validates a phone number using the NumLookupAPI.

        Args:
            phone_number (str): The phone number you want to validate. This can either include the country prefix (e.g. "+1 650-253-0000") or not (e.g. "650-253-0000"). If the `country_code` argument is not provided, the API will try to detect the country automatically.
            country_code (str): An ISO Alpha 2 Country Code for the phone number (e.g. "US"). If this argument is provided, the API will use it to validate the phone number. If not provided, the API will try to detect the country automatically based on the phone number.

        Returns:
            bool: True if the phone number is valid, False otherwise.

        Raises:
            HTTPError: If the API call fails (e.g. due to authentication or network issues).
        """
        if not phone_number:
            raise ValueError("Phone Number cannot be empty!")
        response = self._make_api_call(phone_number, country_code)
        if response.ok:
            return response.json()["valid"]
        else:
            response.raise_for_status()

    def _make_api_call(
        self, phone_number: str, country_code: str = None
    ) -> requests.Response:
        """
        Makes an API call to the NumLookupAPI to validate a phone number.

        Args:
            phone_number (str): The phone number you want to validate.
            country_code (str): An ISO Alpha 2 Country Code for the phone number (e.g. "US").

        Returns:
            requests.Response: The response object returned by the API call.
        """
        params = {"apikey": self.api_key}
        if country_code:
            params["country_code"] = country_code
        response = requests.get(self.api_url + phone_number, params=params)
        return response
