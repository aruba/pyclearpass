from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: Identities
# FileName: api_identities.py


class ApiIdentities(ClearPassAPILogin):
    # API Service: Manage API clients at Administration -> API Services -> API Clients
    def get_api_client(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of API clients
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/api-client"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_api_client(self, body=({})):
        """
                Operation: Create a new API client
                HTTP Response Codes: 201 Created, 400 Client Error, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['access_token_lifetime', 'access_token_lifetime_units', 'client_id', 'id', 'refresh_token_lifetime', 'refresh_token_lifetime_units']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "access_lifetime" : "", #Lifetime of an OAuth2 access token. Object Type: string
                "access_token_lifetime" : "", #Specify the lifetime of an OAuth2 access token. Object Type: string
                "access_token_lifetime_units" : "", #Specify the lifetime of an OAuth2 access token. Object Type: string
                "auto_confirm" : 0, #Not supported at this time. Object Type: integer
                "client_description" : "", #Use this field to store comments or notes about this API client. Object Type: string
                "client_id" : "", #The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter. Object Type: string
                "client_public" : False, #Public clients have no client secret. Object Type: boolean
                "client_refresh" : False, #An OAuth2 refresh token may be used to obtain an updated access token.Use grant_type=refresh_token for this. Object Type: boolean
                "client_secret" : "", #Use this value in the OAuth2 “client_secret” parameter. NOTE: This value is encrypted when stored and cannot be retrieved.. Object Type: string
                "enabled" : False, #Enable API client. Object Type: boolean
                "id" : "", #The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter. Object Type: string
                "grant_types" : "", #Only the selected authentication method will be permitted for use with this client ID. Object Type: string
                "profile_id" : 0, #The operator profile applies role-based access control to authorized OAuth2 clients.
        This determines what API objects and methods are available for use. Object Type: integer
                "profile_name" : "", #Name of operator profile. Object Type: string
                "redirect_uri" : "", #Not supported at this time. Object Type: string
                "refresh_lifetime" : "", #Lifetime of an OAuth2 refresh token. Object Type: string
                "refresh_token_lifetime" : "", #Specify the lifetime of an OAuth2 refresh token. Object Type: string
                "refresh_token_lifetime_units" : "", #Specify the lifetime of an OAuth2 refresh token. Object Type: string
                "scope" : "", #Not supported at this time. Object Type: string
                "user_id" : "", #Not supported at this time. Object Type: string

                }
        """
        url_path = "/api-client"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_api_client_by_client_id(self, client_id=""):
        """
        Operation: Get an API client
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: client_id, Description: URL parameter client_id
        """
        url_path = "/api-client/{client_id}"
        dict_path = {"client_id": client_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_api_client_by_client_id(self, client_id="", body=({})):
        """
                Operation: Update some fields of an API client
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 400 Client Error, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: client_id, Description: URL parameter client_id
                Required Body Parameters:['access_token_lifetime', 'access_token_lifetime_units', 'client_id', 'id', 'refresh_token_lifetime', 'refresh_token_lifetime_units']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "access_lifetime" : "", #Lifetime of an OAuth2 access token. Object Type: string
                "access_token_lifetime" : "", #Specify the lifetime of an OAuth2 access token. Object Type: string
                "access_token_lifetime_units" : "", #Specify the lifetime of an OAuth2 access token. Object Type: string
                "auto_confirm" : 0, #Not supported at this time. Object Type: integer
                "client_description" : "", #Use this field to store comments or notes about this API client. Object Type: string
                "client_id" : "", #The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter. Object Type: string
                "client_public" : False, #Public clients have no client secret. Object Type: boolean
                "client_refresh" : False, #An OAuth2 refresh token may be used to obtain an updated access token.Use grant_type=refresh_token for this. Object Type: boolean
                "client_secret" : "", #Use this value in the OAuth2 “client_secret” parameter. NOTE: This value is encrypted when stored and cannot be retrieved.. Object Type: string
                "enabled" : False, #Enable API client. Object Type: boolean
                "id" : "", #The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter. Object Type: string
                "grant_types" : "", #Only the selected authentication method will be permitted for use with this client ID. Object Type: string
                "profile_id" : 0, #The operator profile applies role-based access control to authorized OAuth2 clients.
        This determines what API objects and methods are available for use. Object Type: integer
                "profile_name" : "", #Name of operator profile. Object Type: string
                "redirect_uri" : "", #Not supported at this time. Object Type: string
                "refresh_lifetime" : "", #Lifetime of an OAuth2 refresh token. Object Type: string
                "refresh_token_lifetime" : "", #Specify the lifetime of an OAuth2 refresh token. Object Type: string
                "refresh_token_lifetime_units" : "", #Specify the lifetime of an OAuth2 refresh token. Object Type: string
                "scope" : "", #Not supported at this time. Object Type: string
                "user_id" : "", #Not supported at this time. Object Type: string

                }
        """
        url_path = "/api-client/{client_id}"
        dict_path = {"client_id": client_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_api_client_by_client_id(self, client_id="", body=({})):
        """
                Operation: Replace an API client
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 400 Client Error, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: client_id, Description: URL parameter client_id
                Required Body Parameters:['access_token_lifetime', 'access_token_lifetime_units', 'client_id', 'id', 'refresh_token_lifetime', 'refresh_token_lifetime_units']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "access_lifetime" : "", #Lifetime of an OAuth2 access token. Object Type: string
                "access_token_lifetime" : "", #Specify the lifetime of an OAuth2 access token. Object Type: string
                "access_token_lifetime_units" : "", #Specify the lifetime of an OAuth2 access token. Object Type: string
                "auto_confirm" : 0, #Not supported at this time. Object Type: integer
                "client_description" : "", #Use this field to store comments or notes about this API client. Object Type: string
                "client_id" : "", #The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter. Object Type: string
                "client_public" : False, #Public clients have no client secret. Object Type: boolean
                "client_refresh" : False, #An OAuth2 refresh token may be used to obtain an updated access token.Use grant_type=refresh_token for this. Object Type: boolean
                "client_secret" : "", #Use this value in the OAuth2 “client_secret” parameter. NOTE: This value is encrypted when stored and cannot be retrieved.. Object Type: string
                "enabled" : False, #Enable API client. Object Type: boolean
                "id" : "", #The unique string identifying this API client.  Use this value in the OAuth2 “client_id” parameter. Object Type: string
                "grant_types" : "", #Only the selected authentication method will be permitted for use with this client ID. Object Type: string
                "profile_id" : 0, #The operator profile applies role-based access control to authorized OAuth2 clients.
        This determines what API objects and methods are available for use. Object Type: integer
                "profile_name" : "", #Name of operator profile. Object Type: string
                "redirect_uri" : "", #Not supported at this time. Object Type: string
                "refresh_lifetime" : "", #Lifetime of an OAuth2 refresh token. Object Type: string
                "refresh_token_lifetime" : "", #Specify the lifetime of an OAuth2 refresh token. Object Type: string
                "refresh_token_lifetime_units" : "", #Specify the lifetime of an OAuth2 refresh token. Object Type: string
                "scope" : "", #Not supported at this time. Object Type: string
                "user_id" : "", #Not supported at this time. Object Type: string

                }
        """
        url_path = "/api-client/{client_id}"
        dict_path = {"client_id": client_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_api_client_by_client_id(self, client_id=""):
        """
        Operation: Delete an API client
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: client_id, Description: URL parameter client_id
        """
        url_path = "/api-client/{client_id}"
        dict_path = {"client_id": client_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage deny listed users
    def get_deny_listed_users(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of deny listed users
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/deny-listed-users"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_deny_listed_users_by_deny_listed_users_id(self, deny_listed_users_id=""):
        """
        Operation: Get a deny listed user
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: deny_listed_users_id, Description: Numeric ID of the deny listed user
        """
        url_path = "/deny-listed-users/{deny_listed_users_id}"
        dict_path = {"deny_listed_users_id": deny_listed_users_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_deny_listed_users_by_deny_listed_users_id(self, deny_listed_users_id=""):
        """
        Operation: Delete a deny listed user
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: deny_listed_users_id, Description: Numeric ID of the deny listed user
        """
        url_path = "/deny-listed-users/{deny_listed_users_id}"
        dict_path = {"deny_listed_users_id": deny_listed_users_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_deny_listed_users_user_id_by_user_id_mac_address_mac_address(
        self, user_id="", mac_address=""
    ):
        """
        Operation: Get a deny listed user by Username and MAC Address
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: user_id, Description: User ID of the deny listed user
        Parameter Type: path, Name: mac_address, Description: MAC address of the deny listed user
        """
        url_path = "/deny-listed-users/user_id/{user_id}/mac_address/{mac_address}"
        dict_path = {"user_id": user_id, "mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_deny_listed_users_user_id_by_user_id_mac_address_mac_address(
        self, user_id="", mac_address=""
    ):
        """
        Operation: Delete a deny listed user by Username and MAC Address
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: user_id, Description: User ID of the deny listed user
        Parameter Type: path, Name: mac_address, Description: MAC address of the deny listed user
        """
        url_path = "/deny-listed-users/user_id/{user_id}/mac_address/{mac_address}"
        dict_path = {"user_id": user_id, "mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage device accounts
    def get_device(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of device accounts
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default -id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/device"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_device(self, change_of_authorization="", body=({})):
        """
        Operation: Create a new device account
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Required Body Parameters:['mac', 'role_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "current_state" : "", #Read-only property indicating the current state of the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "mac" : "", #MAC address of the device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "role_name" : "", #Name of the role assigned to the account. Object Type: string
        "source" : "", #Origin of the account. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Numeric operator profile ID for the account’s sponsor. Object Type: string
        "sponsor_profile_name" : "", #Name of the operator profile for the account’s sponsor. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "visitor_name" : "", #Name to display for the account. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/device"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_device_by_device_id(self, device_id=""):
        """
        Operation: Get a device account
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: device_id, Description: Numeric ID of the device account
        """
        url_path = "/device/{device_id}"
        dict_path = {"device_id": device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_device_by_device_id(
        self, change_of_authorization="", device_id="", body=({})
    ):
        """
        Operation: Update some fields of a device account
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: device_id, Description: Numeric ID of the device account
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "current_state" : "", #Read-only property indicating the current state of the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the device account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the device. Object Type: string
        "mac_auth" : False, #Flag indicating the account is a device, always set to true. Object Type: boolean
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #No Desc. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "role_name" : "", #Name of the role assigned to the account. Object Type: string
        "source" : "", #Origin of the account. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Numeric operator profile ID for the account’s sponsor. Object Type: string
        "sponsor_profile_name" : "", #Name of the operator profile for the account’s sponsor. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #No Desc. Object Type: string
        "visitor_name" : "", #Name to display for the account. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/device/{device_id}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"device_id": device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_device_by_device_id(
        self, change_of_authorization="", device_id="", body=({})
    ):
        """
        Operation: Replace a device account
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: device_id, Description: Numeric ID of the device account
        Required Body Parameters:['mac', 'role_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "current_state" : "", #Read-only property indicating the current state of the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the device account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "role_name" : "", #Name of the role assigned to the account. Object Type: string
        "source" : "", #Origin of the account. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Numeric operator profile ID for the account’s sponsor. Object Type: string
        "sponsor_profile_name" : "", #Name of the operator profile for the account’s sponsor. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "visitor_name" : "", #Name to display for the account. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/device/{device_id}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"device_id": device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_device_by_device_id(self, change_of_authorization="", device_id=""):
        """
        Operation: Delete a device account
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: device_id, Description: Numeric ID of the device account
        """
        url_path = "/device/{device_id}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"device_id": device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_device_mac_by_macaddr(self, macaddr=""):
        """
        Operation: Get a device account by MAC address
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: macaddr, Description: MAC address of the device account
        """
        url_path = "/device/mac/{macaddr}"
        dict_path = {"macaddr": macaddr}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_device_mac_by_macaddr(
        self, change_of_authorization="", macaddr="", body=({})
    ):
        """
        Operation: Update some fields of a device account by MAC address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: macaddr, Description: MAC address of the device account
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "current_state" : "", #Read-only property indicating the current state of the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the device account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the device. Object Type: string
        "mac_auth" : False, #Flag indicating the account is a device, always set to true. Object Type: boolean
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #No Desc. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "role_name" : "", #Name of the role assigned to the account. Object Type: string
        "source" : "", #Origin of the account. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Numeric operator profile ID for the account’s sponsor. Object Type: string
        "sponsor_profile_name" : "", #Name of the operator profile for the account’s sponsor. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #No Desc. Object Type: string
        "visitor_name" : "", #Name to display for the account. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/device/mac/{macaddr}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"macaddr": macaddr}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_device_mac_by_macaddr(
        self, change_of_authorization="", macaddr="", body=({})
    ):
        """
        Operation: Replace a device account by MAC address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: macaddr, Description: MAC address of the device account
        Required Body Parameters:['mac', 'role_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "current_state" : "", #Read-only property indicating the current state of the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the device account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "role_name" : "", #Name of the role assigned to the account. Object Type: string
        "source" : "", #Origin of the account. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Numeric operator profile ID for the account’s sponsor. Object Type: string
        "sponsor_profile_name" : "", #Name of the operator profile for the account’s sponsor. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "visitor_name" : "", #Name to display for the account. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/device/mac/{macaddr}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"macaddr": macaddr}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_device_mac_by_macaddr(self, change_of_authorization="", macaddr=""):
        """
        Operation: Delete a device account by MAC address
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: macaddr, Description: MAC address of the device account
        """
        url_path = "/device/mac/{macaddr}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"macaddr": macaddr}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage endpoints
    def get_endpoint(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of endpoints
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/endpoint"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_endpoint(self, body=({})):
        """
        Operation: Create a new endpoint
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['mac_address', 'status']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mac_address" : "", #MAC Address of the endpoint. Object Type: string
        "description" : "", #Description of the endpoint. Object Type: string
        "status" : "", #Status of the endpoint. Object Type: string
        "device_insight_tags" : "", #List of Device Insight Tags. Object Type: string
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the endpoint. Object Type: object

        }
        """
        url_path = "/endpoint"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_endpoint_by_endpoint_id(self, endpoint_id=""):
        """
        Operation: Get an endpoint
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: endpoint_id, Description: Numeric ID of the endpoint
        """
        url_path = "/endpoint/{endpoint_id}"
        dict_path = {"endpoint_id": endpoint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_endpoint_by_endpoint_id(self, endpoint_id="", body=({})):
        """
        Operation: Update some fields of an endpoint
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: endpoint_id, Description: Numeric ID of the endpoint
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mac_address" : "", #MAC Address of the endpoint. Object Type: string
        "description" : "", #Description of the endpoint. Object Type: string
        "status" : "", #Status of the endpoint. Object Type: string
        "device_insight_tags" : "", #List of Device Insight Tags. Object Type: string
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the endpoint. Object Type: object

        }
        """
        url_path = "/endpoint/{endpoint_id}"
        dict_path = {"endpoint_id": endpoint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_endpoint_by_endpoint_id(self, endpoint_id="", body=({})):
        """
        Operation: Replace an endpoint
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: endpoint_id, Description: Numeric ID of the endpoint
        Required Body Parameters:['mac_address', 'status']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mac_address" : "", #MAC Address of the endpoint. Object Type: string
        "description" : "", #Description of the endpoint. Object Type: string
        "status" : "", #Status of the endpoint. Object Type: string
        "device_insight_tags" : "", #List of Device Insight Tags. Object Type: string
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the endpoint. Object Type: object

        }
        """
        url_path = "/endpoint/{endpoint_id}"
        dict_path = {"endpoint_id": endpoint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_endpoint_by_endpoint_id(self, endpoint_id=""):
        """
        Operation: Delete an endpoint
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: endpoint_id, Description: Numeric ID of the endpoint
        """
        url_path = "/endpoint/{endpoint_id}"
        dict_path = {"endpoint_id": endpoint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_endpoint_mac_address_by_mac_address(self, mac_address=""):
        """
        Operation: Get an endpoint by mac_address
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: mac_address, Description: Unique mac_address of the endpoint
        """
        url_path = "/endpoint/mac-address/{mac_address}"
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_endpoint_mac_address_by_mac_address(self, mac_address="", body=({})):
        """
        Operation: Update some fields of an endpoint by mac_address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: mac_address, Description: Unique mac_address of the endpoint
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mac_address" : "", #MAC Address of the endpoint. Object Type: string
        "description" : "", #Description of the endpoint. Object Type: string
        "status" : "", #Status of the endpoint. Object Type: string
        "device_insight_tags" : "", #List of Device Insight Tags. Object Type: string
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the endpoint. Object Type: object

        }
        """
        url_path = "/endpoint/mac-address/{mac_address}"
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_endpoint_mac_address_by_mac_address(self, mac_address="", body=({})):
        """
        Operation: Replace an endpoint by mac_address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: mac_address, Description: Unique mac_address of the endpoint
        Required Body Parameters:['mac_address', 'status']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mac_address" : "", #MAC Address of the endpoint. Object Type: string
        "description" : "", #Description of the endpoint. Object Type: string
        "status" : "", #Status of the endpoint. Object Type: string
        "device_insight_tags" : "", #List of Device Insight Tags. Object Type: string
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the endpoint. Object Type: object

        }
        """
        url_path = "/endpoint/mac-address/{mac_address}"
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_endpoint_mac_address_by_mac_address(self, mac_address=""):
        """
        Operation: Delete an endpoint by mac_address
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: mac_address, Description: Unique mac_address of the endpoint
        """
        url_path = "/endpoint/mac-address/{mac_address}"
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage external accounts
    def get_external_account(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of external accounts
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/external-account"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_external_account(self, body=({})):
        """
        Operation: Add an external account
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the external account. Object Type: string
        "type" : "", #Type of the external account. Object Type: string
        "description" : "", #Description of the external account. Object Type: string
        "username" : "", #User name for the external account. Object Type: string
        "password" : "", #Password for the external account. Object Type: string
        "domain" : "", #Domain for WMI external account. Object Type: string
        "enable_password" : "", #Enable-password for SSH external account. Object Type: string
        "snmp_version" : "", #SNMP Version for SNMP external account. Object Type: string
        "community" : "", #Community string for V1 and V2C SNMP external account. Object Type: string
        "security_level" : "", #Security level for V3 SNMP external account. Object Type: string
        "auth_protocol" : "", #Authorization protocol for V3 SNMP external account. Object Type: string
        "auth_key" : "", #Authorization key for V3 SNMP external account. Object Type: string
        "priv_protocol" : "", #Privacy protocol for V3 SNMP external account. Object Type: string
        "priv_key" : "", #Privacy key for V3 SNMP external account. Object Type: string

        }
        """
        url_path = "/external-account"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_external_account_by_external_account_id(self, external_account_id=""):
        """
        Operation: Get an external account
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: external_account_id, Description: Numeric ID of external account
        """
        url_path = "/external-account/{external_account_id}"
        dict_path = {"external_account_id": external_account_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_external_account_by_external_account_id(
        self, external_account_id="", body=({})
    ):
        """
        Operation: Update some fields of an external account
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: external_account_id, Description: Numeric ID of external account
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the external account. Object Type: string
        "type" : "", #Type of the external account. Object Type: string
        "description" : "", #Description of the external account. Object Type: string
        "username" : "", #User name for the external account. Object Type: string
        "password" : "", #Password for the external account. Object Type: string
        "domain" : "", #Domain for WMI external account. Object Type: string
        "enable_password" : "", #Enable-password for SSH external account. Object Type: string
        "snmp_version" : "", #SNMP Version for SNMP external account. Object Type: string
        "community" : "", #Community string for V1 and V2C SNMP external account. Object Type: string
        "security_level" : "", #Security level for V3 SNMP external account. Object Type: string
        "auth_protocol" : "", #Authorization protocol for V3 SNMP external account. Object Type: string
        "auth_key" : "", #Authorization key for V3 SNMP external account. Object Type: string
        "priv_protocol" : "", #Privacy protocol for V3 SNMP external account. Object Type: string
        "priv_key" : "", #Privacy key for V3 SNMP external account. Object Type: string

        }
        """
        url_path = "/external-account/{external_account_id}"
        dict_path = {"external_account_id": external_account_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_external_account_by_external_account_id(
        self, external_account_id="", body=({})
    ):
        """
        Operation: Replace an external account
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: external_account_id, Description: Numeric ID of external account
        Required Body Parameters:['name', 'type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the external account. Object Type: string
        "type" : "", #Type of the external account. Object Type: string
        "description" : "", #Description of the external account. Object Type: string
        "username" : "", #User name for the external account. Object Type: string
        "password" : "", #Password for the external account. Object Type: string
        "domain" : "", #Domain for WMI external account. Object Type: string
        "enable_password" : "", #Enable-password for SSH external account. Object Type: string
        "snmp_version" : "", #SNMP Version for SNMP external account. Object Type: string
        "community" : "", #Community string for V1 and V2C SNMP external account. Object Type: string
        "security_level" : "", #Security level for V3 SNMP external account. Object Type: string
        "auth_protocol" : "", #Authorization protocol for V3 SNMP external account. Object Type: string
        "auth_key" : "", #Authorization key for V3 SNMP external account. Object Type: string
        "priv_protocol" : "", #Privacy protocol for V3 SNMP external account. Object Type: string
        "priv_key" : "", #Privacy key for V3 SNMP external account. Object Type: string

        }
        """
        url_path = "/external-account/{external_account_id}"
        dict_path = {"external_account_id": external_account_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_external_account_by_external_account_id(self, external_account_id=""):
        """
        Operation: Delete an external account
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: external_account_id, Description: Numeric ID of external account
        """
        url_path = "/external-account/{external_account_id}"
        dict_path = {"external_account_id": external_account_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_external_account_name_by_name(self, name=""):
        """
        Operation: Get an external account by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of external account
        """
        url_path = "/external-account/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_external_account_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an external account by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of external account
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the external account. Object Type: string
        "type" : "", #Type of the external account. Object Type: string
        "description" : "", #Description of the external account. Object Type: string
        "username" : "", #User name for the external account. Object Type: string
        "password" : "", #Password for the external account. Object Type: string
        "domain" : "", #Domain for WMI external account. Object Type: string
        "enable_password" : "", #Enable-password for SSH external account. Object Type: string
        "snmp_version" : "", #SNMP Version for SNMP external account. Object Type: string
        "community" : "", #Community string for V1 and V2C SNMP external account. Object Type: string
        "security_level" : "", #Security level for V3 SNMP external account. Object Type: string
        "auth_protocol" : "", #Authorization protocol for V3 SNMP external account. Object Type: string
        "auth_key" : "", #Authorization key for V3 SNMP external account. Object Type: string
        "priv_protocol" : "", #Privacy protocol for V3 SNMP external account. Object Type: string
        "priv_key" : "", #Privacy key for V3 SNMP external account. Object Type: string

        }
        """
        url_path = "/external-account/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_external_account_name_by_name(self, name="", body=({})):
        """
        Operation: Replace an external account by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of external account
        Required Body Parameters:['name', 'type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the external account. Object Type: string
        "type" : "", #Type of the external account. Object Type: string
        "description" : "", #Description of the external account. Object Type: string
        "username" : "", #User name for the external account. Object Type: string
        "password" : "", #Password for the external account. Object Type: string
        "domain" : "", #Domain for WMI external account. Object Type: string
        "enable_password" : "", #Enable-password for SSH external account. Object Type: string
        "snmp_version" : "", #SNMP Version for SNMP external account. Object Type: string
        "community" : "", #Community string for V1 and V2C SNMP external account. Object Type: string
        "security_level" : "", #Security level for V3 SNMP external account. Object Type: string
        "auth_protocol" : "", #Authorization protocol for V3 SNMP external account. Object Type: string
        "auth_key" : "", #Authorization key for V3 SNMP external account. Object Type: string
        "priv_protocol" : "", #Privacy protocol for V3 SNMP external account. Object Type: string
        "priv_key" : "", #Privacy key for V3 SNMP external account. Object Type: string

        }
        """
        url_path = "/external-account/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_external_account_name_by_name(self, name=""):
        """
        Operation: Delete an external account by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of external account
        """
        url_path = "/external-account/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage guest accounts
    def get_guest(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of guest accounts
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default -id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/guest"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_guest(self, change_of_authorization="", body=({})):
        """
        Operation: Create a new guest account
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Required Body Parameters:['username', 'password', 'role_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "do_expire" : 0, #Action to take when the expire_time is reached. Object Type: integer
        "email" : "", #Email address for the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "mac" : "", #MAC address of the guest’s device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #Password for the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "simultaneous_use" : 0, #Number of simultaneous sessions allowed for the account. Object Type: integer
        "sponsor_email" : "", #Email address of the sponsor. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Profile of the sponsor of the account. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #Username of the account. Object Type: string
        "visitor_company" : "", #The guest’s company name. Object Type: string
        "visitor_name" : "", #The guest’s full name. Object Type: string
        "visitor_phone" : "", #The guest’s contact telephone number. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/guest"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_guest_by_guest_id(self, guest_id=""):
        """
        Operation: Get a guest account
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        """
        url_path = "/guest/{guest_id}"
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_guest_by_guest_id(
        self, change_of_authorization="", guest_id="", body=({})
    ):
        """
        Operation: Update some fields of a guest account
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "do_expire" : 0, #Action to take when the expire_time is reached. Object Type: integer
        "email" : "", #Email address for the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the guest account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the guest’s device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #Password for the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "simultaneous_use" : 0, #Number of simultaneous sessions allowed for the account. Object Type: integer
        "sponsor_email" : "", #Email address of the sponsor. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Profile of the sponsor of the account. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #Username of the account. Object Type: string
        "visitor_company" : "", #The guest’s company name. Object Type: string
        "visitor_name" : "", #The guest’s full name. Object Type: string
        "visitor_phone" : "", #The guest’s contact telephone number. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/guest/{guest_id}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_guest_by_guest_id(
        self, change_of_authorization="", guest_id="", body=({})
    ):
        """
        Operation: Replace a guest account
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters:['username', 'password', 'role_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "do_expire" : 0, #Action to take when the expire_time is reached. Object Type: integer
        "email" : "", #Email address for the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the guest account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the guest’s device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #Password for the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "simultaneous_use" : 0, #Number of simultaneous sessions allowed for the account. Object Type: integer
        "sponsor_email" : "", #Email address of the sponsor. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Profile of the sponsor of the account. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #Username of the account. Object Type: string
        "visitor_company" : "", #The guest’s company name. Object Type: string
        "visitor_name" : "", #The guest’s full name. Object Type: string
        "visitor_phone" : "", #The guest’s contact telephone number. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/guest/{guest_id}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_guest_by_guest_id(self, change_of_authorization="", guest_id=""):
        """
        Operation: Delete a guest account
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        """
        url_path = "/guest/{guest_id}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_guest_username_by_username(self, username=""):
        """
        Operation: Get a guest account by username
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: username, Description: Unique username of the guest account
        """
        url_path = "/guest/username/{username}"
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_guest_username_by_username(
        self, change_of_authorization="", username="", body=({})
    ):
        """
        Operation: Update some fields of a guest account by username
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: username, Description: Unique username of the guest account
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "do_expire" : 0, #Action to take when the expire_time is reached. Object Type: integer
        "email" : "", #Email address for the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the guest account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the guest’s device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #Password for the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "simultaneous_use" : 0, #Number of simultaneous sessions allowed for the account. Object Type: integer
        "sponsor_email" : "", #Email address of the sponsor. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Profile of the sponsor of the account. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #Username of the account. Object Type: string
        "visitor_company" : "", #The guest’s company name. Object Type: string
        "visitor_name" : "", #The guest’s full name. Object Type: string
        "visitor_phone" : "", #The guest’s contact telephone number. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/guest/username/{username}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_guest_username_by_username(
        self, change_of_authorization="", username="", body=({})
    ):
        """
        Operation: Replace a guest account by username
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: username, Description: Unique username of the guest account
        Required Body Parameters:['username', 'password', 'role_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "create_time" : "", #Time at which the account was created. Object Type: string
        "do_expire" : 0, #Action to take when the expire_time is reached. Object Type: integer
        "email" : "", #Email address for the account. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "expire_time" : "", #Time at which the account will expire. Object Type: string
        "id" : 0, #Numeric ID of the guest account (cannot be changed). Object Type: integer
        "mac" : "", #MAC address of the guest’s device. Object Type: string
        "notes" : "", #Comments or notes stored with the account. Object Type: string
        "password" : "", #Password for the account. Object Type: string
        "role_id" : 0, #Role to assign to the account. Object Type: integer
        "simultaneous_use" : 0, #Number of simultaneous sessions allowed for the account. Object Type: integer
        "sponsor_email" : "", #Email address of the sponsor. Object Type: string
        "sponsor_name" : "", #Name of the sponsor of the account. Object Type: string
        "sponsor_profile" : "", #Profile of the sponsor of the account. Object Type: string
        "start_time" : "", #Time at which the account will be enabled. Object Type: string
        "username" : "", #Username of the account. Object Type: string
        "visitor_company" : "", #The guest’s company name. Object Type: string
        "visitor_name" : "", #The guest’s full name. Object Type: string
        "visitor_phone" : "", #The guest’s contact telephone number. Object Type: string
        "..." : "", #Additional properties (custom fields) may be stored with the account. Object Type: string

        }
        """
        url_path = "/guest/username/{username}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_guest_username_by_username(
        self, change_of_authorization="", username=""
    ):
        """
        Operation: Delete a guest account by username
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: change_of_authorization, Description: <b>true:</b> Updates the network state using Disconnect-Request or CoA-Request, depending on the changes made<br/><b>false:</b> No action is taken<br/><b>blank or unset:</b> Use the default setting from Configuration » Authentication » Dynamic Authorization
        Parameter Type: path, Name: username, Description: Unique username of the guest account
        """
        url_path = "/guest/username/{username}"
        dict_query = {"change_of_authorization": change_of_authorization}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage local users
    def get_local_user(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of local users
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/local-user"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_local_user(self, body=({})):
        """
        Operation: Create a new local user
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['user_id', 'password', 'username', 'role_name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "user_id" : "", #Unique user id of the local user. Object Type: string
        "password" : "", #Password of the local user. Object Type: string
        "username" : "", #User name of the local user. Object Type: string
        "role_name" : "", #Role name of the local user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "change_pwd_next_login" : False, #Flag indicating if the password change is required in next login. Object Type: boolean
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the local user account. Object Type: object

        }
        """
        url_path = "/local-user"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_local_user_by_local_user_id(self, local_user_id=""):
        """
        Operation: Get a local user
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: local_user_id, Description: Numeric ID of the local user
        """
        url_path = "/local-user/{local_user_id}"
        dict_path = {"local_user_id": local_user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_local_user_by_local_user_id(self, local_user_id="", body=({})):
        """
        Operation: Update some fields of a local user
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: local_user_id, Description: Numeric ID of the local user
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "user_id" : "", #Unique user id of the local user. Object Type: string
        "password" : "", #Password of the local user. Object Type: string
        "username" : "", #User name of the local user. Object Type: string
        "role_name" : "", #Role name of the local user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "change_pwd_next_login" : False, #Flag indicating if the password change is required in next login. Object Type: boolean
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the local user account. Object Type: object

        }
        """
        url_path = "/local-user/{local_user_id}"
        dict_path = {"local_user_id": local_user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_local_user_by_local_user_id(self, local_user_id="", body=({})):
        """
        Operation: Replace a local user
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: local_user_id, Description: Numeric ID of the local user
        Required Body Parameters:['user_id', 'password', 'username', 'role_name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "user_id" : "", #Unique user id of the local user. Object Type: string
        "password" : "", #Password of the local user. Object Type: string
        "username" : "", #User name of the local user. Object Type: string
        "role_name" : "", #Role name of the local user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "change_pwd_next_login" : False, #Flag indicating if the password change is required in next login. Object Type: boolean
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the local user account. Object Type: object

        }
        """
        url_path = "/local-user/{local_user_id}"
        dict_path = {"local_user_id": local_user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_local_user_by_local_user_id(self, local_user_id=""):
        """
        Operation: Delete a local user
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: local_user_id, Description: Numeric ID of the local user
        """
        url_path = "/local-user/{local_user_id}"
        dict_path = {"local_user_id": local_user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_local_user_user_id_by_user_id(self, user_id=""):
        """
        Operation: Get a local user by user_id
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: user_id, Description: Unique user_id of the local user
        """
        url_path = "/local-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_local_user_user_id_by_user_id(self, user_id="", body=({})):
        """
        Operation: Update some fields of a local user by user_id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: user_id, Description: Unique user_id of the local user
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "user_id" : "", #Unique user id of the local user. Object Type: string
        "password" : "", #Password of the local user. Object Type: string
        "username" : "", #User name of the local user. Object Type: string
        "role_name" : "", #Role name of the local user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "change_pwd_next_login" : False, #Flag indicating if the password change is required in next login. Object Type: boolean
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the local user account. Object Type: object

        }
        """
        url_path = "/local-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_local_user_user_id_by_user_id(self, user_id="", body=({})):
        """
        Operation: Replace a local user by user_id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: user_id, Description: Unique user_id of the local user
        Required Body Parameters:['user_id', 'password', 'username', 'role_name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "user_id" : "", #Unique user id of the local user. Object Type: string
        "password" : "", #Password of the local user. Object Type: string
        "username" : "", #User name of the local user. Object Type: string
        "role_name" : "", #Role name of the local user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "change_pwd_next_login" : False, #Flag indicating if the password change is required in next login. Object Type: boolean
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the local user account. Object Type: object

        }
        """
        url_path = "/local-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_local_user_user_id_by_user_id(self, user_id=""):
        """
        Operation: Delete a local user by user_id
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: user_id, Description: Unique user_id of the local user
        """
        url_path = "/local-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage static host lists
    def get_static_host_list(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of static host lists
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/static-host-list"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_static_host_list(self, body=({})):
        """
        Operation: Create a static host list
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'host_format', 'host_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the static host list. Object Type: string
        "description" : "", #Description of the static host list. Object Type: string
        "host_format" : "", #Format of the static host list. Object Type: string
        "host_type" : "", #Host type of the static host list. Object Type: string
        "value" : "", #Value for the host format "Subnet" and "Regular Expression". Object Type: string
        "host_entries" : {}, #List of host entries (Address and Description) for the host format "List". For example, "host_entries":[{"host_address": "10.21.11.117", "host_address_desc" : "My host address description."}, {..} ..]. Object Type: object

        }
        """
        url_path = "/static-host-list"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_static_host_list_by_static_host_list_id(self, static_host_list_id=""):
        """
        Operation: Get a static host list
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: static_host_list_id, Description: Numeric ID of the static host list
        """
        url_path = "/static-host-list/{static_host_list_id}"
        dict_path = {"static_host_list_id": static_host_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_static_host_list_by_static_host_list_id(
        self, static_host_list_id="", body=({})
    ):
        """
        Operation: Update some fields of a static host list
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: static_host_list_id, Description: Numeric ID of the static host list
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the static host list. Object Type: string
        "description" : "", #Description of the static host list. Object Type: string
        "host_format" : "", #Format of the static host list. Object Type: string
        "host_type" : "", #Host type of the static host list. Object Type: string
        "value" : "", #Value for the host format "Subnet" and "Regular Expression". Object Type: string
        "host_entries" : {}, #List of host entries (Address and Description) for the host format "List". For example, "host_entries":[{"host_address": "10.21.11.117", "host_address_desc" : "My host address description."}, {..} ..]. Object Type: object

        }
        """
        url_path = "/static-host-list/{static_host_list_id}"
        dict_path = {"static_host_list_id": static_host_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_static_host_list_by_static_host_list_id(
        self, static_host_list_id="", body=({})
    ):
        """
        Operation: Replace a static host list
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: static_host_list_id, Description: Numeric ID of the static host list
        Required Body Parameters:['name', 'host_format', 'host_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the static host list. Object Type: string
        "description" : "", #Description of the static host list. Object Type: string
        "host_format" : "", #Format of the static host list. Object Type: string
        "host_type" : "", #Host type of the static host list. Object Type: string
        "value" : "", #Value for the host format "Subnet" and "Regular Expression". Object Type: string
        "host_entries" : {}, #List of host entries (Address and Description) for the host format "List". For example, "host_entries":[{"host_address": "10.21.11.117", "host_address_desc" : "My host address description."}, {..} ..]. Object Type: object

        }
        """
        url_path = "/static-host-list/{static_host_list_id}"
        dict_path = {"static_host_list_id": static_host_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_static_host_list_by_static_host_list_id(self, static_host_list_id=""):
        """
        Operation: Delete a static host list
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: static_host_list_id, Description: Numeric ID of the static host list
        """
        url_path = "/static-host-list/{static_host_list_id}"
        dict_path = {"static_host_list_id": static_host_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_static_host_list_name_by_name(self, name=""):
        """
        Operation: Get a static host list by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the static host list
        """
        url_path = "/static-host-list/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_static_host_list_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a static host list by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the static host list
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the static host list. Object Type: string
        "description" : "", #Description of the static host list. Object Type: string
        "host_format" : "", #Format of the static host list. Object Type: string
        "host_type" : "", #Host type of the static host list. Object Type: string
        "value" : "", #Value for the host format "Subnet" and "Regular Expression". Object Type: string
        "host_entries" : {}, #List of host entries (Address and Description) for the host format "List". For example, "host_entries":[{"host_address": "10.21.11.117", "host_address_desc" : "My host address description."}, {..} ..]. Object Type: object

        }
        """
        url_path = "/static-host-list/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_static_host_list_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a static host list by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the static host list
        Required Body Parameters:['name', 'host_format', 'host_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the static host list. Object Type: string
        "description" : "", #Description of the static host list. Object Type: string
        "host_format" : "", #Format of the static host list. Object Type: string
        "host_type" : "", #Host type of the static host list. Object Type: string
        "value" : "", #Value for the host format "Subnet" and "Regular Expression". Object Type: string
        "host_entries" : {}, #List of host entries (Address and Description) for the host format "List". For example, "host_entries":[{"host_address": "10.21.11.117", "host_address_desc" : "My host address description."}, {..} ..]. Object Type: object

        }
        """
        url_path = "/static-host-list/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_static_host_list_name_by_name(self, name=""):
        """
        Operation: Delete a static host list by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the static host list
        """
        url_path = "/static-host-list/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
