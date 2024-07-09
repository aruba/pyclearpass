import json
import requests
import urllib.parse, urllib3

urllib3.disable_warnings()


class ClearPassAPILogin:
    def __init__(
        self,
        granttype="",
        clientid="",
        clientsecret="",
        username="",
        password="",
        server="",
        api_token="",
        verify_ssl=False,
    ):
        """
        This is the class constructor for the ClearPassModule.

        This constructor is required to be created before any modules can be used and must contain the following function arguments:

        Mandatory Parameters:
        server (string): Website for ClearPass services example - https://yourserver.network.local:443/api
        verify_ssl (boolean, optional): default value False. Allows use of an invalid SSL certificate.

        Option 1 Parameters -
        granttype (string) = ['client_credentials' or 'password' or 'refresh_token']: OAuth2 authentication method,client_id (string): Client ID defined in API Clients,
        clientsecret (string, optional): Client secret, required if the API client is not a public client,
        username (string, optional): Username for authentication, required for grant_type "password",
        password (string, optional): Password for authentication, required for grant_type "password",

        Option 2 Parameters-
        api_token = Provide the api_token which is the 'access token'.

        }

        """
        self.granttype = granttype
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.username = username
        self.password = password
        self.server = server
        self.api_token = api_token
        self.verify_ssl = False

    def _send_request(
        self, url, method, query="", content_response_type="application/json"
    ):
        """Sends a request to the ClearPass server
        :query: must contain the json request if model required
        :url: must contain the /url (e.g. /oauth)
        :method: must contain the post or get request type of method
        :content_response_type: by default is set as Application/Json however can be changed by the method if required and functionality exists.
        :api_token optional[]: must contain the api_token for the calls.
        """
        full_url_path = self.server + url

        if len(self.api_token) == 0:
            cred = _new_api_token(self)
            try:
                self.api_token = cred["access_token"]
            except TypeError:
                pass
            except KeyError:
                pass

        if len(self.api_token) != 0:
            header = {
                "Authorization": "Bearer " + self.api_token,
                "accept": content_response_type,
            }
            if method == "post":
                response = requests.post(
                    url=full_url_path,
                    json=query,
                    headers=header,
                    verify=self.verify_ssl,
                )
            if method == "patch":
                response = requests.patch(
                    url=full_url_path,
                    json=query,
                    headers=header,
                    verify=self.verify_ssl,
                )
            if method == "put":
                response = requests.put(
                    url=full_url_path,
                    json=query,
                    headers=header,
                    verify=self.verify_ssl,
                )
            if method == "get":
                response = requests.get(
                    url=full_url_path,
                    json=query,
                    headers=header,
                    verify=self.verify_ssl,
                )
            if method == "delete":
                response = requests.delete(
                    url=full_url_path,
                    json=query,
                    headers=header,
                    verify=self.verify_ssl,
                )
            if method == "":
                print(
                    "method needs to be supplied before sending a request to ClearPass"
                )

            if "json" in content_response_type:                
                try:
                    return json.loads(response.text)
                except json.decoder.JSONDecodeError:
                    return response.text
            else:
                return response.content
        else:
            print("Problem logging into ClearPass")
            return cred


def _new_api_token(self):
    """
    Operation: Obtain an OAuth2 access token for making API calls
    HTTP Status Response Codes: 200 OK, 400 Bad Request, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 400 Bad Request, 406 Not Acceptable, 415 Unsupported Media Type
    Required Body Parameters (body description)- TokenEndpoint {grant_type (string) = ['client_credentials' or 'password' or 'refresh_token']: OAuth2 authentication method,client_id (string): Client ID defined in API Clients,client_secret (string, optional): Client secret, required if the API client is not a public client,username (string, optional): Username for authentication, required for grant_type "password",password (string, optional): Password for authentication, required for grant_type "password",scope (string, optional): Scope of the access request,refresh_token (string, optional): Refresh token issued to the client, required for grant_type "refresh_token"}
    Required Body Parameters (type(dict) body example)- {
    "grant_type": "",
    "client_id": "",
    "client_secret": "",
    "username": "",
    "password": "",
    "scope": "",
    "refresh_token": ""
    }
    """
    model = {
        "grant_type": self.granttype,
        "client_id": self.clientid,
        "client_secret": self.clientsecret,
        "username": self.username,
        "password": self.password,
    }

    full_url_path = self.server + "/oauth"
    response = requests.post(url=full_url_path, json=model, verify=self.verify_ssl)

    try:
        response = json.loads(str(response.text))
        return response

    except json.decoder.JSONDecodeError:
        return response


def _remove_empty_keys(keys):
    remove_empty_values_from_dict = []
    for item in keys:
        if keys[item] == "":
            remove_empty_values_from_dict.append(item)
        else:
            # print(item,": ", keys[item])
            pass
    for removal in remove_empty_values_from_dict:
        del keys[removal]
    return keys


def _generate_parameterised_url(url, parameters=""):
    parameters = _remove_empty_keys(keys=parameters)

    if len(parameters) == 0:
        return url
    else:
        encoded_url = urllib.parse.urlencode(parameters)
        final_url = url + "?" + encoded_url
        return final_url
