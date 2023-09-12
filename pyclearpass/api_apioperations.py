from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: ApiOperations
# FileName: api_apioperations.py


class ApiApiOperations(ClearPassAPILogin):
    # API Service: Obtain an OAuth2 access token for making API calls
    def new_oauth(self, body=({})):
        """
        Operation: Obtain an OAuth2 access token for making API calls
        HTTP Response Codes: 200 OK, 400 Bad Request, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters:['grant_type', 'client_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "grant_type" : "", #OAuth2 authentication method. Object Type: string
        "client_id" : "", #Client ID defined in API Clients. Object Type: string
        "client_secret" : "", #Client secret, required if the API client is not a public client. Object Type: string
        "username" : "", #Username for authentication, required for grant_type "password". Object Type: string
        "password" : "", #Password for authentication, required for grant_type "password". Object Type: string
        "scope" : "", #Scope of the access request. Object Type: string
        "refresh_token" : "", #Refresh token issued to the client, required for grant_type "refresh_token". Object Type: string
        }
        """
        url_path = "/oauth"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Returns OAuth2 authenticated client or user information
    def get_oauth_me(self):
        """
        Operation: Returns OAuth2 authenticated client or user information
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/oauth/me"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_oauth_me(self, body=({})):
        """
        Operation: Returns OAuth2 authenticated client or user information
        HTTP Response Codes: 200 OK, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['info', 'name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "info" : "", #Defaults to the operator profile name. Object Type: string
        "name" : "", #Defaults to the authenticated username. Object Type: string
        "..." : "", #Additional properties may be returned for grant_type "password" if corresponding properties are defined in the OAuth API enforcement profile. Object Type: string
        }
        """
        url_path = "/oauth/me"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Determine the privileges available to the user
    def get_oauth_privileges(self):
        """
        Operation: Returns a list of privileges available to the user
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/oauth/privileges"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")
