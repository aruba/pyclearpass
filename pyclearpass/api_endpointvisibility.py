from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: EndpointVisibility
# FileName: api_endpointvisibility.py


class ApiEndpointVisibility(ClearPassAPILogin):
    # API Service: Manage Agentless OnGuard settings
    def get_agentless_onguard_settings(self):
        """
        Operation: Get a list of Agentless OnGuard Settings
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/agentless-onguard/settings"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_agentless_onguard_settings(self, body=({})):
        """
        Operation: Add an Agentless OnGuard Setting
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'client_os', 'working_dir', 'action', 'servers', 'download_url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Setting. Object Type: string
        "description" : "", #Description of Agentless OnGuard Setting. Object Type: string
        "client_os" : "", #Client OS type. Allowed Values: Windows, macOS and Linux. Object Type: string
        "domain_account" : "", #Name of domain account used to launch Agentless OnGuard on endpoints. Object Type: string
        "ssh_account" : "", #Name of ssh account used to launch Agentless OnGuard on endpoints. Object Type: string
        "working_dir" : "", #Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard). Object Type: string
        "action" : "", #Action to be performed on endpoints. Object Type: string
        "servers" : "", #IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]). Object Type: array
        "download_url" : "", #HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe). Object Type: string
        "validate_url_cert" : False, #Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true). Object Type: boolean
        "override_checksum" : False, #Override checksum fields (default=false). Object Type: boolean
        "checksums_32" : False, #SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs. Object Type: array
        "checksums_64" : False, #SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs. Object Type: array

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Setting. Object Type: string
        "description" : "", #Description of Agentless OnGuard Setting. Object Type: string
        "client_os" : "", #Client OS type. Allowed Values: Windows, macOS and Linux. Object Type: string
        "domain_account" : "", #Name of domain account used to launch Agentless OnGuard on endpoints. Object Type: string
        "ssh_account" : "", #Name of ssh account used to launch Agentless OnGuard on endpoints. Object Type: string
        "working_dir" : "", #Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard). Object Type: string
        "action" : "", #Action to be performed on endpoints. Object Type: string
        "servers" : "", #IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]). Object Type: array
        "download_url" : "", #HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe). Object Type: string
        "validate_url_cert" : False, #Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true). Object Type: boolean
        "override_checksum" : False, #Override checksum fields (default=false). Object Type: boolean
        "checksums_32" : False, #SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs. Object Type: array
        "checksums_64" : False, #SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs. Object Type: array

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
        Required Body Parameters:['name', 'client_os', 'working_dir', 'action', 'servers', 'download_url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Setting. Object Type: string
        "description" : "", #Description of Agentless OnGuard Setting. Object Type: string
        "client_os" : "", #Client OS type. Allowed Values: Windows, macOS and Linux. Object Type: string
        "domain_account" : "", #Name of domain account used to launch Agentless OnGuard on endpoints. Object Type: string
        "ssh_account" : "", #Name of ssh account used to launch Agentless OnGuard on endpoints. Object Type: string
        "working_dir" : "", #Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard). Object Type: string
        "action" : "", #Action to be performed on endpoints. Object Type: string
        "servers" : "", #IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]). Object Type: array
        "download_url" : "", #HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe). Object Type: string
        "validate_url_cert" : False, #Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true). Object Type: boolean
        "override_checksum" : False, #Override checksum fields (default=false). Object Type: boolean
        "checksums_32" : False, #SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs. Object Type: array
        "checksums_64" : False, #SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs. Object Type: array

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: settings_id, Description: Numeric ID of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/{settings_id}"
        dict_path = {"settings_id": settings_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_agentless_onguard_settings_name_by_name(self, name=""):
        """
        Operation: Get an Agentless OnGuard Setting by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_agentless_onguard_settings_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an Agentless OnGuard Setting by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of Agentless OnGuard Setting
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Setting. Object Type: string
        "description" : "", #Description of Agentless OnGuard Setting. Object Type: string
        "client_os" : "", #Client OS type. Allowed Values: Windows, macOS and Linux. Object Type: string
        "domain_account" : "", #Name of domain account used to launch Agentless OnGuard on endpoints. Object Type: string
        "ssh_account" : "", #Name of ssh account used to launch Agentless OnGuard on endpoints. Object Type: string
        "working_dir" : "", #Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard). Object Type: string
        "action" : "", #Action to be performed on endpoints. Object Type: string
        "servers" : "", #IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]). Object Type: array
        "download_url" : "", #HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe). Object Type: string
        "validate_url_cert" : False, #Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true). Object Type: boolean
        "override_checksum" : False, #Override checksum fields (default=false). Object Type: boolean
        "checksums_32" : False, #SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs. Object Type: array
        "checksums_64" : False, #SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs. Object Type: array

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of Agentless OnGuard Setting
        Required Body Parameters:['name', 'client_os', 'working_dir', 'action', 'servers', 'download_url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Setting. Object Type: string
        "description" : "", #Description of Agentless OnGuard Setting. Object Type: string
        "client_os" : "", #Client OS type. Allowed Values: Windows, macOS and Linux. Object Type: string
        "domain_account" : "", #Name of domain account used to launch Agentless OnGuard on endpoints. Object Type: string
        "ssh_account" : "", #Name of ssh account used to launch Agentless OnGuard on endpoints. Object Type: string
        "working_dir" : "", #Full path of directory on endpoints where all files required to start Agentless OnGuard will be copied (e.g. C:\OnGuard). Object Type: string
        "action" : "", #Action to be performed on endpoints. Object Type: string
        "servers" : "", #IP addresses or FQDN of ClearPass servers that Agentless OnGuard should use to read agent settings (e.g. ["hostname.example.com", "1.2.3.4"]). Object Type: array
        "download_url" : "", #HTTP/HTTPS URL to download Agentless OnGuardWrapper EXE from the Remote File Server (e.g. https://10.20.30.40/agent/AgentlessOnGuard/windows/AgentlessOnGuardWrapper.exe). Object Type: string
        "validate_url_cert" : False, #Should Agentless OnGuard Launcher validate the Server Certificate of the remote server while downloading Agentless OnGuardWrapper EXE? (default=true). Object Type: boolean
        "override_checksum" : False, #Override checksum fields (default=false). Object Type: boolean
        "checksums_32" : False, #SHA256 checksums of 32-bit Agentless OnGuard Wrapper EXEs. Object Type: array
        "checksums_64" : False, #SHA256 checksums of 64-bit Agentless OnGuard Wrapper EXEs. Object Type: array

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of Agentless OnGuard Setting
        """
        url_path = "/agentless-onguard/settings/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Agentless OnGuard subnet mappings
    def get_agentless_onguard_subnet_mapping(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of subnet mappings
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'client_subnets', 'zone', 'client_scan_setting']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Subnet Mapping. Object Type: string
        "client_subnets" : "", #IP subnets used for selecting clients. Object Type: array
        "zone" : "", #Name of Policy Manager Zone for which the specified client subnet is applicable. Object Type: string
        "agentless_onguard_setting_windows" : "", #Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_macOS" : "", #Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_linux" : "", #Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string. Object Type: string
        "client_scan_setting" : "", #Clients to be scanned in the subnet. Object Type: string
        "enabled" : False, #Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true). Object Type: boolean

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Subnet Mapping. Object Type: string
        "client_subnets" : "", #IP subnets used for selecting clients. Object Type: array
        "zone" : "", #Name of Policy Manager Zone for which the specified client subnet is applicable. Object Type: string
        "agentless_onguard_setting_windows" : "", #Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_macOS" : "", #Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_linux" : "", #Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string. Object Type: string
        "client_scan_setting" : "", #Clients to be scanned in the subnet. Object Type: string
        "enabled" : False, #Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true). Object Type: boolean

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        Required Body Parameters:['name', 'client_subnets', 'zone', 'client_scan_setting']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Subnet Mapping. Object Type: string
        "client_subnets" : "", #IP subnets used for selecting clients. Object Type: array
        "zone" : "", #Name of Policy Manager Zone for which the specified client subnet is applicable. Object Type: string
        "agentless_onguard_setting_windows" : "", #Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_macOS" : "", #Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_linux" : "", #Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string. Object Type: string
        "client_scan_setting" : "", #Clients to be scanned in the subnet. Object Type: string
        "enabled" : False, #Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true). Object Type: boolean

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_agentless_onguard_subnet_mapping_name_by_name(self, name=""):
        """
        Operation: Get a subnet mapping by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_agentless_onguard_subnet_mapping_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of a subnet mapping by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of subnet mapping
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Subnet Mapping. Object Type: string
        "client_subnets" : "", #IP subnets used for selecting clients. Object Type: array
        "zone" : "", #Name of Policy Manager Zone for which the specified client subnet is applicable. Object Type: string
        "agentless_onguard_setting_windows" : "", #Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_macOS" : "", #Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_linux" : "", #Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string. Object Type: string
        "client_scan_setting" : "", #Clients to be scanned in the subnet. Object Type: string
        "enabled" : False, #Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true). Object Type: boolean

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of subnet mapping
        Required Body Parameters:['name', 'client_subnets', 'zone', 'client_scan_setting']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Agentless OnGuard Subnet Mapping. Object Type: string
        "client_subnets" : "", #IP subnets used for selecting clients. Object Type: array
        "zone" : "", #Name of Policy Manager Zone for which the specified client subnet is applicable. Object Type: string
        "agentless_onguard_setting_windows" : "", #Name of Agentless OnGuard setting for Windows for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_macOS" : "", #Name of Agentless OnGuard setting for macOS for the specified subnet and zone. To unset, use empty string. Object Type: string
        "agentless_onguard_setting_linux" : "", #Name of Agentless OnGuard setting for Linux for the specified subnet and zone. To unset, use empty string. Object Type: string
        "client_scan_setting" : "", #Clients to be scanned in the subnet. Object Type: string
        "enabled" : False, #Enable Clearpass server to process clients in the subnet and run Agentless OnGuard (default=true). Object Type: boolean

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of subnet mapping
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: subnet_mapping_id, Description: Numeric ID of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/{subnet_mapping_id}/disable"
        dict_path = {"subnet_mapping_id": subnet_mapping_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_agentless_onguard_subnet_mapping_name_by_name_enable(self, name=""):
        """
        Operation: Enable Agentless OnGuard Settings on client subnets by subnet mapping name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}/enable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_agentless_onguard_subnet_mapping_name_by_name_disable(self, name=""):
        """
        Operation: Disable Agentless OnGuard Settings on client subnets by subnet mapping name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of subnet mapping
        """
        url_path = "/agentless-onguard/subnet-mapping/name/{name}/disable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # API Service: Manage Device Fingerprint Profiling
    def new_device_profiler_device_fingerprint(self, body=({})):
        """
        Operation: Post device fingerprint attributes for profiling
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mac" : "", #MAC address of device. Object Type: string
        "ip" : "", #IP address of device. Object Type: string
        "hostname" : "", #Hostname of device. Object Type: string
        "dhcp" : "", #DHCP attributes as JSON. Object Type: DHCPAttributes
        "active_sync" : "", #Active Sync attributes as JSON. Object Type: ActiveSyncAttributes
        "host" : "", #Host attributes as JSON. Object Type: HostAttributes
        "snmp" : "", #SNMP attributes as JSON. Object Type: SNMPAttributes
        "device" : "", #Device attributes as JSON. Object Type: DeviceAttributes
        "tcp" : "", #TCP attributes as JSON. Object Type: TCPAttributes
        "nmap" : "", #NMAP attributes as JSON. Object Type: NMAPAttributes
        "ssh" : "", #SSH attributes as JSON. Object Type: SSHAttributes
        "wmi" : "", #WMI attributes as JSON. Object Type: WMIAttributes
        "ports" : "", #Port attributes as JSON. Object Type: PortsAttributes

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: mac_or_ip, Description: MAC or IP address of device
        """
        url_path = "/device-profiler/device-fingerprint/{mac_or_ip}"
        dict_path = {"mac_or_ip": mac_or_ip}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_device_profiler_device_fingerprint_by_mac_or_ip(self, mac_or_ip=""):
        """
        Operation: Delete fingerprint of profiled device
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: mac_or_ip, Description: URL parameter mac_or_ip
        """
        url_path = "/device-profiler/device-fingerprint/{mac_or_ip}"
        dict_path = {"mac_or_ip": mac_or_ip}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Fingerprints
    def get_fingerprint(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Fingerprints
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['category', 'family', 'name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "category" : "", #Category name of the fingerprint. Object Type: string
        "family" : "", #Family name of the fingerprint. Object Type: string
        "name" : "", #Unique name of the fingerprint. Object Type: string

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: fingerprint_id, Description: Numeric ID of the fingerprint
        """
        url_path = "/fingerprint/{fingerprint_id}"
        dict_path = {"fingerprint_id": fingerprint_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_fingerprint_by_fingerprint_id(self, fingerprint_id="", body=({})):
        """
        Operation: Update some fields of a Fingerprint
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: fingerprint_id, Description: Numeric ID of the fingerprint
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "category" : "", #Category name of the fingerprint. Object Type: string
        "family" : "", #Family name of the fingerprint. Object Type: string
        "name" : "", #Unique name of the fingerprint. Object Type: string

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: fingerprint_id, Description: Numeric ID of the fingerprint
        Required Body Parameters:['category', 'family', 'name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "category" : "", #Category name of the fingerprint. Object Type: string
        "family" : "", #Family name of the fingerprint. Object Type: string
        "name" : "", #Unique name of the fingerprint. Object Type: string

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: fingerprint_id, Description: Numeric ID of the fingerprint
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: category, Description: Category name of the fingerprint
        Parameter Type: path, Name: family, Description: family name of the fingerprint
        Parameter Type: path, Name: name, Description: Unique name of the fingerprint
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: category, Description: Category name of the fingerprint
        Parameter Type: path, Name: family, Description: family name of the fingerprint
        Parameter Type: path, Name: name, Description: Unique name of the fingerprint
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "category" : "", #Category name of the fingerprint. Object Type: string
        "family" : "", #Family name of the fingerprint. Object Type: string
        "name" : "", #Unique name of the fingerprint. Object Type: string

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: category, Description: Category name of the fingerprint
        Parameter Type: path, Name: family, Description: family name of the fingerprint
        Parameter Type: path, Name: name, Description: Unique name of the fingerprint
        Required Body Parameters:['category', 'family', 'name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "category" : "", #Category name of the fingerprint. Object Type: string
        "family" : "", #Family name of the fingerprint. Object Type: string
        "name" : "", #Unique name of the fingerprint. Object Type: string

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: category, Description: Category name of the fingerprint
        Parameter Type: path, Name: family, Description: family name of the fingerprint
        Parameter Type: path, Name: name, Description: Unique name of the fingerprint
        """
        url_path = "/fingerprint/name/{category}/{family}/{name}"
        dict_path = {"category": category, "family": family, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage NetworkScan Services
    def get_config_network_scan(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of NetworkScan
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['type', 'zone', 'seed_device_or_ip_subnet', 'scan_frequency']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "zone" : "", #Zone for the Network Scan. Object Type: string
        "type" : "", #Type of the Network Scan. Object Type: string
        "seed_device_or_ip_subnet" : "", #Network IP for DISCOVERY (e.g. ["hostname.example.com", "1.2.3.4"]) or IP Subnets for SUBNET (e.g. ["10.1.0.0/16"]) Network Scan. Object Type: string
        "scan_frequency" : "", #Frequency of Network Scan. Object Type: string
        "start_time" : "", #Start time (HH:MM) of Network Scan  (e.g. ["10:40", "23:20"]). Object Type: string
        "interval" : 0, #Interval in hours (3 - 350) for HOURLY Network Scan. Object Type: integer
        "day_of_week" : "", #Day of Week for WEEKLY Network Scan. Object Type: string
        "depth" : 0, #Depth level for DISCOVERY Network Scan. Object Type: integer
        "probe_arp" : False, #Probe all ARP entries found (default=false for type="DISCOVERY", not applicable for type="SUBNET"). Object Type: boolean
        "enabled" : False, #Is Network Scan enabled? (default=true). Object Type: boolean

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_config_network_scan_by_scan_id(self, scan_id="", body=({})):
        """
        Operation: Update some fields of a NetworkScan
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_id, Description: Numeric ID of the NetworkScan
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "zone" : "", #Zone for the Network Scan. Object Type: string
        "type" : "", #Type of the Network Scan. Object Type: string
        "seed_device_or_ip_subnet" : "", #Network IP for DISCOVERY (e.g. ["hostname.example.com", "1.2.3.4"]) or IP Subnets for SUBNET (e.g. ["10.1.0.0/16"]) Network Scan. Object Type: string
        "scan_frequency" : "", #Frequency of Network Scan. Object Type: string
        "start_time" : "", #Start time (HH:MM) of Network Scan  (e.g. ["10:40", "23:20"]). Object Type: string
        "interval" : 0, #Interval in hours (3 - 350) for HOURLY Network Scan. Object Type: integer
        "day_of_week" : "", #Day of Week for WEEKLY Network Scan. Object Type: string
        "depth" : 0, #Depth level for DISCOVERY Network Scan. Object Type: integer
        "probe_arp" : False, #Probe all ARP entries found (default=false for type="DISCOVERY", not applicable for type="SUBNET"). Object Type: boolean
        "enabled" : False, #Is Network Scan enabled? (default=true). Object Type: boolean

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_id, Description: Numeric ID of the NetworkScan
        Required Body Parameters:['type', 'zone', 'seed_device_or_ip_subnet', 'scan_frequency']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "zone" : "", #Zone for the Network Scan. Object Type: string
        "type" : "", #Type of the Network Scan. Object Type: string
        "seed_device_or_ip_subnet" : "", #Network IP for DISCOVERY (e.g. ["hostname.example.com", "1.2.3.4"]) or IP Subnets for SUBNET (e.g. ["10.1.0.0/16"]) Network Scan. Object Type: string
        "scan_frequency" : "", #Frequency of Network Scan. Object Type: string
        "start_time" : "", #Start time (HH:MM) of Network Scan  (e.g. ["10:40", "23:20"]). Object Type: string
        "interval" : 0, #Interval in hours (3 - 350) for HOURLY Network Scan. Object Type: integer
        "day_of_week" : "", #Day of Week for WEEKLY Network Scan. Object Type: string
        "depth" : 0, #Depth level for DISCOVERY Network Scan. Object Type: integer
        "probe_arp" : False, #Probe all ARP entries found (default=false for type="DISCOVERY", not applicable for type="SUBNET"). Object Type: boolean
        "enabled" : False, #Is Network Scan enabled? (default=true). Object Type: boolean

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_config_network_scan_by_scan_id_enable(self, scan_id=""):
        """
        Operation: Update some fields of a NetworkScan
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}/enable"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_config_network_scan_by_scan_id_disable(self, scan_id=""):
        """
        Operation: Update some fields of a NetworkScan
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_id, Description: Numeric ID of the NetworkScan
        """
        url_path = "/config/network-scan/{scan_id}/disable"
        dict_path = {"scan_id": scan_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # API Service: Manage OnGuard Activity
    def get_onguard_activity(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Clearpass OnGuard Endpoints
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: onguard_activity_id, Description: Numeric ID of the OnGuard Activity
        """
        url_path = "/onguard-activity/{onguard_activity_id}"
        dict_path = {"onguard_activity_id": onguard_activity_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_onguard_activity_host_mac_by_host_mac(self, host_mac=""):
        """
        Operation: Get a Clearpass OnGuard Endpoint Details by host_mac
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: host_mac, Description: MAC Address of the agent
        """
        url_path = "/onguard-activity/host_mac/{host_mac}"
        dict_path = {"host_mac": host_mac}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_activity_message(self, body=({})):
        """
        Operation: Send/Broadcast Message
        HTTP Response Codes: 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['host_mac_list', 'message', 'is_broadcast']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_mac_list" : {}, #List of host MAC Address. Object Type: object
        "message" : "", #Message. Object Type: string
        "info_url" : "", #URL. Object Type: string
        "is_broadcast" : False, #Is a broadcast. Object Type: boolean

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
        HTTP Response Codes: 201 Created, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['host_mac_list', 'message', 'is_broadcast', 'action']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "host_mac_list" : {}, #List of host MAC Address. Object Type: object
        "message" : "", #Message. Object Type: string
        "info_url" : "", #URL. Object Type: string
        "is_broadcast" : False, #Is a broadcast. Object Type: boolean
        "action" : "", #Action. Object Type: string
        "endpoint_status" : "", #Status of the endpoint. Object Type: string

        }
        """
        url_path = "/onguard-activity/notification"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage OnGuard Custom Scripts
    def get_onguard_custom_script(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of OnGuard Custom Scripts
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'os_type', 'script_type', 'attributes']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Custom Script. Object Type: string
        "description" : "", #Description of Custom Script. Object Type: string
        "os_type" : "", #OS Type of Custom Script. Object Type: string
        "script_type" : "", #Type of Custom Script. Object Type: string
        "attributes" : {}, #Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}). Object Type: object
        "output_format" : "", #Output Format of Custom Script, applicable only for health collection scripts. Object Type: string
        "output_details" : {}, #Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}). Object Type: object
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts. Object Type: string
        "rules" : {}, #List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}]). Object Type: object

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Custom Script. Object Type: string
        "description" : "", #Description of Custom Script. Object Type: string
        "attributes" : {}, #Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}). Object Type: object
        "output_format" : "", #Output Format of Custom Script, applicable only for health collection scripts. Object Type: string
        "output_details" : {}, #Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}). Object Type: object
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts. Object Type: string
        "rules" : {}, #List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}]). Object Type: object

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
        Required Body Parameters:['name', 'os_type', 'script_type', 'attributes']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Custom Script. Object Type: string
        "description" : "", #Description of Custom Script. Object Type: string
        "os_type" : "", #OS Type of Custom Script. Object Type: string
        "script_type" : "", #Type of Custom Script. Object Type: string
        "attributes" : {}, #Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}). Object Type: object
        "output_format" : "", #Output Format of Custom Script, applicable only for health collection scripts. Object Type: string
        "output_details" : {}, #Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}). Object Type: object
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts. Object Type: string
        "rules" : {}, #List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}]). Object Type: object

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: onguard_custom_script_id, Description: Numeric ID of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/{onguard_custom_script_id}"
        dict_path = {"onguard_custom_script_id": onguard_custom_script_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_onguard_custom_script_name_by_name(self, name=""):
        """
        Operation: Get an OnGuard Custom Script by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onguard_custom_script_name_by_name(self, name="", body=({})):
        """
        Operation: Update some fields of an OnGuard Custom Script by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of OnGuard Custom Script
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Custom Script. Object Type: string
        "description" : "", #Description of Custom Script. Object Type: string
        "attributes" : {}, #Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}). Object Type: object
        "output_format" : "", #Output Format of Custom Script, applicable only for health collection scripts. Object Type: string
        "output_details" : {}, #Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}). Object Type: object
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts. Object Type: string
        "rules" : {}, #List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}]). Object Type: object

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of OnGuard Custom Script
        Required Body Parameters:['name', 'os_type', 'script_type', 'attributes']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of Custom Script. Object Type: string
        "description" : "", #Description of Custom Script. Object Type: string
        "os_type" : "", #OS Type of Custom Script. Object Type: string
        "script_type" : "", #Type of Custom Script. Object Type: string
        "attributes" : {}, #Attributes of Custom Script, allowed attributes - Path,Command,SHA256,ExecutionLevel,WaitTime,PassResults,SuccessMsg,FailureMsg,ProgressMsg,Description,DownloadURL,ValidateURLCert,ScriptExecutionTimeOut,SignerName (e.g. {"Path": "/home/aruba/scripts","SHA256": "cfd6...f7ca","ExecutionLevel": "User","Command": "runscript.sh","SignerName": "signer"}). Object Type: object
        "output_format" : "", #Output Format of Custom Script, applicable only for health collection scripts. Object Type: string
        "output_details" : {}, #Output Details of Custom Script, applicable only for health collection scripts (e.g. {"ExitCode":"Integer", "OutVar1":"Boolean", "OutVar2":"String"}). Object Type: object
        "rule_eval_algo" : "", #Rule Evaluation Algorithm for rules of Custom Script, applicable only for health collection scripts. Object Type: string
        "rules" : {}, #List of Rules for Custom Script, applicable only for health collection scripts (e.g. [{"match_type":"OR","health_status":"Healthy","condition":[{"type":"Script","name":"ExitCode","oper":"EQUALS","value":"0"}]}]). Object Type: object

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of OnGuard Custom Script
        """
        url_path = "/onguard-custom-script/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage OnGuard global settings
    def get_onguard_global_settings(self):
        """
        Operation: Get OnGuard global settings
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/onguard/global-settings"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_global_settings(self, body=({})):
        """
        Operation: Update OnGuard global settings
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "AllowRemoteDesktopSession" : False, #Enable access over Remote Desktop Session. Object Type: boolean
        "CacheCredentialsForDays" : 0, #Cache Credentials Interval(in days). Object Type: integer
        "EnableClientLoadBalance" : False, #Enable OnGuard requests load-balancing. Object Type: boolean
        "HealthCheckQuietPeriod" : 0, #OnGuard Health Check Interval (in hours). Object Type: integer
        "HideLogoutButton" : False, #Enable to hide Logout button. Object Type: boolean
        "InstallVPNComponent" : False, #Enable to install VPN component. Object Type: boolean
        "KeepAliveIntervalSeconds" : 0, #Keep-alive Interval (in seconds). Object Type: integer
        "LogoutBounceDelay" : 0, #Delay to bounce after Logout (in minutes). Object Type: integer
        "RunOnGuardAs" : "", #Run OnGuard As. Object Type: string
        "ServerCertificateValidation" : "", #Server Certificate Validation. Object Type: string
        "ServerCommunicationMode" : "", #Server Communication Mode. Object Type: string
        "SupportEmailAddress" : "", #Support Team Email Address. Object Type: string
        "UseCurrentOSLanguage" : False, #Use Current OS Language (Windows only). Object Type: boolean
        "UseWindowsCredentials" : False, #Enable to use Windows Single-Sign On. Object Type: boolean
        "VPNDeviceNames" : "", #VPN Device Names (Windows). Object Type: string
        "VPNDeviceNamesMacOS" : "", #VPN Device Names (macOS). Object Type: string
        "VPNDeviceNamesLinux" : "", #VPN Device Names (Linux). Object Type: string
        "WiredAllowedSubnets" : "", #[Deprecated] Allowed Subnets for Wired access. Object Type: string
        "WirelessAllowedSubnets" : "", #[Deprecated] Allowed Subnets for Wireless access. Object Type: string

        }
        """
        url_path = "/onguard/global-settings"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage OnGuard settings
    def get_onguard_settings(self):
        """
        Operation: Get OnGuard settings
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/onguard/settings"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_settings(self, body=({})):
        """
        Operation: Update OnGuard settings
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "mode" : "", #Mode of operation. Object Type: string
        "interfaces" : "", #[wired, wireless, vpn, other]: Network interfaces Agent should monitor. Object Type: string
        "web_agent_interfaces" : "", #[wired, wireless, vpn, other]: Network interfaces Native Dissolvable Agent should monitor. Object Type: string
        "auth_type" : "", #Authentication type. Object Type: string
        "field_username_caption" : "", #Caption for username field. Object Type: string
        "field_password_caption" : "", #Caption for password field. Object Type: string
        "cert_filter_criteria" : "", #Filter criteria used by OnGuard client to select certificates for authentication. Object Type: string
        "upgrade_action" : "", #Agent action when an update is available. Object Type: string
        "install_vpn_component" : False, #Install VIA component. Object Type: boolean
        "version" : "", #Agent version. This is read only field. Object Type: string
        "agentLibraryVersion" : "", #Version of the OnGuard Agent Library. This is read-only field. Object Type: string
        "installer_modified_time" : "", #Time when Agent Installers was last updated. This is read only field. Object Type: string
        "installer_modified_time_formatted" : "", #Formatted Time when Agent Installers was last updated. This is read only field. Object Type: string
        "agent_installers" : {}, #Details about Agent installers. This is read-only field. Object Type: object
        "agent_web_installers" : {}, #Details about Native Dissolvable Agent installers. This is read only field. Object Type: object
        "ip_version_onguard" : "", #IP Version for Server Communication (OnGuard). Object Type: string
        "ip_version_native" : "", #IP Version for Server Communication (Native). Object Type: string
        "custom_remediation" : {}, #Customize webpage details for Agent Remediation UI. Input should be in JSON format.. Object Type: object

        }
        """
        url_path = "/onguard/settings"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: API's to configure authentication server IP addresses per zone
    def get_onguard_policy_manager_zones(self):
        """
        Operation: Get Policy Manager Zones with associated authentication server IP addresses(Client Subnets and Server IPs)
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/onguard/policy-manager-zones"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_onguard_policy_manager_zones(self, body=({})):
        """
        Operation: Post Policy Manager Zones with associated authentication server IP addresses
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['policy_manager_zone_name', 'client_subnets']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "policy_manager_zone_name" : "", #Name of the Policy Manager Zone. Object Type: string
        "client_subnets" : "", #client subnet addresses specific to the Policy Manager zone. Object Type: string
        "override_server_ips" : "", #IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs. Object Type: string

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "client_subnets" : "", #client subnet addresses specific to the Policy Manager zone. Object Type: string
        "override_server_ips" : "", #IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs. Object Type: string

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
        Required Body Parameters:['client_subnets']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "client_subnets" : "", #client subnet addresses specific to the Policy Manager zone. Object Type: string
        "override_server_ips" : "", #IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs. Object Type: string

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: policy_manager_zones_id, Description: Numeric ID of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/{policy_manager_zones_id}"
        dict_path = {"policy_manager_zones_id": policy_manager_zones_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_onguard_policy_manager_zones_name_by_name(self, name=""):
        """
        Operation: Get Client Subnets and Server IPs for Policy Manager Zone by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onguard_policy_manager_zones_name_by_name(self, name="", body=({})):
        """
        Operation: Update authentication server IP addresses for Policy Manager Zone by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "client_subnets" : "", #client subnet addresses specific to the Policy Manager zone. Object Type: string
        "override_server_ips" : "", #IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs. Object Type: string

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        Required Body Parameters:['client_subnets']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "client_subnets" : "", #client subnet addresses specific to the Policy Manager zone. Object Type: string
        "override_server_ips" : "", #IP addresses or FQDN to which OnGuard agent will send request. This will override the Default ClearPass Server IPs. Object Type: string

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Unique name of the policy manager zone
        """
        url_path = "/onguard/policy-manager-zones/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage profiler subnet mappings
    def get_profiler_subnet_mapping(self):
        """
        Operation: Get a list of profiler subnet mappings
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/profiler-subnet-mapping"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_profiler_subnet_mapping(self, body=({})):
        """
        Operation: Add a profiler subnet mapping
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['network', 'scan_type', 'ext_accounts']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "network" : "", #IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"). Object Type: string
        "scan_type" : "", #Scan type of Profiler Subnet Mapping. Object Type: string
        "ext_accounts" : "", #List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI). Object Type: array

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "network" : "", #IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"). Object Type: string
        "scan_type" : "", #Scan type of Profiler Subnet Mapping. Object Type: string
        "ext_accounts" : "", #List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI). Object Type: array

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
        Required Body Parameters:['network', 'scan_type', 'ext_accounts']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "network" : "", #IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"). Object Type: string
        "scan_type" : "", #Scan type of Profiler Subnet Mapping. Object Type: string
        "ext_accounts" : "", #List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI). Object Type: array

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: profiler_subnet_mapping_id, Description: Numeric ID of Profiler Subnet Mapping
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: network, Description: Network of Profiler Subnet Mapping
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: network, Description: Network of Profiler Subnet Mapping
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "network" : "", #IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"). Object Type: string
        "scan_type" : "", #Scan type of Profiler Subnet Mapping. Object Type: string
        "ext_accounts" : "", #List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI). Object Type: array

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: network, Description: Network of Profiler Subnet Mapping
        Required Body Parameters:['network', 'scan_type', 'ext_accounts']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "network" : "", #IP Subnets/IP Addresses in CSV format (e.g. "10.21.11.0/24,12.12.12.12"). Object Type: string
        "scan_type" : "", #Scan type of Profiler Subnet Mapping. Object Type: string
        "ext_accounts" : "", #List of external account names according to Scan Type (e.g. ["acc-wmi-1", "acc-wmi-2", "acc-wmi-3"] for Scan Type WMI). Object Type: array

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: scan_type, Description: Scan Type of Profiler Subnet Mapping
        Parameter Type: path, Name: network, Description: Network of Profiler Subnet Mapping
        """
        url_path = "/profiler-subnet-mapping/{scan_type}/network/{network}"
        dict_path = {"scan_type": scan_type, "network": network}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Windows Hotfix
    def get_windows_hotfix(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Windows Hotfixes
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['kbid', 'operating_system', 'title', 'severity_rating']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "kbid" : "", #KBID of the windows hotfix. Object Type: string
        "operating_system" : "", #OS of the windows hotfix. Object Type: string
        "title" : "", #Title of the windows hotfix. Object Type: string
        "severity_rating" : "", #Severity rating of the windows hotfix. Object Type: string
        "superseded_by" : "", #Superseded_by of the windows hotfix. Object Type: string
        "superseding" : "", #Superseding of the windows hotfix. Object Type: string
        "reboot_behavior" : "", #Reboot Behavior of the windows hotfix. Object Type: string
        "release_date" : "", #Release Date of the windows hotfix. Object Type: string
        "url" : "", #URL of the windows hotfix. Object Type: string
        "description" : "", #Description of the windows hotfix. Object Type: string

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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "kbid" : "", #KBID of the windows hotfix. Object Type: string
        "operating_system" : "", #OS of the windows hotfix. Object Type: string
        "title" : "", #Title of the windows hotfix. Object Type: string
        "severity_rating" : "", #Severity rating of the windows hotfix. Object Type: string
        "superseded_by" : "", #Superseded_by of the windows hotfix. Object Type: string
        "superseding" : "", #Superseding of the windows hotfix. Object Type: string
        "reboot_behavior" : "", #Reboot Behavior of the windows hotfix. Object Type: string
        "release_date" : "", #Release Date of the windows hotfix. Object Type: string
        "url" : "", #URL of the windows hotfix. Object Type: string
        "description" : "", #Description of the windows hotfix. Object Type: string

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
        Required Body Parameters:['kbid', 'operating_system', 'title', 'severity_rating']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "kbid" : "", #KBID of the windows hotfix. Object Type: string
        "operating_system" : "", #OS of the windows hotfix. Object Type: string
        "title" : "", #Title of the windows hotfix. Object Type: string
        "severity_rating" : "", #Severity rating of the windows hotfix. Object Type: string
        "superseded_by" : "", #Superseded_by of the windows hotfix. Object Type: string
        "superseding" : "", #Superseding of the windows hotfix. Object Type: string
        "reboot_behavior" : "", #Reboot Behavior of the windows hotfix. Object Type: string
        "release_date" : "", #Release Date of the windows hotfix. Object Type: string
        "url" : "", #URL of the windows hotfix. Object Type: string
        "description" : "", #Description of the windows hotfix. Object Type: string

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: windows_hotfix_id, Description: Numeric ID of the windows hotfix
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: kbid, Description: KBID of the hotfix
        Parameter Type: path, Name: operating_system, Description: Operating system of the hotfix
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: kbid, Description: KBID of the hotfix
        Parameter Type: path, Name: operating_system, Description: Operating system of the hotfix
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "kbid" : "", #KBID of the windows hotfix. Object Type: string
        "operating_system" : "", #OS of the windows hotfix. Object Type: string
        "title" : "", #Title of the windows hotfix. Object Type: string
        "severity_rating" : "", #Severity rating of the windows hotfix. Object Type: string
        "superseded_by" : "", #Superseded_by of the windows hotfix. Object Type: string
        "superseding" : "", #Superseding of the windows hotfix. Object Type: string
        "reboot_behavior" : "", #Reboot Behavior of the windows hotfix. Object Type: string
        "release_date" : "", #Release Date of the windows hotfix. Object Type: string
        "url" : "", #URL of the windows hotfix. Object Type: string
        "description" : "", #Description of the windows hotfix. Object Type: string

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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: kbid, Description: KBID of the hotfix
        Parameter Type: path, Name: operating_system, Description: Operating system of the hotfix
        Required Body Parameters:['kbid', 'operating_system', 'title', 'severity_rating']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "kbid" : "", #KBID of the windows hotfix. Object Type: string
        "operating_system" : "", #OS of the windows hotfix. Object Type: string
        "title" : "", #Title of the windows hotfix. Object Type: string
        "severity_rating" : "", #Severity rating of the windows hotfix. Object Type: string
        "superseded_by" : "", #Superseded_by of the windows hotfix. Object Type: string
        "superseding" : "", #Superseding of the windows hotfix. Object Type: string
        "reboot_behavior" : "", #Reboot Behavior of the windows hotfix. Object Type: string
        "release_date" : "", #Release Date of the windows hotfix. Object Type: string
        "url" : "", #URL of the windows hotfix. Object Type: string
        "description" : "", #Description of the windows hotfix. Object Type: string

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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: kbid, Description: KBID of the hotfix
        Parameter Type: path, Name: operating_system, Description: Operating system of the hotfix
        """
        url_path = "/windows-hotfix/kbid/{kbid}/operating_system/{operating_system}"
        dict_path = {"kbid": kbid, "operating_system": operating_system}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
