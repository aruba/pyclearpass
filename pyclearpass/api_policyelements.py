from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: PolicyElements
# FileName: api_policyelements.py


class ApiPolicyElements(ClearPassAPILogin):
    # API Service: Manage Application Dictionaries
    def get_application_dictionary(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Application Dictionaries
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/application-dictionary"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_application_dictionary(self, body=({})):
        """
                Operation: Create a new Application Dictionary
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Application Dictionary. Object Type: string
                "description" : "", #Description of the Application Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #Application Dictionary Attribute Name. Object Type: string
             "attr_type":"", #Application Dictionary Attribute Type. Object Type: string
             "allowed_values":"", #Allowed Values for Application Dictionary Attributes in CSV format. Object Type: string
        }], #List of Application Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/application-dictionary"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_application_dictionary_by_application_dictionary_id(
        self, application_dictionary_id=""
    ):
        """
        Operation: Get an Application Dictionary
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
        """
        url_path = "/application-dictionary/{application_dictionary_id}"
        dict_path = {"application_dictionary_id": application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_application_dictionary_by_application_dictionary_id(
        self, application_dictionary_id="", body=({})
    ):
        """
                Operation: Update an Application Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Application Dictionary. Object Type: string
                "description" : "", #Description of the Application Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #Application Dictionary Attribute Name. Object Type: string
             "attr_type":"", #Application Dictionary Attribute Type. Object Type: string
             "allowed_values":"", #Allowed Values for Application Dictionary Attributes in CSV format. Object Type: string
        }], #List of Application Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/application-dictionary/{application_dictionary_id}"
        dict_path = {"application_dictionary_id": application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_application_dictionary_by_application_dictionary_id(
        self, application_dictionary_id="", body=({})
    ):
        """
                Operation: Replace an Application Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
                Required Body Parameters:['name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Application Dictionary. Object Type: string
                "description" : "", #Description of the Application Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #Application Dictionary Attribute Name. Object Type: string
             "attr_type":"", #Application Dictionary Attribute Type. Object Type: string
             "allowed_values":"", #Allowed Values for Application Dictionary Attributes in CSV format. Object Type: string
        }], #List of Application Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/application-dictionary/{application_dictionary_id}"
        dict_path = {"application_dictionary_id": application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_application_dictionary_by_application_dictionary_id(
        self, application_dictionary_id=""
    ):
        """
        Operation: Delete an Application Dictionary
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
        """
        url_path = "/application-dictionary/{application_dictionary_id}"
        dict_path = {"application_dictionary_id": application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_application_dictionary_name_by_name(self, name=""):
        """
        Operation: Get an Application Dictionary by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the Application Dictionary
        """
        url_path = "/application-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_application_dictionary_name_by_name(self, name="", body=({})):
        """
                Operation: Update an Application Dictionary by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of the Application Dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Application Dictionary. Object Type: string
                "description" : "", #Description of the Application Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #Application Dictionary Attribute Name. Object Type: string
             "attr_type":"", #Application Dictionary Attribute Type. Object Type: string
             "allowed_values":"", #Allowed Values for Application Dictionary Attributes in CSV format. Object Type: string
        }], #List of Application Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/application-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_application_dictionary_name_by_name(self, name="", body=({})):
        """
                Operation: Replace an Application Dictionary by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of the Application Dictionary
                Required Body Parameters:['name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Application Dictionary. Object Type: string
                "description" : "", #Description of the Application Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #Application Dictionary Attribute Name. Object Type: string
             "attr_type":"", #Application Dictionary Attribute Type. Object Type: string
             "allowed_values":"", #Allowed Values for Application Dictionary Attributes in CSV format. Object Type: string
        }], #List of Application Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/application-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_application_dictionary_name_by_name(self, name=""):
        """
        Operation: Delete an Application Dictionary by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the Application Dictionary
        """
        url_path = "/application-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage authentication methods
    def get_auth_method(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of authentication methods
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/auth-method"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_auth_method(self, body=({})):
        """
        Operation: Create a new authentication method
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'method_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth method. Object Type: string
        "description" : "", #Description of the auth method. Object Type: string
        "method_type" : "", #Type of the auth method. Object Type: string
        "details" : "" #variable unknown: , #Details JSON object of the auth method. Object Type: AuthMethodDetails
        "inner_methods" : "" #variable unknown: , #List of inner methods of the auth method. Object Type: array
        }
        """
        url_path = "/auth-method"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_auth_method_by_auth_method_id(self, auth_method_id=""):
        """
        Operation: Get an authentication method
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: auth_method_id, Description: Numeric ID of the authentication method
        """
        url_path = "/auth-method/{auth_method_id}"
        dict_path = {"auth_method_id": auth_method_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_auth_method_by_auth_method_id(self, auth_method_id="", body=({})):
        """
        Operation: Update some fields of an authentication method
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: auth_method_id, Description: Numeric ID of the authentication method
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth method. Object Type: string
        "description" : "", #Description of the auth method. Object Type: string
        "method_type" : "", #Type of the auth method. Object Type: string
        "details" : "" #variable unknown: , #Details JSON object of the auth method. Object Type: AuthMethodDetails
        "inner_methods" : "" #variable unknown: , #List of inner methods of the auth method. Object Type: array
        }
        """
        url_path = "/auth-method/{auth_method_id}"
        dict_path = {"auth_method_id": auth_method_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_auth_method_by_auth_method_id(self, auth_method_id="", body=({})):
        """
        Operation: Replace an authentication method
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: auth_method_id, Description: Numeric ID of the authentication method
        Required Body Parameters:['name', 'method_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth method. Object Type: string
        "description" : "", #Description of the auth method. Object Type: string
        "method_type" : "", #Type of the auth method. Object Type: string
        "details" : "" #variable unknown: , #Details JSON object of the auth method. Object Type: AuthMethodDetails
        "inner_methods" : "" #variable unknown: , #List of inner methods of the auth method. Object Type: array
        }
        """
        url_path = "/auth-method/{auth_method_id}"
        dict_path = {"auth_method_id": auth_method_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_auth_method_by_auth_method_id(self, auth_method_id=""):
        """
        Operation: Delete an authentication method
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: auth_method_id, Description: Numeric ID of the authentication method
        """
        url_path = "/auth-method/{auth_method_id}"
        dict_path = {"auth_method_id": auth_method_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_auth_method_name_by_name(self, name=""):
        """
        Operation: Get an authentication method by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the authentication method
        """
        url_path = "/auth-method/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_auth_method_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an authentication method by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the authentication method
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth method. Object Type: string
        "description" : "", #Description of the auth method. Object Type: string
        "method_type" : "", #Type of the auth method. Object Type: string
        "details" : "" #variable unknown: , #Details JSON object of the auth method. Object Type: AuthMethodDetails
        "inner_methods" : "" #variable unknown: , #List of inner methods of the auth method. Object Type: array
        }
        """
        url_path = "/auth-method/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_auth_method_name_by_name(self, name="", body=({})):
        """
        Operation: Replace an authentication method by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the authentication method
        Required Body Parameters:['name', 'method_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth method. Object Type: string
        "description" : "", #Description of the auth method. Object Type: string
        "method_type" : "", #Type of the auth method. Object Type: string
        "details" : "" #variable unknown: , #Details JSON object of the auth method. Object Type: AuthMethodDetails
        "inner_methods" : "" #variable unknown: , #List of inner methods of the auth method. Object Type: array
        }
        """
        url_path = "/auth-method/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_auth_method_name_by_name(self, name=""):
        """
        Operation: Delete an authentication method by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the authentication method
        """
        url_path = "/auth-method/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage authentication sources
    def get_auth_source(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of authentication sources
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/auth-source"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_auth_source(self, body=({})):
        """
        Operation: Create a new authentication source
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'type', 'cppm_primary_auth_source_connection_details', 'server_timeout', 'cache_timeout']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth source. Object Type: string
        "description" : "", #Description of the auth source. Object Type: string
        "type" : "", #Type of the auth source. Object Type: string
        "use_for_authorization" : False, #Enable to use this Authentication Source. Object Type: boolean
        "authorization_source_names" : False, #additional auth-sources from which role-mapping attributes to be fetched. Object Type: array
        "cppm_primary_auth_source_connection_details" : "" #variable unknown: , #details of Authentication source. Object Type: AuthSourceConnectionDetailsMetadataCreate
        "auth_source_radius_attributes" : "" #variable unknown: , #details of authSourceRadiusAttributes. Object Type: AuthSourceRadiusAttributeDetailsCreate
        "cppm_auth_source_connection_backups" : "" #variable unknown: , #details of authentication source backups. Object Type: AuthSourceBackupConnectionDetailsMetadataCreate
        "auth_source_filters" : "" #variable unknown: , #details of auth_source_filters. Object Type: AuthSourceFiltersDetailsCreate
        "server_timeout" : 0, #Time out if the Authentication source fails to send a response to an authorization query. Object Type: integer
        "cache_timeout" : 0, #Specify the duration in number of seconds for which the attributes are cached.. Object Type: integer
        }
        """
        url_path = "/auth-source"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_auth_source_by_auth_source_id(self, auth_source_id=""):
        """
        Operation: Get an authentication source
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: auth_source_id, Description: Numeric ID of the authentication source
        """
        url_path = "/auth-source/{auth_source_id}"
        dict_path = {"auth_source_id": auth_source_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_auth_source_by_auth_source_id(self, auth_source_id="", body=({})):
        """
        Operation: Update some fields of an authentication source
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: auth_source_id, Description: Numeric ID of the authentication source
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth source. Object Type: string
        "description" : "", #Description of the auth source. Object Type: string
        "type" : "", #Type of the auth source. Object Type: string
        "use_for_authorization" : False, #Enable to use this Authentication Source. Object Type: boolean
        "authorization_source_names" : False, #additional auth-sources from which role-mapping attributes to be fetched. Object Type: array
        "cppm_primary_auth_source_connection_details" : "" #variable unknown: , #details of Authentication source. Object Type: AuthSourceConnectionDetailsUpdate
        "auth_source_radius_attributes" : "" #variable unknown: , #details of authSourceRadiusAttributes. Object Type: AuthSourceRadiusAttributeDetailsUpdate
        "cppm_auth_source_connection_backups" : "" #variable unknown: , #details of authentication source backups. Object Type: AuthSourceBackupConnectionDetailsMetadataUpdate
        "auth_source_filters" : "" #variable unknown: , #details of auth_source_filters. Object Type: AuthSourceFiltersDetailsUpdate
        "server_timeout" : 0, #Time out if the Authentication source fails to send a response to an authorization query. Object Type: integer
        "cache_timeout" : 0, #Specify the duration in number of seconds for which the attributes are cached.. Object Type: integer
        }
        """
        url_path = "/auth-source/{auth_source_id}"
        dict_path = {"auth_source_id": auth_source_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_auth_source_by_auth_source_id(self, auth_source_id="", body=({})):
        """
        Operation: Replace an authentication source
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: auth_source_id, Description: Numeric ID of the authentication source
        Required Body Parameters:['name', 'type', 'cppm_primary_auth_source_connection_details', 'server_timeout', 'cache_timeout']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth source. Object Type: string
        "description" : "", #Description of the auth source. Object Type: string
        "type" : "", #Type of the auth source. Object Type: string
        "use_for_authorization" : False, #Enable to use this Authentication Source. Object Type: boolean
        "authorization_source_names" : False, #additional auth-sources from which role-mapping attributes to be fetched. Object Type: array
        "cppm_primary_auth_source_connection_details" : "" #variable unknown: , #details of Authentication source. Object Type: AuthSourceConnectionDetailsMetadataReplace
        "auth_source_radius_attributes" : "" #variable unknown: , #details of authSourceRadiusAttributes. Object Type: AuthSourceRadiusAttributeDetailsReplace
        "cppm_auth_source_connection_backups" : "" #variable unknown: , #details of authentication source backups. Object Type: AuthSourceBackupConnectionDetailsMetadataReplace
        "auth_source_filters" : "" #variable unknown: , #details of auth_source_filters. Object Type: AuthSourceFiltersDetailsReplace
        "server_timeout" : 0, #Time out if the Authentication source fails to send a response to an authorization query. Object Type: integer
        "cache_timeout" : 0, #Specify the duration in number of seconds for which the attributes are cached.. Object Type: integer
        }
        """
        url_path = "/auth-source/{auth_source_id}"
        dict_path = {"auth_source_id": auth_source_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_auth_source_by_auth_source_id(self, auth_source_id=""):
        """
        Operation: Delete an authentication source
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: auth_source_id, Description: Numeric ID of the authentication source
        """
        url_path = "/auth-source/{auth_source_id}"
        dict_path = {"auth_source_id": auth_source_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_auth_source_name_by_name(self, name=""):
        """
        Operation: Get an authentication source by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the authentication source
        """
        url_path = "/auth-source/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_auth_source_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an authentication source by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the authentication source
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth source. Object Type: string
        "description" : "", #Description of the auth source. Object Type: string
        "type" : "", #Type of the auth source. Object Type: string
        "use_for_authorization" : False, #Enable to use this Authentication Source. Object Type: boolean
        "authorization_source_names" : False, #additional auth-sources from which role-mapping attributes to be fetched. Object Type: array
        "cppm_primary_auth_source_connection_details" : "" #variable unknown: , #details of Authentication source. Object Type: AuthSourceConnectionDetailsUpdate
        "auth_source_radius_attributes" : "" #variable unknown: , #details of authSourceRadiusAttributes. Object Type: AuthSourceRadiusAttributeDetailsUpdate
        "cppm_auth_source_connection_backups" : "" #variable unknown: , #details of authentication source backups. Object Type: AuthSourceBackupConnectionDetailsMetadataUpdate
        "auth_source_filters" : "" #variable unknown: , #details of auth_source_filters. Object Type: AuthSourceFiltersDetailsUpdate
        "server_timeout" : 0, #Time out if the Authentication source fails to send a response to an authorization query. Object Type: integer
        "cache_timeout" : 0, #Specify the duration in number of seconds for which the attributes are cached.. Object Type: integer
        }
        """
        url_path = "/auth-source/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_auth_source_name_by_name(self, name="", body=({})):
        """
        Operation: Replace an authentication source by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the authentication source
        Required Body Parameters:['name', 'type', 'cppm_primary_auth_source_connection_details', 'server_timeout', 'cache_timeout']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the auth source. Object Type: string
        "description" : "", #Description of the auth source. Object Type: string
        "type" : "", #Type of the auth source. Object Type: string
        "use_for_authorization" : False, #Enable to use this Authentication Source. Object Type: boolean
        "authorization_source_names" : False, #additional auth-sources from which role-mapping attributes to be fetched. Object Type: array
        "cppm_primary_auth_source_connection_details" : "" #variable unknown: , #details of Authentication source. Object Type: AuthSourceConnectionDetailsMetadataReplace
        "auth_source_radius_attributes" : "" #variable unknown: , #details of authSourceRadiusAttributes. Object Type: AuthSourceRadiusAttributeDetailsReplace
        "cppm_auth_source_connection_backups" : "" #variable unknown: , #details of authentication source backups. Object Type: AuthSourceBackupConnectionDetailsMetadataReplace
        "auth_source_filters" : "" #variable unknown: , #details of auth_source_filters. Object Type: AuthSourceFiltersDetailsReplace
        "server_timeout" : 0, #Time out if the Authentication source fails to send a response to an authorization query. Object Type: integer
        "cache_timeout" : 0, #Specify the duration in number of seconds for which the attributes are cached.. Object Type: integer
        }
        """
        url_path = "/auth-source/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_auth_source_name_by_name(self, name=""):
        """
        Operation: Delete an authentication source by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the authentication source
        """
        url_path = "/auth-source/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Enforcement Policies
    def get_enforcement_policy(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of enforcement policies
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/enforcement-policy"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_policy(self, body=({})):
        """
        Operation: Create a new enforcement policy
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'enforcement_type', 'default_enforcement_profile', 'rule_eval_algo', 'rules']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the Enforcement Policy. Object Type: string
        "description" : "", #Description of the Enforcement Policy. Object Type: string
        "enforcement_type" : "", #Enforcement Type of the Enforcement Policy. Object Type: string
        "default_enforcement_profile" : "", #Default Enforcement Profile for the Enforcement Policy. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm of the Enforcement Policy rules. Object Type: string
        "rules" : "" #variable unknown: , #List of Rules for Enforcement Policy. Object Type: RulesSettingsCreate
        }
        """
        url_path = "/enforcement-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_policy_by_enforcement_policy_id(self, enforcement_policy_id=""):
        """
        Operation: Get a enforcement policy
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        """
        url_path = "/enforcement-policy/{enforcement_policy_id}"
        dict_path = {"enforcement_policy_id": enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_policy_by_enforcement_policy_id(
        self, enforcement_policy_id="", body=({})
    ):
        """
        Operation: Update a enforcement policy
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the Enforcement Policy. Object Type: string
        "description" : "", #Description of the Enforcement Policy. Object Type: string
        "enforcement_type" : "", #Enforcement Type of the Enforcement Policy. Object Type: string
        "default_enforcement_profile" : "", #Default Enforcement Profile for the Enforcement Policy. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm of the Enforcement Policy rules. Object Type: string
        "rules" : "" #variable unknown: , #List of Rules for Enforcement Policy. Object Type: RulesSettingsUpdate
        }
        """
        url_path = "/enforcement-policy/{enforcement_policy_id}"
        dict_path = {"enforcement_policy_id": enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_policy_by_enforcement_policy_id(
        self, enforcement_policy_id="", body=({})
    ):
        """
        Operation: Replace a enforcement policy
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        Required Body Parameters:['name', 'enforcement_type', 'default_enforcement_profile', 'rule_eval_algo', 'rules']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the Enforcement Policy. Object Type: string
        "description" : "", #Description of the Enforcement Policy. Object Type: string
        "enforcement_type" : "", #Enforcement Type of the Enforcement Policy. Object Type: string
        "default_enforcement_profile" : "", #Default Enforcement Profile for the Enforcement Policy. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm of the Enforcement Policy rules. Object Type: string
        "rules" : "" #variable unknown: , #List of Rules for Enforcement Policy. Object Type: RulesSettingsReplace
        }
        """
        url_path = "/enforcement-policy/{enforcement_policy_id}"
        dict_path = {"enforcement_policy_id": enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_policy_by_enforcement_policy_id(
        self, enforcement_policy_id=""
    ):
        """
        Operation: Delete a enforcement policy
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        """
        url_path = "/enforcement-policy/{enforcement_policy_id}"
        dict_path = {"enforcement_policy_id": enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_policy_name_by_name(self, name=""):
        """
        Operation: Get a enforcement policy by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the enforcement policy
        """
        url_path = "/enforcement-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_policy_name_by_name(self, name="", body=({})):
        """
        Operation: Update a enforcement policy by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the enforcement policy
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the Enforcement Policy. Object Type: string
        "description" : "", #Description of the Enforcement Policy. Object Type: string
        "enforcement_type" : "", #Enforcement Type of the Enforcement Policy. Object Type: string
        "default_enforcement_profile" : "", #Default Enforcement Profile for the Enforcement Policy. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm of the Enforcement Policy rules. Object Type: string
        "rules" : "" #variable unknown: , #List of Rules for Enforcement Policy. Object Type: RulesSettingsUpdate
        }
        """
        url_path = "/enforcement-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_policy_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a enforcement policy by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the enforcement policy
        Required Body Parameters:['name', 'enforcement_type', 'default_enforcement_profile', 'rule_eval_algo', 'rules']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the Enforcement Policy. Object Type: string
        "description" : "", #Description of the Enforcement Policy. Object Type: string
        "enforcement_type" : "", #Enforcement Type of the Enforcement Policy. Object Type: string
        "default_enforcement_profile" : "", #Default Enforcement Profile for the Enforcement Policy. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm of the Enforcement Policy rules. Object Type: string
        "rules" : "" #variable unknown: , #List of Rules for Enforcement Policy. Object Type: RulesSettingsReplace
        }
        """
        url_path = "/enforcement-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_policy_name_by_name(self, name=""):
        """
        Operation: Delete a enforcement policy by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the enforcement policy
        """
        url_path = "/enforcement-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage network devices
    def get_network_device(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of network devices
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/network-device"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_network_device(self, body=({})):
        """
        Operation: Create a new network device
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'ip_address']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "description" : "", #Description of the network device. Object Type: string
        "name" : "", #Name of the network device. Object Type: string
        "ip_address" : "", #IP or Subnet Address of the network device. Object Type: string
        "radius_secret" : "", #RADIUS Shared Secret of the network device. Object Type: string
        "tacacs_secret" : "", #TACACS+ Shared Secret of the network device. Object Type: string
        "vendor_name" : "", #Vendor Name of the network device. Object Type: string
        "vendor_id" : 0, #Vendor Id of the network device. Object Type: integer
        "coa_capable" : False, #Flag indicating if the network device is capable of CoA. Object Type: boolean
        "coa_port" : 0, #CoA port number of the network device. Object Type: integer
        "radsec_enabled" : False, #Flag indicating if the network device is radSec enabled. Object Type: boolean
        "snmp_read" : "" #variable unknown: , #SNMP read settings of the network device. Object Type: SNMPReadSettings
        "snmp_write" : "" #variable unknown: , #SNMP write settings of the network device. Object Type: SNMPWriteSettings
        "radsec_config" : "" #variable unknown: , #RadSec settings of the network device. Object Type: RadSecSettings
        "cli_config" : "" #variable unknown: , #CLI Configuration details of the network device. Object Type: CLISettings
        "onConnect_enforcement" : "" #variable unknown: , #OnConnect Enforcement settings of the network device. Object Type: OnConnectEnforcementSettings
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the network device. Object Type: object
        }
        """
        url_path = "/network-device"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_network_device_by_network_device_id(self, network_device_id=""):
        """
        Operation: Get a network device
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: network_device_id, Description: Numeric ID of the network device
        """
        url_path = "/network-device/{network_device_id}"
        dict_path = {"network_device_id": network_device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_network_device_by_network_device_id(
        self, network_device_id="", body=({})
    ):
        """
        Operation: Update some fields of a network device
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: network_device_id, Description: Numeric ID of the network device
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "description" : "", #Description of the network device. Object Type: string
        "name" : "", #Name of the network device. Object Type: string
        "ip_address" : "", #IP or Subnet Address of the network device. Object Type: string
        "radius_secret" : "", #RADIUS Shared Secret of the network device. Object Type: string
        "tacacs_secret" : "", #TACACS+ Shared Secret of the network device. Object Type: string
        "vendor_name" : "", #Vendor Name of the network device. Object Type: string
        "vendor_id" : 0, #Vendor Id of the network device. Object Type: integer
        "coa_capable" : False, #Flag indicating if the network device is capable of CoA. Object Type: boolean
        "coa_port" : 0, #CoA port number of the network device. Object Type: integer
        "radsec_enabled" : False, #Flag indicating if the network device is radSec enabled. Object Type: boolean
        "snmp_read" : "" #variable unknown: , #SNMP read settings of the network device. Object Type: SNMPReadSettings
        "snmp_write" : "" #variable unknown: , #SNMP write settings of the network device. Object Type: SNMPWriteSettings
        "radsec_config" : "" #variable unknown: , #RadSec settings of the network device. Object Type: RadSecSettings
        "cli_config" : "" #variable unknown: , #CLI Configuration details of the network device. Object Type: CLISettings
        "onConnect_enforcement" : "" #variable unknown: , #OnConnect Enforcement settings of the network device. Object Type: OnConnectEnforcementSettings
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the network device. Object Type: object
        }
        """
        url_path = "/network-device/{network_device_id}"
        dict_path = {"network_device_id": network_device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_network_device_by_network_device_id(
        self, network_device_id="", body=({})
    ):
        """
        Operation: Replace a network device
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: network_device_id, Description: Numeric ID of the network device
        Required Body Parameters:['name', 'ip_address']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "description" : "", #Description of the network device. Object Type: string
        "name" : "", #Name of the network device. Object Type: string
        "ip_address" : "", #IP or Subnet Address of the network device. Object Type: string
        "radius_secret" : "", #RADIUS Shared Secret of the network device. Object Type: string
        "tacacs_secret" : "", #TACACS+ Shared Secret of the network device. Object Type: string
        "vendor_name" : "", #Vendor Name of the network device. Object Type: string
        "vendor_id" : 0, #Vendor Id of the network device. Object Type: integer
        "coa_capable" : False, #Flag indicating if the network device is capable of CoA. Object Type: boolean
        "coa_port" : 0, #CoA port number of the network device. Object Type: integer
        "radsec_enabled" : False, #Flag indicating if the network device is radSec enabled. Object Type: boolean
        "snmp_read" : "" #variable unknown: , #SNMP read settings of the network device. Object Type: SNMPReadSettings
        "snmp_write" : "" #variable unknown: , #SNMP write settings of the network device. Object Type: SNMPWriteSettings
        "radsec_config" : "" #variable unknown: , #RadSec settings of the network device. Object Type: RadSecSettings
        "cli_config" : "" #variable unknown: , #CLI Configuration details of the network device. Object Type: CLISettings
        "onConnect_enforcement" : "" #variable unknown: , #OnConnect Enforcement settings of the network device. Object Type: OnConnectEnforcementSettings
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the network device. Object Type: object
        }
        """
        url_path = "/network-device/{network_device_id}"
        dict_path = {"network_device_id": network_device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_network_device_by_network_device_id(self, network_device_id=""):
        """
        Operation: Delete a network device
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: network_device_id, Description: Numeric ID of the network device
        """
        url_path = "/network-device/{network_device_id}"
        dict_path = {"network_device_id": network_device_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_network_device_name_by_name(self, name=""):
        """
        Operation: Get a network device by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the network device
        """
        url_path = "/network-device/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_network_device_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a network device by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the network device
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "description" : "", #Description of the network device. Object Type: string
        "name" : "", #Name of the network device. Object Type: string
        "ip_address" : "", #IP or Subnet Address of the network device. Object Type: string
        "radius_secret" : "", #RADIUS Shared Secret of the network device. Object Type: string
        "tacacs_secret" : "", #TACACS+ Shared Secret of the network device. Object Type: string
        "vendor_name" : "", #Vendor Name of the network device. Object Type: string
        "vendor_id" : 0, #Vendor Id of the network device. Object Type: integer
        "coa_capable" : False, #Flag indicating if the network device is capable of CoA. Object Type: boolean
        "coa_port" : 0, #CoA port number of the network device. Object Type: integer
        "radsec_enabled" : False, #Flag indicating if the network device is radSec enabled. Object Type: boolean
        "snmp_read" : "" #variable unknown: , #SNMP read settings of the network device. Object Type: SNMPReadSettings
        "snmp_write" : "" #variable unknown: , #SNMP write settings of the network device. Object Type: SNMPWriteSettings
        "radsec_config" : "" #variable unknown: , #RadSec settings of the network device. Object Type: RadSecSettings
        "cli_config" : "" #variable unknown: , #CLI Configuration details of the network device. Object Type: CLISettings
        "onConnect_enforcement" : "" #variable unknown: , #OnConnect Enforcement settings of the network device. Object Type: OnConnectEnforcementSettings
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the network device. Object Type: object
        }
        """
        url_path = "/network-device/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_network_device_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a network device by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the network device
        Required Body Parameters:['name', 'ip_address']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "description" : "", #Description of the network device. Object Type: string
        "name" : "", #Name of the network device. Object Type: string
        "ip_address" : "", #IP or Subnet Address of the network device. Object Type: string
        "radius_secret" : "", #RADIUS Shared Secret of the network device. Object Type: string
        "tacacs_secret" : "", #TACACS+ Shared Secret of the network device. Object Type: string
        "vendor_name" : "", #Vendor Name of the network device. Object Type: string
        "vendor_id" : 0, #Vendor Id of the network device. Object Type: integer
        "coa_capable" : False, #Flag indicating if the network device is capable of CoA. Object Type: boolean
        "coa_port" : 0, #CoA port number of the network device. Object Type: integer
        "radsec_enabled" : False, #Flag indicating if the network device is radSec enabled. Object Type: boolean
        "snmp_read" : "" #variable unknown: , #SNMP read settings of the network device. Object Type: SNMPReadSettings
        "snmp_write" : "" #variable unknown: , #SNMP write settings of the network device. Object Type: SNMPWriteSettings
        "radsec_config" : "" #variable unknown: , #RadSec settings of the network device. Object Type: RadSecSettings
        "cli_config" : "" #variable unknown: , #CLI Configuration details of the network device. Object Type: CLISettings
        "onConnect_enforcement" : "" #variable unknown: , #OnConnect Enforcement settings of the network device. Object Type: OnConnectEnforcementSettings
        "attributes" : {}, #Additional attributes(key/value pairs) may be stored with the network device. Object Type: object
        }
        """
        url_path = "/network-device/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_network_device_name_by_name(self, name=""):
        """
        Operation: Delete a network device by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the network device
        """
        url_path = "/network-device/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage network device groups
    def get_network_device_group(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of network device groups
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/network-device-group"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_network_device_group(self, body=({})):
        """
        Operation: Create a new network device group
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'group_format', 'value']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the network device group. Object Type: string
        "description" : "", #Description of the network device group. Object Type: string
        "group_format" : "", #Format of the network devices. Object Type: string
        "value" : "", #Network devices in the specified format. Object Type: string
        }
        """
        url_path = "/network-device-group"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_network_device_group_by_network_device_group_id(
        self, network_device_group_id=""
    ):
        """
        Operation: Get a network device group
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: network_device_group_id, Description: Numeric ID of the network device group
        """
        url_path = "/network-device-group/{network_device_group_id}"
        dict_path = {"network_device_group_id": network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_network_device_group_by_network_device_group_id(
        self, network_device_group_id="", body=({})
    ):
        """
        Operation: Update some fields of a network device group
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: network_device_group_id, Description: Numeric ID of the network device group
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the network device group. Object Type: string
        "description" : "", #Description of the network device group. Object Type: string
        "group_format" : "", #Format of the network devices. Object Type: string
        "value" : "", #Network devices in the specified format. Object Type: string
        }
        """
        url_path = "/network-device-group/{network_device_group_id}"
        dict_path = {"network_device_group_id": network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_network_device_group_by_network_device_group_id(
        self, network_device_group_id="", body=({})
    ):
        """
        Operation: Replace a network device group
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: network_device_group_id, Description: Numeric ID of the network device group
        Required Body Parameters:['name', 'group_format', 'value']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the network device group. Object Type: string
        "description" : "", #Description of the network device group. Object Type: string
        "group_format" : "", #Format of the network devices. Object Type: string
        "value" : "", #Network devices in the specified format. Object Type: string
        }
        """
        url_path = "/network-device-group/{network_device_group_id}"
        dict_path = {"network_device_group_id": network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_network_device_group_by_network_device_group_id(
        self, network_device_group_id=""
    ):
        """
        Operation: Delete a network device group
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: network_device_group_id, Description: Numeric ID of the network device group
        """
        url_path = "/network-device-group/{network_device_group_id}"
        dict_path = {"network_device_group_id": network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_network_device_group_name_by_name(self, name=""):
        """
        Operation: Get a network device group by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the network device group
        """
        url_path = "/network-device-group/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_network_device_group_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a network device group by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the network device group
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the network device group. Object Type: string
        "description" : "", #Description of the network device group. Object Type: string
        "group_format" : "", #Format of the network devices. Object Type: string
        "value" : "", #Network devices in the specified format. Object Type: string
        }
        """
        url_path = "/network-device-group/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_network_device_group_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a network device group by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the network device group
        Required Body Parameters:['name', 'group_format', 'value']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the network device group. Object Type: string
        "description" : "", #Description of the network device group. Object Type: string
        "group_format" : "", #Format of the network devices. Object Type: string
        "value" : "", #Network devices in the specified format. Object Type: string
        }
        """
        url_path = "/network-device-group/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_network_device_group_name_by_name(self, name=""):
        """
        Operation: Delete a network device group by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the network device group
        """
        url_path = "/network-device-group/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Posture Policies
    def get_posture_policy(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Posture Policies
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/posture-policy"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_posture_policy(self, body=({})):
        """
        Operation: Create a new Posture Policy
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'posture_agent', 'policy_xml']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Posture Policy Name. Object Type: string
        "description" : "", #Description. Object Type: string
        "posture_agent" : "", #Posture Agent. Object Type: string
        "host_os" : "", #Host Operating System. Object Type: string
        "plugin_version" : "", #Plugin Version. Object Type: string
        "roles" : "", #Restrict by Roles. Object Type: array
        "policy_xml" : "", #Posture Policy XML. Object Type: string
        }
        """
        url_path = "/posture-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_posture_policy_by_posture_policy_id(self, posture_policy_id=""):
        """
        Operation: Get a Posture Policy
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        """
        url_path = "/posture-policy/{posture_policy_id}"
        dict_path = {"posture_policy_id": posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_posture_policy_by_posture_policy_id(
        self, posture_policy_id="", body=({})
    ):
        """
        Operation: Update a Posture Policy
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Posture Policy Name. Object Type: string
        "description" : "", #Description. Object Type: string
        "posture_agent" : "", #Posture Agent. Object Type: string
        "host_os" : "", #Host Operating System. Object Type: string
        "plugin_version" : "", #Plugin Version. Object Type: string
        "roles" : "", #Restrict by Roles. Object Type: array
        "policy_xml" : "", #Posture Policy XML. Object Type: string
        }
        """
        url_path = "/posture-policy/{posture_policy_id}"
        dict_path = {"posture_policy_id": posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_posture_policy_by_posture_policy_id(
        self, posture_policy_id="", body=({})
    ):
        """
        Operation: Replace a Posture Policy
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        Required Body Parameters:['name', 'posture_agent', 'policy_xml']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Posture Policy Name. Object Type: string
        "description" : "", #Description. Object Type: string
        "posture_agent" : "", #Posture Agent. Object Type: string
        "host_os" : "", #Host Operating System. Object Type: string
        "plugin_version" : "", #Plugin Version. Object Type: string
        "roles" : "", #Restrict by Roles. Object Type: array
        "policy_xml" : "", #Posture Policy XML. Object Type: string
        }
        """
        url_path = "/posture-policy/{posture_policy_id}"
        dict_path = {"posture_policy_id": posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_posture_policy_by_posture_policy_id(self, posture_policy_id=""):
        """
        Operation: Delete a Posture Policy
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        """
        url_path = "/posture-policy/{posture_policy_id}"
        dict_path = {"posture_policy_id": posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_posture_policy_name_by_name(self, name=""):
        """
        Operation: Get a Posture Policy by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the Posture Policy
        """
        url_path = "/posture-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_posture_policy_name_by_name(self, name="", body=({})):
        """
        Operation: Update a Posture Policy by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the Posture Policy
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Posture Policy Name. Object Type: string
        "description" : "", #Description. Object Type: string
        "posture_agent" : "", #Posture Agent. Object Type: string
        "host_os" : "", #Host Operating System. Object Type: string
        "plugin_version" : "", #Plugin Version. Object Type: string
        "roles" : "", #Restrict by Roles. Object Type: array
        "policy_xml" : "", #Posture Policy XML. Object Type: string
        }
        """
        url_path = "/posture-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_posture_policy_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a Posture Policy by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the Posture Policy
        Required Body Parameters:['name', 'posture_agent', 'policy_xml']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Posture Policy Name. Object Type: string
        "description" : "", #Description. Object Type: string
        "posture_agent" : "", #Posture Agent. Object Type: string
        "host_os" : "", #Host Operating System. Object Type: string
        "plugin_version" : "", #Plugin Version. Object Type: string
        "roles" : "", #Restrict by Roles. Object Type: array
        "policy_xml" : "", #Posture Policy XML. Object Type: string
        }
        """
        url_path = "/posture-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_posture_policy_name_by_name(self, name=""):
        """
        Operation: Delete a Posture Policy by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the Posture Policy
        """
        url_path = "/posture-policy/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage RADIUS Dictionaries
    def get_radius_dictionary(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of RADIUS Dictionaries
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/radius-dictionary"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_radius_dictionary(self, body=({})):
        """
                Operation: Create a new RADIUS Dictionary
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['vendor_id', 'vendor_name', 'prefix', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_id" : 0, #Vendor ID of RADIUS Dictionary. Object Type: integer
                "vendor_name" : "", #Vendor Name of RADIUS Dictionary. Object Type: string
                "prefix" : "", #Vendor Prefix of RADIUS Dictionary. Object Type: string
                "enabled" : False, #Is RADIUS Dictionary enabled?. Object Type: boolean
                "attributes" : [{
             "attr_id":0, #RADIUS Dictionary Attribute ID. Object Type: integer
             "attr_name":"", #RADIUS Dictionary Attribute Name. Object Type: string
             "attr_type":"", #RADIUS Dictionary Attribute Type. Object Type: string
             "attr_profile":"", #["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile. Object Type: string
             "extra_data":"", #RADIUS Dictionary Attribute Extra Data. Object Type: string
             "valid_values":[{"":""}], #RADIUS Dictionary Attribute Valid Values. Object Type: array
        }], #Attributes of RADIUS Dictionary. Object Type: array
                }
        """
        url_path = "/radius-dictionary"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_radius_dictionary_by_radius_dictionary_id(self, radius_dictionary_id=""):
        """
        Operation: Get a RADIUS Dictionary
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        """
        url_path = "/radius-dictionary/{radius_dictionary_id}"
        dict_path = {"radius_dictionary_id": radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_radius_dictionary_by_radius_dictionary_id(
        self, radius_dictionary_id="", body=({})
    ):
        """
                Operation: Update a RADIUS Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_id" : 0, #Vendor ID of RADIUS Dictionary. Object Type: integer
                "vendor_name" : "", #Vendor Name of RADIUS Dictionary. Object Type: string
                "prefix" : "", #Vendor Prefix of RADIUS Dictionary. Object Type: string
                "enabled" : False, #Is RADIUS Dictionary enabled?. Object Type: boolean
                "attributes" : [{
             "attr_id":0, #RADIUS Dictionary Attribute ID. Object Type: integer
             "attr_name":"", #RADIUS Dictionary Attribute Name. Object Type: string
             "attr_type":"", #RADIUS Dictionary Attribute Type. Object Type: string
             "attr_profile":"", #["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile. Object Type: string
             "extra_data":"", #RADIUS Dictionary Attribute Extra Data. Object Type: string
             "valid_values":[{"":""}], #RADIUS Dictionary Attribute Valid Values. Object Type: array
        }], #Attributes of RADIUS Dictionary. Object Type: array
                }
        """
        url_path = "/radius-dictionary/{radius_dictionary_id}"
        dict_path = {"radius_dictionary_id": radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_radius_dictionary_by_radius_dictionary_id(
        self, radius_dictionary_id="", body=({})
    ):
        """
                Operation: Replace a RADIUS Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
                Required Body Parameters:['vendor_id', 'vendor_name', 'prefix', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_id" : 0, #Vendor ID of RADIUS Dictionary. Object Type: integer
                "vendor_name" : "", #Vendor Name of RADIUS Dictionary. Object Type: string
                "prefix" : "", #Vendor Prefix of RADIUS Dictionary. Object Type: string
                "enabled" : False, #Is RADIUS Dictionary enabled?. Object Type: boolean
                "attributes" : [{
             "attr_id":0, #RADIUS Dictionary Attribute ID. Object Type: integer
             "attr_name":"", #RADIUS Dictionary Attribute Name. Object Type: string
             "attr_type":"", #RADIUS Dictionary Attribute Type. Object Type: string
             "attr_profile":"", #["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile. Object Type: string
             "extra_data":"", #RADIUS Dictionary Attribute Extra Data. Object Type: string
             "valid_values":[{"":""}], #RADIUS Dictionary Attribute Valid Values. Object Type: array
        }], #Attributes of RADIUS Dictionary. Object Type: array
                }
        """
        url_path = "/radius-dictionary/{radius_dictionary_id}"
        dict_path = {"radius_dictionary_id": radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def get_radius_dictionary_name_by_name(self, name=""):
        """
        Operation: Get a RADIUS Dictionary by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the RADIUS Dictionary
        """
        url_path = "/radius-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_radius_dictionary_name_by_name(self, name="", body=({})):
        """
                Operation: Update a RADIUS Dictionary by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of the RADIUS Dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_id" : 0, #Vendor ID of RADIUS Dictionary. Object Type: integer
                "vendor_name" : "", #Vendor Name of RADIUS Dictionary. Object Type: string
                "prefix" : "", #Vendor Prefix of RADIUS Dictionary. Object Type: string
                "enabled" : False, #Is RADIUS Dictionary enabled?. Object Type: boolean
                "attributes" : [{
             "attr_id":0, #RADIUS Dictionary Attribute ID. Object Type: integer
             "attr_name":"", #RADIUS Dictionary Attribute Name. Object Type: string
             "attr_type":"", #RADIUS Dictionary Attribute Type. Object Type: string
             "attr_profile":"", #["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile. Object Type: string
             "extra_data":"", #RADIUS Dictionary Attribute Extra Data. Object Type: string
             "valid_values":[{"":""}], #RADIUS Dictionary Attribute Valid Values. Object Type: array
        }], #Attributes of RADIUS Dictionary. Object Type: array
                }
        """
        url_path = "/radius-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_radius_dictionary_name_by_name(self, name="", body=({})):
        """
                Operation: Replace a RADIUS Dictionary by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of the RADIUS Dictionary
                Required Body Parameters:['vendor_id', 'vendor_name', 'prefix', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_id" : 0, #Vendor ID of RADIUS Dictionary. Object Type: integer
                "vendor_name" : "", #Vendor Name of RADIUS Dictionary. Object Type: string
                "prefix" : "", #Vendor Prefix of RADIUS Dictionary. Object Type: string
                "enabled" : False, #Is RADIUS Dictionary enabled?. Object Type: boolean
                "attributes" : [{
             "attr_id":0, #RADIUS Dictionary Attribute ID. Object Type: integer
             "attr_name":"", #RADIUS Dictionary Attribute Name. Object Type: string
             "attr_type":"", #RADIUS Dictionary Attribute Type. Object Type: string
             "attr_profile":"", #["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile. Object Type: string
             "extra_data":"", #RADIUS Dictionary Attribute Extra Data. Object Type: string
             "valid_values":[{"":""}], #RADIUS Dictionary Attribute Valid Values. Object Type: array
        }], #Attributes of RADIUS Dictionary. Object Type: array
                }
        """
        url_path = "/radius-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_radius_dictionary_by_radius_dictionary_id_enable(
        self, radius_dictionary_id=""
    ):
        """
        Operation: Enable a RADIUS Dictionary
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        """
        url_path = "/radius-dictionary/{radius_dictionary_id}/enable"
        dict_path = {"radius_dictionary_id": radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_radius_dictionary_by_radius_dictionary_id_disable(
        self, radius_dictionary_id=""
    ):
        """
        Operation: Disable a RADIUS Dictionary
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        """
        url_path = "/radius-dictionary/{radius_dictionary_id}/disable"
        dict_path = {"radius_dictionary_id": radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_radius_dictionary_name_by_name_enable(self, name=""):
        """
        Operation: Enable a RADIUS Dictionary by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the RADIUS Dictionary
        """
        url_path = "/radius-dictionary/name/{name}/enable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_radius_dictionary_name_by_name_disable(self, name=""):
        """
        Operation: Disable a RADIUS Dictionary by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the RADIUS Dictionary
        """
        url_path = "/radius-dictionary/name/{name}/disable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # API Service: Manage RADIUS Dynamic Authorization Templates
    def get_radius_dynamic_authorization_template(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of RADIUS Dynamic Authorization Templates
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/radius-dynamic-authorization-template"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_radius_dynamic_authorization_template(self, body=({})):
        """
                Operation: Create a new RADIUS Dynamic Authorization Template
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['name', 'vendor_name', 'template_type', 'display_name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_name" : "", #Vendor Name of RADIUS Dynamic Authorization Template. Object Type: string
                "template_type" : "", #Template Type of RADIUS Dynamic Authorization Template. Object Type: string
                "name" : "", #Name of RADIUS Dynamic Authorization Template. Object Type: string
                "display_name" : "", #Display Name of RADIUS Dynamic Authorization Template. Object Type: string
                "attributes" : [{
             "input_required":"", #RADIUS Dynamic Authorization Template Attribute Input Required. Object Type: string
             "value":"", #RADIUS Dynamic Authorization Template Attribute Value. Object Type: string
             "name":"", #RADIUS Dynamic Authorization Template Attribute Name. Object Type: string
             "type":"", #RADIUS Dynamic Authorization Template Attribute Type. Object Type: string
        }], #Attributes of RADIUS Dynamic Authorization Template. Object Type: array
                }
        """
        url_path = "/radius-dynamic-authorization-template"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(
        self, radius_dynamic_authorization_template_id=""
    ):
        """
        Operation: Get a RADIUS Dynamic Authorization Template
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
        """
        url_path = "/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}"
        dict_path = {
            "radius_dynamic_authorization_template_id": radius_dynamic_authorization_template_id
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(
        self, radius_dynamic_authorization_template_id="", body=({})
    ):
        """
                Operation: Update a RADIUS Dynamic Authorization Template
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_name" : "", #Vendor Name of RADIUS Dynamic Authorization Template. Object Type: string
                "template_type" : "", #Template Type of RADIUS Dynamic Authorization Template. Object Type: string
                "name" : "", #Name of RADIUS Dynamic Authorization Template. Object Type: string
                "display_name" : "", #Display Name of RADIUS Dynamic Authorization Template. Object Type: string
                "attributes" : [{
             "input_required":"", #RADIUS Dynamic Authorization Template Attribute Input Required. Object Type: string
             "value":"", #RADIUS Dynamic Authorization Template Attribute Value. Object Type: string
             "name":"", #RADIUS Dynamic Authorization Template Attribute Name. Object Type: string
             "type":"", #RADIUS Dynamic Authorization Template Attribute Type. Object Type: string
        }], #Attributes of RADIUS Dynamic Authorization Template. Object Type: array
                }
        """
        url_path = "/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}"
        dict_path = {
            "radius_dynamic_authorization_template_id": radius_dynamic_authorization_template_id
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(
        self, radius_dynamic_authorization_template_id="", body=({})
    ):
        """
                Operation: Replace a RADIUS Dynamic Authorization Template
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
                Required Body Parameters:['name', 'vendor_name', 'template_type', 'display_name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_name" : "", #Vendor Name of RADIUS Dynamic Authorization Template. Object Type: string
                "template_type" : "", #Template Type of RADIUS Dynamic Authorization Template. Object Type: string
                "name" : "", #Name of RADIUS Dynamic Authorization Template. Object Type: string
                "display_name" : "", #Display Name of RADIUS Dynamic Authorization Template. Object Type: string
                "attributes" : [{
             "input_required":"", #RADIUS Dynamic Authorization Template Attribute Input Required. Object Type: string
             "value":"", #RADIUS Dynamic Authorization Template Attribute Value. Object Type: string
             "name":"", #RADIUS Dynamic Authorization Template Attribute Name. Object Type: string
             "type":"", #RADIUS Dynamic Authorization Template Attribute Type. Object Type: string
        }], #Attributes of RADIUS Dynamic Authorization Template. Object Type: array
                }
        """
        url_path = "/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}"
        dict_path = {
            "radius_dynamic_authorization_template_id": radius_dynamic_authorization_template_id
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(
        self, radius_dynamic_authorization_template_id=""
    ):
        """
        Operation: Delete a RADIUS Dynamic Authorization Template
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
        """
        url_path = "/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}"
        dict_path = {
            "radius_dynamic_authorization_template_id": radius_dynamic_authorization_template_id
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_radius_dynamic_authorization_template_name_by_name(self, name=""):
        """
        Operation: Get a RADIUS Dynamic Authorization Template by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
        """
        url_path = "/radius-dynamic-authorization-template/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_radius_dynamic_authorization_template_name_by_name(
        self, name="", body=({})
    ):
        """
                Operation: Update a RADIUS Dynamic Authorization Template by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_name" : "", #Vendor Name of RADIUS Dynamic Authorization Template. Object Type: string
                "template_type" : "", #Template Type of RADIUS Dynamic Authorization Template. Object Type: string
                "name" : "", #Name of RADIUS Dynamic Authorization Template. Object Type: string
                "display_name" : "", #Display Name of RADIUS Dynamic Authorization Template. Object Type: string
                "attributes" : [{
             "input_required":"", #RADIUS Dynamic Authorization Template Attribute Input Required. Object Type: string
             "value":"", #RADIUS Dynamic Authorization Template Attribute Value. Object Type: string
             "name":"", #RADIUS Dynamic Authorization Template Attribute Name. Object Type: string
             "type":"", #RADIUS Dynamic Authorization Template Attribute Type. Object Type: string
        }], #Attributes of RADIUS Dynamic Authorization Template. Object Type: array
                }
        """
        url_path = "/radius-dynamic-authorization-template/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_radius_dynamic_authorization_template_name_by_name(
        self, name="", body=({})
    ):
        """
                Operation: Replace a RADIUS Dynamic Authorization Template by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
                Required Body Parameters:['name', 'vendor_name', 'template_type', 'display_name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "vendor_name" : "", #Vendor Name of RADIUS Dynamic Authorization Template. Object Type: string
                "template_type" : "", #Template Type of RADIUS Dynamic Authorization Template. Object Type: string
                "name" : "", #Name of RADIUS Dynamic Authorization Template. Object Type: string
                "display_name" : "", #Display Name of RADIUS Dynamic Authorization Template. Object Type: string
                "attributes" : [{
             "input_required":"", #RADIUS Dynamic Authorization Template Attribute Input Required. Object Type: string
             "value":"", #RADIUS Dynamic Authorization Template Attribute Value. Object Type: string
             "name":"", #RADIUS Dynamic Authorization Template Attribute Name. Object Type: string
             "type":"", #RADIUS Dynamic Authorization Template Attribute Type. Object Type: string
        }], #Attributes of RADIUS Dynamic Authorization Template. Object Type: array
                }
        """
        url_path = "/radius-dynamic-authorization-template/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_radius_dynamic_authorization_template_name_by_name(self, name=""):
        """
        Operation: Delete a RADIUS Dynamic Authorization Template by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
        """
        url_path = "/radius-dynamic-authorization-template/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage proxy targets
    def get_proxy_target(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of proxy targets
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/proxy-target"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_proxy_target(self, body=({})):
        """
        Operation: Create a new proxy target
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'host_name', 'proxy_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the proxy target. Object Type: string
        "host_name" : "", #Host name of the proxy target. Object Type: string
        "description" : "", #Description of the proxy target. Object Type: string
        "authentication_port" : 0, #Authentication port of the proxy target. Object Type: integer
        "proxy_type" : "", #The proxy type, either RADIUS or RadSec. Object Type: string
        "accounting_port" : 0, #Accounting port of the proxy target. Object Type: integer
        "secret" : "", #Shared Secret of the proxy target. Object Type: string
        "radsec_port" : 0, #The RadSec proxy port number (Should be 2083). Object Type: integer
        "radsec_verify_cert" : False, #Enable to verify the server certificate. Object Type: boolean
        "cert_subject" : "", #Client Certificate Subject. Object Type: string
        "enable_status_server_msgs" : False, #Enable to send the status-server message. Object Type: boolean
        }
        """
        url_path = "/proxy-target"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_proxy_target_by_proxy_target_id(self, proxy_target_id=""):
        """
        Operation: Get a proxy target
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: proxy_target_id, Description: Numeric ID of the proxy target
        """
        url_path = "/proxy-target/{proxy_target_id}"
        dict_path = {"proxy_target_id": proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_proxy_target_by_proxy_target_id(self, proxy_target_id="", body=({})):
        """
        Operation: Update some fields of a proxy target
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: proxy_target_id, Description: Numeric ID of the proxy target
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the proxy target. Object Type: string
        "host_name" : "", #Host name of the proxy target. Object Type: string
        "description" : "", #Description of the proxy target. Object Type: string
        "authentication_port" : 0, #Authentication port of the proxy target. Object Type: integer
        "proxy_type" : "", #The proxy type, either RADIUS or RadSec. Object Type: string
        "accounting_port" : 0, #Accounting port of the proxy target. Object Type: integer
        "secret" : "", #Shared Secret of the proxy target. Object Type: string
        "radsec_port" : 0, #The RadSec proxy port number (Should be 2083). Object Type: integer
        "radsec_verify_cert" : False, #Enable to verify the server certificate. Object Type: boolean
        "cert_subject" : "", #Client Certificate Subject. Object Type: string
        "enable_status_server_msgs" : False, #Enable to send the status-server message. Object Type: boolean
        }
        """
        url_path = "/proxy-target/{proxy_target_id}"
        dict_path = {"proxy_target_id": proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_proxy_target_by_proxy_target_id(self, proxy_target_id="", body=({})):
        """
        Operation: Replace a proxy target
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: proxy_target_id, Description: Numeric ID of the proxy target
        Required Body Parameters:['name', 'host_name', 'proxy_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the proxy target. Object Type: string
        "host_name" : "", #Host name of the proxy target. Object Type: string
        "description" : "", #Description of the proxy target. Object Type: string
        "authentication_port" : 0, #Authentication port of the proxy target. Object Type: integer
        "proxy_type" : "", #The proxy type, either RADIUS or RadSec. Object Type: string
        "accounting_port" : 0, #Accounting port of the proxy target. Object Type: integer
        "secret" : "", #Shared Secret of the proxy target. Object Type: string
        "radsec_port" : 0, #The RadSec proxy port number (Should be 2083). Object Type: integer
        "radsec_verify_cert" : False, #Enable to verify the server certificate. Object Type: boolean
        "cert_subject" : "", #Client Certificate Subject. Object Type: string
        "enable_status_server_msgs" : False, #Enable to send the status-server message. Object Type: boolean
        }
        """
        url_path = "/proxy-target/{proxy_target_id}"
        dict_path = {"proxy_target_id": proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_proxy_target_by_proxy_target_id(self, proxy_target_id=""):
        """
        Operation: Delete a proxy target
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: proxy_target_id, Description: Numeric ID of the proxy target
        """
        url_path = "/proxy-target/{proxy_target_id}"
        dict_path = {"proxy_target_id": proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_proxy_target_name_by_name(self, name=""):
        """
        Operation: Get a proxy target by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the proxy target
        """
        url_path = "/proxy-target/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_proxy_target_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a proxy target by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the proxy target
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the proxy target. Object Type: string
        "host_name" : "", #Host name of the proxy target. Object Type: string
        "description" : "", #Description of the proxy target. Object Type: string
        "authentication_port" : 0, #Authentication port of the proxy target. Object Type: integer
        "proxy_type" : "", #The proxy type, either RADIUS or RadSec. Object Type: string
        "accounting_port" : 0, #Accounting port of the proxy target. Object Type: integer
        "secret" : "", #Shared Secret of the proxy target. Object Type: string
        "radsec_port" : 0, #The RadSec proxy port number (Should be 2083). Object Type: integer
        "radsec_verify_cert" : False, #Enable to verify the server certificate. Object Type: boolean
        "cert_subject" : "", #Client Certificate Subject. Object Type: string
        "enable_status_server_msgs" : False, #Enable to send the status-server message. Object Type: boolean
        }
        """
        url_path = "/proxy-target/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_proxy_target_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a proxy target by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the proxy target
        Required Body Parameters:['name', 'host_name', 'proxy_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the proxy target. Object Type: string
        "host_name" : "", #Host name of the proxy target. Object Type: string
        "description" : "", #Description of the proxy target. Object Type: string
        "authentication_port" : 0, #Authentication port of the proxy target. Object Type: integer
        "proxy_type" : "", #The proxy type, either RADIUS or RadSec. Object Type: string
        "accounting_port" : 0, #Accounting port of the proxy target. Object Type: integer
        "secret" : "", #Shared Secret of the proxy target. Object Type: string
        "radsec_port" : 0, #The RadSec proxy port number (Should be 2083). Object Type: integer
        "radsec_verify_cert" : False, #Enable to verify the server certificate. Object Type: boolean
        "cert_subject" : "", #Client Certificate Subject. Object Type: string
        "enable_status_server_msgs" : False, #Enable to send the status-server message. Object Type: boolean
        }
        """
        url_path = "/proxy-target/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_proxy_target_name_by_name(self, name=""):
        """
        Operation: Delete a proxy target by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the proxy target
        """
        url_path = "/proxy-target/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage roles
    def get_role(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of roles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/role"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_role(self, body=({})):
        """
        Operation: Create a new role
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the role. Object Type: string
        "description" : "", #Description of the role. Object Type: string
        }
        """
        url_path = "/role"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_role_by_role_id(self, role_id=""):
        """
        Operation: Get a role
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: role_id, Description: Numeric ID of the role
        """
        url_path = "/role/{role_id}"
        dict_path = {"role_id": role_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_role_by_role_id(self, role_id="", body=({})):
        """
        Operation: Update some fields of a role
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: role_id, Description: Numeric ID of the role
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the role. Object Type: string
        "description" : "", #Description of the role. Object Type: string
        }
        """
        url_path = "/role/{role_id}"
        dict_path = {"role_id": role_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_role_by_role_id(self, role_id="", body=({})):
        """
        Operation: Replace a role
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: role_id, Description: Numeric ID of the role
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the role. Object Type: string
        "description" : "", #Description of the role. Object Type: string
        }
        """
        url_path = "/role/{role_id}"
        dict_path = {"role_id": role_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_role_by_role_id(self, role_id=""):
        """
        Operation: Delete a role
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: role_id, Description: Numeric ID of the role
        """
        url_path = "/role/{role_id}"
        dict_path = {"role_id": role_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_role_name_by_name(self, name=""):
        """
        Operation: Get a role by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the role
        """
        url_path = "/role/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_role_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a role by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the role
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the role. Object Type: string
        "description" : "", #Description of the role. Object Type: string
        }
        """
        url_path = "/role/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_role_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a role by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the role
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Name of the role. Object Type: string
        "description" : "", #Description of the role. Object Type: string
        }
        """
        url_path = "/role/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_role_name_by_name(self, name=""):
        """
        Operation: Delete a role by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the role
        """
        url_path = "/role/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Role Mappings
    def get_role_mapping(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of role mappings
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/role-mapping"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_role_mapping(self, body=({})):
        """
        Operation: Create a new role mapping
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'default_role_name', 'rule_combine_algo', 'rules']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Role mapping policy name. Object Type: string
        "description" : "", #Role mapping description. Object Type: string
        "default_role_name" : "", #Role mapping default role name. Object Type: string
        "rule_combine_algo" : "", #Role mapping rules evaluation algorithm. Object Type: string
        "rules" : "" #variable unknown: , #List of role mapping rules. Object Type: RulesSettingsCreate
        }
        """
        url_path = "/role-mapping"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_role_mapping_by_role_mapping_id(self, role_mapping_id=""):
        """
        Operation: Get a role mapping
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: role_mapping_id, Description: Numeric ID of the role mapping
        """
        url_path = "/role-mapping/{role_mapping_id}"
        dict_path = {"role_mapping_id": role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_role_mapping_by_role_mapping_id(self, role_mapping_id="", body=({})):
        """
        Operation: Update a role mapping
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: role_mapping_id, Description: Numeric ID of the role mapping
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Role mapping policy name. Object Type: string
        "description" : "", #Role mapping description. Object Type: string
        "default_role_name" : "", #Role mapping default role name. Object Type: string
        "rule_combine_algo" : "", #Role mapping rules evaluation algorithm. Object Type: string
        "rules" : "" #variable unknown: , #List of role mapping rules. Object Type: RulesSettingsUpdate
        }
        """
        url_path = "/role-mapping/{role_mapping_id}"
        dict_path = {"role_mapping_id": role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_role_mapping_by_role_mapping_id(self, role_mapping_id="", body=({})):
        """
        Operation: Replace a role mapping
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: role_mapping_id, Description: Numeric ID of the role mapping
        Required Body Parameters:['name', 'default_role_name', 'rule_combine_algo', 'rules']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Role mapping policy name. Object Type: string
        "description" : "", #Role mapping description. Object Type: string
        "default_role_name" : "", #Role mapping default role name. Object Type: string
        "rule_combine_algo" : "", #Role mapping rules evaluation algorithm. Object Type: string
        "rules" : "" #variable unknown: , #List of role mapping rules. Object Type: RulesSettingsReplace
        }
        """
        url_path = "/role-mapping/{role_mapping_id}"
        dict_path = {"role_mapping_id": role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_role_mapping_by_role_mapping_id(self, role_mapping_id=""):
        """
        Operation: Delete a role mapping
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: role_mapping_id, Description: Numeric ID of the role mapping
        """
        url_path = "/role-mapping/{role_mapping_id}"
        dict_path = {"role_mapping_id": role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_role_mapping_name_by_name(self, name=""):
        """
        Operation: Get a role mapping by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the role mapping
        """
        url_path = "/role-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_role_mapping_name_by_name(self, name="", body=({})):
        """
        Operation: Update a role mapping by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the role mapping
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Role mapping policy name. Object Type: string
        "description" : "", #Role mapping description. Object Type: string
        "default_role_name" : "", #Role mapping default role name. Object Type: string
        "rule_combine_algo" : "", #Role mapping rules evaluation algorithm. Object Type: string
        "rules" : "" #variable unknown: , #List of role mapping rules. Object Type: RulesSettingsUpdate
        }
        """
        url_path = "/role-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_role_mapping_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a role mapping by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the role mapping
        Required Body Parameters:['name', 'default_role_name', 'rule_combine_algo', 'rules']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "name" : "", #Role mapping policy name. Object Type: string
        "description" : "", #Role mapping description. Object Type: string
        "default_role_name" : "", #Role mapping default role name. Object Type: string
        "rule_combine_algo" : "", #Role mapping rules evaluation algorithm. Object Type: string
        "rules" : "" #variable unknown: , #List of role mapping rules. Object Type: RulesSettingsReplace
        }
        """
        url_path = "/role-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_role_mapping_name_by_name(self, name=""):
        """
        Operation: Delete a role mapping by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the role mapping
        """
        url_path = "/role-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Configuration Services
    def get_config_service(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Services
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/config/service"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_config_service(self, body=({})):
        """
                Operation: Create a new Service
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['name', 'template', 'enf_policy']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Service. Object Type: string
                "template" : "", #Template of the Service. Object Type: string
                "enabled" : False, #Is Service enabled?. Object Type: boolean
                "order_no" : 0, #Order number of the Service. Object Type: integer
                "description" : "", #Description of the Service. Object Type: string
                "monitor_mode" : False, #Enable to monitor network access without enforcement. Object Type: boolean
                "rules_match_type" : "", #Matches ANY/ALL of the rule conditions. Object Type: string
                "rules_conditions" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of service rules conditions. Object Type: array
                "auth_methods" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Method Names. Object Type: array
                "auth_sources" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Source Names. Object Type: array
                "strip_username" : False, #Enable to specify a comma-separated list of rules to strip username prefixes or suffixes. Object Type: boolean
                "strip_username_csv" : "", #Strip Username Rule. Object Type: string
                "service_cert_cn" : "", #Subject DN of Service Certificate. Object Type: string
                "service_cert_expiry_date" : "", #Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z). Object Type: string
                "role_mapping_policy" : "", #Role Mapping Policy Name. Object Type: string
                "enf_policy" : "", #Enforcement Policy Name. Object Type: string
                "use_cached_policy_results" : False, #Enable to use cached Roles and Posture attributes from previous sessions. Object Type: boolean
                "authz_sources" : False, #List of Additional authorization sources from which to fetch role-mapping attributes. Object Type: array
                "posture_enabled" : False, #Enable Posture Compliance. Object Type: boolean
                "posture_policies" : False, #List of Posture Policy Names. Object Type: array
                "default_posture_token" : "", #Default Posture Token. Object Type: string
                "remediate_end_hosts" : False, #Enable auto-remediation of non-compliant end-hosts. Object Type: boolean
                "remediation_url" : "", #Remediation URL. Object Type: string
                "audit_enabled" : False, #Enable Audit End-hosts. Object Type: boolean
                "audit_server" : "", #Audit Server Name. Object Type: string
                "audit_trigger_condition" : "", #Audit Trigger Conditions. Object Type: string
                "audit_mac_auth_client_type" : "", #Client Type For MAC authentication request Audit Trigger Condition. Object Type: string
                "action_after_audit" : "", #Action after audit. Object Type: string
                "audit_coa_acton" : "", #RADIUS CoA Action to be triggered after audit. Object Type: string
                "profiler_enabled" : False, #Enable Profile Endpoints. Object Type: boolean
                "profiler_endpoint_classification" : False, #List of Endpoint classification(s) after which an action must be triggered. Object Type: array
                "profiler_coa_action" : "", #RADIUS CoA Action to be triggered by Profiler . Object Type: string
                "acct_proxy_enabled" : False, #Enable Accounting Proxy Targets. Object Type: boolean
                "acct_proxy_targets" : False, #List Accounting Proxy Target names. Object Type: array
                "acct_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be deleted for Accounting proxy. Object Type: array
                "acct_proxy_attrs_to_add" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "value":"", #Value. Object Type: string
        }], #RADIUS attributes to be added for Accounting proxy. Object Type: array
                "radius_proxy_scheme" : "", #Proxying Scheme for RADIUS Proxy Service Type. Object Type: string
                "radius_proxy_targets" : "", #List of Proxy Targets for RADIUS Proxy Service Type. Object Type: array
                "radius_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be removed from remote server (proxy target) reply. Object Type: array
                "radius_proxy_enable_for_acct" : False, #Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) . Object Type: boolean
                }
        """
        url_path = "/config/service"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_config_service_by_services_id(self, services_id=""):
        """
        Operation: Get a Service
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: services_id, Description: Numeric ID of the service
        """
        url_path = "/config/service/{services_id}"
        dict_path = {"services_id": services_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_config_service_by_services_id(self, services_id="", body=({})):
        """
                Operation: Update some fields of a Service
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: services_id, Description: Numeric ID of the service
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Service. Object Type: string
                "template" : "", #Template of the Service. Object Type: string
                "enabled" : False, #Is Service enabled?. Object Type: boolean
                "order_no" : 0, #Order number of the Service. Object Type: integer
                "description" : "", #Description of the Service. Object Type: string
                "monitor_mode" : False, #Enable to monitor network access without enforcement. Object Type: boolean
                "rules_match_type" : "", #Matches ANY/ALL of the rule conditions. Object Type: string
                "rules_conditions" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of service rules conditions. Object Type: array
                "auth_methods" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Method Names. Object Type: array
                "auth_sources" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Source Names. Object Type: array
                "strip_username" : False, #Enable to specify a comma-separated list of rules to strip username prefixes or suffixes. Object Type: boolean
                "strip_username_csv" : "", #Strip Username Rule. Object Type: string
                "service_cert_cn" : "", #Subject DN of Service Certificate. Object Type: string
                "service_cert_expiry_date" : "", #Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z). Object Type: string
                "role_mapping_policy" : "", #Role Mapping Policy Name. Object Type: string
                "enf_policy" : "", #Enforcement Policy Name. Object Type: string
                "use_cached_policy_results" : False, #Enable to use cached Roles and Posture attributes from previous sessions. Object Type: boolean
                "authz_sources" : False, #List of Additional authorization sources from which to fetch role-mapping attributes. Object Type: array
                "posture_enabled" : False, #Enable Posture Compliance. Object Type: boolean
                "posture_policies" : False, #List of Posture Policy Names. Object Type: array
                "default_posture_token" : "", #Default Posture Token. Object Type: string
                "remediate_end_hosts" : False, #Enable auto-remediation of non-compliant end-hosts. Object Type: boolean
                "remediation_url" : "", #Remediation URL. Object Type: string
                "audit_enabled" : False, #Enable Audit End-hosts. Object Type: boolean
                "audit_server" : "", #Audit Server Name. Object Type: string
                "audit_trigger_condition" : "", #Audit Trigger Conditions. Object Type: string
                "audit_mac_auth_client_type" : "", #Client Type For MAC authentication request Audit Trigger Condition. Object Type: string
                "action_after_audit" : "", #Action after audit. Object Type: string
                "audit_coa_acton" : "", #RADIUS CoA Action to be triggered after audit. Object Type: string
                "profiler_enabled" : False, #Enable Profile Endpoints. Object Type: boolean
                "profiler_endpoint_classification" : False, #List of Endpoint classification(s) after which an action must be triggered. Object Type: array
                "profiler_coa_action" : "", #RADIUS CoA Action to be triggered by Profiler . Object Type: string
                "acct_proxy_enabled" : False, #Enable Accounting Proxy Targets. Object Type: boolean
                "acct_proxy_targets" : False, #List Accounting Proxy Target names. Object Type: array
                "acct_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be deleted for Accounting proxy. Object Type: array
                "acct_proxy_attrs_to_add" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "value":"", #Value. Object Type: string
        }], #RADIUS attributes to be added for Accounting proxy. Object Type: array
                "radius_proxy_scheme" : "", #Proxying Scheme for RADIUS Proxy Service Type. Object Type: string
                "radius_proxy_targets" : "", #List of Proxy Targets for RADIUS Proxy Service Type. Object Type: array
                "radius_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be removed from remote server (proxy target) reply. Object Type: array
                "radius_proxy_enable_for_acct" : False, #Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) . Object Type: boolean
                }
        """
        url_path = "/config/service/{services_id}"
        dict_path = {"services_id": services_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_config_service_by_services_id(self, services_id="", body=({})):
        """
                Operation: Replace a Service
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: services_id, Description: Numeric ID of the service
                Required Body Parameters:['name', 'template', 'enf_policy']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Service. Object Type: string
                "template" : "", #Template of the Service. Object Type: string
                "enabled" : False, #Is Service enabled?. Object Type: boolean
                "order_no" : 0, #Order number of the Service. Object Type: integer
                "description" : "", #Description of the Service. Object Type: string
                "monitor_mode" : False, #Enable to monitor network access without enforcement. Object Type: boolean
                "rules_match_type" : "", #Matches ANY/ALL of the rule conditions. Object Type: string
                "rules_conditions" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of service rules conditions. Object Type: array
                "auth_methods" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Method Names. Object Type: array
                "auth_sources" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Source Names. Object Type: array
                "strip_username" : False, #Enable to specify a comma-separated list of rules to strip username prefixes or suffixes. Object Type: boolean
                "strip_username_csv" : "", #Strip Username Rule. Object Type: string
                "service_cert_cn" : "", #Subject DN of Service Certificate. Object Type: string
                "service_cert_expiry_date" : "", #Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z). Object Type: string
                "role_mapping_policy" : "", #Role Mapping Policy Name. Object Type: string
                "enf_policy" : "", #Enforcement Policy Name. Object Type: string
                "use_cached_policy_results" : False, #Enable to use cached Roles and Posture attributes from previous sessions. Object Type: boolean
                "authz_sources" : False, #List of Additional authorization sources from which to fetch role-mapping attributes. Object Type: array
                "posture_enabled" : False, #Enable Posture Compliance. Object Type: boolean
                "posture_policies" : False, #List of Posture Policy Names. Object Type: array
                "default_posture_token" : "", #Default Posture Token. Object Type: string
                "remediate_end_hosts" : False, #Enable auto-remediation of non-compliant end-hosts. Object Type: boolean
                "remediation_url" : "", #Remediation URL. Object Type: string
                "audit_enabled" : False, #Enable Audit End-hosts. Object Type: boolean
                "audit_server" : "", #Audit Server Name. Object Type: string
                "audit_trigger_condition" : "", #Audit Trigger Conditions. Object Type: string
                "audit_mac_auth_client_type" : "", #Client Type For MAC authentication request Audit Trigger Condition. Object Type: string
                "action_after_audit" : "", #Action after audit. Object Type: string
                "audit_coa_acton" : "", #RADIUS CoA Action to be triggered after audit. Object Type: string
                "profiler_enabled" : False, #Enable Profile Endpoints. Object Type: boolean
                "profiler_endpoint_classification" : False, #List of Endpoint classification(s) after which an action must be triggered. Object Type: array
                "profiler_coa_action" : "", #RADIUS CoA Action to be triggered by Profiler . Object Type: string
                "acct_proxy_enabled" : False, #Enable Accounting Proxy Targets. Object Type: boolean
                "acct_proxy_targets" : False, #List Accounting Proxy Target names. Object Type: array
                "acct_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be deleted for Accounting proxy. Object Type: array
                "acct_proxy_attrs_to_add" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "value":"", #Value. Object Type: string
        }], #RADIUS attributes to be added for Accounting proxy. Object Type: array
                "radius_proxy_scheme" : "", #Proxying Scheme for RADIUS Proxy Service Type. Object Type: string
                "radius_proxy_targets" : "", #List of Proxy Targets for RADIUS Proxy Service Type. Object Type: array
                "radius_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be removed from remote server (proxy target) reply. Object Type: array
                "radius_proxy_enable_for_acct" : False, #Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) . Object Type: boolean
                }
        """
        url_path = "/config/service/{services_id}"
        dict_path = {"services_id": services_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_config_service_by_services_id(self, services_id=""):
        """
        Operation: Delete a Service
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: services_id, Description: Numeric ID of the service
        """
        url_path = "/config/service/{services_id}"
        dict_path = {"services_id": services_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_config_service_name_by_services_name(self, services_name=""):
        """
        Operation: Get a Service by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: services_name, Description: Name of the Service
        """
        url_path = "/config/service/name/{services_name}"
        dict_path = {"services_name": services_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_config_service_name_by_services_name(self, services_name="", body=({})):
        """
                Operation: Update some fields of a Service by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: services_name, Description: Name of the Service
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Service. Object Type: string
                "template" : "", #Template of the Service. Object Type: string
                "enabled" : False, #Is Service enabled?. Object Type: boolean
                "order_no" : 0, #Order number of the Service. Object Type: integer
                "description" : "", #Description of the Service. Object Type: string
                "monitor_mode" : False, #Enable to monitor network access without enforcement. Object Type: boolean
                "rules_match_type" : "", #Matches ANY/ALL of the rule conditions. Object Type: string
                "rules_conditions" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of service rules conditions. Object Type: array
                "auth_methods" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Method Names. Object Type: array
                "auth_sources" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Source Names. Object Type: array
                "strip_username" : False, #Enable to specify a comma-separated list of rules to strip username prefixes or suffixes. Object Type: boolean
                "strip_username_csv" : "", #Strip Username Rule. Object Type: string
                "service_cert_cn" : "", #Subject DN of Service Certificate. Object Type: string
                "service_cert_expiry_date" : "", #Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z). Object Type: string
                "role_mapping_policy" : "", #Role Mapping Policy Name. Object Type: string
                "enf_policy" : "", #Enforcement Policy Name. Object Type: string
                "use_cached_policy_results" : False, #Enable to use cached Roles and Posture attributes from previous sessions. Object Type: boolean
                "authz_sources" : False, #List of Additional authorization sources from which to fetch role-mapping attributes. Object Type: array
                "posture_enabled" : False, #Enable Posture Compliance. Object Type: boolean
                "posture_policies" : False, #List of Posture Policy Names. Object Type: array
                "default_posture_token" : "", #Default Posture Token. Object Type: string
                "remediate_end_hosts" : False, #Enable auto-remediation of non-compliant end-hosts. Object Type: boolean
                "remediation_url" : "", #Remediation URL. Object Type: string
                "audit_enabled" : False, #Enable Audit End-hosts. Object Type: boolean
                "audit_server" : "", #Audit Server Name. Object Type: string
                "audit_trigger_condition" : "", #Audit Trigger Conditions. Object Type: string
                "audit_mac_auth_client_type" : "", #Client Type For MAC authentication request Audit Trigger Condition. Object Type: string
                "action_after_audit" : "", #Action after audit. Object Type: string
                "audit_coa_acton" : "", #RADIUS CoA Action to be triggered after audit. Object Type: string
                "profiler_enabled" : False, #Enable Profile Endpoints. Object Type: boolean
                "profiler_endpoint_classification" : False, #List of Endpoint classification(s) after which an action must be triggered. Object Type: array
                "profiler_coa_action" : "", #RADIUS CoA Action to be triggered by Profiler . Object Type: string
                "acct_proxy_enabled" : False, #Enable Accounting Proxy Targets. Object Type: boolean
                "acct_proxy_targets" : False, #List Accounting Proxy Target names. Object Type: array
                "acct_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be deleted for Accounting proxy. Object Type: array
                "acct_proxy_attrs_to_add" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "value":"", #Value. Object Type: string
        }], #RADIUS attributes to be added for Accounting proxy. Object Type: array
                "radius_proxy_scheme" : "", #Proxying Scheme for RADIUS Proxy Service Type. Object Type: string
                "radius_proxy_targets" : "", #List of Proxy Targets for RADIUS Proxy Service Type. Object Type: array
                "radius_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be removed from remote server (proxy target) reply. Object Type: array
                "radius_proxy_enable_for_acct" : False, #Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) . Object Type: boolean
                }
        """
        url_path = "/config/service/name/{services_name}"
        dict_path = {"services_name": services_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_config_service_name_by_services_name(self, services_name="", body=({})):
        """
                Operation: Replace a Service by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: services_name, Description: Name of the Service
                Required Body Parameters:['name', 'template', 'enf_policy']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of the Service. Object Type: string
                "template" : "", #Template of the Service. Object Type: string
                "enabled" : False, #Is Service enabled?. Object Type: boolean
                "order_no" : 0, #Order number of the Service. Object Type: integer
                "description" : "", #Description of the Service. Object Type: string
                "monitor_mode" : False, #Enable to monitor network access without enforcement. Object Type: boolean
                "rules_match_type" : "", #Matches ANY/ALL of the rule conditions. Object Type: string
                "rules_conditions" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of service rules conditions. Object Type: array
                "auth_methods" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Method Names. Object Type: array
                "auth_sources" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "operator":"", #Operator. Object Type: string
             "value":"", #Value. Object Type: string
        }], #List of Authentication Source Names. Object Type: array
                "strip_username" : False, #Enable to specify a comma-separated list of rules to strip username prefixes or suffixes. Object Type: boolean
                "strip_username_csv" : "", #Strip Username Rule. Object Type: string
                "service_cert_cn" : "", #Subject DN of Service Certificate. Object Type: string
                "service_cert_expiry_date" : "", #Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z). Object Type: string
                "role_mapping_policy" : "", #Role Mapping Policy Name. Object Type: string
                "enf_policy" : "", #Enforcement Policy Name. Object Type: string
                "use_cached_policy_results" : False, #Enable to use cached Roles and Posture attributes from previous sessions. Object Type: boolean
                "authz_sources" : False, #List of Additional authorization sources from which to fetch role-mapping attributes. Object Type: array
                "posture_enabled" : False, #Enable Posture Compliance. Object Type: boolean
                "posture_policies" : False, #List of Posture Policy Names. Object Type: array
                "default_posture_token" : "", #Default Posture Token. Object Type: string
                "remediate_end_hosts" : False, #Enable auto-remediation of non-compliant end-hosts. Object Type: boolean
                "remediation_url" : "", #Remediation URL. Object Type: string
                "audit_enabled" : False, #Enable Audit End-hosts. Object Type: boolean
                "audit_server" : "", #Audit Server Name. Object Type: string
                "audit_trigger_condition" : "", #Audit Trigger Conditions. Object Type: string
                "audit_mac_auth_client_type" : "", #Client Type For MAC authentication request Audit Trigger Condition. Object Type: string
                "action_after_audit" : "", #Action after audit. Object Type: string
                "audit_coa_acton" : "", #RADIUS CoA Action to be triggered after audit. Object Type: string
                "profiler_enabled" : False, #Enable Profile Endpoints. Object Type: boolean
                "profiler_endpoint_classification" : False, #List of Endpoint classification(s) after which an action must be triggered. Object Type: array
                "profiler_coa_action" : "", #RADIUS CoA Action to be triggered by Profiler . Object Type: string
                "acct_proxy_enabled" : False, #Enable Accounting Proxy Targets. Object Type: boolean
                "acct_proxy_targets" : False, #List Accounting Proxy Target names. Object Type: array
                "acct_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be deleted for Accounting proxy. Object Type: array
                "acct_proxy_attrs_to_add" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
             "value":"", #Value. Object Type: string
        }], #RADIUS attributes to be added for Accounting proxy. Object Type: array
                "radius_proxy_scheme" : "", #Proxying Scheme for RADIUS Proxy Service Type. Object Type: string
                "radius_proxy_targets" : "", #List of Proxy Targets for RADIUS Proxy Service Type. Object Type: array
                "radius_proxy_attrs_to_delete" : [{
             "type":"", #Type. Object Type: string
             "name":"", #Name. Object Type: string
        }], #RADIUS attributes to be removed from remote server (proxy target) reply. Object Type: array
                "radius_proxy_enable_for_acct" : False, #Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) . Object Type: boolean
                }
        """
        url_path = "/config/service/name/{services_name}"
        dict_path = {"services_name": services_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_config_service_name_by_services_name(self, services_name=""):
        """
        Operation: Delete a Service by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: services_name, Description: Name of the Service
        """
        url_path = "/config/service/name/{services_name}"
        dict_path = {"services_name": services_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_config_service_by_services_id_enable(self, services_id=""):
        """
        Operation: Enable a Service
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: services_id, Description: Numeric ID of the service
        """
        url_path = "/config/service/{services_id}/enable"
        dict_path = {"services_id": services_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_config_service_name_by_services_name_enable(self, services_name=""):
        """
        Operation: Enable a Service by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: services_name, Description: Name of the Service
        """
        url_path = "/config/service/name/{services_name}/enable"
        dict_path = {"services_name": services_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_config_service_by_services_id_disable(self, services_id=""):
        """
        Operation: Disable a Service
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: services_id, Description: Numeric ID of the service
        """
        url_path = "/config/service/{services_id}/disable"
        dict_path = {"services_id": services_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_config_service_name_by_services_name_disable(self, services_name=""):
        """
        Operation: Disable a Service by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: services_name, Description: Name of the Service
        """
        url_path = "/config/service/name/{services_name}/disable"
        dict_path = {"services_name": services_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_config_service_reorder(self, body=({})):
        """
                Operation: Reorder Services
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['service_orders']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "service_orders" : [{
             "service_name":"", #Name of the Service. Object Type: string
             "order_no":0, #Order number of the Service. Object Type: integer
        }], #List of Service Orders to be updated. Object Type: array
                }
        """
        url_path = "/config/service/reorder"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Manage TACACS+ Service Dictionaries
    def get_tacacs_service_dictionary(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of TACACS+ Service Dictionaries
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/tacacs-service-dictionary"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_tacacs_service_dictionary(self, body=({})):
        """
                Operation: Create a new TACACS+ Service Dictionary
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['name', 'display_name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of TACACS+ Service Dictionary. Object Type: string
                "display_name" : "", #Display Name of TACACS+ Service Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #TACACS+ Service Dictionary Attribute Name. Object Type: string
             "attr_display_name":"", #TACACS+ Service Dictionary Attribute Display Name. Object Type: string
             "attr_type":"", #TACACS+ Service Dictionary Attribute Data Type. Object Type: string
             "allowed_values":"", #Allowed Values for TACACS+ Service Dictionary Attributes in CSV format. Object Type: string
        }], #List of TACACS+ Service Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/tacacs-service-dictionary"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_tacacs_service_dictionary_by_tacacs_service_dictionary_id(
        self, tacacs_service_dictionary_id=""
    ):
        """
        Operation: Get a TACACS+ Service Dictionary
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
        """
        url_path = "/tacacs-service-dictionary/{tacacs_service_dictionary_id}"
        dict_path = {"tacacs_service_dictionary_id": tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_tacacs_service_dictionary_by_tacacs_service_dictionary_id(
        self, tacacs_service_dictionary_id="", body=({})
    ):
        """
                Operation: Update a TACACS+ Service Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of TACACS+ Service Dictionary. Object Type: string
                "display_name" : "", #Display Name of TACACS+ Service Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #TACACS+ Service Dictionary Attribute Name. Object Type: string
             "attr_display_name":"", #TACACS+ Service Dictionary Attribute Display Name. Object Type: string
             "attr_type":"", #TACACS+ Service Dictionary Attribute Data Type. Object Type: string
             "allowed_values":"", #Allowed Values for TACACS+ Service Dictionary Attributes in CSV format. Object Type: string
        }], #List of TACACS+ Service Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/tacacs-service-dictionary/{tacacs_service_dictionary_id}"
        dict_path = {"tacacs_service_dictionary_id": tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_tacacs_service_dictionary_by_tacacs_service_dictionary_id(
        self, tacacs_service_dictionary_id="", body=({})
    ):
        """
                Operation: Replace a TACACS+ Service Dictionary
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
                Required Body Parameters:['name', 'display_name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of TACACS+ Service Dictionary. Object Type: string
                "display_name" : "", #Display Name of TACACS+ Service Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #TACACS+ Service Dictionary Attribute Name. Object Type: string
             "attr_display_name":"", #TACACS+ Service Dictionary Attribute Display Name. Object Type: string
             "attr_type":"", #TACACS+ Service Dictionary Attribute Data Type. Object Type: string
             "allowed_values":"", #Allowed Values for TACACS+ Service Dictionary Attributes in CSV format. Object Type: string
        }], #List of TACACS+ Service Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/tacacs-service-dictionary/{tacacs_service_dictionary_id}"
        dict_path = {"tacacs_service_dictionary_id": tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_tacacs_service_dictionary_by_tacacs_service_dictionary_id(
        self, tacacs_service_dictionary_id=""
    ):
        """
        Operation: Delete a TACACS+ Service Dictionary
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
        """
        url_path = "/tacacs-service-dictionary/{tacacs_service_dictionary_id}"
        dict_path = {"tacacs_service_dictionary_id": tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_tacacs_service_dictionary_name_by_name(self, name=""):
        """
        Operation: Get a TACACS+ Service Dictionary by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the TACACS+ Service Dictionary
        """
        url_path = "/tacacs-service-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_tacacs_service_dictionary_name_by_name(self, name="", body=({})):
        """
                Operation: Update a TACACS+ Service Dictionary by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of the TACACS+ Service Dictionary
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of TACACS+ Service Dictionary. Object Type: string
                "display_name" : "", #Display Name of TACACS+ Service Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #TACACS+ Service Dictionary Attribute Name. Object Type: string
             "attr_display_name":"", #TACACS+ Service Dictionary Attribute Display Name. Object Type: string
             "attr_type":"", #TACACS+ Service Dictionary Attribute Data Type. Object Type: string
             "allowed_values":"", #Allowed Values for TACACS+ Service Dictionary Attributes in CSV format. Object Type: string
        }], #List of TACACS+ Service Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/tacacs-service-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_tacacs_service_dictionary_name_by_name(self, name="", body=({})):
        """
                Operation: Replace a TACACS+ Service Dictionary by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: Unique name of the TACACS+ Service Dictionary
                Required Body Parameters:['name', 'display_name', 'attributes']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "name" : "", #Name of TACACS+ Service Dictionary. Object Type: string
                "display_name" : "", #Display Name of TACACS+ Service Dictionary. Object Type: string
                "attributes" : [{
             "attr_name":"", #TACACS+ Service Dictionary Attribute Name. Object Type: string
             "attr_display_name":"", #TACACS+ Service Dictionary Attribute Display Name. Object Type: string
             "attr_type":"", #TACACS+ Service Dictionary Attribute Data Type. Object Type: string
             "allowed_values":"", #Allowed Values for TACACS+ Service Dictionary Attributes in CSV format. Object Type: string
        }], #List of TACACS+ Service Dictionary Attributes. Object Type: array
                }
        """
        url_path = "/tacacs-service-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_tacacs_service_dictionary_name_by_name(self, name=""):
        """
        Operation: Delete a TACACS+ Service Dictionary by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the TACACS+ Service Dictionary
        """
        url_path = "/tacacs-service-dictionary/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
