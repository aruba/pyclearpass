from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_localserverconfiguration_v1.py


class ApiLocalServerConfiguration(ClearPassAPILogin):
    # Function Section Name:AccessControl
    # Function Section Description: Manage Application access controls

    def get_server_access_control_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get all application access controls
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: resource_name, Description: Unique resource name of the access control
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: UUID of the server
                Required Path Parameter Name: resource_name, Description: Unique resource name of the access control
                Required Body Parameters (body description)- AccessControlReplace {access (string) = ['Allow' or 'Deny']: Access type of the Access control application,networks (object): hostname, IP address or subnet (CIDR) of the Networks to be restricted (e.g. ["hostname.example.com", "1.2.3.4", "10.1.0.0/16"])}
                Required Body Parameters (type(dict) body example)- {
          "access": "",
          "networks": "object"
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: resource_name, Description: Unique resource name of the access control
        """
        url_path = "/server/access-control/{server_uuid}/{resource_name}"
        dict_path = {"server_uuid": server_uuid, "resource_name": resource_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:ADDomain
    # Function Section Description: Manage AD Domains

    def get_ad_domain_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get a list of AD Domains
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
        Required Path Parameter Name: netbios_name, Description: NetBIOS name of the domain
        """
        url_path = "/ad-domain/{server_uuid}/netbios-name/{netbios_name}"
        dict_path = {"server_uuid": server_uuid, "netbios_name": netbios_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_ad_domain_join_by_server_uuid(self, server_uuid="", body=({})):
        """
                Operation: Join AD Domain
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
                Required Body Parameters (body description)- ADDomainJoin {domain_controller (string): FQDN of the domain controller,netbios_name (string): NetBIOS name of the domain,on_name_conflict (integer): Action to perform in case of a controller name conflict(1 - Use specified Domain Controller, 2 - Use Domain Controller returned by DNS query, 3 - Fail on conflict),username (string): Domain username ,password (string): Domain password}
                Required Body Parameters (type(dict) body example)- {
          "domain_controller": "",
          "netbios_name": "",
          "on_name_conflict": 0,
          "username": "",
          "password": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
                Required Body Parameters (body description)- ADDomainLeave {netbios_name (string): NetBIOS name of the domain,username (string): Domain username ,password (string): Domain password,force_leave (boolean): Leave domain even if AD is down}
                Required Body Parameters (type(dict) body example)- {
          "netbios_name": "",
          "username": "",
          "password": "",
          "force_leave": false
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
                Required Body Parameters (body description)- ADDomainUpdate {netbios_name (string): NetBIOS name of the domain,password_servers (object): List of Hostname or IP Address of the AD password servers}
                Required Body Parameters (type(dict) body example)- {
          "netbios_name": "",
          "password_servers": "object"
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

    # Function Section Name:CppmVersion
    # Function Section Description: Manage Cppm Version

    def get_cppm_version(self, server_uuid="", body=({})):
        """
                Operation: Get Cppm version
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
                Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
                Required Body Parameters (body description)- ADDomainUpdate {netbios_name (string): NetBIOS name of the domain,password_servers (object): List of Hostname or IP Address of the AD password servers}
                Required Body Parameters (type(dict) body example)- {
          "netbios_name": "",
          "password_servers": "object"
        }
        """
        url_path = "/cppm-version"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    # Function Section Name:ServerConfiguration
    # Function Section Description: Manage cluster servers and per-server configuration

    def get_cluster_server(self, server_uuid="", body=({})):
        """
                Operation: Get a list of servers in the cluster
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Path Parameter Name: server_uuid, Description: URL parameter server_uuid
                Required Body Parameters (body description)- ADDomainUpdate {netbios_name (string): NetBIOS name of the domain,password_servers (object): List of Hostname or IP Address of the AD password servers}
                Required Body Parameters (type(dict) body example)- {
          "netbios_name": "",
          "password_servers": "object"
        }
        """
        url_path = "/cluster/server"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def get_cluster_server_by_uuid(self, uuid=""):
        """
        Operation: Get configuration of a server
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: uuid, Description: Server UUID, "publisher" or "this"
        """
        url_path = "/cluster/server/{uuid}"
        dict_path = {"uuid": uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_cluster_server_by_uuid(self, uuid="", body=({})):
        """
                Operation: Update configuration of a server
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: uuid, Description: Server UUID, "publisher" or "this"
                Required Body Parameters (body description)- ServerConfigurationChange {is_insight_enabled (bool, optional): True if this server has Insight reporting enabled}
                Required Body Parameters (type(dict) body example)- {
          "is_insight_enabled": "bool"
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

    # Function Section Name:ServerFips
    # Function Section Description: Get server FIPS mode information

    def get_server_fips(self, uuid="", body=({})):
        """
                Operation: Get server FIPS mode information
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Path Parameter Name: uuid, Description: Server UUID, "publisher" or "this"
                Required Body Parameters (body description)- ServerConfigurationChange {is_insight_enabled (bool, optional): True if this server has Insight reporting enabled}
                Required Body Parameters (type(dict) body example)- {
          "is_insight_enabled": "bool"
        }
        """
        url_path = "/server/fips"
        dict_path = {"uuid": uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    # Function Section Name:ServerSnmp
    # Function Section Description: Manage server snmp settings

    def get_server_snmp_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get server snmp settings
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        """
        url_path = "/server/snmp/{server_uuid}"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_snmp_by_server_uuid(self, server_uuid="", body=({})):
        """
                Operation: Replace server snmp settings
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: UUID of the server
                Required Body Parameters (body description)- ServerSnmpReplace {system_location (string, optional): System location of the system monitoring settings for a server,system_contact (string, optional): System contact of the system monitoring settings for a server,engine_id (string): Engine ID of system monitoring settings,version (string) = ['V1' or 'V2C' or 'V3']: SNMP Version of the system monitoring settings,community_string (string, optional): Community String of the system monitoring settings,username (string, optional): Username for system monitoring settings,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security Level of system monitoring settings,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication Protocol of system monitoring settings,auth_key (string, optional): Authentication key of system monitoring settings,privacy_protocol (string, optional) = ['DES' or 'AES']: Privacy Protocol of system monitoring settings,privacy_key (string, optional): Privacy key of system monitoring settings}
                Required Body Parameters (type(dict) body example)- {
          "system_location": "",
          "system_contact": "",
          "engine_id": "",
          "version": "",
          "community_string": "",
          "username": "",
          "security_level": "",
          "auth_protocol": "",
          "auth_key": "",
          "privacy_protocol": "",
          "privacy_key": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: UUID of the server
                Required Body Parameters (body description)- ServerSnmpUpdate {system_location (string, optional): System location of the system monitoring settings for a server,system_contact (string, optional): System contact of the system monitoring settings for a server,engine_id (string, optional): Engine ID of system monitoring settings,version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version of the system monitoring settings,community_string (string, optional): Community String of the system monitoring settings,username (string, optional): Username for system monitoring settings,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security Level of system monitoring settings,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication Protocol of system monitoring settings,auth_key (string, optional): Authentication key of system monitoring settings,privacy_protocol (string, optional) = ['DES' or 'AES']: Privacy Protocol of system monitoring settings,privacy_key (string, optional): Privacy key of system monitoring settings}
                Required Body Parameters (type(dict) body example)- {
          "system_location": "",
          "system_contact": "",
          "engine_id": "",
          "version": "",
          "community_string": "",
          "username": "",
          "security_level": "",
          "auth_protocol": "",
          "auth_key": "",
          "privacy_protocol": "",
          "privacy_key": ""
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

    # Function Section Name:ServerVersion
    # Function Section Description: Get server version information

    def get_server_version(self, server_uuid="", body=({})):
        """
                Operation: Get server version information
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Path Parameter Name: server_uuid, Description: UUID of the server
                Required Body Parameters (body description)- ServerSnmpUpdate {system_location (string, optional): System location of the system monitoring settings for a server,system_contact (string, optional): System contact of the system monitoring settings for a server,engine_id (string, optional): Engine ID of system monitoring settings,version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP Version of the system monitoring settings,community_string (string, optional): Community String of the system monitoring settings,username (string, optional): Username for system monitoring settings,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security Level of system monitoring settings,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication Protocol of system monitoring settings,auth_key (string, optional): Authentication key of system monitoring settings,privacy_protocol (string, optional) = ['DES' or 'AES']: Privacy Protocol of system monitoring settings,privacy_key (string, optional): Privacy key of system monitoring settings}
                Required Body Parameters (type(dict) body example)- {
          "system_location": "",
          "system_contact": "",
          "engine_id": "",
          "version": "",
          "community_string": "",
          "username": "",
          "security_level": "",
          "auth_protocol": "",
          "auth_key": "",
          "privacy_protocol": "",
          "privacy_key": ""
        }
        """
        url_path = "/server/version"
        dict_path = {"server_uuid": server_uuid}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    # Function Section Name:ServiceParameter
    # Function Section Description: Manage service parameters

    def get_service_parameter_by_server_uuid_service_id(
        self, server_uuid="", service_id=""
    ):
        """
        Operation: Get service parameter details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_id, Description: Unique id for the service
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: UUID of the server
                Required Path Parameter Name: service_id, Description: Unique id for the service
                Required Body Parameters (body description)- ServiceParameterUpdate {param_name_1 (string, optional): param_value_1,param_name_2 (string, optional): param_value_2...}
                Required Body Parameters (type(dict) body example)- {
          "param_name_1": "",
          "param_name_2": ""
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

    # Function Section Name:SystemServiceControl
    # Function Section Description: Control services running on a server

    def get_server_service_by_server_uuid(self, server_uuid=""):
        """
        Operation: Get all services
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Required Path Parameter Name: service_name, Description: Unique Name of the SystemServiceControl
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
        Operation: Start a service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Required Path Parameter Name: service_name, Description: Unique Name of the SystemServiceControl
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
        Operation: Stop a service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: AlphaNumeric Unique Id of the Server
        Required Path Parameter Name: service_name, Description: Unique Name of the SystemServiceControl
        """
        url_path = "/server/service/{server_uuid}/{service_name}/stop"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")
