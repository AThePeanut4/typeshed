from .base import AuthenticationBase

class BackChannelLogin(AuthenticationBase):
    """Back-Channel Login endpoint"""
    def back_channel_login(self, binding_message: str, login_hint: str, scope: str, **kwargs):
        """
        Send a Back-Channel Login.

        Args:
             binding_message (str): Human-readable string displayed on both the device calling /bc-authorize and the user’s 
             authentication device to ensure the user is approves the correct request.

             login_hint (str): String containing information about the user to contact for authentication.

             scope(str): "openid" is a required scope.Multiple scopes are separated 
             with whitespace.

             **kwargs: Other fields to send along with the PAR.

        Returns:
            auth_req_id, expires_in, interval
        """
        ...
