from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_globalserverconfiguration_v1.py


class ApiGlobalServerConfiguration(ClearPassAPILogin):
    # Function Section Name:AdminPrivilege
    # Function Section Description: Manage admin privileges

    def get_admin_privilege(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of admin privileges
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AdminPrivilegeCreate {name (string): Name of the admin privilege,description (string, optional): Description of the admin privilege,access_type (string, optional) = ['UI' or 'API' or 'FULL']: Property to decide the access type of the user.,cppm_privileges (object): Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).,insight_privileges (object, optional): Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).,allow_passwords (boolean, optional): If selected, all passwords may be displayed in the response,allow_security_configs (boolean, optional): If selected, Admin user will have access for security configuration}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "access_type": "",
          "cppm_privileges": "object",
          "insight_privileges": "object",
          "allow_passwords": false,
          "allow_security_configs": false
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: admin_privilege_id, Description: Numeric ID of the admin privilege
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: admin_privilege_id, Description: Numeric ID of the admin privilege
                Required Body Parameters (body description)- AdminPrivilegeUpdate {name (string, optional): Name of the admin privilege,description (string, optional): Description of the admin privilege,access_type (string, optional) = ['UI' or 'API' or 'FULL']: Property to decide the access type of the user.,cppm_privileges (object, optional): Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).,insight_privileges (object, optional): Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).,allow_passwords (boolean, optional): If selected, all passwords may be displayed in the response,allow_security_configs (boolean, optional): If selected, Admin user will have access for security configuration}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "access_type": "",
          "cppm_privileges": "object",
          "insight_privileges": "object",
          "allow_passwords": false,
          "allow_security_configs": false
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: admin_privilege_id, Description: Numeric ID of the admin privilege
                Required Body Parameters (body description)- AdminPrivilegeReplace {name (string): Name of the admin privilege,description (string, optional): Description of the admin privilege,access_type (string, optional) = ['UI' or 'API' or 'FULL']: Property to decide the access type of the user.,cppm_privileges (object): Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).,insight_privileges (object, optional): Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).,allow_passwords (boolean, optional): If selected, all passwords may be displayed in the response,allow_security_configs (boolean, optional): If selected, Admin user will have access for security configuration}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "access_type": "",
          "cppm_privileges": "object",
          "insight_privileges": "object",
          "allow_passwords": false,
          "allow_security_configs": false
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: admin_privilege_id, Description: Numeric ID of the admin privilege
        """
        url_path = "/admin-privilege/{admin_privilege_id}"
        dict_path = {"admin_privilege_id": admin_privilege_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_admin_privilege_name_by_name(self, name=""):
        """
        Operation: Get an admin privilege by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the admin privilege
        """
        url_path = "/admin-privilege/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_privilege_name_by_name(self, name="", body=({})):
        """
                Operation: Update some fields of an admin privilege by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the admin privilege
                Required Body Parameters (body description)- AdminPrivilegeUpdate {name (string, optional): Name of the admin privilege,description (string, optional): Description of the admin privilege,access_type (string, optional) = ['UI' or 'API' or 'FULL']: Property to decide the access type of the user.,cppm_privileges (object, optional): Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).,insight_privileges (object, optional): Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).,allow_passwords (boolean, optional): If selected, all passwords may be displayed in the response,allow_security_configs (boolean, optional): If selected, Admin user will have access for security configuration}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "access_type": "",
          "cppm_privileges": "object",
          "insight_privileges": "object",
          "allow_passwords": false,
          "allow_security_configs": false
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the admin privilege
                Required Body Parameters (body description)- AdminPrivilegeReplace {name (string): Name of the admin privilege,description (string, optional): Description of the admin privilege,access_type (string, optional) = ['UI' or 'API' or 'FULL']: Property to decide the access type of the user.,cppm_privileges (object): Privilege list in JSON object format(e.g., {"con:RWD", "mon":"RW"}).,insight_privileges (object, optional): Privilege list in JSON object format(e.g., {"report": "RWD", "dashboard":"RW"}).,allow_passwords (boolean, optional): If selected, all passwords may be displayed in the response,allow_security_configs (boolean, optional): If selected, Admin user will have access for security configuration}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "access_type": "",
          "cppm_privileges": "object",
          "insight_privileges": "object",
          "allow_passwords": false,
          "allow_security_configs": false
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the admin privilege
        """
        url_path = "/admin-privilege/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:AdminUser
    # Function Section Description: Manage admin users

    def get_admin_user(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of admin users
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AdminUserCreate {name (string): Name of the admin user,user_id (string): Unique user id of the admin user,enabled (boolean, optional): Flag indicating if the account is enabled,password (string): Password of the admin user,privilege_level (string): Name of the admin privilege}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "user_id": "",
          "enabled": false,
          "password": "",
          "privilege_level": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric ID of the admin user
        """
        url_path = "/admin-user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_user_by_id(self, id="", body=({})):
        """
                Operation: Update some fields of an admin user
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: Numeric ID of the admin user
                Required Body Parameters (body description)- AdminUserUpdate {name (string, optional): Name of the admin user,user_id (string, optional): Unique user id of the admin user,enabled (boolean, optional): Flag indicating if the account is enabled,password (string, optional): Password of the admin user,privilege_level (string, optional): Name of the admin privilege}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "user_id": "",
          "enabled": false,
          "password": "",
          "privilege_level": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: Numeric ID of the admin user
                Required Body Parameters (body description)- AdminUserReplace {name (string): Name of the admin user,user_id (string): Unique user id of the admin user,enabled (boolean, optional): Flag indicating if the account is enabled,password (string): Password of the admin user,privilege_level (string): Name of the admin privilege}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "user_id": "",
          "enabled": false,
          "password": "",
          "privilege_level": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: Numeric ID of the admin user
        """
        url_path = "/admin-user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_admin_user_user_id_by_user_id(self, user_id=""):
        """
        Operation: Get an admin user by user_id
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: Unique user_id of the admin user
        """
        url_path = "/admin-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_admin_user_user_id_by_user_id(self, user_id="", body=({})):
        """
                Operation: Update some fields of an admin user by user_id
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: user_id, Description: Unique user_id of the admin user
                Required Body Parameters (body description)- AdminUserUpdate {name (string, optional): Name of the admin user,user_id (string, optional): Unique user id of the admin user,enabled (boolean, optional): Flag indicating if the account is enabled,password (string, optional): Password of the admin user,privilege_level (string, optional): Name of the admin privilege}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "user_id": "",
          "enabled": false,
          "password": "",
          "privilege_level": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: user_id, Description: Unique user_id of the admin user
                Required Body Parameters (body description)- AdminUserReplace {name (string): Name of the admin user,user_id (string): Unique user id of the admin user,enabled (boolean, optional): Flag indicating if the account is enabled,password (string): Password of the admin user,privilege_level (string): Name of the admin privilege}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "user_id": "",
          "enabled": false,
          "password": "",
          "privilege_level": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: Unique user_id of the admin user
        """
        url_path = "/admin-user/user-id/{user_id}"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:AdminUserPasswordPolicy
    # Function Section Description: Manage admin user password policies

    def get_admin_user_password_policy(self, user_id=""):
        """
        Operation: Get the admin user password policies
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: user_id, Description: Unique user_id of the admin user
        """
        url_path = "/admin-user/password-policy"
        dict_path = {"user_id": user_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_admin_user_password_policy(self, body=({})):
        """
                Operation: Put the admin user password policies
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AdminUserPasswordPolicyReplace {password_minimum_length (integer) = ['6-128']: Minimum length of the password,password_complexity (string) = ['NONE' or 'CASE' or 'NUMBER' or 'ALPHANUMERIC' or 'CASENUMERIC' or 'PUNCTUATION' or 'COMPLEX']: Complexity Level of the password,password_disallowed_characters (string, optional): Disallowed characters in the password,password_disallowed_words (string, optional): Disallowed words in the password,password_prohibit_user_id (boolean, optional): May not contain User ID or its characters in reversed order,password_prohibit_repeated_chars (boolean, optional): May not contain repeated character four or more times consecutively,password_expiry_days (integer, optional) = ['0-500']: Password expiry days,disable_after_failed_attempts (integer, optional) = ['1-100']: Failed attempts count,reset_failed_attempts_count (boolean, optional): Reset failed attempts count and enable those users}
                Required Body Parameters (type(dict) body example)- {
          "password_minimum_length": 0,
          "password_complexity": "",
          "password_disallowed_characters": "",
          "password_disallowed_words": "",
          "password_prohibit_user_id": false,
          "password_prohibit_repeated_chars": false,
          "password_expiry_days": 0,
          "disable_after_failed_attempts": 0,
          "reset_failed_attempts_count": false
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AdminUserPasswordPolicyUpdate {password_minimum_length (integer, optional) = ['6-128']: Minimum length of the password,password_complexity (string, optional) = ['NONE' or 'CASE' or 'NUMBER' or 'ALPHANUMERIC' or 'CASENUMERIC' or 'PUNCTUATION' or 'COMPLEX']: Complexity Level of the password,password_disallowed_characters (string, optional): Disallowed characters in the password,password_disallowed_words (string, optional): Disallowed words in the password,password_prohibit_user_id (boolean, optional): May not contain User ID or its characters in reversed order,password_prohibit_repeated_chars (boolean, optional): May not contain repeated character four or more times consecutively,password_expiry_days (integer, optional) = ['0-500']: Password expiry days,disable_after_failed_attempts (integer, optional) = ['1-100']: Failed attempts count,reset_failed_attempts_count (boolean, optional): Reset failed attempts count and enable those users}
                Required Body Parameters (type(dict) body example)- {
          "password_minimum_length": 0,
          "password_complexity": "",
          "password_disallowed_characters": "",
          "password_disallowed_words": "",
          "password_prohibit_user_id": false,
          "password_prohibit_repeated_chars": false,
          "password_expiry_days": 0,
          "disable_after_failed_attempts": 0,
          "reset_failed_attempts_count": false
        }
        """
        url_path = "/admin-user/password-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # Function Section Name:ApplicationLicense
    # Function Section Description: Manage application license

    def get_application_license(self, body=({})):
        """
                Operation: Get a list of application licenses
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- AdminUserPasswordPolicyUpdate {password_minimum_length (integer, optional) = ['6-128']: Minimum length of the password,password_complexity (string, optional) = ['NONE' or 'CASE' or 'NUMBER' or 'ALPHANUMERIC' or 'CASENUMERIC' or 'PUNCTUATION' or 'COMPLEX']: Complexity Level of the password,password_disallowed_characters (string, optional): Disallowed characters in the password,password_disallowed_words (string, optional): Disallowed words in the password,password_prohibit_user_id (boolean, optional): May not contain User ID or its characters in reversed order,password_prohibit_repeated_chars (boolean, optional): May not contain repeated character four or more times consecutively,password_expiry_days (integer, optional) = ['0-500']: Password expiry days,disable_after_failed_attempts (integer, optional) = ['1-100']: Failed attempts count,reset_failed_attempts_count (boolean, optional): Reset failed attempts count and enable those users}
                Required Body Parameters (type(dict) body example)- {
          "password_minimum_length": 0,
          "password_complexity": "",
          "password_disallowed_characters": "",
          "password_disallowed_words": "",
          "password_prohibit_user_id": false,
          "password_prohibit_repeated_chars": false,
          "password_expiry_days": 0,
          "disable_after_failed_attempts": 0,
          "reset_failed_attempts_count": false
        }
        """
        url_path = "/application-license"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def new_application_license(self, body=({})):
        """
                Operation: Create a new application license
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ApplicationLicenseCreate {license_key (string): License key}
                Required Body Parameters (type(dict) body example)- {
          "license_key": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_application_license_by_license_id(self, license_id="", body=({})):
        """
                Operation: Update a license by license id
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: license_id, Description: Numeric ID of Application License
                Required Body Parameters (body description)- ApplicationLicenseReplace {license_key (string): License key}
                Required Body Parameters (type(dict) body example)- {
          "license_key": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_application_license_activate_online_by_license_id(self, license_id=""):
        """
        Operation: Activate license online by license id
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/activate-online/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_application_license_activate_offline_by_license_id(self, license_id=""):
        """
        Operation: Activate license offline by license id
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/activate-offline/{license_id}"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def get_application_license_summary(self, license_id=""):
        """
        Operation: Get application license summary
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: license_id, Description: Numeric ID of Application License
        """
        url_path = "/application-license/summary"
        dict_path = {"license_id": license_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:Attribute
    # Function Section Description: Manage Attributes

    def get_attribute(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of attributes
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AttributeCreate {name (string): Name of the attribute,entity_name (string) = ['Device' or 'LocalUser' or 'GuestUser' or 'Endpoint' or 'Onboard']: Entity Name of the attribute,data_type (string) = ['Boolean' or 'Date' or 'Day' or 'IPv4Address' or 'IPv6Address' or 'Integer32' or 'List' or 'MACAddress' or 'String' or 'Text' or 'Time' or 'TimeOfDay']: Data Type of the attribute,mandatory (boolean, optional): Enable this to make this attribute mandatory for the entity,default_value (string, optional): Default Value of the attribute,allow_multiple (boolean, optional): To Allow Multiple values of the attribute for Data Type String,allowed_value (string, optional): Allowed Value for Data Type List (e.g., example1,example2,example3)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "entity_name": "",
          "data_type": "",
          "mandatory": false,
          "default_value": "",
          "allow_multiple": false,
          "allowed_value": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: attribute_id, Description: Numeric ID of the attribute
        """
        url_path = "/attribute/{attribute_id}"
        dict_path = {"attribute_id": attribute_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_attribute_by_attribute_id(self, attribute_id="", body=({})):
        """
                Operation: Update some fields of an attribute
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: attribute_id, Description: Numeric ID of the attribute
                Required Body Parameters (body description)- AttributeUpdate {name (string, optional): Name of the attribute,entity_name (string, optional) = ['Device' or 'LocalUser' or 'GuestUser' or 'Endpoint' or 'Onboard']: Entity Name of the attribute,data_type (string, optional) = ['Boolean' or 'Date' or 'Day' or 'IPv4Address' or 'IPv6Address' or 'Integer32' or 'List' or 'MACAddress' or 'String' or 'Text' or 'Time' or 'TimeOfDay']: Data Type of the attribute,mandatory (boolean, optional): Enable this to make this attribute mandatory for the entity,default_value (string, optional): Default Value of the attribute,allow_multiple (boolean, optional): To Allow Multiple values of the attribute for Data Type String,allowed_value (string, optional): Allowed Value for Data Type List (e.g., example1,example2,example3)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "entity_name": "",
          "data_type": "",
          "mandatory": false,
          "default_value": "",
          "allow_multiple": false,
          "allowed_value": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: attribute_id, Description: Numeric ID of the attribute
                Required Body Parameters (body description)- AttributeReplace {name (string): Name of the attribute,entity_name (string) = ['Device' or 'LocalUser' or 'GuestUser' or 'Endpoint' or 'Onboard']: Entity Name of the attribute,data_type (string) = ['Boolean' or 'Date' or 'Day' or 'IPv4Address' or 'IPv6Address' or 'Integer32' or 'List' or 'MACAddress' or 'String' or 'Text' or 'Time' or 'TimeOfDay']: Data Type of the attribute,mandatory (boolean, optional): Enable this to make this attribute mandatory for the entity,default_value (string, optional): Default Value of the attribute,allow_multiple (boolean, optional): To Allow Multiple values of the attribute for Data Type String,allowed_value (string, optional): Allowed Value for Data Type List (e.g., example1,example2,example3)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "entity_name": "",
          "data_type": "",
          "mandatory": false,
          "default_value": "",
          "allow_multiple": false,
          "allowed_value": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: attribute_id, Description: Numeric ID of the attribute
        """
        url_path = "/attribute/{attribute_id}"
        dict_path = {"attribute_id": attribute_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_attribute_by_entity_name_name_name(self, entity_name="", name=""):
        """
        Operation: Get an attribute by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: entity_name, Description: Entity Name of the attribute
        Required Path Parameter Name: name, Description: Unique name of the attribute
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: entity_name, Description: Entity Name of the attribute
                Required Path Parameter Name: name, Description: Unique name of the attribute
                Required Body Parameters (body description)- AttributeUpdate {name (string, optional): Name of the attribute,entity_name (string, optional) = ['Device' or 'LocalUser' or 'GuestUser' or 'Endpoint' or 'Onboard']: Entity Name of the attribute,data_type (string, optional) = ['Boolean' or 'Date' or 'Day' or 'IPv4Address' or 'IPv6Address' or 'Integer32' or 'List' or 'MACAddress' or 'String' or 'Text' or 'Time' or 'TimeOfDay']: Data Type of the attribute,mandatory (boolean, optional): Enable this to make this attribute mandatory for the entity,default_value (string, optional): Default Value of the attribute,allow_multiple (boolean, optional): To Allow Multiple values of the attribute for Data Type String,allowed_value (string, optional): Allowed Value for Data Type List (e.g., example1,example2,example3)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "entity_name": "",
          "data_type": "",
          "mandatory": false,
          "default_value": "",
          "allow_multiple": false,
          "allowed_value": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: entity_name, Description: Entity Name of the attribute
                Required Path Parameter Name: name, Description: Unique name of the attribute
                Required Body Parameters (body description)- AttributeReplace {name (string): Name of the attribute,entity_name (string) = ['Device' or 'LocalUser' or 'GuestUser' or 'Endpoint' or 'Onboard']: Entity Name of the attribute,data_type (string) = ['Boolean' or 'Date' or 'Day' or 'IPv4Address' or 'IPv6Address' or 'Integer32' or 'List' or 'MACAddress' or 'String' or 'Text' or 'Time' or 'TimeOfDay']: Data Type of the attribute,mandatory (boolean, optional): Enable this to make this attribute mandatory for the entity,default_value (string, optional): Default Value of the attribute,allow_multiple (boolean, optional): To Allow Multiple values of the attribute for Data Type String,allowed_value (string, optional): Allowed Value for Data Type List (e.g., example1,example2,example3)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "entity_name": "",
          "data_type": "",
          "mandatory": false,
          "default_value": "",
          "allow_multiple": false,
          "allowed_value": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: entity_name, Description: Entity Name of the attribute
        Required Path Parameter Name: name, Description: Unique name of the attribute
        """
        url_path = "/attribute/{entity_name}/name/{name}"
        dict_path = {"entity_name": entity_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:ClearPassPortal
    # Function Section Description: Manage ClearPass portal

    def get_clearpass_portal(self, entity_name="", name=""):
        """
        Operation: Get ClearPass Portal
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: entity_name, Description: Entity Name of the attribute
        Required Path Parameter Name: name, Description: Unique name of the attribute
        """
        url_path = "/clearpass-portal"
        dict_path = {"entity_name": entity_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_clearpass_portal(self, body=({})):
        """
                Operation: Change ClearPass Portal
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ClearPassPortal {title (string, optional): Default Landing page Title,header (string, optional): Default Landing page Header,footer (string, optional): Default Landing page Footer,copyright (string, optional): Default Landing page Copyright text,app_name (string, optional) = ['ClearPass Guest' or 'ClearPass Insight' or 'ClearPass Policy Manager' or 'ClearPass Onboard']: If specified, User will be redirected to the selected ClearPass application login page,guest_portal (string, optional): If specified, User will be redirected to the selected Guest Web Login/Self-Registration Portal,url (string, optional): Redirect URL constructed based on the Guest Portal name(guest_portal) or Application Login Page(app_name)}
                Required Body Parameters (type(dict) body example)- {
          "title": "",
          "header": "",
          "footer": "",
          "copyright": "",
          "app_name": "",
          "guest_portal": "",
          "url": ""
        }
        """
        url_path = "/clearpass-portal"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:ClusterDbSync
    # Function Section Description: Ensure a subscriber node is synchronized with the publisher node

    def new_cluster_db_sync(self, body=({})):
        """
                Operation: Synchronize subscriber with the publisher
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Unprocessable Entity, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Unprocessable Entity, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ClusterDbSync {timeout (string, optional): Maximum time in seconds to wait for the database sync operation}
                Required Body Parameters (type(dict) body example)- {
          "timeout": ""
        }
        """
        url_path = "/cluster/db-sync"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:ClusterWideParameter
    # Function Section Description: Manage cluster wide parameters

    def get_cluster_parameters(self, body=({})):
        """
                Operation: Get cluster wide parameters
                HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- ClusterDbSync {timeout (string, optional): Maximum time in seconds to wait for the database sync operation}
                Required Body Parameters (type(dict) body example)- {
          "timeout": ""
        }
        """
        url_path = "/cluster/parameters"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def replace_cluster_parameters(self, body=({})):
        """
                Operation: Replace cluster wide parameters
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ClusterWideParameter {AdminSessionIdleTimeout (integer, optional): Admin Session Idle Timeout in minutes,AdminUserLoginRemoteTacacsServerIP (string, optional): Remote TACACS+ server for Admin logins,AdminUserLoginRemoteTacacsServerPort (integer, optional): Admin UI Login Remote TACACS+ Server Port,AdminUserLoginRemoteTacacsServerSecret (string, optional): Remote TACACS+ server shared secret,AdminUserLoginSecondaryRemoteTacacsServerIP (string, optional),AdminUserLoginSecondaryRemoteTacacsServerPort (integer, optional),AdminUserLoginSecondaryRemoteTacacsServerSecret (string, optional),AdminUserLoginTacacsClientIpSetByHeaderXFF (string, optional) = ['TRUE' or 'FALSE']: Enable Admin UI TACACS+ Client IP set by X-Forwarded-For (XFF) header,AdminUserLoginTertiaryRemoteTacacsServerIP (string, optional),AdminUserLoginTertiaryRemoteTacacsServerPort (integer, optional),AdminUserLoginTertiaryRemoteTacacsServerSecret (string, optional),AlertNotificationTimeout (string, optional) = ['1' or '2' or '4' or '6' or '8' or '12' or '24' or 'Disabled']: Alert Notification Timeout in hours,AuditRecordsCleanupInterval (integer, optional): Old Audit Records cleanup interval in days,AutoBackupConfigOptions (string, optional) = ['Off' or 'Config' or 'Config|SessionInfo']: Auto backup configuration options,CLISessionIdleTimeout (integer, optional): CLI Session Idle Timeout in minutes,CSRCleanupInterval (integer, optional): Cleanup interval for CSRs and private keys,ClearPassZoneCache (string, optional) = ['OFF' or 'NORMAL' or 'FULL']: ClearPass Zone Cache Durability,ClusterCommunicationMode (string, optional) = ['ipv4' or 'ipv6']: Mode of communication between cluster nodes,CommonCriteriaMode (string, optional) = ['TRUE' or 'FALSE']: Enable Common Criteria mode for the cluster,ConsoleSessionIdleTimeout (integer, optional): Console Session Idle Timeout in minutes,ContentSecurityPolicy (string, optional) = ['Enable' or 'Disable']: Enable Content Security Policy (CSP),ContextServerPollInterval (integer, optional): Endpoint Context Servers polling interval in minutes,ContextServerPollStartTime (string, optional): [00:00:00-23:59:59] Endpoint Context Servers polling start time,DbAppexternalUserPassword (string, optional): Database user "appexternal" password,DesignatedStandbyPublisher (string, optional): Designated Standby Publisher,DisableTLS1.0 (string, optional) = ['None' or 'Admin' or 'Network' or 'All']: Disable TLSv1.0 support,DisableTLS1.1 (string, optional) = ['None' or 'Admin' or 'Network' or 'All']: Disable TLSv1.1 support,DisableTLS1.3 (string, optional) = ['None' or 'Admin'],EnableNTLMV1ForWmi (string, optional) = ['TRUE' or 'FALSE']: Enable NTLMV1 for WMI scans,EnablePublisherFailover (string, optional) = ['TRUE' or 'FALSE']: Enable Publisher Failover,EnableTelemetry (string, optional) = ['TRUE' or 'FALSE']: Enable sharing information about the cluster to Telemetry server,ExpiredGuestAccountsCleanupInterval (integer, optional): Expired guest accounts cleanup interval in days,ExtensionsAutoUpgradesFlag (string, optional) = ['TRUE' or 'FALSE'],FreeDiskSpaceThreshold (integer, optional): Free disk space threshold value in %,FreeMemoryThreshold (integer, optional): Free memory threshold value in %,ICMPv6Filters (string, optional) = ['Enable' or 'Disable']: Enable ICMPv6 Filters,IgnoreConflictNetworkBootAgents (string, optional) = ['TRUE' or 'FALSE']: Enable Ignore Conflict (Network Boot Agents),InformationStoredCleanupInterval (integer, optional): Cleanup interval for information stored on the disk in days,KnownEndpointsCleanupInterval (integer, optional): Known endpoints cleanup interval in days,LoginBannerText (string, optional): Login Banner Text,NetflowReprofileInterval (integer, optional): Netflow reprofile interval in days,NotificationEmailAddress (string, optional): Alert Notification - Email Address,NotificationSmsAddress (string, optional): Alert Notification - SMS Address,OnGuardAutoUpdatesFlag (string, optional) = ['TRUE' or 'FALSE']: Automatically check for available OnGuard Signature Updates,PasswordPrompt (string, optional): TACACS+ Password Prompt Text,PolicyResultCacheTimeout (integer, optional): Policy result cache timeout in minutes,PostAuthUnsubscribeEndpoints (string, optional) = ['Enable' or 'Disable'],PostAuthV2 (string, optional) = ['Enable' or 'Disable']: Enable Post-Auth v2,PostAuthV2HttpEnforcement (string, optional) = ['Enable' or 'Disable']: Enable Post-Auth v2 HTTP enforcement,ProcessWiredFromIfMap (string, optional) = ['TRUE' or 'FALSE']: Process wired device information from IF-MAP interface,ProfiledKnownEndpointsCleanupOption (string, optional) = ['TRUE' or 'FALSE']: Profiled Known endpoints cleanup option in days,ProfiledUnknownEndpointsCleanupInterval (integer, optional): Profiled Unknown endpoints cleanup interval in days,ProfilerConflictStrictMode (string, optional) = ['high' or 'medium' or 'low']: Conflict Detection Strict Mode,ProfilerNmapEnable (string, optional) = ['TRUE' or 'FALSE']: Enable endpoint port scan using Nmap,ProfilerPostureEnable (string, optional) = ['TRUE' or 'FALSE']: Enable Endpoint scan using WMI,ProfilerScanPorts (string, optional): Profiler Scan TCP Ports,ProfilerSubnetScanInterval (integer, optional): Profiler subnet scan interval in hours,ProfilingAutoUpdatesFlag (string, optional) = ['TRUE' or 'FALSE']: Automatically check for available Profiling Updates,SSHCipherMode (string, optional): Allowed SSH Cipher Modes,SessionLogsCleanupInterval (integer, optional): Cleanup interval for Session log details in the database in days,SoftwareAutoUpdatesFlag (string, optional) = ['TRUE' or 'FALSE']: Automatically check for available Software Updates,StaleTLSsessioninDiskclenaup (integer, optional),StandbyFailoverWaitTime (integer, optional): Failover Wait Time in minutes,StaticIPEndpointsCleanupOption (string, optional) = ['TRUE' or 'FALSE']: Static IP endpoints cleanup option,StorePasswordHash (string, optional) = ['TRUE' or 'FALSE']: Store Password Hash for MSCHAP authentication,StoreReversibleLocalUserPasswords (string, optional) = ['TRUE' or 'FALSE']: Store Local User passwords using reversible encryption,SyslogBatchInterval (integer, optional): Syslog Export Interval in seconds,SystemAlertLevel (string, optional) = ['INFO' or 'WARN' or 'ERROR']: System Alert Level,TacacsAllowUnencryptedCommunication (string, optional) = ['Enable' or 'Disable']: Enable TACACS+ clients to communicate with ClearPass server over an unencrypted channel,TacacsDisableChangePassword (string, optional) = ['TRUE' or 'FALSE']: Disable Change Password for TACACS+,TacacsIdleTimeout (integer, optional): TACACS+ Connection Idle Timeout in seconds,TacacsProcessUnauthenticatedRequest (string, optional) = ['Enable' or 'Disable']: Enable unauthenticated TACACS+ user request processing,UnknownEndpointsCleanupInterval (integer, optional): Unknown endpoints cleanup interval in days,UserPrompt (string, optional): TACACS+ User Prompt Text,allowConcurrentLogin (string, optional) = ['TRUE' or 'FALSE']: Enable Concurrent Admin Login,session_cache_type (string, optional) = ['Internal' or 'Internal+Disk']}
                Required Body Parameters (type(dict) body example)- {
          "AdminSessionIdleTimeout": 0,
          "AdminUserLoginRemoteTacacsServerIP": "",
          "AdminUserLoginRemoteTacacsServerPort": 0,
          "AdminUserLoginRemoteTacacsServerSecret": "",
          "AdminUserLoginSecondaryRemoteTacacsServerIP": "",
          "AdminUserLoginSecondaryRemoteTacacsServerPort": 0,
          "AdminUserLoginSecondaryRemoteTacacsServerSecret": "",
          "AdminUserLoginTacacsClientIpSetByHeaderXFF": "",
          "AdminUserLoginTertiaryRemoteTacacsServerIP": "",
          "AdminUserLoginTertiaryRemoteTacacsServerPort": 0,
          "AdminUserLoginTertiaryRemoteTacacsServerSecret": "",
          "AlertNotificationTimeout": "",
          "AuditRecordsCleanupInterval": 0,
          "AutoBackupConfigOptions": "",
          "CLISessionIdleTimeout": 0,
          "CSRCleanupInterval": 0,
          "ClearPassZoneCache": "",
          "ClusterCommunicationMode": "",
          "CommonCriteriaMode": "",
          "ConsoleSessionIdleTimeout": 0,
          "ContentSecurityPolicy": "",
          "ContextServerPollInterval": 0,
          "ContextServerPollStartTime": "",
          "DbAppexternalUserPassword": "",
          "DesignatedStandbyPublisher": "",
          "DisableTLS1.0": "",
          "DisableTLS1.1": "",
          "DisableTLS1.3": "",
          "EnableNTLMV1ForWmi": "",
          "EnablePublisherFailover": "",
          "EnableTelemetry": "",
          "ExpiredGuestAccountsCleanupInterval": 0,
          "ExtensionsAutoUpgradesFlag": "",
          "FreeDiskSpaceThreshold": 0,
          "FreeMemoryThreshold": 0,
          "ICMPv6Filters": "",
          "IgnoreConflictNetworkBootAgents": "",
          "InformationStoredCleanupInterval": 0,
          "KnownEndpointsCleanupInterval": 0,
          "LoginBannerText": "",
          "NetflowReprofileInterval": 0,
          "NotificationEmailAddress": "",
          "NotificationSmsAddress": "",
          "OnGuardAutoUpdatesFlag": "",
          "PasswordPrompt": "",
          "PolicyResultCacheTimeout": 0,
          "PostAuthUnsubscribeEndpoints": "",
          "PostAuthV2": "",
          "PostAuthV2HttpEnforcement": "",
          "ProcessWiredFromIfMap": "",
          "ProfiledKnownEndpointsCleanupOption": "",
          "ProfiledUnknownEndpointsCleanupInterval": 0,
          "ProfilerConflictStrictMode": "",
          "ProfilerNmapEnable": "",
          "ProfilerPostureEnable": "",
          "ProfilerScanPorts": "",
          "ProfilerSubnetScanInterval": 0,
          "ProfilingAutoUpdatesFlag": "",
          "SSHCipherMode": "",
          "SessionLogsCleanupInterval": 0,
          "SoftwareAutoUpdatesFlag": "",
          "StaleTLSsessioninDiskclenaup": 0,
          "StandbyFailoverWaitTime": 0,
          "StaticIPEndpointsCleanupOption": "",
          "StorePasswordHash": "",
          "StoreReversibleLocalUserPasswords": "",
          "SyslogBatchInterval": 0,
          "SystemAlertLevel": "",
          "TacacsAllowUnencryptedCommunication": "",
          "TacacsDisableChangePassword": "",
          "TacacsIdleTimeout": 0,
          "TacacsProcessUnauthenticatedRequest": "",
          "UnknownEndpointsCleanupInterval": 0,
          "UserPrompt": "",
          "allowConcurrentLogin": "",
          "session_cache_type": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ClusterWideParameter {AdminSessionIdleTimeout (integer, optional): Admin Session Idle Timeout in minutes,AdminUserLoginRemoteTacacsServerIP (string, optional): Remote TACACS+ server for Admin logins,AdminUserLoginRemoteTacacsServerPort (integer, optional): Admin UI Login Remote TACACS+ Server Port,AdminUserLoginRemoteTacacsServerSecret (string, optional): Remote TACACS+ server shared secret,AdminUserLoginSecondaryRemoteTacacsServerIP (string, optional),AdminUserLoginSecondaryRemoteTacacsServerPort (integer, optional),AdminUserLoginSecondaryRemoteTacacsServerSecret (string, optional),AdminUserLoginTacacsClientIpSetByHeaderXFF (string, optional) = ['TRUE' or 'FALSE']: Enable Admin UI TACACS+ Client IP set by X-Forwarded-For (XFF) header,AdminUserLoginTertiaryRemoteTacacsServerIP (string, optional),AdminUserLoginTertiaryRemoteTacacsServerPort (integer, optional),AdminUserLoginTertiaryRemoteTacacsServerSecret (string, optional),AlertNotificationTimeout (string, optional) = ['1' or '2' or '4' or '6' or '8' or '12' or '24' or 'Disabled']: Alert Notification Timeout in hours,AuditRecordsCleanupInterval (integer, optional): Old Audit Records cleanup interval in days,AutoBackupConfigOptions (string, optional) = ['Off' or 'Config' or 'Config|SessionInfo']: Auto backup configuration options,CLISessionIdleTimeout (integer, optional): CLI Session Idle Timeout in minutes,CSRCleanupInterval (integer, optional): Cleanup interval for CSRs and private keys,ClearPassZoneCache (string, optional) = ['OFF' or 'NORMAL' or 'FULL']: ClearPass Zone Cache Durability,ClusterCommunicationMode (string, optional) = ['ipv4' or 'ipv6']: Mode of communication between cluster nodes,CommonCriteriaMode (string, optional) = ['TRUE' or 'FALSE']: Enable Common Criteria mode for the cluster,ConsoleSessionIdleTimeout (integer, optional): Console Session Idle Timeout in minutes,ContentSecurityPolicy (string, optional) = ['Enable' or 'Disable']: Enable Content Security Policy (CSP),ContextServerPollInterval (integer, optional): Endpoint Context Servers polling interval in minutes,ContextServerPollStartTime (string, optional): [00:00:00-23:59:59] Endpoint Context Servers polling start time,DbAppexternalUserPassword (string, optional): Database user "appexternal" password,DesignatedStandbyPublisher (string, optional): Designated Standby Publisher,DisableTLS1.0 (string, optional) = ['None' or 'Admin' or 'Network' or 'All']: Disable TLSv1.0 support,DisableTLS1.1 (string, optional) = ['None' or 'Admin' or 'Network' or 'All']: Disable TLSv1.1 support,DisableTLS1.3 (string, optional) = ['None' or 'Admin'],EnableNTLMV1ForWmi (string, optional) = ['TRUE' or 'FALSE']: Enable NTLMV1 for WMI scans,EnablePublisherFailover (string, optional) = ['TRUE' or 'FALSE']: Enable Publisher Failover,EnableTelemetry (string, optional) = ['TRUE' or 'FALSE']: Enable sharing information about the cluster to Telemetry server,ExpiredGuestAccountsCleanupInterval (integer, optional): Expired guest accounts cleanup interval in days,ExtensionsAutoUpgradesFlag (string, optional) = ['TRUE' or 'FALSE'],FreeDiskSpaceThreshold (integer, optional): Free disk space threshold value in %,FreeMemoryThreshold (integer, optional): Free memory threshold value in %,ICMPv6Filters (string, optional) = ['Enable' or 'Disable']: Enable ICMPv6 Filters,IgnoreConflictNetworkBootAgents (string, optional) = ['TRUE' or 'FALSE']: Enable Ignore Conflict (Network Boot Agents),InformationStoredCleanupInterval (integer, optional): Cleanup interval for information stored on the disk in days,KnownEndpointsCleanupInterval (integer, optional): Known endpoints cleanup interval in days,LoginBannerText (string, optional): Login Banner Text,NetflowReprofileInterval (integer, optional): Netflow reprofile interval in days,NotificationEmailAddress (string, optional): Alert Notification - Email Address,NotificationSmsAddress (string, optional): Alert Notification - SMS Address,OnGuardAutoUpdatesFlag (string, optional) = ['TRUE' or 'FALSE']: Automatically check for available OnGuard Signature Updates,PasswordPrompt (string, optional): TACACS+ Password Prompt Text,PolicyResultCacheTimeout (integer, optional): Policy result cache timeout in minutes,PostAuthUnsubscribeEndpoints (string, optional) = ['Enable' or 'Disable'],PostAuthV2 (string, optional) = ['Enable' or 'Disable']: Enable Post-Auth v2,PostAuthV2HttpEnforcement (string, optional) = ['Enable' or 'Disable']: Enable Post-Auth v2 HTTP enforcement,ProcessWiredFromIfMap (string, optional) = ['TRUE' or 'FALSE']: Process wired device information from IF-MAP interface,ProfiledKnownEndpointsCleanupOption (string, optional) = ['TRUE' or 'FALSE']: Profiled Known endpoints cleanup option in days,ProfiledUnknownEndpointsCleanupInterval (integer, optional): Profiled Unknown endpoints cleanup interval in days,ProfilerConflictStrictMode (string, optional) = ['high' or 'medium' or 'low']: Conflict Detection Strict Mode,ProfilerNmapEnable (string, optional) = ['TRUE' or 'FALSE']: Enable endpoint port scan using Nmap,ProfilerPostureEnable (string, optional) = ['TRUE' or 'FALSE']: Enable Endpoint scan using WMI,ProfilerScanPorts (string, optional): Profiler Scan TCP Ports,ProfilerSubnetScanInterval (integer, optional): Profiler subnet scan interval in hours,ProfilingAutoUpdatesFlag (string, optional) = ['TRUE' or 'FALSE']: Automatically check for available Profiling Updates,SSHCipherMode (string, optional): Allowed SSH Cipher Modes,SessionLogsCleanupInterval (integer, optional): Cleanup interval for Session log details in the database in days,SoftwareAutoUpdatesFlag (string, optional) = ['TRUE' or 'FALSE']: Automatically check for available Software Updates,StaleTLSsessioninDiskclenaup (integer, optional),StandbyFailoverWaitTime (integer, optional): Failover Wait Time in minutes,StaticIPEndpointsCleanupOption (string, optional) = ['TRUE' or 'FALSE']: Static IP endpoints cleanup option,StorePasswordHash (string, optional) = ['TRUE' or 'FALSE']: Store Password Hash for MSCHAP authentication,StoreReversibleLocalUserPasswords (string, optional) = ['TRUE' or 'FALSE']: Store Local User passwords using reversible encryption,SyslogBatchInterval (integer, optional): Syslog Export Interval in seconds,SystemAlertLevel (string, optional) = ['INFO' or 'WARN' or 'ERROR']: System Alert Level,TacacsAllowUnencryptedCommunication (string, optional) = ['Enable' or 'Disable']: Enable TACACS+ clients to communicate with ClearPass server over an unencrypted channel,TacacsDisableChangePassword (string, optional) = ['TRUE' or 'FALSE']: Disable Change Password for TACACS+,TacacsIdleTimeout (integer, optional): TACACS+ Connection Idle Timeout in seconds,TacacsProcessUnauthenticatedRequest (string, optional) = ['Enable' or 'Disable']: Enable unauthenticated TACACS+ user request processing,UnknownEndpointsCleanupInterval (integer, optional): Unknown endpoints cleanup interval in days,UserPrompt (string, optional): TACACS+ User Prompt Text,allowConcurrentLogin (string, optional) = ['TRUE' or 'FALSE']: Enable Concurrent Admin Login,session_cache_type (string, optional) = ['Internal' or 'Internal+Disk']}
                Required Body Parameters (type(dict) body example)- {
          "AdminSessionIdleTimeout": 0,
          "AdminUserLoginRemoteTacacsServerIP": "",
          "AdminUserLoginRemoteTacacsServerPort": 0,
          "AdminUserLoginRemoteTacacsServerSecret": "",
          "AdminUserLoginSecondaryRemoteTacacsServerIP": "",
          "AdminUserLoginSecondaryRemoteTacacsServerPort": 0,
          "AdminUserLoginSecondaryRemoteTacacsServerSecret": "",
          "AdminUserLoginTacacsClientIpSetByHeaderXFF": "",
          "AdminUserLoginTertiaryRemoteTacacsServerIP": "",
          "AdminUserLoginTertiaryRemoteTacacsServerPort": 0,
          "AdminUserLoginTertiaryRemoteTacacsServerSecret": "",
          "AlertNotificationTimeout": "",
          "AuditRecordsCleanupInterval": 0,
          "AutoBackupConfigOptions": "",
          "CLISessionIdleTimeout": 0,
          "CSRCleanupInterval": 0,
          "ClearPassZoneCache": "",
          "ClusterCommunicationMode": "",
          "CommonCriteriaMode": "",
          "ConsoleSessionIdleTimeout": 0,
          "ContentSecurityPolicy": "",
          "ContextServerPollInterval": 0,
          "ContextServerPollStartTime": "",
          "DbAppexternalUserPassword": "",
          "DesignatedStandbyPublisher": "",
          "DisableTLS1.0": "",
          "DisableTLS1.1": "",
          "DisableTLS1.3": "",
          "EnableNTLMV1ForWmi": "",
          "EnablePublisherFailover": "",
          "EnableTelemetry": "",
          "ExpiredGuestAccountsCleanupInterval": 0,
          "ExtensionsAutoUpgradesFlag": "",
          "FreeDiskSpaceThreshold": 0,
          "FreeMemoryThreshold": 0,
          "ICMPv6Filters": "",
          "IgnoreConflictNetworkBootAgents": "",
          "InformationStoredCleanupInterval": 0,
          "KnownEndpointsCleanupInterval": 0,
          "LoginBannerText": "",
          "NetflowReprofileInterval": 0,
          "NotificationEmailAddress": "",
          "NotificationSmsAddress": "",
          "OnGuardAutoUpdatesFlag": "",
          "PasswordPrompt": "",
          "PolicyResultCacheTimeout": 0,
          "PostAuthUnsubscribeEndpoints": "",
          "PostAuthV2": "",
          "PostAuthV2HttpEnforcement": "",
          "ProcessWiredFromIfMap": "",
          "ProfiledKnownEndpointsCleanupOption": "",
          "ProfiledUnknownEndpointsCleanupInterval": 0,
          "ProfilerConflictStrictMode": "",
          "ProfilerNmapEnable": "",
          "ProfilerPostureEnable": "",
          "ProfilerScanPorts": "",
          "ProfilerSubnetScanInterval": 0,
          "ProfilingAutoUpdatesFlag": "",
          "SSHCipherMode": "",
          "SessionLogsCleanupInterval": 0,
          "SoftwareAutoUpdatesFlag": "",
          "StaleTLSsessioninDiskclenaup": 0,
          "StandbyFailoverWaitTime": 0,
          "StaticIPEndpointsCleanupOption": "",
          "StorePasswordHash": "",
          "StoreReversibleLocalUserPasswords": "",
          "SyslogBatchInterval": 0,
          "SystemAlertLevel": "",
          "TacacsAllowUnencryptedCommunication": "",
          "TacacsDisableChangePassword": "",
          "TacacsIdleTimeout": 0,
          "TacacsProcessUnauthenticatedRequest": "",
          "UnknownEndpointsCleanupInterval": 0,
          "UserPrompt": "",
          "allowConcurrentLogin": "",
          "session_cache_type": ""
        }
        """
        url_path = "/cluster/parameters"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # Function Section Name:DataFilter
    # Function Section Description: Manage data filters

    def get_data_filter(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of data filters
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- DataFilterCreate {name (string): Name of the Data Filter,description (string, optional): Description of the Data Filter,type (string): Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT,attr_type (string, optional): Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING,configuration_type (string) = ['custom_sql' or 'attribute_rules']: Configuration type of the Data Filter,template (string, optional): Template name for Data Filter (applicable when type=INSIGHT),custom_sql (string, optional): Custom SQL of the Data Filter,rule_eval_algo (string, optional) = ['evaluate-all' or 'first-applicable']: Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes,rules (RulesSettingsCreate, optional): List of Rules for Data Filter, applicable only for attributes}RulesSettingsCreate {match_type (string) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,condition (RulesConditionSettingsCreate): Conditions of data filter attribute rules}RulesConditionSettingsCreate {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "attr_type": "",
          "configuration_type": "",
          "template": "",
          "custom_sql": "",
          "rule_eval_algo": "",
          "rules": {
            "match_type": "",
            "condition": {
              "type": "",
              "name": "",
              "oper": "",
              "value": ""
            }
          }
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: data_filter_id, Description: Numeric ID of the Data Filter
        """
        url_path = "/data-filter/{data_filter_id}"
        dict_path = {"data_filter_id": data_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_data_filter_by_data_filter_id(self, data_filter_id="", body=({})):
        """
                Operation: Update a data filter
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: data_filter_id, Description: Numeric ID of the Data Filter
                Required Body Parameters (body description)- DataFilterUpdate {name (string, optional): Name of the Data Filter,description (string, optional): Description of the Data Filter,type (string, optional): Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT,attr_type (string, optional): Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING,configuration_type (string, optional) = ['custom_sql' or 'attribute_rules']: Configuration type of the Data Filter,template (string, optional): Template name for Data Filter (applicable when type=INSIGHT),custom_sql (string, optional): Custom SQL of the Data Filter,rule_eval_algo (string, optional) = ['evaluate-all' or 'first-applicable']: Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes,rules (RulesSettingsUpdate, optional): List of Rules for Data Filter, applicable only for attributes}RulesSettingsUpdate {match_type (string, optional) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,condition (RulesConditionSettingsUpdate, optional): Conditions of data filter attribute rules}RulesConditionSettingsUpdate {type (string, optional): Condition type,name (string, optional): Condition name,oper (string, optional): Condition operator,value (string, optional): Condition value}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "attr_type": "",
          "configuration_type": "",
          "template": "",
          "custom_sql": "",
          "rule_eval_algo": "",
          "rules": {
            "match_type": "",
            "condition": {
              "type": "",
              "name": "",
              "oper": "",
              "value": ""
            }
          }
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: data_filter_id, Description: Numeric ID of the Data Filter
                Required Body Parameters (body description)- DataFilterReplace {name (string): Name of the Data Filter,description (string, optional): Description of the Data Filter,type (string): Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT,attr_type (string, optional): Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING,configuration_type (string) = ['custom_sql' or 'attribute_rules']: Configuration type of the Data Filter,template (string, optional): Template name for Data Filter (applicable when type=INSIGHT),custom_sql (string, optional): Custom SQL of the Data Filter,rule_eval_algo (string, optional) = ['evaluate-all' or 'first-applicable']: Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes,rules (RulesSettingsReplace, optional): List of Rules for Data Filter, applicable only for attributes}RulesSettingsReplace {match_type (string) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,condition (RulesConditionSettingsReplace): Conditions of data filter attribute rules}RulesConditionSettingsReplace {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "attr_type": "",
          "configuration_type": "",
          "template": "",
          "custom_sql": "",
          "rule_eval_algo": "",
          "rules": {
            "match_type": "",
            "condition": {
              "type": "",
              "name": "",
              "oper": "",
              "value": ""
            }
          }
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: data_filter_id, Description: Numeric ID of the Data Filter
        """
        url_path = "/data-filter/{data_filter_id}"
        dict_path = {"data_filter_id": data_filter_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_data_filter_name_by_name(self, name=""):
        """
        Operation: Get a data filter by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the data filter
        """
        url_path = "/data-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_data_filter_name_by_name(self, name="", body=({})):
        """
                Operation: Update a data filter by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the data filter
                Required Body Parameters (body description)- DataFilterUpdate {name (string, optional): Name of the Data Filter,description (string, optional): Description of the Data Filter,type (string, optional): Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT,attr_type (string, optional): Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING,configuration_type (string, optional) = ['custom_sql' or 'attribute_rules']: Configuration type of the Data Filter,template (string, optional): Template name for Data Filter (applicable when type=INSIGHT),custom_sql (string, optional): Custom SQL of the Data Filter,rule_eval_algo (string, optional) = ['evaluate-all' or 'first-applicable']: Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes,rules (RulesSettingsUpdate, optional): List of Rules for Data Filter, applicable only for attributes}RulesSettingsUpdate {match_type (string, optional) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,condition (RulesConditionSettingsUpdate, optional): Conditions of data filter attribute rules}RulesConditionSettingsUpdate {type (string, optional): Condition type,name (string, optional): Condition name,oper (string, optional): Condition operator,value (string, optional): Condition value}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "attr_type": "",
          "configuration_type": "",
          "template": "",
          "custom_sql": "",
          "rule_eval_algo": "",
          "rules": {
            "match_type": "",
            "condition": {
              "type": "",
              "name": "",
              "oper": "",
              "value": ""
            }
          }
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the data filter
                Required Body Parameters (body description)- DataFilterReplace {name (string): Name of the Data Filter,description (string, optional): Description of the Data Filter,type (string): Type of the Data Filter. i.e. SESSION or ACCOUNTING or INSIGHT,attr_type (string, optional): Attribute type (RADIUS/TACACS+/Any) of the Data Filter. Required only when type is ACCOUNTING,configuration_type (string) = ['custom_sql' or 'attribute_rules']: Configuration type of the Data Filter,template (string, optional): Template name for Data Filter (applicable when type=INSIGHT),custom_sql (string, optional): Custom SQL of the Data Filter,rule_eval_algo (string, optional) = ['evaluate-all' or 'first-applicable']: Rule Evaluation Algorithm for rules of Data Filter, applicable only for attributes,rules (RulesSettingsReplace, optional): List of Rules for Data Filter, applicable only for attributes}RulesSettingsReplace {match_type (string) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,condition (RulesConditionSettingsReplace): Conditions of data filter attribute rules}RulesConditionSettingsReplace {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "attr_type": "",
          "configuration_type": "",
          "template": "",
          "custom_sql": "",
          "rule_eval_algo": "",
          "rules": {
            "match_type": "",
            "condition": {
              "type": "",
              "name": "",
              "oper": "",
              "value": ""
            }
          }
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the data filter
        """
        url_path = "/data-filter/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:FileBackupServer
    # Function Section Description: Manage file backup server

    def get_file_backup_server(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of file backup server
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- FileBackupServerCreate {host_address (string): Server host address of file backup server,description (string, optional): Description of file backup server,protocol (string) = ['SFTP' or 'SCP' or 'NFS 3' or 'NFS 4']: Protocol for file backup server,port (integer): Port for file backup server,username (string): Username of file backup server,password (string): Password for file backup server,time_out (integer): Timeout for file backup server ,remote_dir (string): Remote directory for file backup server,cppm_servers (array[string], optional): ClearPass server UUID List for file backup server}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "protocol": "",
          "port": 0,
          "username": "",
          "password": "",
          "time_out": 0,
          "remote_dir": "",
          "cppm_servers": [
            ""
          ]
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
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
                Required Body Parameters (body description)- FileBackupServerUpdate {host_address (string, optional): Server host address of file backup server,description (string, optional): Description of file backup server,protocol (string, optional) = ['SFTP' or 'SCP' or 'NFS 3' or 'NFS 4']: Protocol for file backup server,port (integer, optional): Port for file backup server,username (string, optional): Username of file backup server,password (string, optional): Password for file backup server,time_out (integer, optional): Timeout for file backup server ,remote_dir (string, optional): Remote directory for file backup server,cppm_servers (array[string], optional): ClearPass server UUID List for file backup server}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "protocol": "",
          "port": 0,
          "username": "",
          "password": "",
          "time_out": 0,
          "remote_dir": "",
          "cppm_servers": [
            ""
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
                Required Body Parameters (body description)- FileBackupServerReplace {host_address (string): Server host address of file backup server,description (string, optional): Description of file backup server,protocol (string) = ['SFTP' or 'SCP' or 'NFS 3' or 'NFS 4']: Protocol for file backup server,port (integer): Port for file backup server,username (string): Username of file backup server,password (string): Password for file backup server,time_out (integer): Timeout for file backup server ,remote_dir (string): Remote directory for file backup server,cppm_servers (array[string], optional): ClearPass server UUID List for file backup server}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "protocol": "",
          "port": 0,
          "username": "",
          "password": "",
          "time_out": 0,
          "remote_dir": "",
          "cppm_servers": [
            ""
          ]
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
        Operation: Delete a syslog export filter
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: file_backup_server_id, Description: Numeric ID of the file-backup-server
        """
        url_path = "/file-backup-server/{file_backup_server_id}"
        dict_path = {"file_backup_server_id": file_backup_server_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_file_backup_server_host_address_by_host_address(self, host_address=""):
        """
        Operation: Get a file backup server by host_address
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: host_address, Description: Unique host_address of the file-backup-server
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: host_address, Description: Unique host_address of the file-backup-server
                Required Body Parameters (body description)- FileBackupServerUpdate {host_address (string, optional): Server host address of file backup server,description (string, optional): Description of file backup server,protocol (string, optional) = ['SFTP' or 'SCP' or 'NFS 3' or 'NFS 4']: Protocol for file backup server,port (integer, optional): Port for file backup server,username (string, optional): Username of file backup server,password (string, optional): Password for file backup server,time_out (integer, optional): Timeout for file backup server ,remote_dir (string, optional): Remote directory for file backup server,cppm_servers (array[string], optional): ClearPass server UUID List for file backup server}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "protocol": "",
          "port": 0,
          "username": "",
          "password": "",
          "time_out": 0,
          "remote_dir": "",
          "cppm_servers": [
            ""
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: host_address, Description: Unique host_address of the file-backup-server
                Required Body Parameters (body description)- FileBackupServerReplace {host_address (string): Server host address of file backup server,description (string, optional): Description of file backup server,protocol (string) = ['SFTP' or 'SCP' or 'NFS 3' or 'NFS 4']: Protocol for file backup server,port (integer): Port for file backup server,username (string): Username of file backup server,password (string): Password for file backup server,time_out (integer): Timeout for file backup server ,remote_dir (string): Remote directory for file backup server,cppm_servers (array[string], optional): ClearPass server UUID List for file backup server}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "protocol": "",
          "port": 0,
          "username": "",
          "password": "",
          "time_out": 0,
          "remote_dir": "",
          "cppm_servers": [
            ""
          ]
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
        Operation: Delete a syslog export filter by host_address
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: host_address, Description: Unique host_address of the file-backup-server
        """
        url_path = "/file-backup-server/host-address/{host_address}"
        dict_path = {"host_address": host_address}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:ListAllPrivileges
    # Function Section Description: Returns the list of system-defined privileges

    def get_oauth_all_privileges(self, format=""):
        """
        Operation: Returns the list of system-defined privileges
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: format, Description: list: List of all privileges by nametree: List of all domains, each containing features
        """
        url_path = "/oauth/all-privileges"
        dict_query = {"format": format}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:LocalUserPasswordPolicy
    # Function Section Description: Manage local user password policies

    def get_local_user_password_policy(self, format=""):
        """
        Operation: Get the local user password policy
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Optional Query Parameter Name: format, Description: list: List of all privileges by nametree: List of all domains, each containing features
        """
        url_path = "/local-user/password-policy"
        dict_query = {"format": format}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_local_user_password_policy(self, body=({})):
        """
                Operation: Put the local user password policy
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- LocalUserPasswordPolicyReplace {password_minimum_length (integer) = ['1-128']: Minimum length of the password,password_complexity (string) = ['NONE' or 'CASE' or 'NUMBER' or 'ALPHANUMERIC' or 'CASENUMERIC' or 'PUNCTUATION' or 'COMPLEX']: Complexity Level of the password,password_disallowed_characters (string, optional): Disallowed characters in the password,password_disallowed_words (string, optional): Disallowed words in the password,password_prohibit_user_id (boolean, optional): May not contain User ID or its characters in reversed order,password_prohibit_repeated_chars (boolean, optional): May not contain repeated character four or more times consecutively,password_expiry_days (integer, optional) = ['0-500']: Password expiry days,password_remember_history (integer, optional) = ['1-99']: Must be different from this many previous passwords,reminder_days (integer, optional) = ['1-365']: Display reminder message after this many days,reminder_message (string, optional): Reminder message to be displayed,disable_after_days (integer, optional) = ['1-1000']: Disable after Days Exceed,disable_after_date (string, optional) = ['yyyy-mm-dd']: Disable after Date Exceeds,disable_after_unchanged_days (integer, optional) = ['1-365']: Disable after password not changed after this many days,disable_after_failed_attempts (integer, optional) = ['1-100']: Failed attempts count,reset_failed_attempts_count (boolean, optional): Reset failed attempts count and enable those users}
                Required Body Parameters (type(dict) body example)- {
          "password_minimum_length": 0,
          "password_complexity": "",
          "password_disallowed_characters": "",
          "password_disallowed_words": "",
          "password_prohibit_user_id": false,
          "password_prohibit_repeated_chars": false,
          "password_expiry_days": 0,
          "password_remember_history": 0,
          "reminder_days": 0,
          "reminder_message": "",
          "disable_after_days": 0,
          "disable_after_date": "",
          "disable_after_unchanged_days": 0,
          "disable_after_failed_attempts": 0,
          "reset_failed_attempts_count": false
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- LocalUserPasswordPolicyUpdate {password_minimum_length (integer, optional) = ['1-128']: Minimum length of the password,password_complexity (string, optional) = ['NONE' or 'CASE' or 'NUMBER' or 'ALPHANUMERIC' or 'CASENUMERIC' or 'PUNCTUATION' or 'COMPLEX']: Complexity Level of the password,password_disallowed_characters (string, optional): Disallowed characters in the password,password_disallowed_words (string, optional): Disallowed words in the password,password_prohibit_user_id (boolean, optional): May not contain User ID or its characters in reversed order,password_prohibit_repeated_chars (boolean, optional): May not contain repeated character four or more times consecutively,password_expiry_days (integer, optional) = ['0-500']: Password expiry days,password_remember_history (integer, optional) = ['1-99']: Must be different from this many previous passwords,reminder_days (integer, optional) = ['1-365']: Display reminder message after this many days,reminder_message (string, optional): Reminder message to be displayed,disable_after_days (integer, optional) = ['1-1000']: Disable after Days Exceed,disable_after_date (string, optional) = ['yyyy-mm-dd']: Disable after Date Exceeds,disable_after_unchanged_days (integer, optional) = ['1-365']: Disable after password not changed after this many days,disable_after_failed_attempts (integer, optional) = ['1-100']: Failed attempts count,reset_failed_attempts_count (boolean, optional): Reset failed attempts count and enable those users}
                Required Body Parameters (type(dict) body example)- {
          "password_minimum_length": 0,
          "password_complexity": "",
          "password_disallowed_characters": "",
          "password_disallowed_words": "",
          "password_prohibit_user_id": false,
          "password_prohibit_repeated_chars": false,
          "password_expiry_days": 0,
          "password_remember_history": 0,
          "reminder_days": 0,
          "reminder_message": "",
          "disable_after_days": 0,
          "disable_after_date": "",
          "disable_after_unchanged_days": 0,
          "disable_after_failed_attempts": 0,
          "reset_failed_attempts_count": false
        }
        """
        url_path = "/local-user/password-policy"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # Function Section Name:MessagingSetup
    # Function Section Description: Operations for MessagingSetup

    def get_messaging_setup(self, body=({})):
        """
                Operation: GET Messaging setup
                HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- LocalUserPasswordPolicyUpdate {password_minimum_length (integer, optional) = ['1-128']: Minimum length of the password,password_complexity (string, optional) = ['NONE' or 'CASE' or 'NUMBER' or 'ALPHANUMERIC' or 'CASENUMERIC' or 'PUNCTUATION' or 'COMPLEX']: Complexity Level of the password,password_disallowed_characters (string, optional): Disallowed characters in the password,password_disallowed_words (string, optional): Disallowed words in the password,password_prohibit_user_id (boolean, optional): May not contain User ID or its characters in reversed order,password_prohibit_repeated_chars (boolean, optional): May not contain repeated character four or more times consecutively,password_expiry_days (integer, optional) = ['0-500']: Password expiry days,password_remember_history (integer, optional) = ['1-99']: Must be different from this many previous passwords,reminder_days (integer, optional) = ['1-365']: Display reminder message after this many days,reminder_message (string, optional): Reminder message to be displayed,disable_after_days (integer, optional) = ['1-1000']: Disable after Days Exceed,disable_after_date (string, optional) = ['yyyy-mm-dd']: Disable after Date Exceeds,disable_after_unchanged_days (integer, optional) = ['1-365']: Disable after password not changed after this many days,disable_after_failed_attempts (integer, optional) = ['1-100']: Failed attempts count,reset_failed_attempts_count (boolean, optional): Reset failed attempts count and enable those users}
                Required Body Parameters (type(dict) body example)- {
          "password_minimum_length": 0,
          "password_complexity": "",
          "password_disallowed_characters": "",
          "password_disallowed_words": "",
          "password_prohibit_user_id": false,
          "password_prohibit_repeated_chars": false,
          "password_expiry_days": 0,
          "password_remember_history": 0,
          "reminder_days": 0,
          "reminder_message": "",
          "disable_after_days": 0,
          "disable_after_date": "",
          "disable_after_unchanged_days": 0,
          "disable_after_failed_attempts": 0,
          "reset_failed_attempts_count": false
        }
        """
        url_path = "/messaging-setup"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def new_messaging_setup(self, body=({})):
        """
                Operation: Configure Messaging setup
                HTTP Status Response Codes: 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- MessagingSetupCreate {server_name (string): SMTP Server Name,user_name (string, optional): Username,password (string, optional): Password,default_from_address (string): Default FROM Address,connection_security (string, optional) = ['ssl' or 'startTLS' or 'none']: Connection Security,port (int, optional): Port Number,connection_timeout (int, optional): Connection Timeout }
                Required Body Parameters (type(dict) body example)- {
          "server_name": "",
          "user_name": "",
          "password": "",
          "default_from_address": "",
          "connection_security": "",
          "port": "int",
          "connection_timeout": "int"
        }
        """
        url_path = "/messaging-setup"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def delete_messaging_setup(self, body=({})):
        """
                Operation: Reset Messaging setup configuration
                HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- MessagingSetupCreate {server_name (string): SMTP Server Name,user_name (string, optional): Username,password (string, optional): Password,default_from_address (string): Default FROM Address,connection_security (string, optional) = ['ssl' or 'startTLS' or 'none']: Connection Security,port (int, optional): Port Number,connection_timeout (int, optional): Connection Timeout }
                Required Body Parameters (type(dict) body example)- {
          "server_name": "",
          "user_name": "",
          "password": "",
          "default_from_address": "",
          "connection_security": "",
          "port": "int",
          "connection_timeout": "int"
        }
        """
        url_path = "/messaging-setup"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="delete", query=body
        )

    # Function Section Name:OperatorProfile
    # Function Section Description: Manage operator profiles

    def get_operator_profile(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of operator profiles
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OperatorProfile {id (integer, optional),name (string): Enter a name for this operator profile,comment (string, optional): Comments or descriptive text about the operator profile,enabled (boolean, optional): If unchecked, operators with this profile will not be able to log in,privileges (array[string], optional): Select the privileges that will be granted to this operator login,user_dbs_list (string, optional): Select the visitor account roles that these operators are permitted to use,sponsor_filter (string): Select the default operator filtering to apply to guest accounts,filter_useraccount (string, optional): Enter a comma-delimited list of field=value pairs to create an account filter,filter_radacct (string, optional): Enter a comma-delimited list of field=value pairs to create a session filter,max_users (string, optional): Maximum number of guests the operator can create.
        Leave blank for no limit,max_devices (string, optional): Maximum number of devices the operator can create.
        Leave blank for no limit,userskin (string, optional): Choose the skin to use for operators with this profile,userskin_name (string, optional),start_page (string, optional): The initial page to show this operator after logging in,lang (string, optional): Select the default language to use for operators with this profile,timezone_id (string, optional): Select the default time zone for operators with this profile,override_ui (boolean, optional): If checked, you can specify different default forms and views to use,override_guest_sessions (string, optional): Override the Active Sessions view,override_change_expiration (string, optional): Override the Change Expiration form,override_create_multi_result (string, optional): Override the Create Multiple Accounts Results form,override_create_multi (string, optional): Override the Create Multiple Guest Accounts form,override_mac_create (string, optional): Override the Create New Device form,override_mac_create_receipt (string, optional): Override the Create New Device Receipt form,override_create_user (string, optional): Override the Create New Guest Account form,override_create_user_receipt (string, optional): Override the Create New Guest Account Receipt form,override_guest_edit (string, optional): Override the Edit Account form,override_guest_multi (string, optional): Override the Edit Accounts view,override_mac_edit (string, optional): Override the Edit Device form,override_mac_multi (string, optional): Override the Edit Devices view,override_guest_multi_form (string, optional): Override the Edit Guest Accounts form,override_mac_multi_form (string, optional): Override the Edit Guest Devices form,override_guest_multi_result (string, optional): Override the Edit Multiple Accounts Results form,override_mac_multi_result (string, optional): Override the Edit Multiple Devices Results form,override_mac_export (string, optional): Override the Export Devices view,override_guest_export (string, optional): Override the Export Guest Accounts view,override_mac_list (string, optional): Override the Manage Devices view,override_guest_users (string, optional): Override the Manage Guest Accounts view,override_guest_edit_receipt (string, optional): Override the Updated Account Details form,override_mac_edit_receipt (string, optional): Override the Updated Device Details form}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "comment": "",
          "enabled": false,
          "privileges": [
            ""
          ],
          "user_dbs_list": "",
          "sponsor_filter": "",
          "filter_useraccount": "",
          "filter_radacct": "",
          "max_users": "",
          "max_devices": "",
          "userskin": "",
          "userskin_name": "",
          "start_page": "",
          "lang": "",
          "timezone_id": "",
          "override_ui": false,
          "override_guest_sessions": "",
          "override_change_expiration": "",
          "override_create_multi_result": "",
          "override_create_multi": "",
          "override_mac_create": "",
          "override_mac_create_receipt": "",
          "override_create_user": "",
          "override_create_user_receipt": "",
          "override_guest_edit": "",
          "override_guest_multi": "",
          "override_mac_edit": "",
          "override_mac_multi": "",
          "override_guest_multi_form": "",
          "override_mac_multi_form": "",
          "override_guest_multi_result": "",
          "override_mac_multi_result": "",
          "override_mac_export": "",
          "override_guest_export": "",
          "override_mac_list": "",
          "override_guest_users": "",
          "override_guest_edit_receipt": "",
          "override_mac_edit_receipt": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: Numeric ID of the operator profile
        """
        url_path = "/operator-profile/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_operator_profile_by_id(self, id="", body=({})):
        """
                Operation: Update an operator profile
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: Numeric ID of the operator profile
                Required Body Parameters (body description)- OperatorProfile {id (integer, optional),name (string): Enter a name for this operator profile,comment (string, optional): Comments or descriptive text about the operator profile,enabled (boolean, optional): If unchecked, operators with this profile will not be able to log in,privileges (array[string], optional): Select the privileges that will be granted to this operator login,user_dbs_list (string, optional): Select the visitor account roles that these operators are permitted to use,sponsor_filter (string): Select the default operator filtering to apply to guest accounts,filter_useraccount (string, optional): Enter a comma-delimited list of field=value pairs to create an account filter,filter_radacct (string, optional): Enter a comma-delimited list of field=value pairs to create a session filter,max_users (string, optional): Maximum number of guests the operator can create.
        Leave blank for no limit,max_devices (string, optional): Maximum number of devices the operator can create.
        Leave blank for no limit,userskin (string, optional): Choose the skin to use for operators with this profile,userskin_name (string, optional),start_page (string, optional): The initial page to show this operator after logging in,lang (string, optional): Select the default language to use for operators with this profile,timezone_id (string, optional): Select the default time zone for operators with this profile,override_ui (boolean, optional): If checked, you can specify different default forms and views to use,override_guest_sessions (string, optional): Override the Active Sessions view,override_change_expiration (string, optional): Override the Change Expiration form,override_create_multi_result (string, optional): Override the Create Multiple Accounts Results form,override_create_multi (string, optional): Override the Create Multiple Guest Accounts form,override_mac_create (string, optional): Override the Create New Device form,override_mac_create_receipt (string, optional): Override the Create New Device Receipt form,override_create_user (string, optional): Override the Create New Guest Account form,override_create_user_receipt (string, optional): Override the Create New Guest Account Receipt form,override_guest_edit (string, optional): Override the Edit Account form,override_guest_multi (string, optional): Override the Edit Accounts view,override_mac_edit (string, optional): Override the Edit Device form,override_mac_multi (string, optional): Override the Edit Devices view,override_guest_multi_form (string, optional): Override the Edit Guest Accounts form,override_mac_multi_form (string, optional): Override the Edit Guest Devices form,override_guest_multi_result (string, optional): Override the Edit Multiple Accounts Results form,override_mac_multi_result (string, optional): Override the Edit Multiple Devices Results form,override_mac_export (string, optional): Override the Export Devices view,override_guest_export (string, optional): Override the Export Guest Accounts view,override_mac_list (string, optional): Override the Manage Devices view,override_guest_users (string, optional): Override the Manage Guest Accounts view,override_guest_edit_receipt (string, optional): Override the Updated Account Details form,override_mac_edit_receipt (string, optional): Override the Updated Device Details form}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "comment": "",
          "enabled": false,
          "privileges": [
            ""
          ],
          "user_dbs_list": "",
          "sponsor_filter": "",
          "filter_useraccount": "",
          "filter_radacct": "",
          "max_users": "",
          "max_devices": "",
          "userskin": "",
          "userskin_name": "",
          "start_page": "",
          "lang": "",
          "timezone_id": "",
          "override_ui": false,
          "override_guest_sessions": "",
          "override_change_expiration": "",
          "override_create_multi_result": "",
          "override_create_multi": "",
          "override_mac_create": "",
          "override_mac_create_receipt": "",
          "override_create_user": "",
          "override_create_user_receipt": "",
          "override_guest_edit": "",
          "override_guest_multi": "",
          "override_mac_edit": "",
          "override_mac_multi": "",
          "override_guest_multi_form": "",
          "override_mac_multi_form": "",
          "override_guest_multi_result": "",
          "override_mac_multi_result": "",
          "override_mac_export": "",
          "override_guest_export": "",
          "override_mac_list": "",
          "override_guest_users": "",
          "override_guest_edit_receipt": "",
          "override_mac_edit_receipt": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: Numeric ID of the operator profile
                Required Body Parameters (body description)- OperatorProfile {id (integer, optional),name (string): Enter a name for this operator profile,comment (string, optional): Comments or descriptive text about the operator profile,enabled (boolean, optional): If unchecked, operators with this profile will not be able to log in,privileges (array[string], optional): Select the privileges that will be granted to this operator login,user_dbs_list (string, optional): Select the visitor account roles that these operators are permitted to use,sponsor_filter (string): Select the default operator filtering to apply to guest accounts,filter_useraccount (string, optional): Enter a comma-delimited list of field=value pairs to create an account filter,filter_radacct (string, optional): Enter a comma-delimited list of field=value pairs to create a session filter,max_users (string, optional): Maximum number of guests the operator can create.
        Leave blank for no limit,max_devices (string, optional): Maximum number of devices the operator can create.
        Leave blank for no limit,userskin (string, optional): Choose the skin to use for operators with this profile,userskin_name (string, optional),start_page (string, optional): The initial page to show this operator after logging in,lang (string, optional): Select the default language to use for operators with this profile,timezone_id (string, optional): Select the default time zone for operators with this profile,override_ui (boolean, optional): If checked, you can specify different default forms and views to use,override_guest_sessions (string, optional): Override the Active Sessions view,override_change_expiration (string, optional): Override the Change Expiration form,override_create_multi_result (string, optional): Override the Create Multiple Accounts Results form,override_create_multi (string, optional): Override the Create Multiple Guest Accounts form,override_mac_create (string, optional): Override the Create New Device form,override_mac_create_receipt (string, optional): Override the Create New Device Receipt form,override_create_user (string, optional): Override the Create New Guest Account form,override_create_user_receipt (string, optional): Override the Create New Guest Account Receipt form,override_guest_edit (string, optional): Override the Edit Account form,override_guest_multi (string, optional): Override the Edit Accounts view,override_mac_edit (string, optional): Override the Edit Device form,override_mac_multi (string, optional): Override the Edit Devices view,override_guest_multi_form (string, optional): Override the Edit Guest Accounts form,override_mac_multi_form (string, optional): Override the Edit Guest Devices form,override_guest_multi_result (string, optional): Override the Edit Multiple Accounts Results form,override_mac_multi_result (string, optional): Override the Edit Multiple Devices Results form,override_mac_export (string, optional): Override the Export Devices view,override_guest_export (string, optional): Override the Export Guest Accounts view,override_mac_list (string, optional): Override the Manage Devices view,override_guest_users (string, optional): Override the Manage Guest Accounts view,override_guest_edit_receipt (string, optional): Override the Updated Account Details form,override_mac_edit_receipt (string, optional): Override the Updated Device Details form}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "comment": "",
          "enabled": false,
          "privileges": [
            ""
          ],
          "user_dbs_list": "",
          "sponsor_filter": "",
          "filter_useraccount": "",
          "filter_radacct": "",
          "max_users": "",
          "max_devices": "",
          "userskin": "",
          "userskin_name": "",
          "start_page": "",
          "lang": "",
          "timezone_id": "",
          "override_ui": false,
          "override_guest_sessions": "",
          "override_change_expiration": "",
          "override_create_multi_result": "",
          "override_create_multi": "",
          "override_mac_create": "",
          "override_mac_create_receipt": "",
          "override_create_user": "",
          "override_create_user_receipt": "",
          "override_guest_edit": "",
          "override_guest_multi": "",
          "override_mac_edit": "",
          "override_mac_multi": "",
          "override_guest_multi_form": "",
          "override_mac_multi_form": "",
          "override_guest_multi_result": "",
          "override_mac_multi_result": "",
          "override_mac_export": "",
          "override_guest_export": "",
          "override_mac_list": "",
          "override_guest_users": "",
          "override_guest_edit_receipt": "",
          "override_mac_edit_receipt": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: Numeric ID of the operator profile
        """
        url_path = "/operator-profile/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_operator_profile_name_by_name(self, name=""):
        """
        Operation: Get an operator profile by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Name of the operator profile
        """
        url_path = "/operator-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_operator_profile_name_by_name(self, name="", body=({})):
        """
                Operation: Update an operator profile by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Name of the operator profile
                Required Body Parameters (body description)- OperatorProfile {id (integer, optional),name (string): Enter a name for this operator profile,comment (string, optional): Comments or descriptive text about the operator profile,enabled (boolean, optional): If unchecked, operators with this profile will not be able to log in,privileges (array[string], optional): Select the privileges that will be granted to this operator login,user_dbs_list (string, optional): Select the visitor account roles that these operators are permitted to use,sponsor_filter (string): Select the default operator filtering to apply to guest accounts,filter_useraccount (string, optional): Enter a comma-delimited list of field=value pairs to create an account filter,filter_radacct (string, optional): Enter a comma-delimited list of field=value pairs to create a session filter,max_users (string, optional): Maximum number of guests the operator can create.
        Leave blank for no limit,max_devices (string, optional): Maximum number of devices the operator can create.
        Leave blank for no limit,userskin (string, optional): Choose the skin to use for operators with this profile,userskin_name (string, optional),start_page (string, optional): The initial page to show this operator after logging in,lang (string, optional): Select the default language to use for operators with this profile,timezone_id (string, optional): Select the default time zone for operators with this profile,override_ui (boolean, optional): If checked, you can specify different default forms and views to use,override_guest_sessions (string, optional): Override the Active Sessions view,override_change_expiration (string, optional): Override the Change Expiration form,override_create_multi_result (string, optional): Override the Create Multiple Accounts Results form,override_create_multi (string, optional): Override the Create Multiple Guest Accounts form,override_mac_create (string, optional): Override the Create New Device form,override_mac_create_receipt (string, optional): Override the Create New Device Receipt form,override_create_user (string, optional): Override the Create New Guest Account form,override_create_user_receipt (string, optional): Override the Create New Guest Account Receipt form,override_guest_edit (string, optional): Override the Edit Account form,override_guest_multi (string, optional): Override the Edit Accounts view,override_mac_edit (string, optional): Override the Edit Device form,override_mac_multi (string, optional): Override the Edit Devices view,override_guest_multi_form (string, optional): Override the Edit Guest Accounts form,override_mac_multi_form (string, optional): Override the Edit Guest Devices form,override_guest_multi_result (string, optional): Override the Edit Multiple Accounts Results form,override_mac_multi_result (string, optional): Override the Edit Multiple Devices Results form,override_mac_export (string, optional): Override the Export Devices view,override_guest_export (string, optional): Override the Export Guest Accounts view,override_mac_list (string, optional): Override the Manage Devices view,override_guest_users (string, optional): Override the Manage Guest Accounts view,override_guest_edit_receipt (string, optional): Override the Updated Account Details form,override_mac_edit_receipt (string, optional): Override the Updated Device Details form}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "comment": "",
          "enabled": false,
          "privileges": [
            ""
          ],
          "user_dbs_list": "",
          "sponsor_filter": "",
          "filter_useraccount": "",
          "filter_radacct": "",
          "max_users": "",
          "max_devices": "",
          "userskin": "",
          "userskin_name": "",
          "start_page": "",
          "lang": "",
          "timezone_id": "",
          "override_ui": false,
          "override_guest_sessions": "",
          "override_change_expiration": "",
          "override_create_multi_result": "",
          "override_create_multi": "",
          "override_mac_create": "",
          "override_mac_create_receipt": "",
          "override_create_user": "",
          "override_create_user_receipt": "",
          "override_guest_edit": "",
          "override_guest_multi": "",
          "override_mac_edit": "",
          "override_mac_multi": "",
          "override_guest_multi_form": "",
          "override_mac_multi_form": "",
          "override_guest_multi_result": "",
          "override_mac_multi_result": "",
          "override_mac_export": "",
          "override_guest_export": "",
          "override_mac_list": "",
          "override_guest_users": "",
          "override_guest_edit_receipt": "",
          "override_mac_edit_receipt": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Name of the operator profile
                Required Body Parameters (body description)- OperatorProfile {id (integer, optional),name (string): Enter a name for this operator profile,comment (string, optional): Comments or descriptive text about the operator profile,enabled (boolean, optional): If unchecked, operators with this profile will not be able to log in,privileges (array[string], optional): Select the privileges that will be granted to this operator login,user_dbs_list (string, optional): Select the visitor account roles that these operators are permitted to use,sponsor_filter (string): Select the default operator filtering to apply to guest accounts,filter_useraccount (string, optional): Enter a comma-delimited list of field=value pairs to create an account filter,filter_radacct (string, optional): Enter a comma-delimited list of field=value pairs to create a session filter,max_users (string, optional): Maximum number of guests the operator can create.
        Leave blank for no limit,max_devices (string, optional): Maximum number of devices the operator can create.
        Leave blank for no limit,userskin (string, optional): Choose the skin to use for operators with this profile,userskin_name (string, optional),start_page (string, optional): The initial page to show this operator after logging in,lang (string, optional): Select the default language to use for operators with this profile,timezone_id (string, optional): Select the default time zone for operators with this profile,override_ui (boolean, optional): If checked, you can specify different default forms and views to use,override_guest_sessions (string, optional): Override the Active Sessions view,override_change_expiration (string, optional): Override the Change Expiration form,override_create_multi_result (string, optional): Override the Create Multiple Accounts Results form,override_create_multi (string, optional): Override the Create Multiple Guest Accounts form,override_mac_create (string, optional): Override the Create New Device form,override_mac_create_receipt (string, optional): Override the Create New Device Receipt form,override_create_user (string, optional): Override the Create New Guest Account form,override_create_user_receipt (string, optional): Override the Create New Guest Account Receipt form,override_guest_edit (string, optional): Override the Edit Account form,override_guest_multi (string, optional): Override the Edit Accounts view,override_mac_edit (string, optional): Override the Edit Device form,override_mac_multi (string, optional): Override the Edit Devices view,override_guest_multi_form (string, optional): Override the Edit Guest Accounts form,override_mac_multi_form (string, optional): Override the Edit Guest Devices form,override_guest_multi_result (string, optional): Override the Edit Multiple Accounts Results form,override_mac_multi_result (string, optional): Override the Edit Multiple Devices Results form,override_mac_export (string, optional): Override the Export Devices view,override_guest_export (string, optional): Override the Export Guest Accounts view,override_mac_list (string, optional): Override the Manage Devices view,override_guest_users (string, optional): Override the Manage Guest Accounts view,override_guest_edit_receipt (string, optional): Override the Updated Account Details form,override_mac_edit_receipt (string, optional): Override the Updated Device Details form}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "comment": "",
          "enabled": false,
          "privileges": [
            ""
          ],
          "user_dbs_list": "",
          "sponsor_filter": "",
          "filter_useraccount": "",
          "filter_radacct": "",
          "max_users": "",
          "max_devices": "",
          "userskin": "",
          "userskin_name": "",
          "start_page": "",
          "lang": "",
          "timezone_id": "",
          "override_ui": false,
          "override_guest_sessions": "",
          "override_change_expiration": "",
          "override_create_multi_result": "",
          "override_create_multi": "",
          "override_mac_create": "",
          "override_mac_create_receipt": "",
          "override_create_user": "",
          "override_create_user_receipt": "",
          "override_guest_edit": "",
          "override_guest_multi": "",
          "override_mac_edit": "",
          "override_mac_multi": "",
          "override_guest_multi_form": "",
          "override_mac_multi_form": "",
          "override_guest_multi_result": "",
          "override_mac_multi_result": "",
          "override_mac_export": "",
          "override_guest_export": "",
          "override_mac_list": "",
          "override_guest_users": "",
          "override_guest_edit_receipt": "",
          "override_mac_edit_receipt": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Name of the operator profile
        """
        url_path = "/operator-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:PolicyManagerZone
    # Function Section Description: Manage Policy Manager Zones

    def get_server_policy_manager_zones(self, name=""):
        """
        Operation: Get list of Policy Manager Zones
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Name of the operator profile
        """
        url_path = "/server/policy-manager-zones"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_server_policy_manager_zones(self, body=({})):
        """
                Operation: Create Policy Manager Zone
                HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- PolicyManagerZoneCreate {zone_name (string): Name of the Policy Manager Zone}
                Required Body Parameters (type(dict) body example)- {
          "zone_name": ""
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
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: zone_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/{zone_id}"
        dict_path = {"zone_id": zone_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_policy_manager_zones_by_zone_id(self, zone_id="", body=({})):
        """
                Operation: Update Policy Manager Zone
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: zone_id, Description: Numeric ID of the policy manager zone
                Required Body Parameters (body description)- PolicyManagerZoneReplace {zone_name (string): Name of the Policy Manager Zone}
                Required Body Parameters (type(dict) body example)- {
          "zone_name": ""
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
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: zone_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/{zone_id}"
        dict_path = {"zone_id": zone_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_server_policy_manager_zones_name_by_name(self, name=""):
        """
        Operation: Get Policy Manager Zone by name
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_policy_manager_zones_name_by_name(self, name="", body=({})):
        """
                Operation: Update Policy Manager Zone by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the policy manager zone
                Required Body Parameters (body description)- PolicyManagerZoneReplace {zone_name (string): Name of the Policy Manager Zone}
                Required Body Parameters (type(dict) body example)- {
          "zone_name": ""
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
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/server/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:SnmpTrapReceiver
    # Function Section Description: Manage Snmp Trap Receiver

    def get_snmp_trap_receiver(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Snmp Trap Receiver
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SnmpTrapReceiverCreate {host_address (string): HostName of the SNMP Trap Server,description (string, optional): Description of the SNMP Trap Server,snmp_version (string): SNMP Version of the SNMP Trap Server,community_string (string, optional): Community String of the SNMP Trap Server,server_port (string, optional): Server Port of the SNMP Trap Server,user (string, optional): Username of the SNMP Trap Server,type (string, optional) = ['Inform' or 'Trap']: Type of SNMP Trap Server,auth_key (string, optional): Authentication key of the SNMP Trap Server,priv_key (string, optional): Privacy key of the SNMP Trap Server,priv_protocol (object, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy Protocol,auth_protocol (object, optional) = ['MD5' or 'SHA']: Authentication Protocol,security_level (object, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: SNMP Version}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "snmp_version": "",
          "community_string": "",
          "server_port": "",
          "user": "",
          "type": "",
          "auth_key": "",
          "priv_key": "",
          "priv_protocol": "object",
          "auth_protocol": "object",
          "security_level": "object"
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
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
                Required Body Parameters (body description)- SnmpTrapReceiverUpdate {host_address (string, optional): HostName of the SNMP Trap Server,description (string, optional): Description of the SNMP Trap Server,snmp_version (string, optional): SNMP Version of the SNMP Trap Server,community_string (string, optional): Community String of the SNMP Trap Server,server_port (string, optional): Server Port of the SNMP Trap Server,user (string, optional): Username of the SNMP Trap Server,type (string, optional) = ['Inform' or 'Trap']: Type of SNMP Trap Server,auth_key (string, optional): Authentication key of the SNMP Trap Server,priv_key (string, optional): Privacy key of the SNMP Trap Server,priv_protocol (object, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy Protocol,auth_protocol (object, optional) = ['MD5' or 'SHA']: Authentication Protocol,security_level (object, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: SNMP Version}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "snmp_version": "",
          "community_string": "",
          "server_port": "",
          "user": "",
          "type": "",
          "auth_key": "",
          "priv_key": "",
          "priv_protocol": "object",
          "auth_protocol": "object",
          "security_level": "object"
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
                Required Body Parameters (body description)- SnmpTrapReceiverReplace {host_address (string): HostName of the SNMP Trap Server,description (string, optional): Description of the SNMP Trap Server,snmp_version (string): SNMP Version of the SNMP Trap Server,community_string (string, optional): Community String of the SNMP Trap Server,server_port (string, optional): Server Port of the SNMP Trap Server,user (string, optional): Username of the SNMP Trap Server,type (string, optional) = ['Inform' or 'Trap']: Type of SNMP Trap Server,auth_key (string, optional): Authentication key of the SNMP Trap Server,priv_key (string, optional): Privacy key of the SNMP Trap Server,priv_protocol (object, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy Protocol,auth_protocol (object, optional) = ['MD5' or 'SHA']: Authentication Protocol,security_level (object, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: SNMP Version}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "snmp_version": "",
          "community_string": "",
          "server_port": "",
          "user": "",
          "type": "",
          "auth_key": "",
          "priv_key": "",
          "priv_protocol": "object",
          "auth_protocol": "object",
          "security_level": "object"
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
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: snmp_trap_receiver_id, Description: Numeric ID of the SNMPTrap Server
        """
        url_path = "/snmp-trap-receiver/{snmp_trap_receiver_id}"
        dict_path = {"snmp_trap_receiver_id": snmp_trap_receiver_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_snmp_trap_receiver_name_by_name(self, name=""):
        """
        Operation: Get a Snmp Trap Receiver by name
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the Host Address
        """
        url_path = "/snmp-trap-receiver/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_snmp_trap_receiver_name_by_name(self, name="", body=({})):
        """
                Operation: Update some fields of Snmp Trap Receiver by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the Host Address
                Required Body Parameters (body description)- SnmpTrapReceiverUpdate {host_address (string, optional): HostName of the SNMP Trap Server,description (string, optional): Description of the SNMP Trap Server,snmp_version (string, optional): SNMP Version of the SNMP Trap Server,community_string (string, optional): Community String of the SNMP Trap Server,server_port (string, optional): Server Port of the SNMP Trap Server,user (string, optional): Username of the SNMP Trap Server,type (string, optional) = ['Inform' or 'Trap']: Type of SNMP Trap Server,auth_key (string, optional): Authentication key of the SNMP Trap Server,priv_key (string, optional): Privacy key of the SNMP Trap Server,priv_protocol (object, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy Protocol,auth_protocol (object, optional) = ['MD5' or 'SHA']: Authentication Protocol,security_level (object, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: SNMP Version}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "snmp_version": "",
          "community_string": "",
          "server_port": "",
          "user": "",
          "type": "",
          "auth_key": "",
          "priv_key": "",
          "priv_protocol": "object",
          "auth_protocol": "object",
          "security_level": "object"
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the Host Address
                Required Body Parameters (body description)- SnmpTrapReceiverReplace {host_address (string): HostName of the SNMP Trap Server,description (string, optional): Description of the SNMP Trap Server,snmp_version (string): SNMP Version of the SNMP Trap Server,community_string (string, optional): Community String of the SNMP Trap Server,server_port (string, optional): Server Port of the SNMP Trap Server,user (string, optional): Username of the SNMP Trap Server,type (string, optional) = ['Inform' or 'Trap']: Type of SNMP Trap Server,auth_key (string, optional): Authentication key of the SNMP Trap Server,priv_key (string, optional): Privacy key of the SNMP Trap Server,priv_protocol (object, optional) = ['DES_CBC' or 'AES_128' or 'AES_192' or 'AES_256']: Privacy Protocol,auth_protocol (object, optional) = ['MD5' or 'SHA']: Authentication Protocol,security_level (object, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: SNMP Version}
                Required Body Parameters (type(dict) body example)- {
          "host_address": "",
          "description": "",
          "snmp_version": "",
          "community_string": "",
          "server_port": "",
          "user": "",
          "type": "",
          "auth_key": "",
          "priv_key": "",
          "priv_protocol": "object",
          "auth_protocol": "object",
          "security_level": "object"
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
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the Host Address
        """
        url_path = "/snmp-trap-receiver/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
