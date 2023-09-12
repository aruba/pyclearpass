from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: Integrations
# FileName: api_integrations.py


class ApiIntegrations(ClearPassAPILogin):
    # API Service: Manage Context Server Actions
    def get_context_server_action(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Context Server Actions
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/context-server-action"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_context_server_action(self, body=({})):
        """
        Operation: Create a new Context Server Action
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['server_type', 'action_name', 'http_method', 'url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type of the Context Server Action. Object Type: string
        "server_name" : "", #Server Name of the Context Server Action. Object Type: string
        "action_name" : "", #Action Name of the Context Server Action. Object Type: string
        "action_type" : "", #Action Type of the Context Server Action. Object Type: string
        "description" : "", #Description of the Context Server Action. Object Type: string
        "http_method" : "", #Http method of the Context Server Action. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server Action. Object Type: string
        "url" : "", #URL of the Context Server Action. Object Type: string
        "content_type" : "", #Content-Type of the Context Server Action. Note : For CUSTOM type use any string. Object Type: string
        "content" : "", #Content of the Context Server Action. Object Type: string
        "headers" : {}, #Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]). Object Type: object
        "attributes" : {}, #Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}]). Object Type: object
        }
        """
        url_path = "/context-server-action"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_context_server_action_by_context_server_action_id(
        self, context_server_action_id=""
    ):
        """
        Operation: Get a Context Server Action
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: context_server_action_id, Description: Numeric ID of the csa
        """
        url_path = "/context-server-action/{context_server_action_id}"
        dict_path = {"context_server_action_id": context_server_action_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_context_server_action_by_context_server_action_id(
        self, context_server_action_id="", body=({})
    ):
        """
        Operation: Update some fields of a Context Server Action
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: context_server_action_id, Description: Numeric ID of the csa
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type of the Context Server Action. Object Type: string
        "server_name" : "", #Server Name of the Context Server Action. Object Type: string
        "action_name" : "", #Action Name of the Context Server Action. Object Type: string
        "action_type" : "", #Action Type of the Context Server Action. Object Type: string
        "description" : "", #Description of the Context Server Action. Object Type: string
        "http_method" : "", #Http method of the Context Server Action. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server Action. Object Type: string
        "url" : "", #URL of the Context Server Action. Object Type: string
        "content_type" : "", #Content-Type of the Context Server Action. Note : For CUSTOM type use any string. Object Type: string
        "content" : "", #Content of the Context Server Action. Object Type: string
        "headers" : {}, #Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]). Object Type: object
        "attributes" : {}, #Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}]). Object Type: object
        }
        """
        url_path = "/context-server-action/{context_server_action_id}"
        dict_path = {"context_server_action_id": context_server_action_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_context_server_action_by_context_server_action_id(
        self, context_server_action_id="", body=({})
    ):
        """
        Operation: Replace a Context Server Action
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: context_server_action_id, Description: Numeric ID of the csa
        Required Body Parameters:['server_type', 'action_name', 'http_method', 'url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type of the Context Server Action. Object Type: string
        "server_name" : "", #Server Name of the Context Server Action. Object Type: string
        "action_name" : "", #Action Name of the Context Server Action. Object Type: string
        "action_type" : "", #Action Type of the Context Server Action. Object Type: string
        "description" : "", #Description of the Context Server Action. Object Type: string
        "http_method" : "", #Http method of the Context Server Action. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server Action. Object Type: string
        "url" : "", #URL of the Context Server Action. Object Type: string
        "content_type" : "", #Content-Type of the Context Server Action. Note : For CUSTOM type use any string. Object Type: string
        "content" : "", #Content of the Context Server Action. Object Type: string
        "headers" : {}, #Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]). Object Type: object
        "attributes" : {}, #Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}]). Object Type: object
        }
        """
        url_path = "/context-server-action/{context_server_action_id}"
        dict_path = {"context_server_action_id": context_server_action_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_context_server_action_by_context_server_action_id(
        self, context_server_action_id=""
    ):
        """
        Operation: Delete a Context Server Action
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: context_server_action_id, Description: Numeric ID of the csa
        """
        url_path = "/context-server-action/{context_server_action_id}"
        dict_path = {"context_server_action_id": context_server_action_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_context_server_action_by_server_type_action_name_action_name(
        self, server_type="", action_name=""
    ):
        """
        Operation: Get a Context Server Action by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_type, Description: Server type of the context server action
        Parameter Type: path, Name: action_name, Description: Unique action name of the context server action
        """
        url_path = "/context-server-action/{server_type}/action-name/{action_name}"
        dict_path = {"server_type": server_type, "action_name": action_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_context_server_action_by_server_type_action_name_action_name(
        self, server_type="", action_name="", body=({})
    ):
        """
        Operation: Update some fields of a Context Server Action by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_type, Description: Server type of the context server action
        Parameter Type: path, Name: action_name, Description: Unique action name of the context server action
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type of the Context Server Action. Object Type: string
        "server_name" : "", #Server Name of the Context Server Action. Object Type: string
        "action_name" : "", #Action Name of the Context Server Action. Object Type: string
        "action_type" : "", #Action Type of the Context Server Action. Object Type: string
        "description" : "", #Description of the Context Server Action. Object Type: string
        "http_method" : "", #Http method of the Context Server Action. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server Action. Object Type: string
        "url" : "", #URL of the Context Server Action. Object Type: string
        "content_type" : "", #Content-Type of the Context Server Action. Note : For CUSTOM type use any string. Object Type: string
        "content" : "", #Content of the Context Server Action. Object Type: string
        "headers" : {}, #Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]). Object Type: object
        "attributes" : {}, #Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}]). Object Type: object
        }
        """
        url_path = "/context-server-action/{server_type}/action-name/{action_name}"
        dict_path = {"server_type": server_type, "action_name": action_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_context_server_action_by_server_type_action_name_action_name(
        self, server_type="", action_name="", body=({})
    ):
        """
        Operation: Replace a Context Server Action by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_type, Description: Server type of the context server action
        Parameter Type: path, Name: action_name, Description: Unique action name of the context server action
        Required Body Parameters:['server_type', 'action_name', 'http_method', 'url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type of the Context Server Action. Object Type: string
        "server_name" : "", #Server Name of the Context Server Action. Object Type: string
        "action_name" : "", #Action Name of the Context Server Action. Object Type: string
        "action_type" : "", #Action Type of the Context Server Action. Object Type: string
        "description" : "", #Description of the Context Server Action. Object Type: string
        "http_method" : "", #Http method of the Context Server Action. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server Action. Object Type: string
        "url" : "", #URL of the Context Server Action. Object Type: string
        "content_type" : "", #Content-Type of the Context Server Action. Note : For CUSTOM type use any string. Object Type: string
        "content" : "", #Content of the Context Server Action. Object Type: string
        "headers" : {}, #Headers(key/value pairs) of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1"},{"attr_name":"key2", "attr_value":"value2"}]). Object Type: object
        "attributes" : {}, #Attributes of the Context Server Action (e.g., [{"attr_name":"key1", "attr_value":"value1", "is_sensitive":true},{"attr_name":"key2", "attr_value":"value2", "is_sensitive": false}]). Object Type: object
        }
        """
        url_path = "/context-server-action/{server_type}/action-name/{action_name}"
        dict_path = {"server_type": server_type, "action_name": action_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_context_server_action_by_server_type_action_name_action_name(
        self, server_type="", action_name=""
    ):
        """
        Operation: Delete a Context Server Action by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_type, Description: Server type of the context server action
        Parameter Type: path, Name: action_name, Description: Unique action name of the context server action
        """
        url_path = "/context-server-action/{server_type}/action-name/{action_name}"
        dict_path = {"server_type": server_type, "action_name": action_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Device Insight Integration
    def get_device_insight(self):
        """
        Operation: Get Device Insight Integration details
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/device-insight"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_device_insight(self, body=({})):
        """
        Operation: Update Device Insight Integration values
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "enable_device_insight" : False, #Enable/Disable Device Insight Integration. Object Type: boolean
        "activation_token" : "", #Registration Token. Object Type: string
        "primary_clearpass_server_uuid" : "", #Primary ClearPass Server UUID. Object Type: string
        "standby_clearpass_server_uuid" : "", #null. Object Type: string
        "bypass_proxy" : False, #Bypass Proxy. Object Type: boolean
        "polling_interval" : 0, #Polling Interval. Object Type: integer
        "sync_time" : 0, #Sync Time. Object Type: integer
        "activation_status" : "", #Activation Status. Object Type: string
        "activation_error" : "", #Activation Error. Object Type: string
        "activation_timestamp" : "", #Activation Timestamp. Object Type: string
        "registration_status" : "", #Registration Status. Object Type: string
        "last_sync_timestamp" : "", #Last Sync Timestamp. Object Type: string
        "last_sync_run" : "", #Last Sync Run. Object Type: string
        "aruba_central_tenant_id" : "", #Aruba Central Tenant Id. Object Type: string
        "device_insight_collector_id" : "", #Device Insight Collector Id. Object Type: string
        "tag_update_action" : "", #Tags Update Action. Object Type: string
        "tags_for_disconnect" : "", #Tags for Disconnect. Object Type: string
        "radius_coa_action" : "", #Radius CoA action. Object Type: string
        "analyzer_admin_url" : "", #Analyzer Admin URL. Object Type: string
        }
        """
        url_path = "/device-insight"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage Endpoint Context servers
    def get_endpoint_context_server(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list endpoint context servers
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/endpoint-context-server"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_endpoint_context_server(self, body=({})):
        """
        Operation: Create a new endpoint context server
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['server_type', 'server_name', 'server_base_url', 'auth_method', 'validate_server', 'status', 'bypass_proxy']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type. Object Type: string
        "server_name" : "", #Server Name. Object Type: string
        "server_base_url" : "", #Server Base URL. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server. Object Type: string
        "username" : "", #Username. Object Type: string
        "password" : "", #Password. Object Type: string
        "oauth2_client_id" : "", #Client ID of OAuth2. Object Type: string
        "oauth2_client_secret" : "", #Client Secret of OAuth2. Object Type: string
        "oauth2_access_token_url" : "", #Access token URL of OAuth2. Object Type: string
        "client_cert_CN" : "", #Client Certificate CN. Object Type: string
        "client_cert_expiry_date" : "", #Client Certificate expiry date. Object Type: string
        "vendor_attrs" : {}, #Attributes. Object Type: object
        "validate_server" : False, #Enable to validate the server certificate. Object Type: boolean
        "status" : False, #Enable Server. Object Type: boolean
        "ip_version" : "", #IP Version. Object Type: string
        "bypass_proxy" : False, #Enable to bypass proxy server. Object Type: boolean
        }
        """
        url_path = "/endpoint-context-server"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_endpoint_context_server_by_endpoint_context_server_id(
        self, endpoint_context_server_id=""
    ):
        """
        Operation: Get an endpoint context server
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        """
        url_path = "/endpoint-context-server/{endpoint_context_server_id}"
        dict_path = {"endpoint_context_server_id": endpoint_context_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_endpoint_context_server_by_endpoint_context_server_id(
        self, endpoint_context_server_id="", body=({})
    ):
        """
        Operation: Update some fields of an endpoint context server
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type. Object Type: string
        "server_name" : "", #Server Name. Object Type: string
        "server_base_url" : "", #Server Base URL. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server. Object Type: string
        "username" : "", #Username. Object Type: string
        "password" : "", #Password. Object Type: string
        "oauth2_client_id" : "", #Client ID of OAuth2. Object Type: string
        "oauth2_client_secret" : "", #Client Secret of OAuth2. Object Type: string
        "oauth2_access_token_url" : "", #Access token URL of OAuth2. Object Type: string
        "client_cert_CN" : "", #Client Certificate CN. Object Type: string
        "client_cert_expiry_date" : "", #Client Certificate expiry date. Object Type: string
        "vendor_attrs" : {}, #Attributes. Object Type: object
        "validate_server" : False, #Enable to validate the server certificate. Object Type: boolean
        "status" : False, #Enable Server. Object Type: boolean
        "ip_version" : "", #IP Version. Object Type: string
        "bypass_proxy" : False, #Enable to bypass proxy server. Object Type: boolean
        }
        """
        url_path = "/endpoint-context-server/{endpoint_context_server_id}"
        dict_path = {"endpoint_context_server_id": endpoint_context_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_endpoint_context_server_by_endpoint_context_server_id(
        self, endpoint_context_server_id="", body=({})
    ):
        """
        Operation: Replace an endpoint context server
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        Required Body Parameters:['server_type', 'server_name', 'server_base_url', 'auth_method', 'validate_server', 'status', 'bypass_proxy']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type. Object Type: string
        "server_name" : "", #Server Name. Object Type: string
        "server_base_url" : "", #Server Base URL. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server. Object Type: string
        "username" : "", #Username. Object Type: string
        "password" : "", #Password. Object Type: string
        "oauth2_client_id" : "", #Client ID of OAuth2. Object Type: string
        "oauth2_client_secret" : "", #Client Secret of OAuth2. Object Type: string
        "oauth2_access_token_url" : "", #Access token URL of OAuth2. Object Type: string
        "client_cert_CN" : "", #Client Certificate CN. Object Type: string
        "client_cert_expiry_date" : "", #Client Certificate expiry date. Object Type: string
        "vendor_attrs" : {}, #Attributes. Object Type: object
        "validate_server" : False, #Enable to validate the server certificate. Object Type: boolean
        "status" : False, #Enable Server. Object Type: boolean
        "ip_version" : "", #IP Version. Object Type: string
        "bypass_proxy" : False, #Enable to bypass proxy server. Object Type: boolean
        }
        """
        url_path = "/endpoint-context-server/{endpoint_context_server_id}"
        dict_path = {"endpoint_context_server_id": endpoint_context_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_endpoint_context_server_by_endpoint_context_server_id(
        self, endpoint_context_server_id=""
    ):
        """
        Operation: Delete an endpoint context server
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        """
        url_path = "/endpoint-context-server/{endpoint_context_server_id}"
        dict_path = {"endpoint_context_server_id": endpoint_context_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_endpoint_context_server_server_name_by_server_name(self, server_name=""):
        """
        Operation: Get an endpoint context server by server name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_name, Description: Unique name of the Endpoint Context Server
        """
        url_path = "/endpoint-context-server/server-name/{server_name}"
        dict_path = {"server_name": server_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_endpoint_context_server_server_name_by_server_name(
        self, server_name="", body=({})
    ):
        """
        Operation: Update some fields of an endpoint context server by server name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_name, Description: Unique name of the Endpoint Context Server
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type. Object Type: string
        "server_name" : "", #Server Name. Object Type: string
        "server_base_url" : "", #Server Base URL. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server. Object Type: string
        "username" : "", #Username. Object Type: string
        "password" : "", #Password. Object Type: string
        "oauth2_client_id" : "", #Client ID of OAuth2. Object Type: string
        "oauth2_client_secret" : "", #Client Secret of OAuth2. Object Type: string
        "oauth2_access_token_url" : "", #Access token URL of OAuth2. Object Type: string
        "client_cert_CN" : "", #Client Certificate CN. Object Type: string
        "client_cert_expiry_date" : "", #Client Certificate expiry date. Object Type: string
        "vendor_attrs" : {}, #Attributes. Object Type: object
        "validate_server" : False, #Enable to validate the server certificate. Object Type: boolean
        "status" : False, #Enable Server. Object Type: boolean
        "ip_version" : "", #IP Version. Object Type: string
        "bypass_proxy" : False, #Enable to bypass proxy server. Object Type: boolean
        }
        """
        url_path = "/endpoint-context-server/server-name/{server_name}"
        dict_path = {"server_name": server_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_endpoint_context_server_server_name_by_server_name(
        self, server_name="", body=({})
    ):
        """
        Operation: Replace an endpoint context server by server name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_name, Description: Unique name of the Endpoint Context Server
        Required Body Parameters:['server_type', 'server_name', 'server_base_url', 'auth_method', 'validate_server', 'status', 'bypass_proxy']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "server_type" : "", #Server Type. Object Type: string
        "server_name" : "", #Server Name. Object Type: string
        "server_base_url" : "", #Server Base URL. Object Type: string
        "auth_method" : "", #Authentication Method of the Context Server. Object Type: string
        "username" : "", #Username. Object Type: string
        "password" : "", #Password. Object Type: string
        "oauth2_client_id" : "", #Client ID of OAuth2. Object Type: string
        "oauth2_client_secret" : "", #Client Secret of OAuth2. Object Type: string
        "oauth2_access_token_url" : "", #Access token URL of OAuth2. Object Type: string
        "client_cert_CN" : "", #Client Certificate CN. Object Type: string
        "client_cert_expiry_date" : "", #Client Certificate expiry date. Object Type: string
        "vendor_attrs" : {}, #Attributes. Object Type: object
        "validate_server" : False, #Enable to validate the server certificate. Object Type: boolean
        "status" : False, #Enable Server. Object Type: boolean
        "ip_version" : "", #IP Version. Object Type: string
        "bypass_proxy" : False, #Enable to bypass proxy server. Object Type: boolean
        }
        """
        url_path = "/endpoint-context-server/server-name/{server_name}"
        dict_path = {"server_name": server_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_endpoint_context_server_server_name_by_server_name(self, server_name=""):
        """
        Operation: Delete an endpoint context server by server name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_name, Description: Unique name of the Endpoint Context Server
        """
        url_path = "/endpoint-context-server/server-name/{server_name}"
        dict_path = {"server_name": server_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_endpoint_context_server_by_endpoint_context_server_id_trigger_poll(
        self, endpoint_context_server_id=""
    ):
        """
        Operation:  Trigger polling for an endpoint context server
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: endpoint_context_server_id, Description: URL parameter endpoint_context_server_id
        """
        url_path = "/endpoint-context-server/{endpoint_context_server_id}/trigger-poll"
        dict_path = {"endpoint_context_server_id": endpoint_context_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_endpoint_context_server_server_name_by_server_name_trigger_poll(
        self, server_name=""
    ):
        """
        Operation:  Trigger polling for an endpoint context server by server name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_name, Description: Unique name of the Endpoint Context Server
        """
        url_path = "/endpoint-context-server/server-name/{server_name}/trigger-poll"
        dict_path = {"server_name": server_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # API Service: Manage event sources
    def get_event_sources(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of event sources
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/event-sources"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_event_sources(self, body=({})):
        """
        Operation: Create a new event source
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'ipaddress', 'vendor', 'type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Event source Name. Object Type: string
        "description" : "", #Event source description. Object Type: string
        "ipaddress" : "", #Unique IP Address of the event source. Object Type: string
        "vendor" : "", #Vendor name. Object Type: string
        "type" : "", #Event source type. Object Type: string
        "enable" : False, #Enable event source. Object Type: boolean
        }
        """
        url_path = "/event-sources"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_event_sources_by_event_sources_id(self, event_sources_id=""):
        """
        Operation: Get an event source
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: event_sources_id, Description: Unique id of the Event source
        """
        url_path = "/event-sources/{event_sources_id}"
        dict_path = {"event_sources_id": event_sources_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_event_sources_by_event_sources_id(self, event_sources_id="", body=({})):
        """
        Operation: Update some fields of an event source
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: event_sources_id, Description: Unique id of the Event source
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Event source Name. Object Type: string
        "description" : "", #Event source description. Object Type: string
        "ipaddress" : "", #Unique IP Address of the event source. Object Type: string
        "vendor" : "", #Vendor name. Object Type: string
        "type" : "", #Event source type. Object Type: string
        "enable" : False, #Enable event source. Object Type: boolean
        }
        """
        url_path = "/event-sources/{event_sources_id}"
        dict_path = {"event_sources_id": event_sources_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_event_sources_by_event_sources_id(self, event_sources_id="", body=({})):
        """
        Operation: Replace an event source
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: event_sources_id, Description: Unique id of the Event source
        Required Body Parameters:['name', 'ipaddress', 'vendor', 'type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Event source Name. Object Type: string
        "description" : "", #Event source description. Object Type: string
        "ipaddress" : "", #Unique IP Address of the event source. Object Type: string
        "vendor" : "", #Vendor name. Object Type: string
        "type" : "", #Event source type. Object Type: string
        "enable" : False, #Enable event source. Object Type: boolean
        }
        """
        url_path = "/event-sources/{event_sources_id}"
        dict_path = {"event_sources_id": event_sources_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_event_sources_by_event_sources_id(self, event_sources_id=""):
        """
        Operation: Delete an event source
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: event_sources_id, Description: Unique id of the Event source
        """
        url_path = "/event-sources/{event_sources_id}"
        dict_path = {"event_sources_id": event_sources_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_event_sources_name_by_name(self, name=""):
        """
        Operation: Get an event source by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the event source
        """
        url_path = "/event-sources/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_event_sources_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an event source by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the event source
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Event source Name. Object Type: string
        "description" : "", #Event source description. Object Type: string
        "ipaddress" : "", #Unique IP Address of the event source. Object Type: string
        "vendor" : "", #Vendor name. Object Type: string
        "type" : "", #Event source type. Object Type: string
        "enable" : False, #Enable event source. Object Type: boolean
        }
        """
        url_path = "/event-sources/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_event_sources_name_by_name(self, name="", body=({})):
        """
        Operation: Replace an event source by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the event source
        Required Body Parameters:['name', 'ipaddress', 'vendor', 'type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Event source Name. Object Type: string
        "description" : "", #Event source description. Object Type: string
        "ipaddress" : "", #Unique IP Address of the event source. Object Type: string
        "vendor" : "", #Vendor name. Object Type: string
        "type" : "", #Event source type. Object Type: string
        "enable" : False, #Enable event source. Object Type: boolean
        }
        """
        url_path = "/event-sources/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_event_sources_name_by_name(self, name=""):
        """
        Operation: Delete an event source by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the event source
        """
        url_path = "/event-sources/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage the system’s installed extensions
    def get_extension_instance(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of installed extensions
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +name)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/extension/instance"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_extension_instance(self, body=({})):
        """
        Operation: Install an extension
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['store_id']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "state" : "", #Desired state of the extension. Object Type: string
        "store_id" : "", #ID from the extension store. Object Type: string
        "files" : {}, #Maps extension file IDs to local content items, with ‘public:’ or ‘private:’ prefix. Object Type: object
        "ip_address" : "", #IP address to allocate to the extension, or null. Object Type: string
        "note" : "", #Note to be displayed with the extension.. Object Type: string
        }
        """
        url_path = "/extension/instance"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_extension_instance_by_id(self, id=""):
        """
        Operation: Get details of an installed extension
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_extension_instance_by_id(self, id="", body=({})):
        """
        Operation: Change the state of an installed extension
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "state" : "", #Desired state of the extension. Object Type: string
        "note" : "", #Note to be displayed with the extension.. Object Type: string
        }
        """
        url_path = "/extension/instance/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def delete_extension_instance_by_id(self, force="", id=""):
        """
        Operation: Uninstall an extension
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: force, Description: True to send a kill signal to the extension before deleting
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}"
        dict_query = {"force": force}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Configure an installed extension
    def get_extension_instance_by_id_config(self, id=""):
        """
        Operation: Get the configuration of an installed extension
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}/config"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_extension_instance_by_id_config(self, id="", body=({})):
        """
        Operation: Set the configuration of an installed extension
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        }
        """
        url_path = "/extension/instance/{id}/config"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    # API Service: Read logs from an installed extension
    def get_extension_instance_by_id_log(
        self, stdout="", stderr="", since="", timestamps="", tail="", id=""
    ):
        """
        Operation: Get the log output from an installed extension
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: stdout, Description: Include extension’s standard-output messages
        Parameter Type (Optional): query, Name: stderr, Description: Include extension’s standard-error messages
        Parameter Type (Optional): query, Name: since, Description: Specify a UNIX timestamp to only return log entries since that time
        Parameter Type (Optional): query, Name: timestamps, Description: Prefix every log line with its UTC timestamp
        Parameter Type (Optional): query, Name: tail, Description: Return this number of lines at the end of the logs, or "all" for everything
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}/log"
        dict_query = {
            "stdout": stdout,
            "stderr": stderr,
            "since": since,
            "timestamps": timestamps,
            "tail": tail,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Reinstall an extension
    def new_extension_instance_by_id_reinstall(self, id="", body=({})):
        """
        Operation: Reinstall an extension
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "state" : "", #Desired state of the extension. Object Type: string
        "files" : {}, #Maps extension file IDs to local content items, with ‘public:’ or ‘private:’ prefix. Object Type: object
        "ip_address" : "", #IP address to allocate to the extension, or null. Object Type: string
        }
        """
        url_path = "/extension/instance/{id}/reinstall"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Restart an installed extension
    def new_extension_instance_by_id_restart(self, id=""):
        """
        Operation: Restart an installed extension
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}/restart"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="post")

    # API Service: Start an installed extension
    def new_extension_instance_by_id_start(self, id=""):
        """
        Operation: Start an installed extension
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}/start"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="post")

    # API Service: Stop an installed extension
    def new_extension_instance_by_id_stop(self, id=""):
        """
        Operation: Stop an installed extension
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}/stop"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="post")

    # API Service: Upgrade an extension
    def get_extension_instance_by_id_upgrade(self, id=""):
        """
        Operation: Get information on an extension's available upgrade
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: ID of the extension instance
        """
        url_path = "/extension/instance/{id}/upgrade"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_extension_instance_by_id_upgrade(self, id="", body=({})):
        """
        Operation: Upgrade an extension
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: ID of the extension instance
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "major" : False, #Indicated whether to install major extension upgrades. False by default.. Object Type: boolean
        "state" : "", #Desired state of the extension. Object Type: string
        "files" : {}, #Maps extension file IDs to local content items, with ‘public:’ or ‘private:’ prefix. Object Type: object
        "ip_address" : "", #IP address to allocate to the extension, or null. Object Type: string
        }
        """
        url_path = "/extension/instance/{id}/upgrade"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Query the extension store
    def get_extension_store(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Find a extension in the store
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +name)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/extension/store"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_extension_store_by_id(self, id=""):
        """
        Operation: Get details of an extension in the store
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/extension/store/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage Ingress Event Dictionaries
    def get_ingress_event_dictionary(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Ingress Event Dictionaries
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/ingress-event-dictionary"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_ingress_event_dictionary(self, body=({})):
        """
                Operation: Create a new Ingress Event Dictionary
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['vendor', 'format_name', 'prefix', 'filter', 'fields', 'generic_fields']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor" : "", #Vendor of the ingress event. Object Type: string
                "format_name" : "", #Format Name of the ingress event. Object Type: string
                "prefix" : "", #Prefix of the ingress event. Object Type: string
                "status" : False, #Status of the ingress event. Object Type: boolean
                "description" : "", #Description of the ingress event. Object Type: string
                "format" : "", #Format of the ingress event. Object Type: string
                "sample" : "", #Sample of the ingress event. Object Type: string
                "filter" : "", #Filter of the ingress event. Object Type: string
                "fields" : [{
             "attr_name":"", #Ingress Event Field atrribute name. Object Type: string
             "data_type":"", #Ingress Event Field attribute type. Object Type: string
             "allowed_values":"", #Allowed values for Ingress Event Field in CSV format. Object Type: string
        }], #Fields of the ingress event. Object Type: array
                "generic_fields" : [{
             "attr_name":"", #Ingress Event Generic Field attribute name. Object Type: string
             "generic_name":"", #Ingress Event Generic name of the attribute. Object Type: string
        }], #Generic Fields of the ingress event. Object Type: array
                }
        """
        url_path = "/ingress-event-dictionary"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_ingress_event_dictionary_by_ingress_event_dictionary_id(
        self, ingress_event_dictionary_id=""
    ):
        """
        Operation: Get an Ingress Event Dictionary
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
        """
        url_path = "/ingress-event-dictionary/{ingress_event_dictionary_id}"
        dict_path = {"ingress_event_dictionary_id": ingress_event_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_ingress_event_dictionary_by_ingress_event_dictionary_id(
        self, ingress_event_dictionary_id="", body=({})
    ):
        """
                Operation: Update an Ingress Event Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor" : "", #Vendor of the ingress event. Object Type: string
                "format_name" : "", #Format Name of the ingress event. Object Type: string
                "prefix" : "", #Prefix of the ingress event. Object Type: string
                "status" : False, #Status of the ingress event. Object Type: boolean
                "description" : "", #Description of the ingress event. Object Type: string
                "format" : "", #Format of the ingress event. Object Type: string
                "sample" : "", #Sample of the ingress event. Object Type: string
                "filter" : "", #Filter of the ingress event. Object Type: string
                "fields" : [{
             "attr_name":"", #Ingress Event Field atrribute name. Object Type: string
             "data_type":"", #Ingress Event Field attribute type. Object Type: string
             "allowed_values":"", #Allowed values for Ingress Event Field in CSV format. Object Type: string
        }], #Fields of the ingress event. Object Type: array
                "generic_fields" : [{
             "attr_name":"", #Ingress Event Generic Field attribute name. Object Type: string
             "generic_name":"", #Ingress Event Generic name of the attribute. Object Type: string
        }], #Generic Fields of the ingress event. Object Type: array
                }
        """
        url_path = "/ingress-event-dictionary/{ingress_event_dictionary_id}"
        dict_path = {"ingress_event_dictionary_id": ingress_event_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_ingress_event_dictionary_by_ingress_event_dictionary_id(
        self, ingress_event_dictionary_id="", body=({})
    ):
        """
                Operation: Replace an Ingress Event Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
                Required Body Parameters:['vendor', 'format_name', 'prefix', 'filter', 'fields', 'generic_fields']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor" : "", #Vendor of the ingress event. Object Type: string
                "format_name" : "", #Format Name of the ingress event. Object Type: string
                "prefix" : "", #Prefix of the ingress event. Object Type: string
                "status" : False, #Status of the ingress event. Object Type: boolean
                "description" : "", #Description of the ingress event. Object Type: string
                "format" : "", #Format of the ingress event. Object Type: string
                "sample" : "", #Sample of the ingress event. Object Type: string
                "filter" : "", #Filter of the ingress event. Object Type: string
                "fields" : [{
             "attr_name":"", #Ingress Event Field atrribute name. Object Type: string
             "data_type":"", #Ingress Event Field attribute type. Object Type: string
             "allowed_values":"", #Allowed values for Ingress Event Field in CSV format. Object Type: string
        }], #Fields of the ingress event. Object Type: array
                "generic_fields" : [{
             "attr_name":"", #Ingress Event Generic Field attribute name. Object Type: string
             "generic_name":"", #Ingress Event Generic name of the attribute. Object Type: string
        }], #Generic Fields of the ingress event. Object Type: array
                }
        """
        url_path = "/ingress-event-dictionary/{ingress_event_dictionary_id}"
        dict_path = {"ingress_event_dictionary_id": ingress_event_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_ingress_event_dictionary_by_ingress_event_dictionary_id(
        self, ingress_event_dictionary_id=""
    ):
        """
        Operation: Delete an Ingress Event Dictionary
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: ingress_event_dictionary_id, Description: Numeric ID of the ingress event dictionary
        """
        url_path = "/ingress-event-dictionary/{ingress_event_dictionary_id}"
        dict_path = {"ingress_event_dictionary_id": ingress_event_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_ingress_event_dictionary_format_name_by_format_name(self, format_name=""):
        """
        Operation: Get an Ingress Event Dictionary by format_name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: format_name, Description: format_name of the ingress event dictionary
        """
        url_path = "/ingress-event-dictionary/format_name/{format_name}"
        dict_path = {"format_name": format_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_ingress_event_dictionary_format_name_by_format_name(
        self, format_name="", body=({})
    ):
        """
                Operation: Update an Ingress Event Dictionary by format_name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: format_name, Description: format_name of the ingress event dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor" : "", #Vendor of the ingress event. Object Type: string
                "format_name" : "", #Format Name of the ingress event. Object Type: string
                "prefix" : "", #Prefix of the ingress event. Object Type: string
                "status" : False, #Status of the ingress event. Object Type: boolean
                "description" : "", #Description of the ingress event. Object Type: string
                "format" : "", #Format of the ingress event. Object Type: string
                "sample" : "", #Sample of the ingress event. Object Type: string
                "filter" : "", #Filter of the ingress event. Object Type: string
                "fields" : [{
             "attr_name":"", #Ingress Event Field atrribute name. Object Type: string
             "data_type":"", #Ingress Event Field attribute type. Object Type: string
             "allowed_values":"", #Allowed values for Ingress Event Field in CSV format. Object Type: string
        }], #Fields of the ingress event. Object Type: array
                "generic_fields" : [{
             "attr_name":"", #Ingress Event Generic Field attribute name. Object Type: string
             "generic_name":"", #Ingress Event Generic name of the attribute. Object Type: string
        }], #Generic Fields of the ingress event. Object Type: array
                }
        """
        url_path = "/ingress-event-dictionary/format_name/{format_name}"
        dict_path = {"format_name": format_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_ingress_event_dictionary_format_name_by_format_name(
        self, format_name="", body=({})
    ):
        """
                Operation: Replace an Ingress Event Dictionary by format_name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: format_name, Description: format_name of the ingress event dictionary
                Required Body Parameters:['vendor', 'format_name', 'prefix', 'filter', 'fields', 'generic_fields']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor" : "", #Vendor of the ingress event. Object Type: string
                "format_name" : "", #Format Name of the ingress event. Object Type: string
                "prefix" : "", #Prefix of the ingress event. Object Type: string
                "status" : False, #Status of the ingress event. Object Type: boolean
                "description" : "", #Description of the ingress event. Object Type: string
                "format" : "", #Format of the ingress event. Object Type: string
                "sample" : "", #Sample of the ingress event. Object Type: string
                "filter" : "", #Filter of the ingress event. Object Type: string
                "fields" : [{
             "attr_name":"", #Ingress Event Field atrribute name. Object Type: string
             "data_type":"", #Ingress Event Field attribute type. Object Type: string
             "allowed_values":"", #Allowed values for Ingress Event Field in CSV format. Object Type: string
        }], #Fields of the ingress event. Object Type: array
                "generic_fields" : [{
             "attr_name":"", #Ingress Event Generic Field attribute name. Object Type: string
             "generic_name":"", #Ingress Event Generic name of the attribute. Object Type: string
        }], #Generic Fields of the ingress event. Object Type: array
                }
        """
        url_path = "/ingress-event-dictionary/format_name/{format_name}"
        dict_path = {"format_name": format_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_ingress_event_dictionary_format_name_by_format_name(
        self, format_name=""
    ):
        """
        Operation: Delete an Ingress Event Dictionary by format_name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: format_name, Description: format_name of the ingress event dictionary
        """
        url_path = "/ingress-event-dictionary/format_name/{format_name}"
        dict_path = {"format_name": format_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage syslog export filter
    def get_syslog_export_filter(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of syslog export filter
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/syslog-export-filter"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_syslog_export_filter(self, body=({})):
        """
        Operation: Create a new syslog export filter
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'export_template', 'export_event_format_type', 'syslog_servers']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of syslog export filter. Object Type: string
        "description" : "", #Description of syslog export filter. Object Type: string
        "export_template" : "", #Export Template type for syslog export filter. Object Type: string
        "export_event_format_type" : "", #Export Event format type for syslog export filter. Object Type: string
        "local_facility_level" : "", #Local Facility Level for syslog export filter. Object Type: string
        "syslog_servers" : "", #List of syslog servers for syslog export filter. Object Type: array
        "cluster_servers" : "", #List of ClearPass servers for syslog export filter. Object Type: array
        "enabled" : False, #Status of syslog export filter. Object Type: boolean
        "data_filter" : "", #Data Filter name for syslog export filter. Object Type: string
        "selected_columns" : "", #List of selected columns for syslog export filter. Object Type: array
        "field_group_name" : "", #Field group name for syslog export filter. Object Type: string
        "custom_sql" : "", #Custom SQL for syslog export filter. Object Type: string
        "include_audit_data" : False, #null. Object Type: boolean
        }
        """
        url_path = "/syslog-export-filter"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_syslog_export_filter_by_syslog_export_filter_id(
        self, syslog_export_filter_id=""
    ):
        """
        Operation: Get a syslog export filter
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: syslog_export_filter_id, Description: Numeric ID of the syslog-export-filter
        """
        url_path = "/syslog-export-filter/{syslog_export_filter_id}"
        dict_path = {"syslog_export_filter_id": syslog_export_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_syslog_export_filter_by_syslog_export_filter_id(
        self, syslog_export_filter_id="", body=({})
    ):
        """
        Operation: Update some fields of a syslog export filter
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: syslog_export_filter_id, Description: Numeric ID of the syslog-export-filter
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of syslog export filter. Object Type: string
        "description" : "", #Description of syslog export filter. Object Type: string
        "export_template" : "", #Export Template type for syslog export filter. Object Type: string
        "export_event_format_type" : "", #Export Event format type for syslog export filter. Object Type: string
        "local_facility_level" : "", #Local Facility Level for syslog export filter. Object Type: string
        "syslog_servers" : "", #List of syslog servers for syslog export filter. Object Type: array
        "cluster_servers" : "", #List of ClearPass servers for syslog export filter. Object Type: array
        "enabled" : False, #Status of syslog export filter. Object Type: boolean
        "data_filter" : "", #Data Filter name for syslog export filter. Object Type: string
        "selected_columns" : "", #List of selected columns for syslog export filter. Object Type: array
        "field_group_name" : "", #Field group name for syslog export filter. Object Type: string
        "custom_sql" : "", #Custom SQL for syslog export filter. Object Type: string
        "include_audit_data" : False, #null. Object Type: boolean
        }
        """
        url_path = "/syslog-export-filter/{syslog_export_filter_id}"
        dict_path = {"syslog_export_filter_id": syslog_export_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_syslog_export_filter_by_syslog_export_filter_id(
        self, syslog_export_filter_id="", body=({})
    ):
        """
        Operation: Replace a syslog export filter
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: syslog_export_filter_id, Description: Numeric ID of the syslog-export-filter
        Required Body Parameters:['name', 'export_template', 'export_event_format_type', 'syslog_servers']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of syslog export filter. Object Type: string
        "description" : "", #Description of syslog export filter. Object Type: string
        "export_template" : "", #Export Template type for syslog export filter. Object Type: string
        "export_event_format_type" : "", #Export Event format type for syslog export filter. Object Type: string
        "local_facility_level" : "", #Local Facility Level for syslog export filter. Object Type: string
        "syslog_servers" : "", #List of syslog servers for syslog export filter. Object Type: array
        "cluster_servers" : "", #List of ClearPass servers for syslog export filter. Object Type: array
        "enabled" : False, #Status of syslog export filter. Object Type: boolean
        "data_filter" : "", #Data Filter name for syslog export filter. Object Type: string
        "selected_columns" : "", #List of selected columns for syslog export filter. Object Type: array
        "field_group_name" : "", #Field group name for syslog export filter. Object Type: string
        "custom_sql" : "", #Custom SQL for syslog export filter. Object Type: string
        "include_audit_data" : False, #null. Object Type: boolean
        }
        """
        url_path = "/syslog-export-filter/{syslog_export_filter_id}"
        dict_path = {"syslog_export_filter_id": syslog_export_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_syslog_export_filter_by_syslog_export_filter_id(
        self, syslog_export_filter_id=""
    ):
        """
        Operation: Delete a syslog export filter
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: syslog_export_filter_id, Description: Numeric ID of the syslog-export-filter
        """
        url_path = "/syslog-export-filter/{syslog_export_filter_id}"
        dict_path = {"syslog_export_filter_id": syslog_export_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_syslog_export_filter_name_by_name(self, name=""):
        """
        Operation: Get a syslog export filter by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the syslog-export-filter
        """
        url_path = "/syslog-export-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_syslog_export_filter_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a syslog export filter by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the syslog-export-filter
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of syslog export filter. Object Type: string
        "description" : "", #Description of syslog export filter. Object Type: string
        "export_template" : "", #Export Template type for syslog export filter. Object Type: string
        "export_event_format_type" : "", #Export Event format type for syslog export filter. Object Type: string
        "local_facility_level" : "", #Local Facility Level for syslog export filter. Object Type: string
        "syslog_servers" : "", #List of syslog servers for syslog export filter. Object Type: array
        "cluster_servers" : "", #List of ClearPass servers for syslog export filter. Object Type: array
        "enabled" : False, #Status of syslog export filter. Object Type: boolean
        "data_filter" : "", #Data Filter name for syslog export filter. Object Type: string
        "selected_columns" : "", #List of selected columns for syslog export filter. Object Type: array
        "field_group_name" : "", #Field group name for syslog export filter. Object Type: string
        "custom_sql" : "", #Custom SQL for syslog export filter. Object Type: string
        "include_audit_data" : False, #null. Object Type: boolean
        }
        """
        url_path = "/syslog-export-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_syslog_export_filter_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a syslog export filter by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the syslog-export-filter
        Required Body Parameters:['name', 'export_template', 'export_event_format_type', 'syslog_servers']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of syslog export filter. Object Type: string
        "description" : "", #Description of syslog export filter. Object Type: string
        "export_template" : "", #Export Template type for syslog export filter. Object Type: string
        "export_event_format_type" : "", #Export Event format type for syslog export filter. Object Type: string
        "local_facility_level" : "", #Local Facility Level for syslog export filter. Object Type: string
        "syslog_servers" : "", #List of syslog servers for syslog export filter. Object Type: array
        "cluster_servers" : "", #List of ClearPass servers for syslog export filter. Object Type: array
        "enabled" : False, #Status of syslog export filter. Object Type: boolean
        "data_filter" : "", #Data Filter name for syslog export filter. Object Type: string
        "selected_columns" : "", #List of selected columns for syslog export filter. Object Type: array
        "field_group_name" : "", #Field group name for syslog export filter. Object Type: string
        "custom_sql" : "", #Custom SQL for syslog export filter. Object Type: string
        "include_audit_data" : False, #null. Object Type: boolean
        }
        """
        url_path = "/syslog-export-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_syslog_export_filter_name_by_name(self, name=""):
        """
        Operation: Delete a syslog export filter by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the syslog-export-filter
        """
        url_path = "/syslog-export-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage syslog target
    def get_syslog_target(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of syslog target
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/syslog-target"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_syslog_target(self, body=({})):
        """
        Operation: Create a new syslog target
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['host_address', 'protocol', 'server_port']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "host_address" : "", #Server host address of syslog target. Object Type: string
        "description" : "", #Description of syslog target. Object Type: string
        "server_port" : 0, #Server port of syslog target. Object Type: integer
        "protocol" : "", #Protocol used for syslog target. Object Type: string
        }
        """
        url_path = "/syslog-target"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_syslog_target_by_syslog_target_id(self, syslog_target_id=""):
        """
        Operation: Get a syslog target
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: syslog_target_id, Description: Numeric ID of the syslog-target
        """
        url_path = "/syslog-target/{syslog_target_id}"
        dict_path = {"syslog_target_id": syslog_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_syslog_target_by_syslog_target_id(self, syslog_target_id="", body=({})):
        """
        Operation: Update some fields of a syslog target
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: syslog_target_id, Description: Numeric ID of the syslog-target
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "host_address" : "", #Server host address of syslog target. Object Type: string
        "description" : "", #Description of syslog target. Object Type: string
        "server_port" : 0, #Server port of syslog target. Object Type: integer
        "protocol" : "", #Protocol used for syslog target. Object Type: string
        }
        """
        url_path = "/syslog-target/{syslog_target_id}"
        dict_path = {"syslog_target_id": syslog_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_syslog_target_by_syslog_target_id(self, syslog_target_id="", body=({})):
        """
        Operation: Replace a syslog target
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: syslog_target_id, Description: Numeric ID of the syslog-target
        Required Body Parameters:['host_address', 'protocol', 'server_port']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "host_address" : "", #Server host address of syslog target. Object Type: string
        "description" : "", #Description of syslog target. Object Type: string
        "server_port" : 0, #Server port of syslog target. Object Type: integer
        "protocol" : "", #Protocol used for syslog target. Object Type: string
        }
        """
        url_path = "/syslog-target/{syslog_target_id}"
        dict_path = {"syslog_target_id": syslog_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_syslog_target_by_syslog_target_id(self, syslog_target_id=""):
        """
        Operation: Delete a syslog target
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: syslog_target_id, Description: Numeric ID of the syslog-target
        """
        url_path = "/syslog-target/{syslog_target_id}"
        dict_path = {"syslog_target_id": syslog_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_syslog_target_host_address_by_host_address(self, host_address=""):
        """
        Operation: Get a syslog target by host_address
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: host_address, Description: Unique host_address of the syslog-target
        """
        url_path = "/syslog-target/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_syslog_target_host_address_by_host_address(
        self, host_address="", body=({})
    ):
        """
        Operation: Update some fields of a syslog target by host_address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: host_address, Description: Unique host_address of the syslog-target
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "host_address" : "", #Server host address of syslog target. Object Type: string
        "description" : "", #Description of syslog target. Object Type: string
        "server_port" : 0, #Server port of syslog target. Object Type: integer
        "protocol" : "", #Protocol used for syslog target. Object Type: string
        }
        """
        url_path = "/syslog-target/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_syslog_target_host_address_by_host_address(
        self, host_address="", body=({})
    ):
        """
        Operation: Replace a syslog target by host_address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: host_address, Description: Unique host_address of the syslog-target
        Required Body Parameters:['host_address', 'protocol', 'server_port']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "host_address" : "", #Server host address of syslog target. Object Type: string
        "description" : "", #Description of syslog target. Object Type: string
        "server_port" : 0, #Server port of syslog target. Object Type: integer
        "protocol" : "", #Protocol used for syslog target. Object Type: string
        }
        """
        url_path = "/syslog-target/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_syslog_target_host_address_by_host_address(self, host_address=""):
        """
        Operation: Delete a syslog target by host_address
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: host_address, Description: Unique host_address of the syslog-target
        """
        url_path = "/syslog-target/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
