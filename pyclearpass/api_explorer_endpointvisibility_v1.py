from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_endpointvisibility_v1.py


class ApiEndpointVisibility(ClearPassAPILogin):
    # Function Section Name:AgentlessOnGuardSettings
    # Function Section Description: Manage Agentless OnGuard settings

    def get_agentless_onguard_settings(
        self, id="", disconnect_active_sessions="", ignore_disconnect_errors=""
    ):
        """
                Operation: Get a list of Agentless OnGuard Settings
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Path Parameter Name: id, Description: Numeric ID of the device
                Optional Query Parameter Name: disconnect_active_sessions, Description: true: Disconnects the device from the network (default)false: No action is taken
                Optional Query Parameter Name: ignore_disconnect_errors, Description: true: Optional Disconnect — failure to disconnect will be ignored and the device will be forcibly deleted
        false: Require Disconnect (Recommended) — failure to disconnect will stop the device from being deleted (default)
        When false (‘Require Disconnect’), the device will only be deleted if all other sessions can be disconnected,
        which ensures that the device does not retain access to the network through a currently active session.
        You should only select true (‘Optional Disconnect’) if necessary.
        This parameter is ignored if disconnect_active_sessions is false.
        """
        url_path = "/agentless-onguard/settings"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {
            "disconnect_active_sessions": disconnect_active_sessions,
            "ignore_disconnect_errors": ignore_disconnect_errors,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_agentless_onguard_settings(self, body=({})):
        """
                Operation: Add an Agentless OnGuard Setting
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AgentlessOnGuardSettingsCreate {name (string): Name of Agentless OnGuard Setting,description (string, optional): Description of Agentless OnGuard Setting,client_os (string): Client OS type. Allowed Values: Windows, macOS and Linux,domain_account (string, optional): Name of domain account used to launch Agentless OnGuard on endpoints,ssh_account (string, optional): Name of ssh account used to launch Agentless OnGuard on endpoints,working_dir (string): Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard),action (string) = ['START_HEALTH_CHECKS']: Action to be performed on endpoints,servers (array[string]): IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]),download_url (string): HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe),validate_url_cert (boolean, optional): Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true),override_checksum (boolean, optional): Override checksum fields (default=false),checksums_32 (array[string], optional): SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs,checksums_64 (array[string], optional): SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "client_os": "",
          "domain_account": "",
          "ssh_account": "",
          "working_dir": "",
          "action": "",
          "servers": [
            ""
          ],
          "download_url": "",
          "validate_url_cert": false,
          "override_checksum": false,
          "checksums_32": [
            ""
          ],
          "checksums_64": [
            ""
          ]
        }
        """
        url_path = "/agentless-onguard/settings"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_agentless_onguard_settings_by_settings_id(self, settings_id=""):
        """
        Operation: Get an Agentless OnGuard Setting
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/{settings_id}"
        dict_path = {"settings_id": settings_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_agentless_onguard_settings_by_settings_id(
        self, settings_id="", body=({})
    ):
        """
                Operation: Update some fields of an Agentless OnGuard Setting
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
                Required Body Parameters (body description)- AgentlessOnGuardSettingsUpdate {name (string, optional): Name of Agentless OnGuard Setting,description (string, optional): Description of Agentless OnGuard Setting,client_os (string, optional): Client OS type. Allowed Values: Windows, macOS and Linux,domain_account (string, optional): Name of domain account used to launch Agentless OnGuard on endpoints,ssh_account (string, optional): Name of ssh account used to launch Agentless OnGuard on endpoints,working_dir (string, optional): Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard),action (string, optional) = ['START_HEALTH_CHECKS']: Action to be performed on endpoints,servers (array[string], optional): IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]),download_url (string, optional): HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe),validate_url_cert (boolean, optional): Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true),override_checksum (boolean, optional): Override checksum fields (default=false),checksums_32 (array[string], optional): SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs,checksums_64 (array[string], optional): SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "client_os": "",
          "domain_account": "",
          "ssh_account": "",
          "working_dir": "",
          "action": "",
          "servers": [
            ""
          ],
          "download_url": "",
          "validate_url_cert": false,
          "override_checksum": false,
          "checksums_32": [
            ""
          ],
          "checksums_64": [
            ""
          ]
        }
        """
        url_path = "/agentless-onguard/settings/{settings_id}"
        dict_path = {"settings_id": settings_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_agentless_onguard_settings_by_settings_id(
        self, settings_id="", body=({})
    ):
        """
                Operation: Replace an Agentless OnGuard Setting
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
                Required Body Parameters (body description)- AgentlessOnGuardSettingsReplace {name (string): Name of Agentless OnGuard Setting,description (string, optional): Description of Agentless OnGuard Setting,client_os (string): Client OS type. Allowed Values: Windows, macOS and Linux,domain_account (string, optional): Name of domain account used to launch Agentless OnGuard on endpoints,ssh_account (string, optional): Name of ssh account used to launch Agentless OnGuard on endpoints,working_dir (string): Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard),action (string) = ['START_HEALTH_CHECKS']: Action to be performed on endpoints,servers (array[string]): IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]),download_url (string): HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe),validate_url_cert (boolean, optional): Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true),override_checksum (boolean, optional): Override checksum fields (default=false),checksums_32 (array[string], optional): SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs,checksums_64 (array[string], optional): SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "client_os": "",
          "domain_account": "",
          "ssh_account": "",
          "working_dir": "",
          "action": "",
          "servers": [
            ""
          ],
          "download_url": "",
          "validate_url_cert": false,
          "override_checksum": false,
          "checksums_32": [
            ""
          ],
          "checksums_64": [
            ""
          ]
        }
        """
        url_path = "/agentless-onguard/settings/{settings_id}"
        dict_path = {"settings_id": settings_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_agentless_onguard_settings_by_settings_id(self, settings_id=""):
        """
        Operation: Delete an Agentless OnGuard Setting
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/{settings_id}"
        dict_path = {"settings_id": settings_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_agentless_onguard_settings_name_by_name(self, name=""):
        """
        Operation: Get an Agentless OnGuard Setting by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_agentless_onguard_settings_name_by_name(self, name="", body=({})):
        """
                Operation: Update some fields of an Agentless OnGuard Setting by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of Agentless OnGuard Setting
                Required Body Parameters (body description)- AgentlessOnGuardSettingsUpdate {name (string, optional): Name of Agentless OnGuard Setting,description (string, optional): Description of Agentless OnGuard Setting,client_os (string, optional): Client OS type. Allowed Values: Windows, macOS and Linux,domain_account (string, optional): Name of domain account used to launch Agentless OnGuard on endpoints,ssh_account (string, optional): Name of ssh account used to launch Agentless OnGuard on endpoints,working_dir (string, optional): Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard),action (string, optional) = ['START_HEALTH_CHECKS']: Action to be performed on endpoints,servers (array[string], optional): IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]),download_url (string, optional): HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe),validate_url_cert (boolean, optional): Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true),override_checksum (boolean, optional): Override checksum fields (default=false),checksums_32 (array[string], optional): SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs,checksums_64 (array[string], optional): SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "client_os": "",
          "domain_account": "",
          "ssh_account": "",
          "working_dir": "",
          "action": "",
          "servers": [
            ""
          ],
          "download_url": "",
          "validate_url_cert": false,
          "override_checksum": false,
          "checksums_32": [
            ""
          ],
          "checksums_64": [
            ""
          ]
        }
        """
        url_path = "/agentless-onguard/settings/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_agentless_onguard_settings_name_by_name(self, name="", body=({})):
        """
                Operation: Replace an Agentless OnGuard Setting by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of Agentless OnGuard Setting
                Required Body Parameters (body description)- AgentlessOnGuardSettingsReplace {name (string): Name of Agentless OnGuard Setting,description (string, optional): Description of Agentless OnGuard Setting,client_os (string): Client OS type. Allowed Values: Windows, macOS and Linux,domain_account (string, optional): Name of domain account used to launch Agentless OnGuard on endpoints,ssh_account (string, optional): Name of ssh account used to launch Agentless OnGuard on endpoints,working_dir (string): Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard),action (string) = ['START_HEALTH_CHECKS']: Action to be performed on endpoints,servers (array[string]): IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]),download_url (string): HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe),validate_url_cert (boolean, optional): Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true),override_checksum (boolean, optional): Override checksum fields (default=false),checksums_32 (array[string], optional): SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs,checksums_64 (array[string], optional): SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "client_os": "",
          "domain_account": "",
          "ssh_account": "",
          "working_dir": "",
          "action": "",
          "servers": [
            ""
          ],
          "download_url": "",
          "validate_url_cert": false,
          "override_checksum": false,
          "checksums_32": [
            ""
          ],
          "checksums_64": [
            ""
          ]
        }
        """
        url_path = "/agentless-onguard/settings/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_agentless_onguard_settings_name_by_name(self, name=""):
        """
        Operation: Delete an Agentless OnGuard Setting by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:AgentlessOnGuardSubnetMapping
    # Function Section Description: Manage Agentless OnGuard subnet mappings

    def get_agentless_onguard_subnet_mapping(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of subnet mappings
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/agentless-onguard/subnet-mapping"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_agentless_onguard_subnet_mapping(self, body=({})):
        """
                Operation: Add a subnet mapping
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- AgentlessOnGuardSubnetMappingCreate {name (string): Name of Agentless OnGuard Subnet Mapping,client_subnets (array[string]): IP subnets used for selecting clients,zone (string): Name of Policy Manager Zone for which the specified client subnet is applicable,agentless_onguard_setting_windows (string, optional): Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_macOS (string, optional): Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_linux (string, optional): Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string,client_scan_setting (string) = ['AllClients' or 'StaticIPClients']: Clients to be scanned in the subnet,enabled (boolean, optional): Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "client_subnets": [
            ""
          ],
          "zone": "",
          "agentless_onguard_setting_windows": "",
          "agentless_onguard_setting_macOS": "",
          "agentless_onguard_setting_linux": "",
          "client_scan_setting": "",
          "enabled": false
        }
        """
        url_path = "/agentless-onguard/subnet-mapping"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_agentless_onguard_subnet_mapping_by_subnet_mapping_id(
        self, subnet_mapping_id=""
    ):
        """
        Operation: Get a subnet mapping
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_agentless_onguard_subnet_mapping_by_subnet_mapping_id(
        self, subnet_mapping_id="", body=({})
    ):
        """
                Operation: Update some fields of a subnet mapping
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
                Required Body Parameters (body description)- AgentlessOnGuardSubnetMappingUpdate {name (string, optional): Name of Agentless OnGuard Subnet Mapping,client_subnets (array[string], optional): IP subnets used for selecting clients,zone (string, optional): Name of Policy Manager Zone for which the specified client subnet is applicable,agentless_onguard_setting_windows (string, optional): Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_macOS (string, optional): Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_linux (string, optional): Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string,client_scan_setting (string, optional) = ['AllClients' or 'StaticIPClients']: Clients to be scanned in the subnet,enabled (boolean, optional): Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "client_subnets": [
            ""
          ],
          "zone": "",
          "agentless_onguard_setting_windows": "",
          "agentless_onguard_setting_macOS": "",
          "agentless_onguard_setting_linux": "",
          "client_scan_setting": "",
          "enabled": false
        }
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_agentless_onguard_subnet_mapping_by_subnet_mapping_id(
        self, subnet_mapping_id="", body=({})
    ):
        """
                Operation: Replace a subnet mapping
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
                Required Body Parameters (body description)- AgentlessOnGuardSubnetMappingReplace {name (string): Name of Agentless OnGuard Subnet Mapping,client_subnets (array[string]): IP subnets used for selecting clients,zone (string): Name of Policy Manager Zone for which the specified client subnet is applicable,agentless_onguard_setting_windows (string, optional): Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_macOS (string, optional): Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_linux (string, optional): Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string,client_scan_setting (string) = ['AllClients' or 'StaticIPClients']: Clients to be scanned in the subnet,enabled (boolean, optional): Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "client_subnets": [
            ""
          ],
          "zone": "",
          "agentless_onguard_setting_windows": "",
          "agentless_onguard_setting_macOS": "",
          "agentless_onguard_setting_linux": "",
          "client_scan_setting": "",
          "enabled": false
        }
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_agentless_onguard_subnet_mapping_by_subnet_mapping_id(
        self, subnet_mapping_id=""
    ):
        """
        Operation: Delete a subnet mapping
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_agentless_onguard_subnet_mapping_name_by_name(self, name=""):
        """
        Operation: Get a subnet mapping by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_agentless_onguard_subnet_mapping_name_by_name(self, name="", body=({})):
        """
                Operation: Update some fields of a subnet mapping by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of subnet mapping
                Required Body Parameters (body description)- AgentlessOnGuardSubnetMappingUpdate {name (string, optional): Name of Agentless OnGuard Subnet Mapping,client_subnets (array[string], optional): IP subnets used for selecting clients,zone (string, optional): Name of Policy Manager Zone for which the specified client subnet is applicable,agentless_onguard_setting_windows (string, optional): Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_macOS (string, optional): Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_linux (string, optional): Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string,client_scan_setting (string, optional) = ['AllClients' or 'StaticIPClients']: Clients to be scanned in the subnet,enabled (boolean, optional): Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "client_subnets": [
            ""
          ],
          "zone": "",
          "agentless_onguard_setting_windows": "",
          "agentless_onguard_setting_macOS": "",
          "agentless_onguard_setting_linux": "",
          "client_scan_setting": "",
          "enabled": false
        }
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_agentless_onguard_subnet_mapping_name_by_name(self, name="", body=({})):
        """
                Operation: Replace a subnet mapping by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of subnet mapping
                Required Body Parameters (body description)- AgentlessOnGuardSubnetMappingReplace {name (string): Name of Agentless OnGuard Subnet Mapping,client_subnets (array[string]): IP subnets used for selecting clients,zone (string): Name of Policy Manager Zone for which the specified client subnet is applicable,agentless_onguard_setting_windows (string, optional): Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_macOS (string, optional): Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string,agentless_onguard_setting_linux (string, optional): Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string,client_scan_setting (string) = ['AllClients' or 'StaticIPClients']: Clients to be scanned in the subnet,enabled (boolean, optional): Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "client_subnets": [
            ""
          ],
          "zone": "",
          "agentless_onguard_setting_windows": "",
          "agentless_onguard_setting_macOS": "",
          "agentless_onguard_setting_linux": "",
          "client_scan_setting": "",
          "enabled": false
        }
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_agentless_onguard_subnet_mapping_name_by_name(self, name=""):
        """
        Operation: Delete a subnet mapping by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_agentless_onguard_subnet_mapping_by_subnet_mapping_id_enable(
        self, subnet_mapping_id=""
    ):
        """
        Operation: Enable Agentless OnGuard Settings on client subnets
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}/enable"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_agentless_onguard_subnet_mapping_by_subnet_mapping_id_disable(
        self, subnet_mapping_id=""
    ):
        """
        Operation: Disable Agentless OnGuard Settings on client subnets
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}/disable"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_agentless_onguard_subnet_mapping_name_by_name_enable(self, name=""):
        """
        Operation: Enable Agentless OnGuard Settings on client subnets by subnet mapping name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}/enable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_agentless_onguard_subnet_mapping_name_by_name_disable(self, name=""):
        """
        Operation: Disable Agentless OnGuard Settings on client subnets by subnet mapping name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}/disable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # Function Section Name:DeviceFingerprint
    # Function Section Description: Manage Device Fingerprint Profiling

    def new_device_profiler_device_fingerprint(self, body=({})):
        """
                Operation: Post device fingerprint attributes for profiling
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- DeviceFingerprintCreate {mac (string, optional): MAC address of device,ip (string, optional): IP address of device,hostname (string, optional): Hostname of device,dhcp (DHCPAttributes, optional): DHCP attributes as JSON,active_sync (ActiveSyncAttributes, optional): Active Sync attributes as JSON,host (HostAttributes, optional): Host attributes as JSON,snmp (SNMPAttributes, optional): SNMP attributes as JSON,device (DeviceAttributes, optional): Device attributes as JSON,tcp (TCPAttributes, optional): TCP attributes as JSON,nmap (NMAPAttributes, optional): NMAP attributes as JSON,ssh (SSHAttributes, optional): SSH attributes as JSON,wmi (WMIAttributes, optional): WMI attributes as JSON,ports (PortsAttributes, optional): Port attributes as JSON}DHCPAttributes {device_type (array[string], optional): DHCP Options,option12 (array[string], optional): DHCP Option12,option54 (array[string], optional): DHCP Option54,option55 (array[string], optional): DHCP Option55,option60 (array[string], optional): DHCP Option60}ActiveSyncAttributes {device_type (array[string], optional): ActiveSync Device Type,user_agent (array[string], optional): ActiveSync User Agent,device_model (array[string], optional): ActiveSync Device Model,ip (array[string], optional): ActiveSync IP Address}HostAttributes {os_type (array[string], optional): Host OS Type,user_agent (array[string], optional): Host User Agent,ports (array[string], optional): Host Open Ports,services (array[string], optional): Host Services,device_type (array[string], optional): Host Device Type,dst_conns (array[string], optional): Destination Connections,app_group (array[string], optional): Application Group,mac_oui (array[string], optional): MAC OUI,access_type (array[string], optional): Access Type}SNMPAttributes {name (array[string], optional): SNMP Device Name,sys_name (array[string], optional): SNMP System Name,sys_descr (array[string], optional): SNMP System Description,hr_device_descr (array[string], optional): SNMP Device Description,device_type (array[string], optional): SNMP Device Type,cdp_cache_platform (array[string], optional): CDP Device Description,lldp_sys_descr (array[string], optional): null}DeviceAttributes {category (array[string], optional): Device Category,family (array[string], optional): Device Family,name (array[string], optional): Device Name}TCPAttributes {device (array[string], optional): TCP Device Category,fp (array[string], optional): TCP Fingerprint}NMAPAttributes {device (array[string], optional): Nmap Device Name}SSHAttributes {device_name (array[string], optional): SSH device name}WMIAttributes {os_name (array[string], optional): WMI OS Name}PortsAttributes {open (array[string], optional): Open Ports}
                Required Body Parameters (type(dict) body example)- {
          "mac": "",
          "ip": "",
          "hostname": "",
          "dhcp": {
            "device_type": [
              ""
            ],
            "option12": [
              ""
            ],
            "option54": [
              ""
            ],
            "option55": [
              ""
            ],
            "option60": [
              ""
            ]
          },
          "active_sync": {
            "device_type": [
              ""
            ],
            "user_agent": [
              ""
            ],
            "device_model": [
              ""
            ],
            "ip": [
              ""
            ]
          },
          "host": {
            "os_type": [
              ""
            ],
            "user_agent": [
              ""
            ],
            "ports": [
              ""
            ],
            "services": [
              ""
            ],
            "device_type": [
              ""
            ],
            "dst_conns": [
              ""
            ],
            "app_group": [
              ""
            ],
            "mac_oui": [
              ""
            ],
            "access_type": [
              ""
            ]
          },
          "snmp": {
            "name": [
              ""
            ],
            "sys_name": [
              ""
            ],
            "sys_descr": [
              ""
            ],
            "hr_device_descr": [
              ""
            ],
            "device_type": [
              ""
            ],
            "cdp_cache_platform": [
              ""
            ],
            "lldp_sys_descr": [
              ""
            ]
          },
          "device": {
            "category": [
              ""
            ],
            "family": [
              ""
            ],
            "name": [
              ""
            ]
          },
          "tcp": {
            "device": [
              ""
            ],
            "fp": [
              ""
            ]
          },
          "nmap": {
            "device": [
              ""
            ]
          },
          "ssh": {
            "device_name": [
              ""
            ]
          },
          "wmi": {
            "os_name": [
              ""
            ]
          },
          "ports": {
            "open": [
              ""
            ]
          }
        }
        """
        url_path = "/device-profiler/device-fingerprint"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_device_profiler_device_fingerprint_by_mac_or_ip(self, mac_or_ip=""):
        """
        Operation: Get profiled device
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: mac_or_ip, Description: MAC or IP address of device
        """
        url_path = "/device-profiler/device-fingerprint/{mac_or_ip}"
        dict_path = {"mac_or_ip": mac_or_ip}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_device_profiler_device_fingerprint_by_mac_or_ip(self, mac_or_ip=""):
        """
        Operation: Delete fingerprint of profiled device
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: mac_or_ip, Description: URL parameter mac_or_ip
        """
        url_path = "/device-profiler/device-fingerprint/{mac_or_ip}"
        dict_path = {"mac_or_ip": mac_or_ip}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:FingerprintDictionary
    # Function Section Description: Manage Fingerprints

    def get_fingerprint(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Fingerprints
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/fingerprint"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_fingerprint(self, body=({})):
        """
                Operation: Create a new Fingerprint
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- FingerprintDictionaryCreate {category (string): Category name of the fingerprint,family (string): Family name of the fingerprint,name (string): Unique name of the fingerprint}
                Required Body Parameters (type(dict) body example)- {
          "category": "",
          "family": "",
          "name": ""
        }
        """
        url_path = "/fingerprint"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_fingerprint_by_fingerprint_id(self, fingerprint_id=""):
        """
        Operation: Get a Fingerprint
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: fingerprint_id, Description: Numeric ID of the fingerprint
        """
        url_path = "/fingerprint/{fingerprint_id}"
        dict_path = {"fingerprint_id": fingerprint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_fingerprint_by_fingerprint_id(self, fingerprint_id="", body=({})):
        """
                Operation: Update some fields of a Fingerprint
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: fingerprint_id, Description: Numeric ID of the fingerprint
                Required Body Parameters (body description)- FingerprintDictionaryUpdate {category (string, optional): Category name of the fingerprint,family (string, optional): Family name of the fingerprint,name (string, optional): Unique name of the fingerprint}
                Required Body Parameters (type(dict) body example)- {
          "category": "",
          "family": "",
          "name": ""
        }
        """
        url_path = "/fingerprint/{fingerprint_id}"
        dict_path = {"fingerprint_id": fingerprint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_fingerprint_by_fingerprint_id(self, fingerprint_id="", body=({})):
        """
                Operation: Replace a Fingerprint
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: fingerprint_id, Description: Numeric ID of the fingerprint
                Required Body Parameters (body description)- FingerprintDictionaryReplace {category (string): Category name of the fingerprint,family (string): Family name of the fingerprint,name (string): Unique name of the fingerprint}
                Required Body Parameters (type(dict) body example)- {
          "category": "",
          "family": "",
          "name": ""
        }
        """
        url_path = "/fingerprint/{fingerprint_id}"
        dict_path = {"fingerprint_id": fingerprint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_fingerprint_by_fingerprint_id(self, fingerprint_id=""):
        """
        Operation: Delete a Fingerprint
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: fingerprint_id, Description: Numeric ID of the fingerprint
        """
        url_path = "/fingerprint/{fingerprint_id}"
        dict_path = {"fingerprint_id": fingerprint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_fingerprint_name_by_category_family_name(
        self, category="", family="", name=""
    ):
        """
        Operation: Get a Fingerprint by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: category, Description: Category name of the fingerprint
        Required Path Parameter Name: family, Description: family name of the fingerprint
        Required Path Parameter Name: name, Description: Unique name of the fingerprint
        """
        url_path = "/fingerprint/name/{category}/{family}/{name}"
        dict_path = {"category": category, "family": family, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_fingerprint_name_by_category_family_name(
        self, category="", family="", name="", body=({})
    ):
        """
                Operation: Update some fields of a Fingerprint by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: category, Description: Category name of the fingerprint
                Required Path Parameter Name: family, Description: family name of the fingerprint
                Required Path Parameter Name: name, Description: Unique name of the fingerprint
                Required Body Parameters (body description)- FingerprintDictionaryUpdate {category (string, optional): Category name of the fingerprint,family (string, optional): Family name of the fingerprint,name (string, optional): Unique name of the fingerprint}
                Required Body Parameters (type(dict) body example)- {
          "category": "",
          "family": "",
          "name": ""
        }
        """
        url_path = "/fingerprint/name/{category}/{family}/{name}"
        dict_path = {"category": category, "family": family, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_fingerprint_name_by_category_family_name(
        self, category="", family="", name="", body=({})
    ):
        """
                Operation: Replace a Fingerprint by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: category, Description: Category name of the fingerprint
                Required Path Parameter Name: family, Description: family name of the fingerprint
                Required Path Parameter Name: name, Description: Unique name of the fingerprint
                Required Body Parameters (body description)- FingerprintDictionaryReplace {category (string): Category name of the fingerprint,family (string): Family name of the fingerprint,name (string): Unique name of the fingerprint}
                Required Body Parameters (type(dict) body example)- {
          "category": "",
          "family": "",
          "name": ""
        }
        """
        url_path = "/fingerprint/name/{category}/{family}/{name}"
        dict_path = {"category": category, "family": family, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_fingerprint_name_by_category_family_name(
        self, category="", family="", name=""
    ):
        """
        Operation: Delete a Fingerprint by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: category, Description: Category name of the fingerprint
        Required Path Parameter Name: family, Description: family name of the fingerprint
        Required Path Parameter Name: name, Description: Unique name of the fingerprint
        """
        url_path = "/fingerprint/name/{category}/{family}/{name}"
        dict_path = {"category": category, "family": family, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:NetworkScan
    # Function Section Description: Manage NetworkScan Services

    def get_config_network_scan(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of NetworkScan
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/config/network-scan"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_config_network_scan(self, body=({})):
        """
                Operation: Add a NetworkScan
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- NetworkScanCreate {zone (string): Zone for the Network Scan,type (string) = ['DISCOVERY' or 'SUBNET']: Type of the Network Scan,seed_device_or_ip_subnet (string): Network IP for DISCOVERY (e.g. ["hostname.example.com", "1.2.3.4"]) or IP Subnets for SUBNET (e.g. ["10.1.0.0/16"]) Network Scan,scan_frequency (string) = ['ONDEMAND' or 'HOURLY' or 'DAILY' or 'WEEKLY']: Frequency of Network Scan,start_time (string, optional): Start time (HH:MM) of Network Scan  (e.g. ["10:40", "23:20"]),interval (integer, optional): Interval in hours (3 - 350) for HOURLY Network Scan,day_of_week (string, optional) = ['MONDAY' or 'TUESDAY' or 'WEDNESDAY' or 'THURSDAY' or 'FRIDAY' or 'SATURDAY' or 'SUNDAY']: Day of Week for WEEKLY Network Scan,depth (integer, optional) = ['1' or '2' or '3' or '4' or '5']: Depth level for DISCOVERY Network Scan,probe_arp (boolean, optional): Probe all ARP entries found (default=false for type="DISCOVERY", not applicable for type="SUBNET"),enabled (boolean, optional): Is Network Scan enabled? (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "zone": "",
          "type": "",
          "seed_device_or_ip_subnet": "",
          "scan_frequency": "",
          "start_time": "",
          "interval": 0,
          "day_of_week": "",
          "depth": 0,
          "probe_arp": false,
          "enabled": false
        }
        """
        url_path = "/config/network-scan"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_config_network_scan_by_scan_id(self, scan_id=""):
        """
        Operation: Get a NetworkScan
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_config_network_scan_by_scan_id(self, scan_id="", body=({})):
        """
                Operation: Update some fields of a NetworkScan
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: scan_id, Description: Numeric ID of the NetworkScan
                Required Body Parameters (body description)- NetworkScanUpdate {zone (string, optional): Zone for the Network Scan,type (string, optional) = ['DISCOVERY' or 'SUBNET']: Type of the Network Scan,seed_device_or_ip_subnet (string, optional): Network IP for DISCOVERY (e.g. ["hostname.example.com", "1.2.3.4"]) or IP Subnets for SUBNET (e.g. ["10.1.0.0/16"]) Network Scan,scan_frequency (string, optional) = ['ONDEMAND' or 'HOURLY' or 'DAILY' or 'WEEKLY']: Frequency of Network Scan,start_time (string, optional): Start time (HH:MM) of Network Scan  (e.g. ["10:40", "23:20"]),interval (integer, optional): Interval in hours (3 - 350) for HOURLY Network Scan,day_of_week (string, optional) = ['MONDAY' or 'TUESDAY' or 'WEDNESDAY' or 'THURSDAY' or 'FRIDAY' or 'SATURDAY' or 'SUNDAY']: Day of Week for WEEKLY Network Scan,depth (integer, optional) = ['1' or '2' or '3' or '4' or '5']: Depth level for DISCOVERY Network Scan,probe_arp (boolean, optional): Probe all ARP entries found (default=false for type="DISCOVERY", not applicable for type="SUBNET"),enabled (boolean, optional): Is Network Scan enabled? (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "zone": "",
          "type": "",
          "seed_device_or_ip_subnet": "",
          "scan_frequency": "",
          "start_time": "",
          "interval": 0,
          "day_of_week": "",
          "depth": 0,
          "probe_arp": false,
          "enabled": false
        }
        """
        url_path = "/config/network-scan/{scan_id}"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_config_network_scan_by_scan_id(self, scan_id="", body=({})):
        """
                Operation: Update all fields of a NetworkScan
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: scan_id, Description: Numeric ID of the NetworkScan
                Required Body Parameters (body description)- NetworkScanReplace {zone (string): Zone for the Network Scan,type (string) = ['DISCOVERY' or 'SUBNET']: Type of the Network Scan,seed_device_or_ip_subnet (string): Network IP for DISCOVERY (e.g. ["hostname.example.com", "1.2.3.4"]) or IP Subnets for SUBNET (e.g. ["10.1.0.0/16"]) Network Scan,scan_frequency (string) = ['ONDEMAND' or 'HOURLY' or 'DAILY' or 'WEEKLY']: Frequency of Network Scan,start_time (string, optional): Start time (HH:MM) of Network Scan  (e.g. ["10:40", "23:20"]),interval (integer, optional): Interval in hours (3 - 350) for HOURLY Network Scan,day_of_week (string, optional) = ['MONDAY' or 'TUESDAY' or 'WEDNESDAY' or 'THURSDAY' or 'FRIDAY' or 'SATURDAY' or 'SUNDAY']: Day of Week for WEEKLY Network Scan,depth (integer, optional) = ['1' or '2' or '3' or '4' or '5']: Depth level for DISCOVERY Network Scan,probe_arp (boolean, optional): Probe all ARP entries found (default=false for type="DISCOVERY", not applicable for type="SUBNET"),enabled (boolean, optional): Is Network Scan enabled? (default=true)}
                Required Body Parameters (type(dict) body example)- {
          "zone": "",
          "type": "",
          "seed_device_or_ip_subnet": "",
          "scan_frequency": "",
          "start_time": "",
          "interval": 0,
          "day_of_week": "",
          "depth": 0,
          "probe_arp": false,
          "enabled": false
        }
        """
        url_path = "/config/network-scan/{scan_id}"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_config_network_scan_by_scan_id(self, scan_id=""):
        """
        Operation: Delete a NetworkScan
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_config_network_scan_by_scan_id_enable(self, scan_id=""):
        """
        Operation: Update some fields of a NetworkScan
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}/enable"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_config_network_scan_by_scan_id_disable(self, scan_id=""):
        """
        Operation: Update some fields of a NetworkScan
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}/disable"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # Function Section Name:OnGuardActivity
    # Function Section Description: Manage OnGuard Activity

    def get_onguard_activity(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Clearpass OnGuard Endpoints
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/onguard-activity"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_onguard_activity_by_onguard_activity_id(self, onguard_activity_id=""):
        """
        Operation: Get a Clearpass OnGuard Endpoint Details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: onguard_activity_id, Description: Numeric ID of the OnGuard Activity
        """
        url_path = "/onguard-activity/{onguard_activity_id}"
        dict_path = {"onguard_activity_id": onguard_activity_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_onguard_activity_host_mac_by_host_mac(self, host_mac=""):
        """
        Operation: Get a Clearpass OnGuard Endpoint Details by host_mac
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: host_mac, Description: MAC Address of the agent
        """
        url_path = "/onguard-activity/host_mac/{host_mac}"
        dict_path = {"host_mac": host_mac}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_activity_message(self, body=({})):
        """
                Operation: Send/Broadcast Message
                HTTP Status Response Codes: 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OnGuardActivityMessage {host_mac_list (object): List of host MAC Address,message (string): Message,info_url (string, optional): URL,is_broadcast (boolean): Is a broadcast}
                Required Body Parameters (type(dict) body example)- {
          "host_mac_list": "object",
          "message": "",
          "info_url": "",
          "is_broadcast": false
        }
        """
        url_path = "/onguard-activity/message"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def new_onguard_activity_notification(self, body=({})):
        """
                Operation: Send/Broadcast Notification
                HTTP Status Response Codes: 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OnGuardActivityNotification {host_mac_list (object): List of host MAC Address,message (string): Message,info_url (string, optional): URL,is_broadcast (boolean): Is a broadcast,action (string) = ['RestartSession' or 'Bounce']: Action,endpoint_status (string, optional) = ['NO_CHANGE' or 'BLOCK_ACCESS' or 'ALLOW_ACCESS']: Status of the endpoint}
                Required Body Parameters (type(dict) body example)- {
          "host_mac_list": "object",
          "message": "",
          "info_url": "",
          "is_broadcast": false,
          "action": "",
          "endpoint_status": ""
        }
        """
        url_path = "/onguard-activity/notification"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:OnGuardCustomScript
    # Function Section Description: Manage OnGuard Custom Scripts

    def get_onguard_custom_script(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of OnGuard Custom Scripts
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/onguard-custom-script"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_custom_script(self, body=({})):
        """
                Operation: Create a new OnGuard Custom Script
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OnGuardCustomScriptCreate {name (string): Name of Custom Script,description (string, optional): Description of Custom Script,os_type (string) = ['linux' or 'macos' or 'windows']: OS Type of Custom Script,script_type (string) = ['agentScriptEnforcementProfile' or 'autoRemediation' or 'healthCollection']: Type of Custom Script,attributes (object): Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}),output_format (string, optional) = ['json' or 'keyValuePair']: Output Format of Custom Script, applicable only for health collection scripts,output_details (object, optional): Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}),rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts,rules (object, optional): List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}])}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "os_type": "",
          "script_type": "",
          "attributes": "object",
          "output_format": "",
          "output_details": "object",
          "rule_eval_algo": "",
          "rules": "object"
        }
        """
        url_path = "/onguard-custom-script"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_onguard_custom_script_by_onguard_custom_script_id(
        self, onguard_custom_script_id=""
    ):
        """
        Operation: Get an OnGuard Custom Script
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/{onguard_custom_script_id}"
        dict_path = {"onguard_custom_script_id": onguard_custom_script_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onguard_custom_script_by_onguard_custom_script_id(
        self, onguard_custom_script_id="", body=({})
    ):
        """
                Operation: Update some fields of an OnGuard Custom Script
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
                Required Body Parameters (body description)- OnGuardCustomScriptUpdate {name (string, optional): Name of Custom Script,description (string, optional): Description of Custom Script,attributes (object, optional): Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}),output_format (string, optional) = ['json' or 'keyValuePair']: Output Format of Custom Script, applicable only for health collection scripts,output_details (object, optional): Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}),rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts,rules (object, optional): List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}])}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "attributes": "object",
          "output_format": "",
          "output_details": "object",
          "rule_eval_algo": "",
          "rules": "object"
        }
        """
        url_path = "/onguard-custom-script/{onguard_custom_script_id}"
        dict_path = {"onguard_custom_script_id": onguard_custom_script_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_onguard_custom_script_by_onguard_custom_script_id(
        self, onguard_custom_script_id="", body=({})
    ):
        """
                Operation: Replace an OnGuard Custom Script
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
                Required Body Parameters (body description)- OnGuardCustomScriptReplace {name (string): Name of Custom Script,description (string, optional): Description of Custom Script,os_type (string) = ['linux' or 'macos' or 'windows']: OS Type of Custom Script,script_type (string) = ['agentScriptEnforcementProfile' or 'autoRemediation' or 'healthCollection']: Type of Custom Script,attributes (object): Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}),output_format (string, optional) = ['json' or 'keyValuePair']: Output Format of Custom Script, applicable only for health collection scripts,output_details (object, optional): Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}),rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts,rules (object, optional): List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}])}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "os_type": "",
          "script_type": "",
          "attributes": "object",
          "output_format": "",
          "output_details": "object",
          "rule_eval_algo": "",
          "rules": "object"
        }
        """
        url_path = "/onguard-custom-script/{onguard_custom_script_id}"
        dict_path = {"onguard_custom_script_id": onguard_custom_script_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_onguard_custom_script_by_onguard_custom_script_id(
        self, onguard_custom_script_id=""
    ):
        """
        Operation: Delete an OnGuard Custom Script
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/{onguard_custom_script_id}"
        dict_path = {"onguard_custom_script_id": onguard_custom_script_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_onguard_custom_script_name_by_name(self, name=""):
        """
        Operation: Get an OnGuard Custom Script by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onguard_custom_script_name_by_name(self, name="", body=({})):
        """
                Operation: Update some fields of an OnGuard Custom Script by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of OnGuard Custom Script
                Required Body Parameters (body description)- OnGuardCustomScriptUpdate {name (string, optional): Name of Custom Script,description (string, optional): Description of Custom Script,attributes (object, optional): Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}),output_format (string, optional) = ['json' or 'keyValuePair']: Output Format of Custom Script, applicable only for health collection scripts,output_details (object, optional): Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}),rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts,rules (object, optional): List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}])}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "attributes": "object",
          "output_format": "",
          "output_details": "object",
          "rule_eval_algo": "",
          "rules": "object"
        }
        """
        url_path = "/onguard-custom-script/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_onguard_custom_script_name_by_name(self, name="", body=({})):
        """
                Operation: Replace an OnGuard Custom Script by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of OnGuard Custom Script
                Required Body Parameters (body description)- OnGuardCustomScriptReplace {name (string): Name of Custom Script,description (string, optional): Description of Custom Script,os_type (string) = ['linux' or 'macos' or 'windows']: OS Type of Custom Script,script_type (string) = ['agentScriptEnforcementProfile' or 'autoRemediation' or 'healthCollection']: Type of Custom Script,attributes (object): Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}),output_format (string, optional) = ['json' or 'keyValuePair']: Output Format of Custom Script, applicable only for health collection scripts,output_details (object, optional): Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}),rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts,rules (object, optional): List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}])}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "os_type": "",
          "script_type": "",
          "attributes": "object",
          "output_format": "",
          "output_details": "object",
          "rule_eval_algo": "",
          "rules": "object"
        }
        """
        url_path = "/onguard-custom-script/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_onguard_custom_script_name_by_name(self, name=""):
        """
        Operation: Delete an OnGuard Custom Script by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:OnGuardGlobalSettings
    # Function Section Description: Manage OnGuard global settings

    def get_onguard_global_settings(self, name=""):
        """
        Operation: Get OnGuard global settings
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of OnGuard Custom Script
        """
        url_path = "/onguard/global-settings"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_global_settings(self, body=({})):
        """
                Operation: Update OnGuard global settings
                HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OnGuardGlobalSettingsCreate {AllowRemoteDesktopSession (boolean, optional): Enable access over Remote Desktop Session,CacheCredentialsForDays (integer, optional): Cache Credentials Interval(in days),EnableClientLoadBalance (boolean, optional): Enable OnGuard requests load-balancing,HealthCheckQuietPeriod (integer, optional) = ['>=0']: OnGuard Health Check Interval (in hours),HideLogoutButton (boolean, optional): Enable to hide Logout button,InstallVPNComponent (boolean, optional): Enable to install VPN component,KeepAliveIntervalSeconds (integer, optional) = ['30-600']: Keep-alive Interval (in seconds),LogoutBounceDelay (integer, optional): Delay to bounce after Logout (in minutes),RunOnGuardAs (string, optional) = ['Agent' or 'Service' or 'BothServiceAndAgent']: Run OnGuard As,ServerCertificateValidation (string, optional) = ['Required' or 'WarnAndProceed' or 'Skip']: Server Certificate Validation,ServerCommunicationMode (string, optional) = ['IP' or 'HostName' or 'FQDN']: Server Communication Mode,SupportEmailAddress (string, optional): Support Team Email Address,UseCurrentOSLanguage (boolean, optional): Use Current OS Language (Windows only),UseWindowsCredentials (boolean, optional): Enable to use Windows Single-Sign On,VPNDeviceNames (string, optional): VPN Device Names (Windows),VPNDeviceNamesMacOS (string, optional): VPN Device Names (macOS),VPNDeviceNamesLinux (string, optional): VPN Device Names (Linux),WiredAllowedSubnets (string, optional): [Deprecated] Allowed Subnets for Wired access,WirelessAllowedSubnets (string, optional): [Deprecated] Allowed Subnets for Wireless access}
                Required Body Parameters (type(dict) body example)- {
          "AllowRemoteDesktopSession": false,
          "CacheCredentialsForDays": 0,
          "EnableClientLoadBalance": false,
          "HealthCheckQuietPeriod": 0,
          "HideLogoutButton": false,
          "InstallVPNComponent": false,
          "KeepAliveIntervalSeconds": 0,
          "LogoutBounceDelay": 0,
          "RunOnGuardAs": "",
          "ServerCertificateValidation": "",
          "ServerCommunicationMode": "",
          "SupportEmailAddress": "",
          "UseCurrentOSLanguage": false,
          "UseWindowsCredentials": false,
          "VPNDeviceNames": "",
          "VPNDeviceNamesMacOS": "",
          "VPNDeviceNamesLinux": "",
          "WiredAllowedSubnets": "",
          "WirelessAllowedSubnets": ""
        }
        """
        url_path = "/onguard/global-settings"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:OnGuardSettings
    # Function Section Description: Manage OnGuard settings

    def get_onguard_settings(self, body=({})):
        """
                Operation: Get OnGuard settings
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- OnGuardGlobalSettingsCreate {AllowRemoteDesktopSession (boolean, optional): Enable access over Remote Desktop Session,CacheCredentialsForDays (integer, optional): Cache Credentials Interval(in days),EnableClientLoadBalance (boolean, optional): Enable OnGuard requests load-balancing,HealthCheckQuietPeriod (integer, optional) = ['>=0']: OnGuard Health Check Interval (in hours),HideLogoutButton (boolean, optional): Enable to hide Logout button,InstallVPNComponent (boolean, optional): Enable to install VPN component,KeepAliveIntervalSeconds (integer, optional) = ['30-600']: Keep-alive Interval (in seconds),LogoutBounceDelay (integer, optional): Delay to bounce after Logout (in minutes),RunOnGuardAs (string, optional) = ['Agent' or 'Service' or 'BothServiceAndAgent']: Run OnGuard As,ServerCertificateValidation (string, optional) = ['Required' or 'WarnAndProceed' or 'Skip']: Server Certificate Validation,ServerCommunicationMode (string, optional) = ['IP' or 'HostName' or 'FQDN']: Server Communication Mode,SupportEmailAddress (string, optional): Support Team Email Address,UseCurrentOSLanguage (boolean, optional): Use Current OS Language (Windows only),UseWindowsCredentials (boolean, optional): Enable to use Windows Single-Sign On,VPNDeviceNames (string, optional): VPN Device Names (Windows),VPNDeviceNamesMacOS (string, optional): VPN Device Names (macOS),VPNDeviceNamesLinux (string, optional): VPN Device Names (Linux),WiredAllowedSubnets (string, optional): [Deprecated] Allowed Subnets for Wired access,WirelessAllowedSubnets (string, optional): [Deprecated] Allowed Subnets for Wireless access}
                Required Body Parameters (type(dict) body example)- {
          "AllowRemoteDesktopSession": false,
          "CacheCredentialsForDays": 0,
          "EnableClientLoadBalance": false,
          "HealthCheckQuietPeriod": 0,
          "HideLogoutButton": false,
          "InstallVPNComponent": false,
          "KeepAliveIntervalSeconds": 0,
          "LogoutBounceDelay": 0,
          "RunOnGuardAs": "",
          "ServerCertificateValidation": "",
          "ServerCommunicationMode": "",
          "SupportEmailAddress": "",
          "UseCurrentOSLanguage": false,
          "UseWindowsCredentials": false,
          "VPNDeviceNames": "",
          "VPNDeviceNamesMacOS": "",
          "VPNDeviceNamesLinux": "",
          "WiredAllowedSubnets": "",
          "WirelessAllowedSubnets": ""
        }
        """
        url_path = "/onguard/settings"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def new_onguard_settings(self, body=({})):
        """
                Operation: Update OnGuard settings
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OnGuardSettingsCreate {mode (string, optional) = ['auth' or 'health' or 'both']: Mode of operation,interfaces (string, optional): [wired, wireless, vpn, other]: Network interfaces Agent should monitor,web_agent_interfaces (string, optional): [wired, wireless, vpn, other]: Network interfaces Native Dissolvable Agent should monitor,auth_type (string, optional) = ['cert' or 'password']: Authentication type,field_username_caption (string, optional): Caption for username field,field_password_caption (string, optional): Caption for password field,cert_filter_criteria (string, optional): Filter criteria used by OnGuard client to select certificates for authentication,upgrade_action (string, optional) = ['DoNothing' or 'NotifyOnly' or 'DownloadOnly' or 'AutoUpdate']: Agent action when an update is available,install_vpn_component (boolean, optional): Install VIA component,version (string, optional): Agent version. This is read only field,agentLibraryVersion (string, optional): Version of the OnGuard Agent Library. This is read-only field,installer_modified_time (string, optional): Time when Agent Installers was last updated. This is read only field,installer_modified_time_formatted (string, optional): Formatted Time when Agent Installers was last updated. This is read only field,agent_installers (object, optional): Details about Agent installers. This is read-only field,agent_web_installers (object, optional): Details about Native Dissolvable Agent installers. This is read only field,ip_version_onguard (string, optional) = ['IPv4Only' or 'IPv6Only' or 'dualPreferIPv4' or 'dualPreferIPv6' or 'dualBoth']: IP Version for Server Communication (OnGuard),ip_version_native (string, optional) = ['IPv4Only' or 'IPv6Only' or 'dualPreferIPv4' or 'dualPreferIPv6']: IP Version for Server Communication (Native),custom_remediation (object, optional): Customize webpage details for Agent Remediation UI. Input should be in JSON format.}
                Required Body Parameters (type(dict) body example)- {
          "mode": "",
          "interfaces": "",
          "web_agent_interfaces": "",
          "auth_type": "",
          "field_username_caption": "",
          "field_password_caption": "",
          "cert_filter_criteria": "",
          "upgrade_action": "",
          "install_vpn_component": false,
          "version": "",
          "agentLibraryVersion": "",
          "installer_modified_time": "",
          "installer_modified_time_formatted": "",
          "agent_installers": "object",
          "agent_web_installers": "object",
          "ip_version_onguard": "",
          "ip_version_native": "",
          "custom_remediation": "object"
        }
        """
        url_path = "/onguard/settings"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:OnGuardZoneMapping
    # Function Section Description: API's to configure authentication server IP addresses per zone

    def get_onguard_policy_manager_zones(self, body=({})):
        """
                Operation: Get Policy Manager Zones with associated authentication server IP addresses(Client Subnets and Server IPs)
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- OnGuardSettingsCreate {mode (string, optional) = ['auth' or 'health' or 'both']: Mode of operation,interfaces (string, optional): [wired, wireless, vpn, other]: Network interfaces Agent should monitor,web_agent_interfaces (string, optional): [wired, wireless, vpn, other]: Network interfaces Native Dissolvable Agent should monitor,auth_type (string, optional) = ['cert' or 'password']: Authentication type,field_username_caption (string, optional): Caption for username field,field_password_caption (string, optional): Caption for password field,cert_filter_criteria (string, optional): Filter criteria used by OnGuard client to select certificates for authentication,upgrade_action (string, optional) = ['DoNothing' or 'NotifyOnly' or 'DownloadOnly' or 'AutoUpdate']: Agent action when an update is available,install_vpn_component (boolean, optional): Install VIA component,version (string, optional): Agent version. This is read only field,agentLibraryVersion (string, optional): Version of the OnGuard Agent Library. This is read-only field,installer_modified_time (string, optional): Time when Agent Installers was last updated. This is read only field,installer_modified_time_formatted (string, optional): Formatted Time when Agent Installers was last updated. This is read only field,agent_installers (object, optional): Details about Agent installers. This is read-only field,agent_web_installers (object, optional): Details about Native Dissolvable Agent installers. This is read only field,ip_version_onguard (string, optional) = ['IPv4Only' or 'IPv6Only' or 'dualPreferIPv4' or 'dualPreferIPv6' or 'dualBoth']: IP Version for Server Communication (OnGuard),ip_version_native (string, optional) = ['IPv4Only' or 'IPv6Only' or 'dualPreferIPv4' or 'dualPreferIPv6']: IP Version for Server Communication (Native),custom_remediation (object, optional): Customize webpage details for Agent Remediation UI. Input should be in JSON format.}
                Required Body Parameters (type(dict) body example)- {
          "mode": "",
          "interfaces": "",
          "web_agent_interfaces": "",
          "auth_type": "",
          "field_username_caption": "",
          "field_password_caption": "",
          "cert_filter_criteria": "",
          "upgrade_action": "",
          "install_vpn_component": false,
          "version": "",
          "agentLibraryVersion": "",
          "installer_modified_time": "",
          "installer_modified_time_formatted": "",
          "agent_installers": "object",
          "agent_web_installers": "object",
          "ip_version_onguard": "",
          "ip_version_native": "",
          "custom_remediation": "object"
        }
        """
        url_path = "/onguard/policy-manager-zones"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def new_onguard_policy_manager_zones(self, body=({})):
        """
                Operation: Post Policy Manager Zones with associated authentication server IP addresses
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- OnGuardZoneMappingCreate {policy_manager_zone_name (string): Name of the Policy Manager Zone,client_subnets (string): client subnet addresses specific to the Policy Manager zone,override_server_ips (string, optional): IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs}
                Required Body Parameters (type(dict) body example)- {
          "policy_manager_zone_name": "",
          "client_subnets": "",
          "override_server_ips": ""
        }
        """
        url_path = "/onguard/policy-manager-zones"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_onguard_policy_manager_zones_by_policy_manager_zones_id(
        self, policy_manager_zones_id=""
    ):
        """
        Operation: Get Client Subnets and Server IPs for Policy Manager Zone
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/{policy_manager_zones_id}"
        dict_path = {"policy_manager_zones_id": policy_manager_zones_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onguard_policy_manager_zones_by_policy_manager_zones_id(
        self, policy_manager_zones_id="", body=({})
    ):
        """
                Operation: Update authentication server IP addresses for Policy Manager Zone
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
                Required Body Parameters (body description)- OnGuardZoneMappingUpdate {client_subnets (string, optional): client subnet addresses specific to the Policy Manager zone,override_server_ips (string, optional): IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs}
                Required Body Parameters (type(dict) body example)- {
          "client_subnets": "",
          "override_server_ips": ""
        }
        """
        url_path = "/onguard/policy-manager-zones/{policy_manager_zones_id}"
        dict_path = {"policy_manager_zones_id": policy_manager_zones_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_onguard_policy_manager_zones_by_policy_manager_zones_id(
        self, policy_manager_zones_id="", body=({})
    ):
        """
                Operation: Post Client Subnets and Server IPs for Policy Manager Zone
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
                Required Body Parameters (body description)- OnGuardZoneMappingReplace {client_subnets (string): client subnet addresses specific to the Policy Manager zone,override_server_ips (string, optional): IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs}
                Required Body Parameters (type(dict) body example)- {
          "client_subnets": "",
          "override_server_ips": ""
        }
        """
        url_path = "/onguard/policy-manager-zones/{policy_manager_zones_id}"
        dict_path = {"policy_manager_zones_id": policy_manager_zones_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_onguard_policy_manager_zones_by_policy_manager_zones_id(
        self, policy_manager_zones_id=""
    ):
        """
        Operation: Delete authentication server IP addresses for Policy Manager Zone
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/{policy_manager_zones_id}"
        dict_path = {"policy_manager_zones_id": policy_manager_zones_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_onguard_policy_manager_zones_name_by_name(self, name=""):
        """
        Operation: Get Client Subnets and Server IPs for Policy Manager Zone by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onguard_policy_manager_zones_name_by_name(self, name="", body=({})):
        """
                Operation: Update authentication server IP addresses for Policy Manager Zone by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the policy manager zone
                Required Body Parameters (body description)- OnGuardZoneMappingUpdate {client_subnets (string, optional): client subnet addresses specific to the Policy Manager zone,override_server_ips (string, optional): IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs}
                Required Body Parameters (type(dict) body example)- {
          "client_subnets": "",
          "override_server_ips": ""
        }
        """
        url_path = "/onguard/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_onguard_policy_manager_zones_name_by_name(self, name="", body=({})):
        """
                Operation: Post Client Subnets and Server IPs for Policy Manager Zone by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: Unique name of the policy manager zone
                Required Body Parameters (body description)- OnGuardZoneMappingReplace {client_subnets (string): client subnet addresses specific to the Policy Manager zone,override_server_ips (string, optional): IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs}
                Required Body Parameters (type(dict) body example)- {
          "client_subnets": "",
          "override_server_ips": ""
        }
        """
        url_path = "/onguard/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_onguard_policy_manager_zones_name_by_name(self, name=""):
        """
        Operation: Delete authentication server IP addresses for Policy Manager Zone by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:ProfilerSubnetMapping
    # Function Section Description: Manage profiler subnet mappings

    def get_profiler_subnet_mapping(self, name=""):
        """
        Operation: Get a list of profiler subnet mappings
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/profiler-subnet-mapping"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_profiler_subnet_mapping(self, body=({})):
        """
                Operation: Add a profiler subnet mapping
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ProfilerSubnetMappingCreate {network (string): IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"),scan_type (string) = ['WMI' or 'SSH' or 'SNMP']: Scan type of Profiler Subnet Mapping,ext_accounts (array[string]): List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI)}
                Required Body Parameters (type(dict) body example)- {
          "network": "",
          "scan_type": "",
          "ext_accounts": [
            ""
          ]
        }
        """
        url_path = "/profiler-subnet-mapping"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_profiler_subnet_mapping_by_scan_type_profiler_subnet_mapping_id(
        self, scan_type="", profiler_subnet_mapping_id=""
    ):
        """
        Operation: Get a profiler subnet mapping
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Required Path Parameter Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/{profiler_subnet_mapping_id}"
        dict_path = {
            "scan_type": scan_type,
            "profiler_subnet_mapping_id": profiler_subnet_mapping_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_profiler_subnet_mapping_by_scan_type_profiler_subnet_mapping_id(
        self, scan_type="", profiler_subnet_mapping_id="", body=({})
    ):
        """
                Operation: Update some fields of a profiler subnet mapping
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
                Required Path Parameter Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
                Required Body Parameters (body description)- ProfilerSubnetMappingUpdate {network (string, optional): IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"),scan_type (string, optional) = ['WMI' or 'SSH' or 'SNMP']: Scan type of Profiler Subnet Mapping,ext_accounts (array[string], optional): List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI)}
                Required Body Parameters (type(dict) body example)- {
          "network": "",
          "scan_type": "",
          "ext_accounts": [
            ""
          ]
        }
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/{profiler_subnet_mapping_id}"
        dict_path = {
            "scan_type": scan_type,
            "profiler_subnet_mapping_id": profiler_subnet_mapping_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_profiler_subnet_mapping_by_scan_type_profiler_subnet_mapping_id(
        self, scan_type="", profiler_subnet_mapping_id="", body=({})
    ):
        """
                Operation: Replace a profiler subnet mapping
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
                Required Path Parameter Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
                Required Body Parameters (body description)- ProfilerSubnetMappingReplace {network (string): IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"),scan_type (string) = ['WMI' or 'SSH' or 'SNMP']: Scan type of Profiler Subnet Mapping,ext_accounts (array[string]): List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI)}
                Required Body Parameters (type(dict) body example)- {
          "network": "",
          "scan_type": "",
          "ext_accounts": [
            ""
          ]
        }
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/{profiler_subnet_mapping_id}"
        dict_path = {
            "scan_type": scan_type,
            "profiler_subnet_mapping_id": profiler_subnet_mapping_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_profiler_subnet_mapping_by_scan_type_profiler_subnet_mapping_id(
        self, scan_type="", profiler_subnet_mapping_id=""
    ):
        """
        Operation: Delete a profiler subnet mapping
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Required Path Parameter Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/{profiler_subnet_mapping_id}"
        dict_path = {
            "scan_type": scan_type,
            "profiler_subnet_mapping_id": profiler_subnet_mapping_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_profiler_subnet_mapping_by_scan_type_network_network(
        self, scan_type="", network=""
    ):
        """
        Operation: Get a profiler subnet mapping
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Required Path Parameter Name: network, Description: Network of Profiler Subnet Mapping
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/network/{network}"
        dict_path = {"scan_type": scan_type, "network": network}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_profiler_subnet_mapping_by_scan_type_network_network(
        self, scan_type="", network="", body=({})
    ):
        """
                Operation: Update some fields of a profiler subnet mapping
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
                Required Path Parameter Name: network, Description: Network of Profiler Subnet Mapping
                Required Body Parameters (body description)- ProfilerSubnetMappingUpdate {network (string, optional): IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"),scan_type (string, optional) = ['WMI' or 'SSH' or 'SNMP']: Scan type of Profiler Subnet Mapping,ext_accounts (array[string], optional): List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI)}
                Required Body Parameters (type(dict) body example)- {
          "network": "",
          "scan_type": "",
          "ext_accounts": [
            ""
          ]
        }
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/network/{network}"
        dict_path = {"scan_type": scan_type, "network": network}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_profiler_subnet_mapping_by_scan_type_network_network(
        self, scan_type="", network="", body=({})
    ):
        """
                Operation: Replace a profiler subnet mapping
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
                Required Path Parameter Name: network, Description: Network of Profiler Subnet Mapping
                Required Body Parameters (body description)- ProfilerSubnetMappingReplace {network (string): IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"),scan_type (string) = ['WMI' or 'SSH' or 'SNMP']: Scan type of Profiler Subnet Mapping,ext_accounts (array[string]): List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI)}
                Required Body Parameters (type(dict) body example)- {
          "network": "",
          "scan_type": "",
          "ext_accounts": [
            ""
          ]
        }
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/network/{network}"
        dict_path = {"scan_type": scan_type, "network": network}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_profiler_subnet_mapping_by_scan_type_network_network(
        self, scan_type="", network=""
    ):
        """
        Operation: Delete a profiler subnet mapping
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Required Path Parameter Name: network, Description: Network of Profiler Subnet Mapping
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/network/{network}"
        dict_path = {"scan_type": scan_type, "network": network}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:WindowsHotfix
    # Function Section Description: Manage Windows Hotfix

    def get_windows_hotfix(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Windows Hotfixes
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/windows-hotfix"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_windows_hotfix(self, body=({})):
        """
                Operation: Add a Windows Hotfix
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- WindowsHotfixCreate {kbid (string): KBID of the windows hotfix,operating_system (string) = ['Windows 10' or 'Windows 11' or 'Windows 7' or 'Windows 8' or 'Windows Server 2008' or 'Windows Server 2012' or 'Windows Server 2016' or 'Windows Server 2019']: OS of the windows hotfix,title (string): Title of the windows hotfix,severity_rating (string) = ['Critical' or 'Important' or 'Low' or 'Moderate' or 'Unspecified']: Severity rating of the windows hotfix,superseded_by (string, optional): Superseded_by of the windows hotfix,superseding (string, optional): Superseding of the windows hotfix,reboot_behavior (string, optional) = ['' or 'AlwaysRequiresReboot' or 'CanRequestReboot' or 'NeverReboots']: Reboot Behavior of the windows hotfix,release_date (string, optional): Release Date of the windows hotfix,url (string, optional): URL of the windows hotfix,description (string, optional): Description of the windows hotfix}
                Required Body Parameters (type(dict) body example)- {
          "kbid": "",
          "operating_system": "",
          "title": "",
          "severity_rating": "",
          "superseded_by": "",
          "superseding": "",
          "reboot_behavior": "",
          "release_date": "",
          "url": "",
          "description": ""
        }
        """
        url_path = "/windows-hotfix"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_windows_hotfix_by_windows_hotfix_id(self, windows_hotfix_id=""):
        """
        Operation: Get a windows hotfix
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
        """
        url_path = "/windows-hotfix/{windows_hotfix_id}"
        dict_path = {"windows_hotfix_id": windows_hotfix_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_windows_hotfix_by_windows_hotfix_id(
        self, windows_hotfix_id="", body=({})
    ):
        """
                Operation: Update some fields of a windows hotfix
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
                Required Body Parameters (body description)- WindowsHotfixUpdate {kbid (string, optional): KBID of the windows hotfix,operating_system (string, optional) = ['Windows 10' or 'Windows 11' or 'Windows 7' or 'Windows 8' or 'Windows Server 2008' or 'Windows Server 2012' or 'Windows Server 2016' or 'Windows Server 2019']: OS of the windows hotfix,title (string, optional): Title of the windows hotfix,severity_rating (string, optional) = ['Critical' or 'Important' or 'Low' or 'Moderate' or 'Unspecified']: Severity rating of the windows hotfix,superseded_by (string, optional): Superseded_by of the windows hotfix,superseding (string, optional): Superseding of the windows hotfix,reboot_behavior (string, optional) = ['' or 'AlwaysRequiresReboot' or 'CanRequestReboot' or 'NeverReboots']: Reboot Behavior of the windows hotfix,release_date (string, optional): Release Date of the windows hotfix,url (string, optional): URL of the windows hotfix,description (string, optional): Description of the windows hotfix}
                Required Body Parameters (type(dict) body example)- {
          "kbid": "",
          "operating_system": "",
          "title": "",
          "severity_rating": "",
          "superseded_by": "",
          "superseding": "",
          "reboot_behavior": "",
          "release_date": "",
          "url": "",
          "description": ""
        }
        """
        url_path = "/windows-hotfix/{windows_hotfix_id}"
        dict_path = {"windows_hotfix_id": windows_hotfix_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_windows_hotfix_by_windows_hotfix_id(
        self, windows_hotfix_id="", body=({})
    ):
        """
                Operation: Replace a windows hotfix
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
                Required Body Parameters (body description)- WindowsHotfixReplace {kbid (string): KBID of the windows hotfix,operating_system (string) = ['Windows 10' or 'Windows 11' or 'Windows 7' or 'Windows 8' or 'Windows Server 2008' or 'Windows Server 2012' or 'Windows Server 2016' or 'Windows Server 2019']: OS of the windows hotfix,title (string): Title of the windows hotfix,severity_rating (string) = ['Critical' or 'Important' or 'Low' or 'Moderate' or 'Unspecified']: Severity rating of the windows hotfix,superseded_by (string, optional): Superseded_by of the windows hotfix,superseding (string, optional): Superseding of the windows hotfix,reboot_behavior (string, optional) = ['' or 'AlwaysRequiresReboot' or 'CanRequestReboot' or 'NeverReboots']: Reboot Behavior of the windows hotfix,release_date (string, optional): Release Date of the windows hotfix,url (string, optional): URL of the windows hotfix,description (string, optional): Description of the windows hotfix}
                Required Body Parameters (type(dict) body example)- {
          "kbid": "",
          "operating_system": "",
          "title": "",
          "severity_rating": "",
          "superseded_by": "",
          "superseding": "",
          "reboot_behavior": "",
          "release_date": "",
          "url": "",
          "description": ""
        }
        """
        url_path = "/windows-hotfix/{windows_hotfix_id}"
        dict_path = {"windows_hotfix_id": windows_hotfix_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_windows_hotfix_by_windows_hotfix_id(self, windows_hotfix_id=""):
        """
        Operation: Delete a windows hotfix
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
        """
        url_path = "/windows-hotfix/{windows_hotfix_id}"
        dict_path = {"windows_hotfix_id": windows_hotfix_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_windows_hotfix_kbid_by_kbid_operating_system_operating_system(
        self, kbid="", operating_system=""
    ):
        """
        Operation: Get a windows hotfix by kbid and os
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: kbid, Description: KBID of the hotfix
        Required Path Parameter Name: operating_system, Description: Operating system of the hotfix
        """
        url_path = "/windows-hotfix/kbid/{kbid}/operating_system/{operating_system}"
        dict_path = {"kbid": kbid, "operating_system": operating_system}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_windows_hotfix_kbid_by_kbid_operating_system_operating_system(
        self, kbid="", operating_system="", body=({})
    ):
        """
                Operation: Update some fields of a windows hotfix by kbid and os
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: kbid, Description: KBID of the hotfix
                Required Path Parameter Name: operating_system, Description: Operating system of the hotfix
                Required Body Parameters (body description)- WindowsHotfixUpdate {kbid (string, optional): KBID of the windows hotfix,operating_system (string, optional) = ['Windows 10' or 'Windows 11' or 'Windows 7' or 'Windows 8' or 'Windows Server 2008' or 'Windows Server 2012' or 'Windows Server 2016' or 'Windows Server 2019']: OS of the windows hotfix,title (string, optional): Title of the windows hotfix,severity_rating (string, optional) = ['Critical' or 'Important' or 'Low' or 'Moderate' or 'Unspecified']: Severity rating of the windows hotfix,superseded_by (string, optional): Superseded_by of the windows hotfix,superseding (string, optional): Superseding of the windows hotfix,reboot_behavior (string, optional) = ['' or 'AlwaysRequiresReboot' or 'CanRequestReboot' or 'NeverReboots']: Reboot Behavior of the windows hotfix,release_date (string, optional): Release Date of the windows hotfix,url (string, optional): URL of the windows hotfix,description (string, optional): Description of the windows hotfix}
                Required Body Parameters (type(dict) body example)- {
          "kbid": "",
          "operating_system": "",
          "title": "",
          "severity_rating": "",
          "superseded_by": "",
          "superseding": "",
          "reboot_behavior": "",
          "release_date": "",
          "url": "",
          "description": ""
        }
        """
        url_path = "/windows-hotfix/kbid/{kbid}/operating_system/{operating_system}"
        dict_path = {"kbid": kbid, "operating_system": operating_system}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_windows_hotfix_kbid_by_kbid_operating_system_operating_system(
        self, kbid="", operating_system="", body=({})
    ):
        """
                Operation: Replace a windows hotfix by kbid and os
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: kbid, Description: KBID of the hotfix
                Required Path Parameter Name: operating_system, Description: Operating system of the hotfix
                Required Body Parameters (body description)- WindowsHotfixReplace {kbid (string): KBID of the windows hotfix,operating_system (string) = ['Windows 10' or 'Windows 11' or 'Windows 7' or 'Windows 8' or 'Windows Server 2008' or 'Windows Server 2012' or 'Windows Server 2016' or 'Windows Server 2019']: OS of the windows hotfix,title (string): Title of the windows hotfix,severity_rating (string) = ['Critical' or 'Important' or 'Low' or 'Moderate' or 'Unspecified']: Severity rating of the windows hotfix,superseded_by (string, optional): Superseded_by of the windows hotfix,superseding (string, optional): Superseding of the windows hotfix,reboot_behavior (string, optional) = ['' or 'AlwaysRequiresReboot' or 'CanRequestReboot' or 'NeverReboots']: Reboot Behavior of the windows hotfix,release_date (string, optional): Release Date of the windows hotfix,url (string, optional): URL of the windows hotfix,description (string, optional): Description of the windows hotfix}
                Required Body Parameters (type(dict) body example)- {
          "kbid": "",
          "operating_system": "",
          "title": "",
          "severity_rating": "",
          "superseded_by": "",
          "superseding": "",
          "reboot_behavior": "",
          "release_date": "",
          "url": "",
          "description": ""
        }
        """
        url_path = "/windows-hotfix/kbid/{kbid}/operating_system/{operating_system}"
        dict_path = {"kbid": kbid, "operating_system": operating_system}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_windows_hotfix_kbid_by_kbid_operating_system_operating_system(
        self, kbid="", operating_system=""
    ):
        """
        Operation: Delete a windows hotfix by kbid and os
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: kbid, Description: KBID of the hotfix
        Required Path Parameter Name: operating_system, Description: Operating system of the hotfix
        """
        url_path = "/windows-hotfix/kbid/{kbid}/operating_system/{operating_system}"
        dict_path = {"kbid": kbid, "operating_system": operating_system}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
