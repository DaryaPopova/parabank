from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    address_street: str
    address_city: str
    address_state: str
    address_zip_code: str
    phone_number: str
    ssn: str
    username: str
    password: str
    repeated_password: str
