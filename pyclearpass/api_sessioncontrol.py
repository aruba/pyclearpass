from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: SessionControl
# FileName: api_sessioncontrol.py


class ApiSessionControl(ClearPassAPILogin):
    # API Service: Manage active sessions
    def get_session(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of active sessions
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default -id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/session"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_session_by_id(self, id=""):
        """
        Operation: Get an active session
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/session/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Disconnect an active session
    def new_session_by_id_disconnect(self, id="", body=({})):
        """
        Operation: Disconnect active session
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the session to disconnect
        Required Body Parameters:['id', 'confirm_disconnect']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : "", #ID of the session to disconnect. Object Type: string
        "confirm_disconnect" : False, #Flag to confirm disconnecting the active session. Object Type: boolean
        }
        """
        url_path = "/session/{id}/disconnect"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Reauthorize an active session
    def get_session_by_id_reauthorize(self, template_type="", id=""):
        """
        Operation: Get reauthorization profile(s) for an active session
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type (Optional): query, Name: template_type, Description: Reauthorize profile type (Disconnect/CoA)
        Parameter Type: path, Name: id, Description: ID of the session to reauthorize
        """
        url_path = "/session/{id}/reauthorize"
        dict_query = {"template_type": template_type}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_session_by_id_reauthorize(self, id="", body=({})):
        """
        Operation: Reauthorize active session
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the session to reauthorize
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "confirm_reauthorize" : False, #Flag to confirm the session reauthorization. Object Type: boolean
        "reauthorize_profile" : "", #Specify the name of the reauthorization profile to apply to the session. Object Type: string
        }
        """
        url_path = "/session/{id}/reauthorize"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage Session Action Methods
    def new_session_action_disconnect(self, async_="", body=({})):
        """
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by multiple fields.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/disconnect"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_disconnect_mac_by_mac_address(
        self, async_="", mac_address="", body=({})
    ):
        """
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by mac-address.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Parameter Type: path, Name: mac_address, Description: filter by mac-address
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/disconnect/mac/{mac_address}"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_disconnect_username_by_username(
        self, async_="", username="", body=({})
    ):
        """
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by username.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Parameter Type: path, Name: username, Description: filter by username
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/disconnect/username/{username}"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_disconnect_ip_by_client_ip_address(
        self, async_="", client_ip_address="", body=({})
    ):
        """
        Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by client-ip-address.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Parameter Type: path, Name: client_ip_address, Description: filter by client-ip-address
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/disconnect/ip/{client_ip_address}"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"client_ip_address": client_ip_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa(self, async_="", body=({})):
        """
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by multiple fields.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/coa"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa_mac_by_mac_address(
        self, async_="", mac_address="", body=({})
    ):
        """
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by mac-address.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Parameter Type: path, Name: mac_address, Description: filter by mac-address
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/coa/mac/{mac_address}"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa_username_by_username(
        self, async_="", username="", body=({})
    ):
        """
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by username.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Parameter Type: path, Name: username, Description: filter by username
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/coa/username/{username}"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa_ip_by_client_ip_address(
        self, async_="", client_ip_address="", body=({})
    ):
        """
        Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by client-ip-address.
        HTTP Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: async, Description: trigger asynchronous API calls
        Parameter Type: path, Name: client_ip_address, Description: filter by client-ip-address
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "filter" : {}, #JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...}. Object Type: object
        "enforcement_profile" : {}, #When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"]. Object Type: object
        "sort" : "", #Sorting the result set, e.g. "sort": "-id". Object Type: string
        }
        """
        url_path = "/session-action/coa/ip/{client_ip_address}"
        dict_query = {"async_": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"client_ip_address": client_ip_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_session_action_by_action_id(self, offset="", limit="", action_id=""):
        """
        Operation: Returns the current status of a disconnected or reauthorized active session by the action ID.
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type (Optional): query, Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Parameter Type (Optional): query, Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        Parameter Type: path, Name: action_id, Description: request body
        """
        url_path = "/session-action/{action_id}"
        dict_query = {"offset": offset, "limit": limit}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"action_id": action_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")
