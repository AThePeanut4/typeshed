from .base import BaseEndpoint as BaseEndpoint

class AuthorizationEndpoint(BaseEndpoint):
    """
    An endpoint responsible for letting authenticated users authorize access
    to their protected resources to a client.

    Typical use would be to have two views, one for displaying the authorization
    form and one to process said form on submission.

    The first view will want to utilize ``get_realms_and_credentials`` to fetch
    requested realms and useful client credentials, such as name and
    description, to be used when creating the authorization form.

    During form processing you can use ``create_authorization_response`` to
    validate the request, create a verifier as well as prepare the final
    redirection URI used to send the user back to the client.

    See :doc:`/oauth1/validator` for details on which validator methods to implement
    for this endpoint.
    """
    def create_verifier(self, request, credentials):
        """
        Create and save a new request token.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param credentials: A dict of extra token credentials.
        :returns: The verifier as a dict.
        """
        ...
    def create_authorization_response(
        self, uri, http_method: str = "GET", body=None, headers=None, realms=None, credentials=None
    ): ...
    def get_realms_and_credentials(self, uri, http_method: str = "GET", body=None, headers=None): ...
