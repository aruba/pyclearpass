from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: LocalServerConfiguration
# FileName: api_localserverconfiguration.py


class ApiLocalServerConfiguration(ClearPassAPILogin):
    # API Service: Manage Application access controls
    def get_server_access_control_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get all application access controls
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        """
        url_path = "/server/access-control/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_server_access_control_by_server_uuid_resource_name(
        self, server_uuid="", resource_name=""
    ):
        """
        Operation: Get an application access control by resource name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: resource_name, Description: Unique resource name of the access control
        """
        url_path = "/server/access-control/{server_uuid}/{resource_name}"
        dict_path = {"server_uuid": server_uuid, "resource_name": resource_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_access_control_by_server_uuid_resource_name(
        self, server_uuid="", resource_name="", body=({})
    ):
        """
        Operation: Replace an application access controls by resource name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: resource_name, Description: Unique resource name of the access control
        Required Body Parameters:['access', 'networks']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "access" : "", #Access type of the Access control application. Object Type: string
        "networks" : {}, #hostname, IP address or subnet (CIDR) of the Networks to be restricted (e.g. ["hostname.example.com", "1.2.3.4", "10.1.0.0/16"]). Object Type: object

        }
        """
        url_path = "/server/access-control/{server_uuid}/{resource_name}"
        dict_path = {"server_uuid": server_uuid, "resource_name": resource_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_server_access_control_by_server_uuid_resource_name(
        self, server_uuid="", resource_name=""
    ):
        """
        Operation: Delete an application access control by resource name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: resource_name, Description: Unique resource name of the access control
        """
        url_path = "/server/access-control/{server_uuid}/{resource_name}"
        dict_path = {"server_uuid": server_uuid, "resource_name": resource_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage AD Domains
    def get_ad_domain_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get a list of AD Domains
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: URL parameter server_uuid
        """
        url_path = "/ad-domain/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_ad_domain_by_server_uuid_netbios_name_netbios_name(
        self, server_uuid="", netbios_name=""
    ):
        """
        Operation: GET an AD domain by netbios_name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: URL parameter server_uuid
        Parameter Type: path, Name: netbios_name, Description: NetBIOS name of the domain
        """
        url_path = "/ad-domain/{server_uuid}/netbios-name/{netbios_name}"
        dict_path = {"server_uuid": server_uuid, "netbios_name": netbios_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_ad_domain_join_by_server_uuid(self, server_uuid="", body=({})):
        """
        Operation: Join AD Domain
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters:['domain_controller', 'netbios_name', 'on_name_conflict', 'username', 'password']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "domain_controller" : "", #FQDN of the domain controller. Object Type: string
        "netbios_name" : "", #NetBIOS name of the domain. Object Type: string
        "on_name_conflict" : 0, #Action to perform in case of a controller name conflict(1 - Use specified Domain Controller, 2 - Use Domain Controller returned by DNS query, 3 - Fail on conflict). Object Type: integer
        "username" : "", #Domain username . Object Type: string
        "password" : "", #Domain password. Object Type: string

        }
        """
        url_path = "/ad-domain/join/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def replace_ad_domain_leave_by_server_uuid(self, server_uuid="", body=({})):
        """
        Operation: Leave AD domain
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters:['netbios_name', 'username', 'password', 'force_leave']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "netbios_name" : "", #NetBIOS name of the domain. Object Type: string
        "username" : "", #Domain username . Object Type: string
        "password" : "", #Domain password. Object Type: string
        "force_leave" : False, #Leave domain even if AD is down. Object Type: boolean

        }
        """
        url_path = "/ad-domain/leave/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_ad_domain_password_servers_by_server_uuid(
        self, server_uuid="", body=({})
    ):
        """
        Operation: Configure AD Password Servers
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: URL parameter server_uuid
        Required Body Parameters:['netbios_name', 'password_servers']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "netbios_name" : "", #NetBIOS name of the domain. Object Type: string
        "password_servers" : {}, #List of Hostname or IP Address of the AD password servers. Object Type: object

        }
        """
        url_path = "/ad-domain/password-servers/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Manage Cppm Version
    def get_cppm_version(self):
        """
        Operation: Get Cppm version
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/cppm-version"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage cluster servers and per-server configuration
    def get_cluster_server(self):
        """
        Operation: Get a list of servers in the cluster
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/cluster/server"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_cluster_server_by_uuid(self, uuid=""):
        """
        Operation: Get configuration of a server
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: uuid, Description: Server UUID, "publisher" or "this"
        """
        url_path = "/cluster/server/{uuid}"
        dict_path = {"uuid": uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_cluster_server_by_uuid(self, uuid="", body=({})):
        """
        Operation: Update configuration of a server
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: uuid, Description: Server UUID, "publisher" or "this"
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "is_insight_enabled" : {}, #True if this server has Insight reporting enabled. Object Type: bool

        }
        """
        url_path = "/cluster/server/{uuid}"
        dict_path = {"uuid": uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Get server FIPS mode information
    def get_server_fips(self):
        """
        Operation: Get server FIPS mode information
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/server/fips"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage server snmp settings
    def get_server_snmp_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get server snmp settings
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        """
        url_path = "/server/snmp/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_snmp_by_server_uuid(self, server_uuid="", body=({})):
        """
        Operation: Replace server snmp settings
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Required Body Parameters:['engine_id', 'version']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "system_location" : "", #System location of the system monitoring settings for a server. Object Type: string
        "system_contact" : "", #System contact of the system monitoring settings for a server. Object Type: string
        "engine_id" : "", #Engine ID of system monitoring settings. Object Type: string
        "version" : "", #SNMP Version of the system monitoring settings. Object Type: string
        "community_string" : "", #Community String of the system monitoring settings. Object Type: string
        "username" : "", #Username for system monitoring settings. Object Type: string
        "security_level" : "", #Security Level of system monitoring settings. Object Type: string
        "auth_protocol" : "", #Authentication Protocol of system monitoring settings. Object Type: string
        "auth_key" : "", #Authentication key of system monitoring settings. Object Type: string
        "privacy_protocol" : "", #Privacy Protocol of system monitoring settings. Object Type: string
        "privacy_key" : "", #Privacy key of system monitoring settings. Object Type: string

        }
        """
        url_path = "/server/snmp/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_server_snmp_by_server_uuid(self, server_uuid="", body=({})):
        """
        Operation: Update some fields of server snmp settings
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "system_location" : "", #System location of the system monitoring settings for a server. Object Type: string
        "system_contact" : "", #System contact of the system monitoring settings for a server. Object Type: string
        "engine_id" : "", #Engine ID of system monitoring settings. Object Type: string
        "version" : "", #SNMP Version of the system monitoring settings. Object Type: string
        "community_string" : "", #Community String of the system monitoring settings. Object Type: string
        "username" : "", #Username for system monitoring settings. Object Type: string
        "security_level" : "", #Security Level of system monitoring settings. Object Type: string
        "auth_protocol" : "", #Authentication Protocol of system monitoring settings. Object Type: string
        "auth_key" : "", #Authentication key of system monitoring settings. Object Type: string
        "privacy_protocol" : "", #Privacy Protocol of system monitoring settings. Object Type: string
        "privacy_key" : "", #Privacy key of system monitoring settings. Object Type: string

        }
        """
        url_path = "/server/snmp/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Get server version information
    def get_server_version(self):
        """
        Operation: Get server version information
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/server/version"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage service parameters
    def get_service_parameter_by_server_uuid_service_id(
        self, server_uuid="", service_id=""
    ):
        """
        Operation: Get service parameter details
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: service_id, Description: Unique id for the service
        """
        url_path = "/service-parameter/{server_uuid}/{service_id}"
        dict_path = {"server_uuid": server_uuid, "service_id": service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_service_parameter_by_server_uuid_service_id(
        self, server_uuid="", service_id="", body=({})
    ):
        """
        Operation: Update service parameter values
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: service_id, Description: Unique id for the service
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "param_name_1" : "", #param_value_1. Object Type: string
        "param_name_2" : "", #param_value_2.... Object Type: string

        }
        """
        url_path = "/service-parameter/{server_uuid}/{service_id}"
        dict_path = {"server_uuid": server_uuid, "service_id": service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Control services running on a server
    def get_server_service_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get all services
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        """
        url_path = "/server/service/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_server_service_by_server_uuid_service_name(
        self, server_uuid="", service_name=""
    ):
        """
        Operation: Get a service by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Parameter Type: path, Name: service_name, Description: Unique Name of the SystemServiceControl
        """
        url_path = "/server/service/{server_uuid}/{service_name}"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_server_service_by_server_uuid_service_name_start(
        self, server_uuid="", service_name=""
    ):
        """
        Operation:  Start a service by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Parameter Type: path, Name: service_name, Description: Unique Name of the SystemServiceControl
        """
        url_path = "/server/service/{server_uuid}/{service_name}/start"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_server_service_by_server_uuid_service_name_stop(
        self, server_uuid="", service_name=""
    ):
        """
        Operation:  Stop a service by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Parameter Type: path, Name: service_name, Description: Unique Name of the SystemServiceControl
        """
        url_path = "/server/service/{server_uuid}/{service_name}/stop"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")
