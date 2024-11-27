from _typeshed import Incomplete
from enum import Enum
from typing import Final

from braintree.address import Address
from braintree.credit_card_verification import CreditCardVerification
from braintree.resource import Resource
from braintree.subscription import Subscription

class CreditCard(Resource):
    """
    A class representing Braintree CreditCard objects.

    An example of creating an credit card with all available fields::

        result = braintree.CreditCard.create({
            "cardholder_name": "John Doe",
            "cvv": "123",
            "expiration_date": "12/2012",
            "number": "4111111111111111",
            "token": "my_token",
            "billing_address": {
                "first_name": "John",
                "last_name": "Doe",
                "company": "Braintree",
                "street_address": "111 First Street",
                "extended_address": "Unit 1",
                "locality": "Chicago",
                "postal_code": "60606",
                "region": "IL",
                "country_name": "United States of America"
                "phone_number": "312-123-4567"
            },
            "options": {
                "verify_card": True,
                "verification_amount": "2.00"
            }
        })

        print(result.credit_card.token)
        print(result.credit_card.masked_number)

    For more information on CreditCards, see https://developer.paypal.com/braintree/docs/reference/request/credit-card/create/python
    """
    class CardType:
        """
        Contants representing the type of the credit card.  Available types are:

        * Braintree.CreditCard.AmEx
        * Braintree.CreditCard.CarteBlanche
        * Braintree.CreditCard.ChinaUnionPay
        * Braintree.CreditCard.DinersClubInternational
        * Braintree.CreditCard.Discover
        * Braintree.CreditCard.Electron
        * Braintree.CreditCard.Elo
        * Braintree.CreditCard.Hiper
        * Braintree.CreditCard.Hipercard
        * Braintree.CreditCard.JCB
        * Braintree.CreditCard.Laser
        * Braintree.CreditCard.UK_Maestro
        * Braintree.CreditCard.Maestro
        * Braintree.CreditCard.MasterCard
        * Braintree.CreditCard.Solo
        * Braintree.CreditCard.Switch
        * Braintree.CreditCard.Visa
        * Braintree.CreditCard.Unknown
        """
        AmEx: Final = "American Express"
        CarteBlanche: Final = "Carte Blanche"
        ChinaUnionPay: Final = "China UnionPay"
        DinersClubInternational: Final = "Diners Club"
        Discover: Final = "Discover"
        Electron: Final = "Electron"
        Elo: Final = "Elo"
        Hiper: Final = "Hiper"
        Hipercard: Final = "Hipercard"
        JCB: Final = "JCB"
        Laser: Final = "Laser"
        UK_Maestro: Final = "UK Maestro"
        Maestro: Final = "Maestro"
        MasterCard: Final = "MasterCard"
        Solo: Final = "Solo"
        Switch: Final = "Switch"
        Visa: Final = "Visa"
        Unknown: Final = "Unknown"

    class CustomerLocation:
        """
        Contants representing the issuer location of the credit card.  Available locations are:

        * braintree.CreditCard.CustomerLocation.International
        * braintree.CreditCard.CustomerLocation.US
        """
        International: Final = "international"
        US: Final = "us"

    class CardTypeIndicator:
        """
        Constants representing the three states for the card type indicator attributes

        * braintree.CreditCard.CardTypeIndicator.Yes
        * braintree.CreditCard.CardTypeIndicator.No
        * braintree.CreditCard.CardTypeIndicator.Unknown
        """
        Yes: Final = "Yes"
        No: Final = "No"
        Unknown: Final = "Unknown"

    class DebitNetwork(Enum):
        """
        Constants representing the debit networks used for processing a pinless debit transaction

        * braintree.CreditCard.DebitNetwork.Accel
        * braintree.CreditCard.DebitNetwork.Maestro
        * braintree.CreditCard.DebitNetwork.Nyce
        * braintree.CreditCard.DebitNetwork.Pulse
        * braintree.CreditCard.DebitNetwork.Star
        * braintree.CreditCard.DebitNetwork.Star_Access
        """
        Accel = "ACCEL"
        Maestro = "MAESTRO"
        Nyce = "NYCE"
        Pulse = "PULSE"
        Star = "STAR"
        Star_Access = "STAR_ACCESS"

    Commercial: type[CardTypeIndicator]
    DurbinRegulated: type[CardTypeIndicator]
    Debit: type[CardTypeIndicator]
    Healthcare: type[CardTypeIndicator]
    CountryOfIssuance: type[CardTypeIndicator]
    IssuingBank: type[CardTypeIndicator]
    Payroll: type[CardTypeIndicator]
    Prepaid: type[CardTypeIndicator]
    ProductId: type[CardTypeIndicator]
    @staticmethod
    def create(params: Incomplete | None = None):
        """
        Create a CreditCard.

        A number and expiration_date are required. ::

            result = braintree.CreditCard.create({
                "number": "4111111111111111",
                "expiration_date": "12/2012"
            })
        """
        ...
    @staticmethod
    def update(credit_card_token, params: Incomplete | None = None):
        """
        Update an existing CreditCard

        By credit_card_id.  The params are similar to create::

            result = braintree.CreditCard.update("my_credit_card_id", {
                "cardholder_name": "John Doe"
            })
        """
        ...
    @staticmethod
    def delete(credit_card_token):
        """
        Delete a credit card

        Given a credit_card_id::

            result = braintree.CreditCard.delete("my_credit_card_id")
        """
        ...
    @staticmethod
    def expired():
        """Return a collection of expired credit cards. """
        ...
    @staticmethod
    def expiring_between(start_date, end_date):
        """Return a collection of credit cards expiring between the given dates. """
        ...
    @staticmethod
    def find(credit_card_token):
        """
        Find a credit card, given a credit_card_id. This does not return
        a result object. This will raise a :class:`NotFoundError <braintree.exceptions.not_found_error.NotFoundError>` if the provided
        credit_card_id is not found. ::

            credit_card = braintree.CreditCard.find("my_credit_card_token")
        """
        ...
    @staticmethod
    def from_nonce(nonce):
        """
        Convert a payment method nonce into a CreditCard. This does not return
        a result object. This will raise a :class:`NotFoundError <braintree.exceptions.not_found_error.NotFoundError>` if the provided
        credit_card_id is not found. ::

            credit_card = braintree.CreditCard.from_nonce("my_payment_method_nonce")
        """
        ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def update_signature(): ...
    @staticmethod
    def signature(type): ...
    is_expired = expired
    billing_address: Address | None
    subscriptions: list[Subscription]
    verification: CreditCardVerification
    def __init__(self, gateway, attributes): ...
    @property
    def expiration_date(self): ...
    @property
    def masked_number(self):
        """Returns the masked number of the CreditCard."""
        ...
