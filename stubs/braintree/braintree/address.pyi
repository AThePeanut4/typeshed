from _typeshed import Incomplete
from typing import Final

from braintree.resource import Resource

class Address(Resource):
    """
    A class representing Braintree Address objects.

    An example of creating an address with all available fields::

        customer = braintree.Customer.create().customer
        result = braintree.Address.create({
            "company": "Braintree",
            "country_name": "United States of America",
            "customer_id": customer.id,
            "extended_address": "Apartment 1",
            "first_name": "John",
            "international_phone": { "country_code": "1", "national_number": "3121234567" },
            "last_name": "Doe",
            "locality": "Chicago",
            "phone_number": "312-123-4567",
            "postal_code": "60606",
            "region": "IL",
            "street_address": "111 First Street"
        })

        print(result.customer.first_name)
        print(result.customer.last_name)
    """
    class ShippingMethod:
        """
        Constants representing shipping methods for shipping addresses. Available types are:

        * braintree.Address.ShippingMethod.SameDay
        * braintree.Address.ShippingMethod.NextDay
        * braintree.Address.ShippingMethod.Priority
        * braintree.Address.ShippingMethod.Ground
        * braintree.Address.ShippingMethod.Electronic
        * braintree.Address.ShippingMethod.ShipToStore
        * braintree.Address.ShippingMethod.PickupInStore
        """
        SameDay: Final = "same_day"
        NextDay: Final = "next_day"
        Priority: Final = "priority"
        Ground: Final = "ground"
        Electronic: Final = "electronic"
        ShipToStore: Final = "ship_to_store"
        PickupInStore: Final = "pickup_in_store"

    @staticmethod
    def create(params: dict[str, Incomplete] | None = None): ...
    @staticmethod
    def delete(customer_id: str, address_id: str): ...
    @staticmethod
    def find(customer_id: str, address_id: str): ...
    @staticmethod
    def update(customer_id: str, address_id: str, params: dict[str, Incomplete] | None = None): ...
    @staticmethod
    def create_signature() -> list[str | dict[str, list[str]]]: ...
    @staticmethod
    def update_signature() -> list[str | dict[str, list[str]]]: ...
