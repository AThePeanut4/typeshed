from .base import AuthenticationBase

class Passwordless(AuthenticationBase):
    """
    Passwordless connections endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: my-domain.us.auth0.com)
    """
    def email(self, email: str, send: str = "link", auth_params: dict[str, str] | None = None):
        """
        Start flow sending an email.

        Given the user email address, it will send an email with:

          - A link (default, send:"link"). You can then authenticate with
            this user opening the link and he will be automatically logged in
            to the application. Optionally, you can append/override
            parameters to the link (like scope, redirect_uri, protocol,
            response_type, etc.) using auth_params dict.

          - A verification code (send:"code"). You can then authenticate with
            this user using email as username and code as password.

        Complete the authentication using the get_token.passwordless_login method.

        Args:
            email (str): Email address.

            send (str, optional): Can be: 'link' or 'code'. Defaults to 'link'.

            auth_params (dict, optional): Parameters to append or override.
        """
        ...
    def sms(self, phone_number: str):
        """
        Start flow sending an SMS message.

        Given the user phone number, it will send an SMS with
        a verification code. You can then authenticate with
        this user using phone number as username and code as password.

        Complete the authentication using the get_token.passwordless_login method.

        Args:
            phone_number (str): Phone number.
        """
        ...
