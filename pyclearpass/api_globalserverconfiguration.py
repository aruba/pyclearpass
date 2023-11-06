from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: GlobalServerConfiguration
# FileName: api_globalserverconfiguration.py


class ApiGlobalServerConfiguration(ClearPassAPILogin):
    # API Service: Manage admin privileges
    def get_admin_privilege(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of admin privileges
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/admin-privilege"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_admin_privilege(self, body=({})):
        """
        Operation: Create a new admin privilege
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'cppm_privileges']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin privilege. Object Type: string
        "description" : "", #Description of the admin privilege. Object Type: string
        "access_type" : "", #Property to decide the access type of the user.. Object Type: string
        "cppm_privileges" : {}, #Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).. Object Type: object
        "insight_privileges" : {}, #Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).. Object Type: object
        "allow_passwords" : False, #If selected, all passwords may be displayed in the response. Object Type: boolean
        "allow_security_configs" : False, #If selected, Admin user will have access for security configuration. Object Type: boolean

        }
        """
        url_path = "/admin-privilege"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_admin_privilege_by_admin_privilege_id(self, admin_privilege_id=""):
        """
        Operation: Get an admin privilege
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: admin_privilege_id, Description: Numeric ID of the admin privilege
        """
        url_path = "/admin-privilege/{admin_privilege_id}"
        dict_path = {"admin_privilege_id": admin_privilege_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_privilege_by_admin_privilege_id(
        self, admin_privilege_id="", body=({})
    ):
        """
        Operation: Update some fields of an admin privilege
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: admin_privilege_id, Description: Numeric ID of the admin privilege
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin privilege. Object Type: string
        "description" : "", #Description of the admin privilege. Object Type: string
        "access_type" : "", #Property to decide the access type of the user.. Object Type: string
        "cppm_privileges" : {}, #Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).. Object Type: object
        "insight_privileges" : {}, #Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).. Object Type: object
        "allow_passwords" : False, #If selected, all passwords may be displayed in the response. Object Type: boolean
        "allow_security_configs" : False, #If selected, Admin user will have access for security configuration. Object Type: boolean

        }
        """
        url_path = "/admin-privilege/{admin_privilege_id}"
        dict_path = {"admin_privilege_id": admin_privilege_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_admin_privilege_by_admin_privilege_id(
        self, admin_privilege_id="", body=({})
    ):
        """
        Operation: Replace an admin privilege
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: admin_privilege_id, Description: Numeric ID of the admin privilege
        Required Body Parameters:['name', 'cppm_privileges']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin privilege. Object Type: string
        "description" : "", #Description of the admin privilege. Object Type: string
        "access_type" : "", #Property to decide the access type of the user.. Object Type: string
        "cppm_privileges" : {}, #Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).. Object Type: object
        "insight_privileges" : {}, #Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).. Object Type: object
        "allow_passwords" : False, #If selected, all passwords may be displayed in the response. Object Type: boolean
        "allow_security_configs" : False, #If selected, Admin user will have access for security configuration. Object Type: boolean

        }
        """
        url_path = "/admin-privilege/{admin_privilege_id}"
        dict_path = {"admin_privilege_id": admin_privilege_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_admin_privilege_by_admin_privilege_id(self, admin_privilege_id=""):
        """
        Operation: Delete an admin privilege
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: admin_privilege_id, Description: Numeric ID of the admin privilege
        """
        url_path = "/admin-privilege/{admin_privilege_id}"
        dict_path = {"admin_privilege_id": admin_privilege_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_admin_privilege_name_by_name(self, name=""):
        """
        Operation: Get an admin privilege by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the admin privilege
        """
        url_path = "/admin-privilege/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_privilege_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an admin privilege by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the admin privilege
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin privilege. Object Type: string
        "description" : "", #Description of the admin privilege. Object Type: string
        "access_type" : "", #Property to decide the access type of the user.. Object Type: string
        "cppm_privileges" : {}, #Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).. Object Type: object
        "insight_privileges" : {}, #Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).. Object Type: object
        "allow_passwords" : False, #If selected, all passwords may be displayed in the response. Object Type: boolean
        "allow_security_configs" : False, #If selected, Admin user will have access for security configuration. Object Type: boolean

        }
        """
        url_path = "/admin-privilege/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_admin_privilege_name_by_name(self, name="", body=({})):
        """
        Operation: Replace an admin privilege by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the admin privilege
        Required Body Parameters:['name', 'cppm_privileges']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin privilege. Object Type: string
        "description" : "", #Description of the admin privilege. Object Type: string
        "access_type" : "", #Property to decide the access type of the user.. Object Type: string
        "cppm_privileges" : {}, #Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).. Object Type: object
        "insight_privileges" : {}, #Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).. Object Type: object
        "allow_passwords" : False, #If selected, all passwords may be displayed in the response. Object Type: boolean
        "allow_security_configs" : False, #If selected, Admin user will have access for security configuration. Object Type: boolean

        }
        """
        url_path = "/admin-privilege/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_admin_privilege_name_by_name(self, name=""):
        """
        Operation: Delete an admin privilege by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the admin privilege
        """
        url_path = "/admin-privilege/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage admin users
    def get_admin_user(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of admin users
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/admin-user"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_admin_user(self, body=({})):
        """
        Operation: Create a new admin user
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'user_id', 'password', 'privilege_level']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin user. Object Type: string
        "user_id" : "", #Unique user id of the admin user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "password" : "", #Password of the admin user. Object Type: string
        "privilege_level" : "", #Name of the admin privilege. Object Type: string

        }
        """
        url_path = "/admin-user"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_admin_user_by_id(self, id=""):
        """
        Operation: Get an admin user
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric ID of the admin user
        """
        url_path = "/admin-user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_user_by_id(self, id="", body=({})):
        """
        Operation: Update some fields of an admin user
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the admin user
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin user. Object Type: string
        "user_id" : "", #Unique user id of the admin user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "password" : "", #Password of the admin user. Object Type: string
        "privilege_level" : "", #Name of the admin privilege. Object Type: string

        }
        """
        url_path = "/admin-user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_admin_user_by_id(self, id="", body=({})):
        """
        Operation: Replace an admin user
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the admin user
        Required Body Parameters:['name', 'user_id', 'password', 'privilege_level']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin user. Object Type: string
        "user_id" : "", #Unique user id of the admin user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "password" : "", #Password of the admin user. Object Type: string
        "privilege_level" : "", #Name of the admin privilege. Object Type: string

        }
        """
        url_path = "/admin-user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_admin_user_by_id(self, id=""):
        """
        Operation: Delete an admin user
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric ID of the admin user
        """
        url_path = "/admin-user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_admin_user_user_id_by_user_id(self, user_id=""):
        """
        Operation: Get an admin user by user_id
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: user_id, Description: Unique user_id of the admin user
        """
        url_path = "/admin-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_user_user_id_by_user_id(self, user_id="", body=({})):
        """
        Operation: Update some fields of an admin user by user_id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: user_id, Description: Unique user_id of the admin user
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin user. Object Type: string
        "user_id" : "", #Unique user id of the admin user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "password" : "", #Password of the admin user. Object Type: string
        "privilege_level" : "", #Name of the admin privilege. Object Type: string

        }
        """
        url_path = "/admin-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_admin_user_user_id_by_user_id(self, user_id="", body=({})):
        """
        Operation: Replace an admin user by user_id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: user_id, Description: Unique user_id of the admin user
        Required Body Parameters:['name', 'user_id', 'password', 'privilege_level']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the admin user. Object Type: string
        "user_id" : "", #Unique user id of the admin user. Object Type: string
        "enabled" : False, #Flag indicating if the account is enabled. Object Type: boolean
        "password" : "", #Password of the admin user. Object Type: string
        "privilege_level" : "", #Name of the admin privilege. Object Type: string

        }
        """
        url_path = "/admin-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_admin_user_user_id_by_user_id(self, user_id=""):
        """
        Operation: Delete an admin user by user_id
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: user_id, Description: Unique user_id of the admin user
        """
        url_path = "/admin-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage admin user password policies
    def get_admin_user_password_policy(self):
        """
        Operation: Get the admin user password policies
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/admin-user/password-policy"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_admin_user_password_policy(self, body=({})):
        """
        Operation: Put the admin user password policies
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['password_minimum_length', 'password_complexity']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "password_minimum_length" : 0, #Minimum length of the password. Object Type: integer
        "password_complexity" : "", #Complexity Level of the password. Object Type: string
        "password_disallowed_characters" : "", #Disallowed characters in the password. Object Type: string
        "password_disallowed_words" : "", #Disallowed words in the password. Object Type: string
        "password_prohibit_user_id" : False, #May not contain User ID or its characters in reversed order. Object Type: boolean
        "password_prohibit_repeated_chars" : False, #May not contain repeated character four or more times consecutively. Object Type: boolean
        "password_expiry_days" : 0, #Password expiry days. Object Type: integer
        "disable_after_failed_attempts" : 0, #Failed attempts count. Object Type: integer
        "password_remember_history" : 0, #Must be different from this many previous passwords. Object Type: integer
        "reset_failed_attempts_count" : False, #Reset failed attempts count and enable those users. Object Type: boolean

        }
        """
        url_path = "/admin-user/password-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_admin_user_password_policy(self, body=({})):
        """
        Operation: Patch the admin user password policies
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "password_minimum_length" : 0, #Minimum length of the password. Object Type: integer
        "password_complexity" : "", #Complexity Level of the password. Object Type: string
        "password_disallowed_characters" : "", #Disallowed characters in the password. Object Type: string
        "password_disallowed_words" : "", #Disallowed words in the password. Object Type: string
        "password_prohibit_user_id" : False, #May not contain User ID or its characters in reversed order. Object Type: boolean
        "password_prohibit_repeated_chars" : False, #May not contain repeated character four or more times consecutively. Object Type: boolean
        "password_expiry_days" : 0, #Password expiry days. Object Type: integer
        "disable_after_failed_attempts" : 0, #Failed attempts count. Object Type: integer
        "password_remember_history" : 0, #Must be different from this many previous passwords. Object Type: integer
        "reset_failed_attempts_count" : False, #Reset failed attempts count and enable those users. Object Type: boolean

        }
        """
        url_path = "/admin-user/password-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Manage application license
    def get_application_license(self):
        """
        Operation: Get a list of application licenses
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/application-license"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_application_license(self, body=({})):
        """
        Operation: Create a new application license
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['license_key']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "license_key" : "", #License key. Object Type: string

        }
        """
        url_path = "/application-license"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_application_license_by_license_id(self, license_id=""):
        """
        Operation: Get a license by license id
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_application_license_by_license_id(self, license_id="", body=({})):
        """
        Operation: Update a license by license id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: license_id, Description: Numeric ID of Application License
        Required Body Parameters:['license_key']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "license_key" : "", #License key. Object Type: string

        }
        """
        url_path = "/application-license/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_application_license_by_license_id(self, license_id=""):
        """
        Operation: Delete a license by license id
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_application_license_activate_online_by_license_id(self, license_id=""):
        """
        Operation: Activate license online by license id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/activate-online/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_application_license_activate_offline_by_license_id(self, license_id=""):
        """
        Operation: Activate license offline by license id
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/activate-offline/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def get_application_license_summary(self):
        """
        Operation: Get application license summary
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/application-license/summary"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage Attributes
    def get_attribute(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of attributes
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/attribute"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_attribute(self, body=({})):
        """
        Operation: Create a new attribute
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'entity_name', 'data_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the attribute. Object Type: string
        "entity_name" : "", #Entity Name of the attribute. Object Type: string
        "data_type" : "", #Data Type of the attribute. Object Type: string
        "mandatory" : False, #Enable this to make this attribute mandatory for the entity. Object Type: boolean
        "default_value" : "", #Default Value of the attribute. Object Type: string
        "allow_multiple" : False, #To Allow Multiple values of the attribute for Data Type String. Object Type: boolean
        "allowed_value" : "", #Allowed Value for Data Type List (e.g., example1,example2,example3). Object Type: string

        }
        """
        url_path = "/attribute"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_attribute_by_attribute_id(self, attribute_id=""):
        """
        Operation: Get an attribute
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: attribute_id, Description: Numeric ID of the attribute
        """
        url_path = "/attribute/{attribute_id}"
        dict_path = {"attribute_id": attribute_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_attribute_by_attribute_id(self, attribute_id="", body=({})):
        """
        Operation: Update some fields of an attribute
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: attribute_id, Description: Numeric ID of the attribute
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the attribute. Object Type: string
        "entity_name" : "", #Entity Name of the attribute. Object Type: string
        "data_type" : "", #Data Type of the attribute. Object Type: string
        "mandatory" : False, #Enable this to make this attribute mandatory for the entity. Object Type: boolean
        "default_value" : "", #Default Value of the attribute. Object Type: string
        "allow_multiple" : False, #To Allow Multiple values of the attribute for Data Type String. Object Type: boolean
        "allowed_value" : "", #Allowed Value for Data Type List (e.g., example1,example2,example3). Object Type: string

        }
        """
        url_path = "/attribute/{attribute_id}"
        dict_path = {"attribute_id": attribute_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_attribute_by_attribute_id(self, attribute_id="", body=({})):
        """
        Operation: Replace an attribute
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: attribute_id, Description: Numeric ID of the attribute
        Required Body Parameters:['name', 'entity_name', 'data_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the attribute. Object Type: string
        "entity_name" : "", #Entity Name of the attribute. Object Type: string
        "data_type" : "", #Data Type of the attribute. Object Type: string
        "mandatory" : False, #Enable this to make this attribute mandatory for the entity. Object Type: boolean
        "default_value" : "", #Default Value of the attribute. Object Type: string
        "allow_multiple" : False, #To Allow Multiple values of the attribute for Data Type String. Object Type: boolean
        "allowed_value" : "", #Allowed Value for Data Type List (e.g., example1,example2,example3). Object Type: string

        }
        """
        url_path = "/attribute/{attribute_id}"
        dict_path = {"attribute_id": attribute_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_attribute_by_attribute_id(self, attribute_id=""):
        """
        Operation: Delete an attribute
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: attribute_id, Description: Numeric ID of the attribute
        """
        url_path = "/attribute/{attribute_id}"
        dict_path = {"attribute_id": attribute_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_attribute_by_entity_name_name_name(self, entity_name="", name=""):
        """
        Operation: Get an attribute by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: entity_name, Description: Entity Name of the attribute
        Parameter Type: path, Name: name, Description: Unique name of the attribute
        """
        url_path = "/attribute/{entity_name}/name/{name}"
        dict_path = {"entity_name": entity_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_attribute_by_entity_name_name_name(
        self, entity_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of an attribute by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: entity_name, Description: Entity Name of the attribute
        Parameter Type: path, Name: name, Description: Unique name of the attribute
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the attribute. Object Type: string
        "entity_name" : "", #Entity Name of the attribute. Object Type: string
        "data_type" : "", #Data Type of the attribute. Object Type: string
        "mandatory" : False, #Enable this to make this attribute mandatory for the entity. Object Type: boolean
        "default_value" : "", #Default Value of the attribute. Object Type: string
        "allow_multiple" : False, #To Allow Multiple values of the attribute for Data Type String. Object Type: boolean
        "allowed_value" : "", #Allowed Value for Data Type List (e.g., example1,example2,example3). Object Type: string

        }
        """
        url_path = "/attribute/{entity_name}/name/{name}"
        dict_path = {"entity_name": entity_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_attribute_by_entity_name_name_name(
        self, entity_name="", name="", body=({})
    ):
        """
        Operation: Replace an attribute by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: entity_name, Description: Entity Name of the attribute
        Parameter Type: path, Name: name, Description: Unique name of the attribute
        Required Body Parameters:['name', 'entity_name', 'data_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the attribute. Object Type: string
        "entity_name" : "", #Entity Name of the attribute. Object Type: string
        "data_type" : "", #Data Type of the attribute. Object Type: string
        "mandatory" : False, #Enable this to make this attribute mandatory for the entity. Object Type: boolean
        "default_value" : "", #Default Value of the attribute. Object Type: string
        "allow_multiple" : False, #To Allow Multiple values of the attribute for Data Type String. Object Type: boolean
        "allowed_value" : "", #Allowed Value for Data Type List (e.g., example1,example2,example3). Object Type: string

        }
        """
        url_path = "/attribute/{entity_name}/name/{name}"
        dict_path = {"entity_name": entity_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_attribute_by_entity_name_name_name(self, entity_name="", name=""):
        """
        Operation: Delete an attribute by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: entity_name, Description: Entity Name of the attribute
        Parameter Type: path, Name: name, Description: Unique name of the attribute
        """
        url_path = "/attribute/{entity_name}/name/{name}"
        dict_path = {"entity_name": entity_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage ClearPass portal
    def get_clearpass_portal(self):
        """
        Operation: Get ClearPass Portal
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/clearpass-portal"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_clearpass_portal(self, body=({})):
        """
        Operation: Change ClearPass Portal
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "title" : "", #Default Landing page Title. Object Type: string
        "header" : "", #Default Landing page Header. Object Type: string
        "footer" : "", #Default Landing page Footer. Object Type: string
        "copyright" : "", #Default Landing page Copyright text. Object Type: string
        "app_name" : "", #If specified, User will be redirected to the selected ClearPass application login page. Object Type: string
        "guest_portal" : "", #If specified, User will be redirected to the selected Guest Web Login/Self-Registration Portal. Object Type: string
        "url" : "", #Redirect URL constructed based on the Guest Portal name(guest_portal) or Application Login Page(app_name). Object Type: string

        }
        """
        url_path = "/clearpass-portal"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Ensure a subscriber node is synchronized with the publisher node
    def new_cluster_db_sync(self, body=({})):
        """
        Operation: Synchronize subscriber with the publisher
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Unprocessable Entity, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "timeout" : "", #Maximum time in seconds to wait for the database sync operation. Object Type: string

        }
        """
        url_path = "/cluster/db-sync"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage cluster wide parameters
    def get_cluster_parameters(self):
        """
        Operation: Get cluster wide parameters
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/cluster/parameters"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_cluster_parameters(self, body=({})):
        """
        Operation: Replace cluster wide parameters
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "AdminSessionIdleTimeout" : 0, #Admin Session Idle Timeout in minutes. Object Type: integer
        "AdminUserLoginRemoteTacacsServerIP" : "", #Remote TACACS+ server for Admin logins. Object Type: string
        "AdminUserLoginRemoteTacacsServerPort" : 0, #Admin UI Login Remote TACACS+ Server Port. Object Type: integer
        "AdminUserLoginRemoteTacacsServerSecret" : "", #Remote TACACS+ server shared secret. Object Type: string
        "AdminUserLoginSecondaryRemoteTacacsServerIP" : "", #No Desc. Object Type: string
        "AdminUserLoginSecondaryRemoteTacacsServerPort" : 0, #No Desc. Object Type: integer
        "AdminUserLoginSecondaryRemoteTacacsServerSecret" : "", #No Desc. Object Type: string
        "AdminUserLoginTacacsClientIpSetByHeaderXFF" : "", #Enable Admin UI TACACS+ Client IP set by X-Forwarded-For (XFF) header. Object Type: string
        "AdminUserLoginTertiaryRemoteTacacsServerIP" : "", #No Desc. Object Type: string
        "AdminUserLoginTertiaryRemoteTacacsServerPort" : 0, #No Desc. Object Type: integer
        "AdminUserLoginTertiaryRemoteTacacsServerSecret" : "", #No Desc. Object Type: string
        "AlertNotificationTimeout" : "", #Alert Notification Timeout in hours. Object Type: string
        "AuditRecordsCleanupInterval" : 0, #Old Audit Records cleanup interval in days. Object Type: integer
        "AutoBackupConfigOptions" : "", #Auto backup configuration options. Object Type: string
        "CLISessionIdleTimeout" : 0, #CLI Session Idle Timeout in minutes. Object Type: integer
        "CSRCleanupInterval" : 0, #Cleanup interval for CSRs and private keys. Object Type: integer
        "ClearPassZoneCache" : "", #ClearPass Zone Cache Durability. Object Type: string
        "ClusterCommunicationMode" : "", #Mode of communication between cluster nodes. Object Type: string
        "CommonCriteriaMode" : "", #Enable Common Criteria mode for the cluster. Object Type: string
        "ConsoleSessionIdleTimeout" : 0, #Console Session Idle Timeout in minutes. Object Type: integer
        "ContentSecurityPolicy" : "", #Enable Content Security Policy (CSP). Object Type: string
        "ContextServerPollInterval" : 0, #Endpoint Context Servers polling interval in minutes. Object Type: integer
        "ContextServerPollStartTime" : "", #[00:00:00-23:59:59] Endpoint Context Servers polling start time. Object Type: string
        "DbAppexternalUserPassword" : "", #Database user "appexternal" password. Object Type: string
        "DesignatedStandbyPublisher" : "", #Designated Standby Publisher. Object Type: string
        "DisableTLS1.0" : "", #Disable TLSv1.0 support. Object Type: string
        "DisableTLS1.1" : "", #Disable TLSv1.1 support. Object Type: string
        "DisableTLS1.3" : "", #No Desc. Object Type: string
        "EnableNTLMV1ForWmi" : "", #Enable NTLMV1 for WMI scans. Object Type: string
        "EnablePublisherFailover" : "", #Enable Publisher Failover. Object Type: string
        "EnableTelemetry" : "", #Enable sharing information about the cluster to Telemetry server. Object Type: string
        "EnableUserAcknowledgement" : "", #Force Enable User Acknowledgement. Object Type: string
        "ExpiredGuestAccountsCleanupInterval" : 0, #Expired guest accounts cleanup interval in days. Object Type: integer
        "ExtensionsAutoUpgradesFlag" : "", #No Desc. Object Type: string
        "FreeDiskSpaceThreshold" : 0, #Free disk space threshold value in %. Object Type: integer
        "FreeMemoryThreshold" : 0, #Free memory threshold value in %. Object Type: integer
        "ICMPv6Filters" : "", #Enable ICMPv6 Filters. Object Type: string
        "IgnoreConflictNetworkBootAgents" : "", #Enable Ignore Conflict (Network Boot Agents). Object Type: string
        "InformationStoredCleanupInterval" : 0, #Cleanup interval for information stored on the disk in days. Object Type: integer
        "KnownEndpointsCleanupInterval" : 0, #Known endpoints cleanup interval in days. Object Type: integer
        "LoginBannerText" : "", #Login Banner Text. Object Type: string
        "NetflowReprofileInterval" : 0, #Netflow reprofile interval in days. Object Type: integer
        "NotificationEmailAddress" : "", #Alert Notification - Email Address. Object Type: string
        "NotificationSmsAddress" : "", #Alert Notification - SMS Address. Object Type: string
        "OnGuardAutoUpdatesFlag" : "", #Automatically check for available OnGuard Signature Updates. Object Type: string
        "PasswordPrompt" : "", #TACACS+ Password Prompt Text. Object Type: string
        "PolicyResultCacheTimeout" : 0, #Policy result cache timeout in minutes. Object Type: integer
        "PostAuthUnsubscribeEndpoints" : "", #No Desc. Object Type: string
        "PostAuthV2" : "", #Enable Post-Auth v2. Object Type: string
        "PostAuthV2HttpEnforcement" : "", #Enable Post-Auth v2 HTTP enforcement. Object Type: string
        "ProcessWiredFromIfMap" : "", #Process wired device information from IF-MAP interface. Object Type: string
        "ProfiledKnownEndpointsCleanupOption" : "", #Profiled Known endpoints cleanup option in days. Object Type: string
        "ProfiledUnknownEndpointsCleanupInterval" : 0, #Profiled Unknown endpoints cleanup interval in days. Object Type: integer
        "ProfilerConflictStrictMode" : "", #Conflict Detection Strict Mode. Object Type: string
        "ProfilerNmapEnable" : "", #Enable endpoint port scan using Nmap. Object Type: string
        "ProfilerPostureEnable" : "", #Enable Endpoint scan using WMI. Object Type: string
        "ProfilerScanPorts" : "", #Profiler Scan TCP Ports. Object Type: string
        "ProfilerSubnetScanInterval" : 0, #Profiler subnet scan interval in hours. Object Type: integer
        "ProfilingAutoUpdatesFlag" : "", #Automatically check for available Profiling Updates. Object Type: string
        "SSHCipherMode" : "", #Allowed SSH Cipher Modes. Object Type: string
        "SessionLogsCleanupInterval" : 0, #Cleanup interval for Session log details in the database in days. Object Type: integer
        "SoftwareAutoUpdatesFlag" : "", #Automatically check for available Software Updates. Object Type: string
        "StaleTLSsessioninDiskclenaup" : 0, #No Desc. Object Type: integer
        "StandbyFailoverWaitTime" : 0, #Failover Wait Time in minutes. Object Type: integer
        "StaticIPEndpointsCleanupOption" : "", #Static IP endpoints cleanup option. Object Type: string
        "StorePasswordHash" : "", #Store Password Hash for MSCHAP authentication. Object Type: string
        "StoreReversibleLocalUserPasswords" : "", #Store Local User passwords using reversible encryption. Object Type: string
        "SyslogBatchInterval" : 0, #Syslog Export Interval in seconds. Object Type: integer
        "SystemAlertLevel" : "", #System Alert Level. Object Type: string
        "TacacsAllowUnencryptedCommunication" : "", #Enable TACACS+ clients to communicate with ClearPass server over an unencrypted channel. Object Type: string
        "TacacsDisableChangePassword" : "", #Disable Change Password for TACACS+. Object Type: string
        "TacacsIdleTimeout" : 0, #TACACS+ Connection Idle Timeout in seconds. Object Type: integer
        "TacacsProcessUnauthenticatedRequest" : "", #Enable unauthenticated TACACS+ user request processing. Object Type: string
        "UnknownEndpointsCleanupInterval" : 0, #Unknown endpoints cleanup interval in days. Object Type: integer
        "UserPrompt" : "", #TACACS+ User Prompt Text. Object Type: string
        "allowConcurrentLogin" : "", #Enable Concurrent Admin Login. Object Type: string
        "session_cache_type" : "", #No Desc. Object Type: string

        }
        """
        url_path = "/cluster/parameters"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_cluster_parameters(self, body=({})):
        """
        Operation: Update some cluster wide parameters
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "AdminSessionIdleTimeout" : 0, #Admin Session Idle Timeout in minutes. Object Type: integer
        "AdminUserLoginRemoteTacacsServerIP" : "", #Remote TACACS+ server for Admin logins. Object Type: string
        "AdminUserLoginRemoteTacacsServerPort" : 0, #Admin UI Login Remote TACACS+ Server Port. Object Type: integer
        "AdminUserLoginRemoteTacacsServerSecret" : "", #Remote TACACS+ server shared secret. Object Type: string
        "AdminUserLoginSecondaryRemoteTacacsServerIP" : "", #No Desc. Object Type: string
        "AdminUserLoginSecondaryRemoteTacacsServerPort" : 0, #No Desc. Object Type: integer
        "AdminUserLoginSecondaryRemoteTacacsServerSecret" : "", #No Desc. Object Type: string
        "AdminUserLoginTacacsClientIpSetByHeaderXFF" : "", #Enable Admin UI TACACS+ Client IP set by X-Forwarded-For (XFF) header. Object Type: string
        "AdminUserLoginTertiaryRemoteTacacsServerIP" : "", #No Desc. Object Type: string
        "AdminUserLoginTertiaryRemoteTacacsServerPort" : 0, #No Desc. Object Type: integer
        "AdminUserLoginTertiaryRemoteTacacsServerSecret" : "", #No Desc. Object Type: string
        "AlertNotificationTimeout" : "", #Alert Notification Timeout in hours. Object Type: string
        "AuditRecordsCleanupInterval" : 0, #Old Audit Records cleanup interval in days. Object Type: integer
        "AutoBackupConfigOptions" : "", #Auto backup configuration options. Object Type: string
        "CLISessionIdleTimeout" : 0, #CLI Session Idle Timeout in minutes. Object Type: integer
        "CSRCleanupInterval" : 0, #Cleanup interval for CSRs and private keys. Object Type: integer
        "ClearPassZoneCache" : "", #ClearPass Zone Cache Durability. Object Type: string
        "ClusterCommunicationMode" : "", #Mode of communication between cluster nodes. Object Type: string
        "CommonCriteriaMode" : "", #Enable Common Criteria mode for the cluster. Object Type: string
        "ConsoleSessionIdleTimeout" : 0, #Console Session Idle Timeout in minutes. Object Type: integer
        "ContentSecurityPolicy" : "", #Enable Content Security Policy (CSP). Object Type: string
        "ContextServerPollInterval" : 0, #Endpoint Context Servers polling interval in minutes. Object Type: integer
        "ContextServerPollStartTime" : "", #[00:00:00-23:59:59] Endpoint Context Servers polling start time. Object Type: string
        "DbAppexternalUserPassword" : "", #Database user "appexternal" password. Object Type: string
        "DesignatedStandbyPublisher" : "", #Designated Standby Publisher. Object Type: string
        "DisableTLS1.0" : "", #Disable TLSv1.0 support. Object Type: string
        "DisableTLS1.1" : "", #Disable TLSv1.1 support. Object Type: string
        "DisableTLS1.3" : "", #No Desc. Object Type: string
        "EnableNTLMV1ForWmi" : "", #Enable NTLMV1 for WMI scans. Object Type: string
        "EnablePublisherFailover" : "", #Enable Publisher Failover. Object Type: string
        "EnableTelemetry" : "", #Enable sharing information about the cluster to Telemetry server. Object Type: string
        "EnableUserAcknowledgement" : "", #Force Enable User Acknowledgement. Object Type: string
        "ExpiredGuestAccountsCleanupInterval" : 0, #Expired guest accounts cleanup interval in days. Object Type: integer
        "ExtensionsAutoUpgradesFlag" : "", #No Desc. Object Type: string
        "FreeDiskSpaceThreshold" : 0, #Free disk space threshold value in %. Object Type: integer
        "FreeMemoryThreshold" : 0, #Free memory threshold value in %. Object Type: integer
        "ICMPv6Filters" : "", #Enable ICMPv6 Filters. Object Type: string
        "IgnoreConflictNetworkBootAgents" : "", #Enable Ignore Conflict (Network Boot Agents). Object Type: string
        "InformationStoredCleanupInterval" : 0, #Cleanup interval for information stored on the disk in days. Object Type: integer
        "KnownEndpointsCleanupInterval" : 0, #Known endpoints cleanup interval in days. Object Type: integer
        "LoginBannerText" : "", #Login Banner Text. Object Type: string
        "NetflowReprofileInterval" : 0, #Netflow reprofile interval in days. Object Type: integer
        "NotificationEmailAddress" : "", #Alert Notification - Email Address. Object Type: string
        "NotificationSmsAddress" : "", #Alert Notification - SMS Address. Object Type: string
        "OnGuardAutoUpdatesFlag" : "", #Automatically check for available OnGuard Signature Updates. Object Type: string
        "PasswordPrompt" : "", #TACACS+ Password Prompt Text. Object Type: string
        "PolicyResultCacheTimeout" : 0, #Policy result cache timeout in minutes. Object Type: integer
        "PostAuthUnsubscribeEndpoints" : "", #No Desc. Object Type: string
        "PostAuthV2" : "", #Enable Post-Auth v2. Object Type: string
        "PostAuthV2HttpEnforcement" : "", #Enable Post-Auth v2 HTTP enforcement. Object Type: string
        "ProcessWiredFromIfMap" : "", #Process wired device information from IF-MAP interface. Object Type: string
        "ProfiledKnownEndpointsCleanupOption" : "", #Profiled Known endpoints cleanup option in days. Object Type: string
        "ProfiledUnknownEndpointsCleanupInterval" : 0, #Profiled Unknown endpoints cleanup interval in days. Object Type: integer
        "ProfilerConflictStrictMode" : "", #Conflict Detection Strict Mode. Object Type: string
        "ProfilerNmapEnable" : "", #Enable endpoint port scan using Nmap. Object Type: string
        "ProfilerPostureEnable" : "", #Enable Endpoint scan using WMI. Object Type: string
        "ProfilerScanPorts" : "", #Profiler Scan TCP Ports. Object Type: string
        "ProfilerSubnetScanInterval" : 0, #Profiler subnet scan interval in hours. Object Type: integer
        "ProfilingAutoUpdatesFlag" : "", #Automatically check for available Profiling Updates. Object Type: string
        "SSHCipherMode" : "", #Allowed SSH Cipher Modes. Object Type: string
        "SessionLogsCleanupInterval" : 0, #Cleanup interval for Session log details in the database in days. Object Type: integer
        "SoftwareAutoUpdatesFlag" : "", #Automatically check for available Software Updates. Object Type: string
        "StaleTLSsessioninDiskclenaup" : 0, #No Desc. Object Type: integer
        "StandbyFailoverWaitTime" : 0, #Failover Wait Time in minutes. Object Type: integer
        "StaticIPEndpointsCleanupOption" : "", #Static IP endpoints cleanup option. Object Type: string
        "StorePasswordHash" : "", #Store Password Hash for MSCHAP authentication. Object Type: string
        "StoreReversibleLocalUserPasswords" : "", #Store Local User passwords using reversible encryption. Object Type: string
        "SyslogBatchInterval" : 0, #Syslog Export Interval in seconds. Object Type: integer
        "SystemAlertLevel" : "", #System Alert Level. Object Type: string
        "TacacsAllowUnencryptedCommunication" : "", #Enable TACACS+ clients to communicate with ClearPass server over an unencrypted channel. Object Type: string
        "TacacsDisableChangePassword" : "", #Disable Change Password for TACACS+. Object Type: string
        "TacacsIdleTimeout" : 0, #TACACS+ Connection Idle Timeout in seconds. Object Type: integer
        "TacacsProcessUnauthenticatedRequest" : "", #Enable unauthenticated TACACS+ user request processing. Object Type: string
        "UnknownEndpointsCleanupInterval" : 0, #Unknown endpoints cleanup interval in days. Object Type: integer
        "UserPrompt" : "", #TACACS+ User Prompt Text. Object Type: string
        "allowConcurrentLogin" : "", #Enable Concurrent Admin Login. Object Type: string
        "session_cache_type" : "", #No Desc. Object Type: string

        }
        """
        url_path = "/cluster/parameters"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Manage data filters
    def get_data_filter(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of data filters
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/data-filter"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_data_filter(self, body=({})):
        """
        Operation: Create a new data filter
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'type', 'configuration_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Data Filter. Object Type: string
        "description" : "", #Description of the Data Filter. Object Type: string
        "type" : "", #Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT. Object Type: string
        "attr_type" : "", #Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING. Object Type: string
        "configuration_type" : "", #Configuration type of the Data Filter. Object Type: string
        "template" : "", #Template name for Data Filter (applicable when type=INSIGHT). Object Type: string
        "custom_sql" : "", #Custom SQL of the Data Filter. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes. Object Type: string
        "rules" : "", #List of Rules for Data Filter, applicable only for attributes. Object Type: RulesSettingsCreate

        }
        """
        url_path = "/data-filter"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_data_filter_by_data_filter_id(self, data_filter_id=""):
        """
        Operation: Get a data filter
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: data_filter_id, Description: Numeric ID of the Data Filter
        """
        url_path = "/data-filter/{data_filter_id}"
        dict_path = {"data_filter_id": data_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_data_filter_by_data_filter_id(self, data_filter_id="", body=({})):
        """
        Operation: Update a data filter
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: data_filter_id, Description: Numeric ID of the Data Filter
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Data Filter. Object Type: string
        "description" : "", #Description of the Data Filter. Object Type: string
        "type" : "", #Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT. Object Type: string
        "attr_type" : "", #Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING. Object Type: string
        "configuration_type" : "", #Configuration type of the Data Filter. Object Type: string
        "template" : "", #Template name for Data Filter (applicable when type=INSIGHT). Object Type: string
        "custom_sql" : "", #Custom SQL of the Data Filter. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes. Object Type: string
        "rules" : "", #List of Rules for Data Filter, applicable only for attributes. Object Type: RulesSettingsUpdate

        }
        """
        url_path = "/data-filter/{data_filter_id}"
        dict_path = {"data_filter_id": data_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_data_filter_by_data_filter_id(self, data_filter_id="", body=({})):
        """
        Operation: Replace a data filter
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: data_filter_id, Description: Numeric ID of the Data Filter
        Required Body Parameters:['name', 'type', 'configuration_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Data Filter. Object Type: string
        "description" : "", #Description of the Data Filter. Object Type: string
        "type" : "", #Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT. Object Type: string
        "attr_type" : "", #Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING. Object Type: string
        "configuration_type" : "", #Configuration type of the Data Filter. Object Type: string
        "template" : "", #Template name for Data Filter (applicable when type=INSIGHT). Object Type: string
        "custom_sql" : "", #Custom SQL of the Data Filter. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes. Object Type: string
        "rules" : "", #List of Rules for Data Filter, applicable only for attributes. Object Type: RulesSettingsReplace

        }
        """
        url_path = "/data-filter/{data_filter_id}"
        dict_path = {"data_filter_id": data_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_data_filter_by_data_filter_id(self, data_filter_id=""):
        """
        Operation: Delete a data filter
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: data_filter_id, Description: Numeric ID of the Data Filter
        """
        url_path = "/data-filter/{data_filter_id}"
        dict_path = {"data_filter_id": data_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_data_filter_name_by_name(self, name=""):
        """
        Operation: Get a data filter by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the data filter
        """
        url_path = "/data-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_data_filter_name_by_name(self, name="", body=({})):
        """
        Operation: Update a data filter by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the data filter
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Data Filter. Object Type: string
        "description" : "", #Description of the Data Filter. Object Type: string
        "type" : "", #Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT. Object Type: string
        "attr_type" : "", #Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING. Object Type: string
        "configuration_type" : "", #Configuration type of the Data Filter. Object Type: string
        "template" : "", #Template name for Data Filter (applicable when type=INSIGHT). Object Type: string
        "custom_sql" : "", #Custom SQL of the Data Filter. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes. Object Type: string
        "rules" : "", #List of Rules for Data Filter, applicable only for attributes. Object Type: RulesSettingsUpdate

        }
        """
        url_path = "/data-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_data_filter_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a data filter by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the data filter
        Required Body Parameters:['name', 'type', 'configuration_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Data Filter. Object Type: string
        "description" : "", #Description of the Data Filter. Object Type: string
        "type" : "", #Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT. Object Type: string
        "attr_type" : "", #Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING. Object Type: string
        "configuration_type" : "", #Configuration type of the Data Filter. Object Type: string
        "template" : "", #Template name for Data Filter (applicable when type=INSIGHT). Object Type: string
        "custom_sql" : "", #Custom SQL of the Data Filter. Object Type: string
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes. Object Type: string
        "rules" : "", #List of Rules for Data Filter, applicable only for attributes. Object Type: RulesSettingsReplace

        }
        """
        url_path = "/data-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_data_filter_name_by_name(self, name=""):
        """
        Operation: Delete a data filter by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the data filter
        """
        url_path = "/data-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage file backup server
    def get_file_backup_server(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of file backup server
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/file-backup-server"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_file_backup_server(self, body=({})):
        """
        Operation: Create a new file backup server
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['host_address', 'protocol', 'port', 'username', 'password', 'time_out', 'remote_dir']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #Server host address of file backup server. Object Type: string
        "description" : "", #Description of file backup server. Object Type: string
        "protocol" : "", #Protocol for file backup server. Object Type: string
        "port" : 0, #Port for file backup server. Object Type: integer
        "username" : "", #Username of file backup server. Object Type: string
        "password" : "", #Password for file backup server. Object Type: string
        "time_out" : 0, #Timeout for file backup server . Object Type: integer
        "remote_dir" : "", #Remote directory for file backup server. Object Type: string
        "cppm_servers" : "", #ClearPass server UUID List for file backup server. Object Type: array

        }
        """
        url_path = "/file-backup-server"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_file_backup_server_by_file_backup_server_id(self, file_backup_server_id=""):
        """
        Operation: Get a file backup server
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
        """
        url_path = "/file-backup-server/{file_backup_server_id}"
        dict_path = {"file_backup_server_id": file_backup_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_file_backup_server_by_file_backup_server_id(
        self, file_backup_server_id="", body=({})
    ):
        """
        Operation: Update some fields of a file backup server
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #Server host address of file backup server. Object Type: string
        "description" : "", #Description of file backup server. Object Type: string
        "protocol" : "", #Protocol for file backup server. Object Type: string
        "port" : 0, #Port for file backup server. Object Type: integer
        "username" : "", #Username of file backup server. Object Type: string
        "password" : "", #Password for file backup server. Object Type: string
        "time_out" : 0, #Timeout for file backup server . Object Type: integer
        "remote_dir" : "", #Remote directory for file backup server. Object Type: string
        "cppm_servers" : "", #ClearPass server UUID List for file backup server. Object Type: array

        }
        """
        url_path = "/file-backup-server/{file_backup_server_id}"
        dict_path = {"file_backup_server_id": file_backup_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_file_backup_server_by_file_backup_server_id(
        self, file_backup_server_id="", body=({})
    ):
        """
        Operation: Replace a file backup server
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
        Required Body Parameters:['host_address', 'protocol', 'port', 'username', 'password', 'time_out', 'remote_dir']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #Server host address of file backup server. Object Type: string
        "description" : "", #Description of file backup server. Object Type: string
        "protocol" : "", #Protocol for file backup server. Object Type: string
        "port" : 0, #Port for file backup server. Object Type: integer
        "username" : "", #Username of file backup server. Object Type: string
        "password" : "", #Password for file backup server. Object Type: string
        "time_out" : 0, #Timeout for file backup server . Object Type: integer
        "remote_dir" : "", #Remote directory for file backup server. Object Type: string
        "cppm_servers" : "", #ClearPass server UUID List for file backup server. Object Type: array

        }
        """
        url_path = "/file-backup-server/{file_backup_server_id}"
        dict_path = {"file_backup_server_id": file_backup_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_file_backup_server_by_file_backup_server_id(
        self, file_backup_server_id=""
    ):
        """
        Operation: Delete a file backup server
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
        """
        url_path = "/file-backup-server/{file_backup_server_id}"
        dict_path = {"file_backup_server_id": file_backup_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_file_backup_server_host_address_by_host_address(self, host_address=""):
        """
        Operation: Get a file backup server by host_address
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: host_address, Description: Unique host_address of the file-backup-server
        """
        url_path = "/file-backup-server/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_file_backup_server_host_address_by_host_address(
        self, host_address="", body=({})
    ):
        """
        Operation: Update some fields of a file backup server by host_address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: host_address, Description: Unique host_address of the file-backup-server
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #Server host address of file backup server. Object Type: string
        "description" : "", #Description of file backup server. Object Type: string
        "protocol" : "", #Protocol for file backup server. Object Type: string
        "port" : 0, #Port for file backup server. Object Type: integer
        "username" : "", #Username of file backup server. Object Type: string
        "password" : "", #Password for file backup server. Object Type: string
        "time_out" : 0, #Timeout for file backup server . Object Type: integer
        "remote_dir" : "", #Remote directory for file backup server. Object Type: string
        "cppm_servers" : "", #ClearPass server UUID List for file backup server. Object Type: array

        }
        """
        url_path = "/file-backup-server/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_file_backup_server_host_address_by_host_address(
        self, host_address="", body=({})
    ):
        """
        Operation: Replace a file backup server by host_address
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: host_address, Description: Unique host_address of the file-backup-server
        Required Body Parameters:['host_address', 'protocol', 'port', 'username', 'password', 'time_out', 'remote_dir']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #Server host address of file backup server. Object Type: string
        "description" : "", #Description of file backup server. Object Type: string
        "protocol" : "", #Protocol for file backup server. Object Type: string
        "port" : 0, #Port for file backup server. Object Type: integer
        "username" : "", #Username of file backup server. Object Type: string
        "password" : "", #Password for file backup server. Object Type: string
        "time_out" : 0, #Timeout for file backup server . Object Type: integer
        "remote_dir" : "", #Remote directory for file backup server. Object Type: string
        "cppm_servers" : "", #ClearPass server UUID List for file backup server. Object Type: array

        }
        """
        url_path = "/file-backup-server/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_file_backup_server_host_address_by_host_address(self, host_address=""):
        """
        Operation: Delete a file backup server by host_address
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: host_address, Description: Unique host_address of the file-backup-server
        """
        url_path = "/file-backup-server/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Returns the list of system-defined privileges
    def get_oauth_all_privileges(self, format=""):
        """
        Operation: Returns the list of system-defined privileges
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: format, Description: <b>list:</b> List of all privileges by name<br/><b>tree:</b> List of all domains, each containing features
        """
        url_path = "/oauth/all-privileges"
        dict_query = {"format": format}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage local user password policies
    def get_local_user_password_policy(self):
        """
        Operation: Get the local user password policy
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/local-user/password-policy"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_local_user_password_policy(self, body=({})):
        """
        Operation: Put the local user password policy
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['password_minimum_length', 'password_complexity']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "password_minimum_length" : 0, #Minimum length of the password. Object Type: integer
        "password_complexity" : "", #Complexity Level of the password. Object Type: string
        "password_disallowed_characters" : "", #Disallowed characters in the password. Object Type: string
        "password_disallowed_words" : "", #Disallowed words in the password. Object Type: string
        "password_prohibit_user_id" : False, #May not contain User ID or its characters in reversed order. Object Type: boolean
        "password_prohibit_repeated_chars" : False, #May not contain repeated character four or more times consecutively. Object Type: boolean
        "password_expiry_days" : 0, #Password expiry days. Object Type: integer
        "password_remember_history" : 0, #Must be different from this many previous passwords. Object Type: integer
        "reminder_days" : 0, #Display reminder message after this many days. Object Type: integer
        "reminder_message" : "", #Reminder message to be displayed. Object Type: string
        "disable_after_days" : 0, #Disable after Days Exceed. Object Type: integer
        "disable_after_date" : "", #Disable after Date Exceeds. Object Type: string
        "disable_after_unchanged_days" : 0, #Disable after password not changed after this many days. Object Type: integer
        "disable_after_failed_attempts" : 0, #Failed attempts count. Object Type: integer
        "reset_failed_attempts_count" : False, #Reset failed attempts count and enable those users. Object Type: boolean

        }
        """
        url_path = "/local-user/password-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_local_user_password_policy(self, body=({})):
        """
        Operation: Patch the local user password policy
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "password_minimum_length" : 0, #Minimum length of the password. Object Type: integer
        "password_complexity" : "", #Complexity Level of the password. Object Type: string
        "password_disallowed_characters" : "", #Disallowed characters in the password. Object Type: string
        "password_disallowed_words" : "", #Disallowed words in the password. Object Type: string
        "password_prohibit_user_id" : False, #May not contain User ID or its characters in reversed order. Object Type: boolean
        "password_prohibit_repeated_chars" : False, #May not contain repeated character four or more times consecutively. Object Type: boolean
        "password_expiry_days" : 0, #Password expiry days. Object Type: integer
        "password_remember_history" : 0, #Must be different from this many previous passwords. Object Type: integer
        "reminder_days" : 0, #Display reminder message after this many days. Object Type: integer
        "reminder_message" : "", #Reminder message to be displayed. Object Type: string
        "disable_after_days" : 0, #Disable after Days Exceed. Object Type: integer
        "disable_after_date" : "", #Disable after Date Exceeds. Object Type: string
        "disable_after_unchanged_days" : 0, #Disable after password not changed after this many days. Object Type: integer
        "disable_after_failed_attempts" : 0, #Failed attempts count. Object Type: integer
        "reset_failed_attempts_count" : False, #Reset failed attempts count and enable those users. Object Type: boolean

        }
        """
        url_path = "/local-user/password-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Operations for MessagingSetup
    def get_messaging_setup(self):
        """
        Operation: GET Messaging setup
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/messaging-setup"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_messaging_setup(self, body=({})):
        """
        Operation: Configure Messaging setup
        HTTP Response Codes: 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['server_name', 'default_from_address']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "server_name" : "", #SMTP Server Name. Object Type: string
        "user_name" : "", #Username. Object Type: string
        "password" : "", #Password. Object Type: string
        "default_from_address" : "", #Default FROM Address. Object Type: string
        "connection_security" : "", #Connection Security. Object Type: string
        "port" : "", #Port Number. Object Type: int
        "connection_timeout" : "", #Connection Timeout . Object Type: int

        }
        """
        url_path = "/messaging-setup"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def delete_messaging_setup(self):
        """
        Operation: Reset Messaging setup configuration
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/messaging-setup"
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage operator profiles
    def get_operator_profile(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of operator profiles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/operator-profile"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_operator_profile(self, body=({})):
        """
        Operation: Create a new operator profile
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'sponsor_filter']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #Enter a name for this operator profile. Object Type: string
        "comment" : "", #Comments or descriptive text about the operator profile. Object Type: string
        "enabled" : False, #If unchecked, operators with this profile will not be able to log in. Object Type: boolean
        "privileges" : False, #Select the privileges that will be granted to this operator login. Object Type: array
        "user_dbs_list" : "", #Select the visitor account roles that these operators are permitted to use. Object Type: string
        "sponsor_filter" : "", #Select the default operator filtering to apply to guest accounts. Object Type: string
        "filter_useraccount" : "", #Enter a comma-delimited list of field=value pairs to create an account filter. Object Type: string
        "filter_radacct" : "", #Enter a comma-delimited list of field=value pairs to create a session filter. Object Type: string
        "max_users" : "", #Maximum number of guests the operator can create.Leave blank for no limit. Object Type: string
        "max_devices" : "", #Maximum number of devices the operator can create.Leave blank for no limit. Object Type: string
        "userskin" : "", #Choose the skin to use for operators with this profile. Object Type: string
        "userskin_name" : "", #No Desc. Object Type: string
        "start_page" : "", #The initial page to show this operator after logging in. Object Type: string
        "lang" : "", #Select the default language to use for operators with this profile. Object Type: string
        "timezone_id" : "", #Select the default time zone for operators with this profile. Object Type: string
        "override_ui" : False, #If checked, you can specify different default forms and views to use. Object Type: boolean
        "override_guest_sessions" : "", #Override the Active Sessions view. Object Type: string
        "override_change_expiration" : "", #Override the Change Expiration form. Object Type: string
        "override_create_multi_result" : "", #Override the Create Multiple Accounts Results form. Object Type: string
        "override_create_multi" : "", #Override the Create Multiple Guest Accounts form. Object Type: string
        "override_mac_create" : "", #Override the Create New Device form. Object Type: string
        "override_mac_create_receipt" : "", #Override the Create New Device Receipt form. Object Type: string
        "override_create_user" : "", #Override the Create New Guest Account form. Object Type: string
        "override_create_user_receipt" : "", #Override the Create New Guest Account Receipt form. Object Type: string
        "override_guest_edit" : "", #Override the Edit Account form. Object Type: string
        "override_guest_multi" : "", #Override the Edit Accounts view. Object Type: string
        "override_mac_edit" : "", #Override the Edit Device form. Object Type: string
        "override_mac_multi" : "", #Override the Edit Devices view. Object Type: string
        "override_guest_multi_form" : "", #Override the Edit Guest Accounts form. Object Type: string
        "override_mac_multi_form" : "", #Override the Edit Guest Devices form. Object Type: string
        "override_guest_multi_result" : "", #Override the Edit Multiple Accounts Results form. Object Type: string
        "override_mac_multi_result" : "", #Override the Edit Multiple Devices Results form. Object Type: string
        "override_mac_export" : "", #Override the Export Devices view. Object Type: string
        "override_guest_export" : "", #Override the Export Guest Accounts view. Object Type: string
        "override_mac_list" : "", #Override the Manage Devices view. Object Type: string
        "override_guest_users" : "", #Override the Manage Guest Accounts view. Object Type: string
        "override_guest_edit_receipt" : "", #Override the Updated Account Details form. Object Type: string
        "override_mac_edit_receipt" : "", #Override the Updated Device Details form. Object Type: string

        }
        """
        url_path = "/operator-profile"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_operator_profile_by_id(self, id=""):
        """
        Operation: Get an operator profile
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the operator profile
        """
        url_path = "/operator-profile/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_operator_profile_by_id(self, id="", body=({})):
        """
        Operation: Update an operator profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the operator profile
        Required Body Parameters:['name', 'sponsor_filter']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #Enter a name for this operator profile. Object Type: string
        "comment" : "", #Comments or descriptive text about the operator profile. Object Type: string
        "enabled" : False, #If unchecked, operators with this profile will not be able to log in. Object Type: boolean
        "privileges" : False, #Select the privileges that will be granted to this operator login. Object Type: array
        "user_dbs_list" : "", #Select the visitor account roles that these operators are permitted to use. Object Type: string
        "sponsor_filter" : "", #Select the default operator filtering to apply to guest accounts. Object Type: string
        "filter_useraccount" : "", #Enter a comma-delimited list of field=value pairs to create an account filter. Object Type: string
        "filter_radacct" : "", #Enter a comma-delimited list of field=value pairs to create a session filter. Object Type: string
        "max_users" : "", #Maximum number of guests the operator can create.Leave blank for no limit. Object Type: string
        "max_devices" : "", #Maximum number of devices the operator can create.Leave blank for no limit. Object Type: string
        "userskin" : "", #Choose the skin to use for operators with this profile. Object Type: string
        "userskin_name" : "", #No Desc. Object Type: string
        "start_page" : "", #The initial page to show this operator after logging in. Object Type: string
        "lang" : "", #Select the default language to use for operators with this profile. Object Type: string
        "timezone_id" : "", #Select the default time zone for operators with this profile. Object Type: string
        "override_ui" : False, #If checked, you can specify different default forms and views to use. Object Type: boolean
        "override_guest_sessions" : "", #Override the Active Sessions view. Object Type: string
        "override_change_expiration" : "", #Override the Change Expiration form. Object Type: string
        "override_create_multi_result" : "", #Override the Create Multiple Accounts Results form. Object Type: string
        "override_create_multi" : "", #Override the Create Multiple Guest Accounts form. Object Type: string
        "override_mac_create" : "", #Override the Create New Device form. Object Type: string
        "override_mac_create_receipt" : "", #Override the Create New Device Receipt form. Object Type: string
        "override_create_user" : "", #Override the Create New Guest Account form. Object Type: string
        "override_create_user_receipt" : "", #Override the Create New Guest Account Receipt form. Object Type: string
        "override_guest_edit" : "", #Override the Edit Account form. Object Type: string
        "override_guest_multi" : "", #Override the Edit Accounts view. Object Type: string
        "override_mac_edit" : "", #Override the Edit Device form. Object Type: string
        "override_mac_multi" : "", #Override the Edit Devices view. Object Type: string
        "override_guest_multi_form" : "", #Override the Edit Guest Accounts form. Object Type: string
        "override_mac_multi_form" : "", #Override the Edit Guest Devices form. Object Type: string
        "override_guest_multi_result" : "", #Override the Edit Multiple Accounts Results form. Object Type: string
        "override_mac_multi_result" : "", #Override the Edit Multiple Devices Results form. Object Type: string
        "override_mac_export" : "", #Override the Export Devices view. Object Type: string
        "override_guest_export" : "", #Override the Export Guest Accounts view. Object Type: string
        "override_mac_list" : "", #Override the Manage Devices view. Object Type: string
        "override_guest_users" : "", #Override the Manage Guest Accounts view. Object Type: string
        "override_guest_edit_receipt" : "", #Override the Updated Account Details form. Object Type: string
        "override_mac_edit_receipt" : "", #Override the Updated Device Details form. Object Type: string

        }
        """
        url_path = "/operator-profile/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_operator_profile_by_id(self, id="", body=({})):
        """
        Operation: Replace an operator profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the operator profile
        Required Body Parameters:['name', 'sponsor_filter']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #Enter a name for this operator profile. Object Type: string
        "comment" : "", #Comments or descriptive text about the operator profile. Object Type: string
        "enabled" : False, #If unchecked, operators with this profile will not be able to log in. Object Type: boolean
        "privileges" : False, #Select the privileges that will be granted to this operator login. Object Type: array
        "user_dbs_list" : "", #Select the visitor account roles that these operators are permitted to use. Object Type: string
        "sponsor_filter" : "", #Select the default operator filtering to apply to guest accounts. Object Type: string
        "filter_useraccount" : "", #Enter a comma-delimited list of field=value pairs to create an account filter. Object Type: string
        "filter_radacct" : "", #Enter a comma-delimited list of field=value pairs to create a session filter. Object Type: string
        "max_users" : "", #Maximum number of guests the operator can create.Leave blank for no limit. Object Type: string
        "max_devices" : "", #Maximum number of devices the operator can create.Leave blank for no limit. Object Type: string
        "userskin" : "", #Choose the skin to use for operators with this profile. Object Type: string
        "userskin_name" : "", #No Desc. Object Type: string
        "start_page" : "", #The initial page to show this operator after logging in. Object Type: string
        "lang" : "", #Select the default language to use for operators with this profile. Object Type: string
        "timezone_id" : "", #Select the default time zone for operators with this profile. Object Type: string
        "override_ui" : False, #If checked, you can specify different default forms and views to use. Object Type: boolean
        "override_guest_sessions" : "", #Override the Active Sessions view. Object Type: string
        "override_change_expiration" : "", #Override the Change Expiration form. Object Type: string
        "override_create_multi_result" : "", #Override the Create Multiple Accounts Results form. Object Type: string
        "override_create_multi" : "", #Override the Create Multiple Guest Accounts form. Object Type: string
        "override_mac_create" : "", #Override the Create New Device form. Object Type: string
        "override_mac_create_receipt" : "", #Override the Create New Device Receipt form. Object Type: string
        "override_create_user" : "", #Override the Create New Guest Account form. Object Type: string
        "override_create_user_receipt" : "", #Override the Create New Guest Account Receipt form. Object Type: string
        "override_guest_edit" : "", #Override the Edit Account form. Object Type: string
        "override_guest_multi" : "", #Override the Edit Accounts view. Object Type: string
        "override_mac_edit" : "", #Override the Edit Device form. Object Type: string
        "override_mac_multi" : "", #Override the Edit Devices view. Object Type: string
        "override_guest_multi_form" : "", #Override the Edit Guest Accounts form. Object Type: string
        "override_mac_multi_form" : "", #Override the Edit Guest Devices form. Object Type: string
        "override_guest_multi_result" : "", #Override the Edit Multiple Accounts Results form. Object Type: string
        "override_mac_multi_result" : "", #Override the Edit Multiple Devices Results form. Object Type: string
        "override_mac_export" : "", #Override the Export Devices view. Object Type: string
        "override_guest_export" : "", #Override the Export Guest Accounts view. Object Type: string
        "override_mac_list" : "", #Override the Manage Devices view. Object Type: string
        "override_guest_users" : "", #Override the Manage Guest Accounts view. Object Type: string
        "override_guest_edit_receipt" : "", #Override the Updated Account Details form. Object Type: string
        "override_mac_edit_receipt" : "", #Override the Updated Device Details form. Object Type: string

        }
        """
        url_path = "/operator-profile/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_operator_profile_by_id(self, id=""):
        """
        Operation: Delete an operator profile
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the operator profile
        """
        url_path = "/operator-profile/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_operator_profile_name_by_name(self, name=""):
        """
        Operation: Get an operator profile by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Name of the operator profile
        """
        url_path = "/operator-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_operator_profile_name_by_name(self, name="", body=({})):
        """
        Operation: Update an operator profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Name of the operator profile
        Required Body Parameters:['name', 'sponsor_filter']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #Enter a name for this operator profile. Object Type: string
        "comment" : "", #Comments or descriptive text about the operator profile. Object Type: string
        "enabled" : False, #If unchecked, operators with this profile will not be able to log in. Object Type: boolean
        "privileges" : False, #Select the privileges that will be granted to this operator login. Object Type: array
        "user_dbs_list" : "", #Select the visitor account roles that these operators are permitted to use. Object Type: string
        "sponsor_filter" : "", #Select the default operator filtering to apply to guest accounts. Object Type: string
        "filter_useraccount" : "", #Enter a comma-delimited list of field=value pairs to create an account filter. Object Type: string
        "filter_radacct" : "", #Enter a comma-delimited list of field=value pairs to create a session filter. Object Type: string
        "max_users" : "", #Maximum number of guests the operator can create.Leave blank for no limit. Object Type: string
        "max_devices" : "", #Maximum number of devices the operator can create.Leave blank for no limit. Object Type: string
        "userskin" : "", #Choose the skin to use for operators with this profile. Object Type: string
        "userskin_name" : "", #No Desc. Object Type: string
        "start_page" : "", #The initial page to show this operator after logging in. Object Type: string
        "lang" : "", #Select the default language to use for operators with this profile. Object Type: string
        "timezone_id" : "", #Select the default time zone for operators with this profile. Object Type: string
        "override_ui" : False, #If checked, you can specify different default forms and views to use. Object Type: boolean
        "override_guest_sessions" : "", #Override the Active Sessions view. Object Type: string
        "override_change_expiration" : "", #Override the Change Expiration form. Object Type: string
        "override_create_multi_result" : "", #Override the Create Multiple Accounts Results form. Object Type: string
        "override_create_multi" : "", #Override the Create Multiple Guest Accounts form. Object Type: string
        "override_mac_create" : "", #Override the Create New Device form. Object Type: string
        "override_mac_create_receipt" : "", #Override the Create New Device Receipt form. Object Type: string
        "override_create_user" : "", #Override the Create New Guest Account form. Object Type: string
        "override_create_user_receipt" : "", #Override the Create New Guest Account Receipt form. Object Type: string
        "override_guest_edit" : "", #Override the Edit Account form. Object Type: string
        "override_guest_multi" : "", #Override the Edit Accounts view. Object Type: string
        "override_mac_edit" : "", #Override the Edit Device form. Object Type: string
        "override_mac_multi" : "", #Override the Edit Devices view. Object Type: string
        "override_guest_multi_form" : "", #Override the Edit Guest Accounts form. Object Type: string
        "override_mac_multi_form" : "", #Override the Edit Guest Devices form. Object Type: string
        "override_guest_multi_result" : "", #Override the Edit Multiple Accounts Results form. Object Type: string
        "override_mac_multi_result" : "", #Override the Edit Multiple Devices Results form. Object Type: string
        "override_mac_export" : "", #Override the Export Devices view. Object Type: string
        "override_guest_export" : "", #Override the Export Guest Accounts view. Object Type: string
        "override_mac_list" : "", #Override the Manage Devices view. Object Type: string
        "override_guest_users" : "", #Override the Manage Guest Accounts view. Object Type: string
        "override_guest_edit_receipt" : "", #Override the Updated Account Details form. Object Type: string
        "override_mac_edit_receipt" : "", #Override the Updated Device Details form. Object Type: string

        }
        """
        url_path = "/operator-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_operator_profile_name_by_name(self, name="", body=({})):
        """
        Operation: Replace an operator profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Name of the operator profile
        Required Body Parameters:['name', 'sponsor_filter']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #Enter a name for this operator profile. Object Type: string
        "comment" : "", #Comments or descriptive text about the operator profile. Object Type: string
        "enabled" : False, #If unchecked, operators with this profile will not be able to log in. Object Type: boolean
        "privileges" : False, #Select the privileges that will be granted to this operator login. Object Type: array
        "user_dbs_list" : "", #Select the visitor account roles that these operators are permitted to use. Object Type: string
        "sponsor_filter" : "", #Select the default operator filtering to apply to guest accounts. Object Type: string
        "filter_useraccount" : "", #Enter a comma-delimited list of field=value pairs to create an account filter. Object Type: string
        "filter_radacct" : "", #Enter a comma-delimited list of field=value pairs to create a session filter. Object Type: string
        "max_users" : "", #Maximum number of guests the operator can create.Leave blank for no limit. Object Type: string
        "max_devices" : "", #Maximum number of devices the operator can create.Leave blank for no limit. Object Type: string
        "userskin" : "", #Choose the skin to use for operators with this profile. Object Type: string
        "userskin_name" : "", #No Desc. Object Type: string
        "start_page" : "", #The initial page to show this operator after logging in. Object Type: string
        "lang" : "", #Select the default language to use for operators with this profile. Object Type: string
        "timezone_id" : "", #Select the default time zone for operators with this profile. Object Type: string
        "override_ui" : False, #If checked, you can specify different default forms and views to use. Object Type: boolean
        "override_guest_sessions" : "", #Override the Active Sessions view. Object Type: string
        "override_change_expiration" : "", #Override the Change Expiration form. Object Type: string
        "override_create_multi_result" : "", #Override the Create Multiple Accounts Results form. Object Type: string
        "override_create_multi" : "", #Override the Create Multiple Guest Accounts form. Object Type: string
        "override_mac_create" : "", #Override the Create New Device form. Object Type: string
        "override_mac_create_receipt" : "", #Override the Create New Device Receipt form. Object Type: string
        "override_create_user" : "", #Override the Create New Guest Account form. Object Type: string
        "override_create_user_receipt" : "", #Override the Create New Guest Account Receipt form. Object Type: string
        "override_guest_edit" : "", #Override the Edit Account form. Object Type: string
        "override_guest_multi" : "", #Override the Edit Accounts view. Object Type: string
        "override_mac_edit" : "", #Override the Edit Device form. Object Type: string
        "override_mac_multi" : "", #Override the Edit Devices view. Object Type: string
        "override_guest_multi_form" : "", #Override the Edit Guest Accounts form. Object Type: string
        "override_mac_multi_form" : "", #Override the Edit Guest Devices form. Object Type: string
        "override_guest_multi_result" : "", #Override the Edit Multiple Accounts Results form. Object Type: string
        "override_mac_multi_result" : "", #Override the Edit Multiple Devices Results form. Object Type: string
        "override_mac_export" : "", #Override the Export Devices view. Object Type: string
        "override_guest_export" : "", #Override the Export Guest Accounts view. Object Type: string
        "override_mac_list" : "", #Override the Manage Devices view. Object Type: string
        "override_guest_users" : "", #Override the Manage Guest Accounts view. Object Type: string
        "override_guest_edit_receipt" : "", #Override the Updated Account Details form. Object Type: string
        "override_mac_edit_receipt" : "", #Override the Updated Device Details form. Object Type: string

        }
        """
        url_path = "/operator-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_operator_profile_name_by_name(self, name=""):
        """
        Operation: Delete an operator profile by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Name of the operator profile
        """
        url_path = "/operator-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Policy Manager Zones
    def get_server_policy_manager_zones(self):
        """
        Operation: Get list of Policy Manager Zones
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/server/policy-manager-zones"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_server_policy_manager_zones(self, body=({})):
        """
        Operation: Create Policy Manager Zone
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['zone_name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "zone_name" : "", #Name of the Policy Manager Zone. Object Type: string

        }
        """
        url_path = "/server/policy-manager-zones"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_server_policy_manager_zones_by_zone_id(self, zone_id=""):
        """
        Operation: Get Policy Manager Zone
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: zone_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/{zone_id}"
        dict_path = {"zone_id": zone_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_policy_manager_zones_by_zone_id(self, zone_id="", body=({})):
        """
        Operation: Update Policy Manager Zone
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: zone_id, Description: Numeric ID of the policy manager zone
        Required Body Parameters:['zone_name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "zone_name" : "", #Name of the Policy Manager Zone. Object Type: string

        }
        """
        url_path = "/server/policy-manager-zones/{zone_id}"
        dict_path = {"zone_id": zone_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_server_policy_manager_zones_by_zone_id(self, zone_id=""):
        """
        Operation: Delete Policy Manager Zone
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: zone_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/{zone_id}"
        dict_path = {"zone_id": zone_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_server_policy_manager_zones_name_by_name(self, name=""):
        """
        Operation: Get Policy Manager Zone by name
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_policy_manager_zones_name_by_name(self, name="", body=({})):
        """
        Operation: Update Policy Manager Zone by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        Required Body Parameters:['zone_name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "zone_name" : "", #Name of the Policy Manager Zone. Object Type: string

        }
        """
        url_path = "/server/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_server_policy_manager_zones_name_by_name(self, name=""):
        """
        Operation: Delete Policy Manager Zone by name
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Snmp Trap Receiver
    def get_snmp_trap_receiver(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Snmp Trap Receiver
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/snmp-trap-receiver"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_snmp_trap_receiver(self, body=({})):
        """
        Operation: Create a new Snmp Trap Receiver
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['host_address', 'snmp_version']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #HostName of the SNMP Trap Server. Object Type: string
        "description" : "", #Description of the SNMP Trap Server. Object Type: string
        "snmp_version" : "", #SNMP Version of the SNMP Trap Server. Object Type: string
        "community_string" : "", #Community String of the SNMP Trap Server. Object Type: string
        "server_port" : "", #Server Port of the SNMP Trap Server. Object Type: string
        "user" : "", #Username of the SNMP Trap Server. Object Type: string
        "type" : "", #Type of SNMP Trap Server. Object Type: string
        "auth_key" : "", #Authentication key of the SNMP Trap Server. Object Type: string
        "priv_key" : "", #Privacy key of the SNMP Trap Server. Object Type: string
        "priv_protocol" : {}, #Privacy Protocol. Object Type: object
        "auth_protocol" : {}, #Authentication Protocol. Object Type: object
        "security_level" : {}, #SNMP Version. Object Type: object

        }
        """
        url_path = "/snmp-trap-receiver"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_snmp_trap_receiver_by_snmp_trap_receiver_id(self, snmp_trap_receiver_id=""):
        """
        Operation: Get a Snmp Trap Receiver
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
        """
        url_path = "/snmp-trap-receiver/{snmp_trap_receiver_id}"
        dict_path = {"snmp_trap_receiver_id": snmp_trap_receiver_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_snmp_trap_receiver_by_snmp_trap_receiver_id(
        self, snmp_trap_receiver_id="", body=({})
    ):
        """
        Operation: Update some fields of Snmp Trap Receiver
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #HostName of the SNMP Trap Server. Object Type: string
        "description" : "", #Description of the SNMP Trap Server. Object Type: string
        "snmp_version" : "", #SNMP Version of the SNMP Trap Server. Object Type: string
        "community_string" : "", #Community String of the SNMP Trap Server. Object Type: string
        "server_port" : "", #Server Port of the SNMP Trap Server. Object Type: string
        "user" : "", #Username of the SNMP Trap Server. Object Type: string
        "type" : "", #Type of SNMP Trap Server. Object Type: string
        "auth_key" : "", #Authentication key of the SNMP Trap Server. Object Type: string
        "priv_key" : "", #Privacy key of the SNMP Trap Server. Object Type: string
        "priv_protocol" : {}, #Privacy Protocol. Object Type: object
        "auth_protocol" : {}, #Authentication Protocol. Object Type: object
        "security_level" : {}, #SNMP Version. Object Type: object

        }
        """
        url_path = "/snmp-trap-receiver/{snmp_trap_receiver_id}"
        dict_path = {"snmp_trap_receiver_id": snmp_trap_receiver_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_snmp_trap_receiver_by_snmp_trap_receiver_id(
        self, snmp_trap_receiver_id="", body=({})
    ):
        """
        Operation: Replace a Snmp Trap Receiver
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
        Required Body Parameters:['host_address', 'snmp_version']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #HostName of the SNMP Trap Server. Object Type: string
        "description" : "", #Description of the SNMP Trap Server. Object Type: string
        "snmp_version" : "", #SNMP Version of the SNMP Trap Server. Object Type: string
        "community_string" : "", #Community String of the SNMP Trap Server. Object Type: string
        "server_port" : "", #Server Port of the SNMP Trap Server. Object Type: string
        "user" : "", #Username of the SNMP Trap Server. Object Type: string
        "type" : "", #Type of SNMP Trap Server. Object Type: string
        "auth_key" : "", #Authentication key of the SNMP Trap Server. Object Type: string
        "priv_key" : "", #Privacy key of the SNMP Trap Server. Object Type: string
        "priv_protocol" : {}, #Privacy Protocol. Object Type: object
        "auth_protocol" : {}, #Authentication Protocol. Object Type: object
        "security_level" : {}, #SNMP Version. Object Type: object

        }
        """
        url_path = "/snmp-trap-receiver/{snmp_trap_receiver_id}"
        dict_path = {"snmp_trap_receiver_id": snmp_trap_receiver_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_snmp_trap_receiver_by_snmp_trap_receiver_id(
        self, snmp_trap_receiver_id=""
    ):
        """
        Operation: Delete a Snmp Trap Receiver
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
        """
        url_path = "/snmp-trap-receiver/{snmp_trap_receiver_id}"
        dict_path = {"snmp_trap_receiver_id": snmp_trap_receiver_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_snmp_trap_receiver_name_by_name(self, name=""):
        """
        Operation: Get a Snmp Trap Receiver by name
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the Host Address
        """
        url_path = "/snmp-trap-receiver/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_snmp_trap_receiver_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of Snmp Trap Receiver by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the Host Address
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #HostName of the SNMP Trap Server. Object Type: string
        "description" : "", #Description of the SNMP Trap Server. Object Type: string
        "snmp_version" : "", #SNMP Version of the SNMP Trap Server. Object Type: string
        "community_string" : "", #Community String of the SNMP Trap Server. Object Type: string
        "server_port" : "", #Server Port of the SNMP Trap Server. Object Type: string
        "user" : "", #Username of the SNMP Trap Server. Object Type: string
        "type" : "", #Type of SNMP Trap Server. Object Type: string
        "auth_key" : "", #Authentication key of the SNMP Trap Server. Object Type: string
        "priv_key" : "", #Privacy key of the SNMP Trap Server. Object Type: string
        "priv_protocol" : {}, #Privacy Protocol. Object Type: object
        "auth_protocol" : {}, #Authentication Protocol. Object Type: object
        "security_level" : {}, #SNMP Version. Object Type: object

        }
        """
        url_path = "/snmp-trap-receiver/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_snmp_trap_receiver_name_by_name(self, name="", body=({})):
        """
        Operation: Replace a Snmp Trap Receiver by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the Host Address
        Required Body Parameters:['host_address', 'snmp_version']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_address" : "", #HostName of the SNMP Trap Server. Object Type: string
        "description" : "", #Description of the SNMP Trap Server. Object Type: string
        "snmp_version" : "", #SNMP Version of the SNMP Trap Server. Object Type: string
        "community_string" : "", #Community String of the SNMP Trap Server. Object Type: string
        "server_port" : "", #Server Port of the SNMP Trap Server. Object Type: string
        "user" : "", #Username of the SNMP Trap Server. Object Type: string
        "type" : "", #Type of SNMP Trap Server. Object Type: string
        "auth_key" : "", #Authentication key of the SNMP Trap Server. Object Type: string
        "priv_key" : "", #Privacy key of the SNMP Trap Server. Object Type: string
        "priv_protocol" : {}, #Privacy Protocol. Object Type: object
        "auth_protocol" : {}, #Authentication Protocol. Object Type: object
        "security_level" : {}, #SNMP Version. Object Type: object

        }
        """
        url_path = "/snmp-trap-receiver/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_snmp_trap_receiver_name_by_name(self, name=""):
        """
        Operation: Delete a Snmp Trap Receiver by name
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the Host Address
        """
        url_path = "/snmp-trap-receiver/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
