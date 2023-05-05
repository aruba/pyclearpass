from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_sessioncontrol_v1.py


class ApiSessionControl(ClearPassAPILogin):
    # Function Section Name:ActiveSession
    # Function Section Description: Manage active sessions

    def get_session(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of active sessions
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default -id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/session/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:ActiveSessionDisconnect
    # Function Section Description: Disconnect an active session

    def new_session_by_id_disconnect(self, id="", body=({})):
        """
                Operation: Disconnect active session
                HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: ID of the session to disconnect
                Required Body Parameters (body description)- ActiveSessionDisconnect {id (string): ID of the session to disconnect,confirm_disconnect (boolean): Flag to confirm disconnecting the active session}
                Required Body Parameters (type(dict) body example)- {
          "id": "",
          "confirm_disconnect": false
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

    # Function Section Name:ActiveSessionReauthorize
    # Function Section Description: Reauthorize an active session

    def get_session_by_id_reauthorize(self, id="", template_type=""):
        """
        Operation: Get reauthorization profile(s) for an active session
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: ID of the session to reauthorize
        Optional Query Parameter Name: template_type, Description: Reauthorize profile type (Disconnect/CoA)
        """
        url_path = "/session/{id}/reauthorize"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"template_type": template_type}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_session_by_id_reauthorize(self, id="", body=({})):
        """
                Operation: Reauthorize active session
                HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: ID of the session to reauthorize
                Required Body Parameters (body description)- ActiveSessionReauthorize {confirm_reauthorize (boolean, optional): Flag to confirm the session reauthorization,reauthorize_profile (string, optional): Specify the name of the reauthorization profile to apply to the session}
                Required Body Parameters (type(dict) body example)- {
          "confirm_reauthorize": false,
          "reauthorize_profile": ""
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

    # Function Section Name:SessionAction
    # Function Section Description: Manage Session Action Methods

    def new_session_action_disconnect(self, body=({}), async_=""):
        """
                Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by multiple fields.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        """
        url_path = "/session-action/disconnect"
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_disconnect_mac_by_mac_address(
        self, body=({}), async_="", mac_address=""
    ):
        """
                Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by mac-address.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
                Required Path Parameter Name: mac_address, Description: filter by mac-address
        """
        url_path = "/session-action/disconnect/mac/{mac_address}"
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_disconnect_username_by_username(
        self, body=({}), async_="", username=""
    ):
        """
                Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by username.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
                Required Path Parameter Name: username, Description: filter by username
        """
        url_path = "/session-action/disconnect/username/{username}"
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_disconnect_ip_by_client_ip_address(
        self, body=({}), async_="", client_ip_address=""
    ):
        """
                Operation: Performs active session disconnect with a synchronous or asynchronous action & filter by client-ip-address.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
                Required Path Parameter Name: client_ip_address, Description: filter by client-ip-address
        """
        url_path = "/session-action/disconnect/ip/{client_ip_address}"
        dict_path = {"client_ip_address": client_ip_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa(self, body=({}), async_=""):
        """
                Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by multiple fields.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
        """
        url_path = "/session-action/coa"
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa_mac_by_mac_address(
        self, body=({}), async_="", mac_address=""
    ):
        """
                Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by mac-address.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
                Required Path Parameter Name: mac_address, Description: filter by mac-address
        """
        url_path = "/session-action/coa/mac/{mac_address}"
        dict_path = {"mac_address": mac_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa_username_by_username(
        self, body=({}), async_="", username=""
    ):
        """
                Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by username.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
                Required Path Parameter Name: username, Description: filter by username
        """
        url_path = "/session-action/coa/username/{username}"
        dict_path = {"username": username}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_session_action_coa_ip_by_client_ip_address(
        self, body=({}), async_="", client_ip_address=""
    ):
        """
                Operation: Performs active session reauthorize with a synchronous or asynchronous action & filter by client-ip-address.
                HTTP Status Response Codes: 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 202 Accepted, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SessionActionParams {filter (object, optional): JSON filter expression specifying the items to return, e.g. "filter":{"username":"admin", ...},enforcement_profile (object, optional): When performing CoA, the 'enforcement_profile' parameter MUST be provided, e.g. "enforcement_profile":["...", "...'"],sort (string, optional): Sorting the result set, e.g. "sort": "-id"}
                Required Body Parameters (type(dict) body example)- {
          "filter": "object",
          "enforcement_profile": "object",
          "sort": ""
        }
                Optional Query Parameter Name: async, Description: trigger asynchronous API calls
                Required Path Parameter Name: client_ip_address, Description: filter by client-ip-address
        """
        url_path = "/session-action/coa/ip/{client_ip_address}"
        dict_path = {"client_ip_address": client_ip_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"async": async_}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_session_action_by_action_id(self, action_id="", offset="", limit=""):
        """
        Operation: Returns the current status of a disconnected or reauthorized active session by the action ID.
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: action_id, Description: request body
        Optional Query Parameter Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Optional Query Parameter Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        """
        url_path = "/session-action/{action_id}"
        dict_path = {"action_id": action_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"offset": offset, "limit": limit}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")
