from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: PlatformCertificates
# FileName: api_platformcertificates.py


class ApiPlatformCertificates(ClearPassAPILogin):
    # API Service: Manage Certificate Signing Requests
    def new_cert_sign_request(self, body=({})):
        """
        Operation: Post a certificate sign request
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['subject_CN', 'private_key_password', 'private_key_type', 'digest_algorithm']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "subject_CN" : "", #Common Name (CN). Object Type: string
        "subject_O" : "", #Organization (O). Object Type: string
        "subject_OU" : "", #Organizational Unit (OU). Object Type: string
        "subject_L" : "", #Location (L). Object Type: string
        "subject_ST" : "", #State (ST). Object Type: string
        "subject_C" : "", #Country (C). Object Type: string
        "subject_SAN" : "", #Subject Alternate Name (SAN). Object Type: string
        "private_key_password" : "", #Private Key Password. Object Type: string
        "private_key_type" : "", #null. Object Type: string
        "digest_algorithm" : "", #Digest Algorithm. Object Type: string
        }
        """
        url_path = "/cert-sign-request"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage Certificate Trust List
    def get_cert_trust_list(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of certificate trust list
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/cert-trust-list"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_cert_trust_list(self, body=({})):
        """
        Operation: Add a new certificate trust list
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['cert_file', 'cert_usage']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "cert_file" : "", #Certificate trust list file. Object Type: string
        "enabled" : False, #Enable certificate trust list. Object Type: boolean
        "cert_usage" : False, #Usage of the certificate. Object Type: array
        }
        """
        url_path = "/cert-trust-list"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_cert_trust_list_by_cert_trust_list_id(self, cert_trust_list_id=""):
        """
        Operation: Get a certificate trust list
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        """
        url_path = "/cert-trust-list/{cert_trust_list_id}"
        dict_path = {"cert_trust_list_id": cert_trust_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_cert_trust_list_by_cert_trust_list_id(
        self, cert_trust_list_id="", body=({})
    ):
        """
        Operation: Enbale certificate trust list
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "cert_file" : "", #Certificate trust list file. Object Type: string
        "enabled" : False, #Enable certificate trust list. Object Type: boolean
        "cert_usage" : False, #Usage of the certificate. Object Type: array
        }
        """
        url_path = "/cert-trust-list/{cert_trust_list_id}"
        dict_path = {"cert_trust_list_id": cert_trust_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def delete_cert_trust_list_by_cert_trust_list_id(self, cert_trust_list_id=""):
        """
        Operation: Delete a certificate trust list
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        """
        url_path = "/cert-trust-list/{cert_trust_list_id}"
        dict_path = {"cert_trust_list_id": cert_trust_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Certificate Trust List details
    def get_cert_trust_list_details(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of certificate trust list details
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/cert-trust-list-details"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_cert_trust_list_details_by_cert_trust_list_details_id(
        self, cert_trust_list_details_id=""
    ):
        """
        Operation: Get a certificate trust list details
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: cert_trust_list_details_id, Description: URL parameter cert_trust_list_details_id
        """
        url_path = "/cert-trust-list-details/{cert_trust_list_details_id}"
        dict_path = {"cert_trust_list_details_id": cert_trust_list_details_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Manage Client Certificates
    def get_client_cert(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of client certificates
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/client-cert"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_client_cert(self, body=({})):
        """
        Operation: Add a client certificate
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "certificate_url" : "", #Certificate File URL. Object Type: string
        "pkcs12_file_url" : "", #PKCS12 File URL. Object Type: string
        "pkcs12_passphrase" : "", #PKCS12 passphrase. Object Type: string
        }
        """
        url_path = "/client-cert"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_client_cert_by_client_cert_id(self, client_cert_id=""):
        """
        Operation: Get a client certificate
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: client_cert_id, Description: URL parameter client_cert_id
        """
        url_path = "/client-cert/{client_cert_id}"
        dict_path = {"client_cert_id": client_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_client_cert_by_client_cert_id(self, client_cert_id=""):
        """
        Operation: Delete a client certificate
        HTTP Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: client_cert_id, Description: URL parameter client_cert_id
        """
        url_path = "/client-cert/{client_cert_id}"
        dict_path = {"client_cert_id": client_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Revocation Certificate List
    def get_revocation_list(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of revocation certificate list
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/revocation-list"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_revocation_list(self, body=({})):
        """
        Operation: Add a new revocation certificate list
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "url" : "", #URL of the Certificate. Object Type: string
        "bypass_proxy" : False, #Bypass Proxy status of the Certificate. Object Type: boolean
        "periodic_update" : False, #Periodic Update status of the Certificate. Object Type: boolean
        "periodic_update_interval" : 0, #Periodic update time of the Certificate. Object Type: integer
        "last_update_status" : "", #Last updated status. Object Type: string
        "last_updated_time" : "", #Last updated time. Object Type: string
        "next_updated_time" : "", #Next update time. Object Type: string
        }
        """
        url_path = "/revocation-list"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_revocation_list_by_revocation_list_id(self, revocation_list_id=""):
        """
        Operation: Get a certificate by id
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: revocation_list_id, Description: URL parameter revocation_list_id
        """
        url_path = "/revocation-list/{revocation_list_id}"
        dict_path = {"revocation_list_id": revocation_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_revocation_list_by_revocation_list_id(
        self, revocation_list_id="", body=({})
    ):
        """
        Operation: Update a certificate
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: revocation_list_id, Description: URL parameter revocation_list_id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "url" : "", #URL of the Certificate. Object Type: string
        "bypass_proxy" : False, #Bypass Proxy status of the Certificate. Object Type: boolean
        "periodic_update" : False, #Periodic Update status of the Certificate. Object Type: boolean
        "periodic_update_interval" : 0, #Periodic update time of the Certificate. Object Type: integer
        "last_update_status" : "", #Last updated status. Object Type: string
        "last_updated_time" : "", #Last updated time. Object Type: string
        "next_updated_time" : "", #Next update time. Object Type: string
        }
        """
        url_path = "/revocation-list/{revocation_list_id}"
        dict_path = {"revocation_list_id": revocation_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def delete_revocation_list_by_revocation_list_id(self, revocation_list_id=""):
        """
        Operation: Delete a certificate list by id
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: revocation_list_id, Description: URL parameter revocation_list_id
        """
        url_path = "/revocation-list/{revocation_list_id}"
        dict_path = {"revocation_list_id": revocation_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Self-Signed Certificates
    def new_self_signed_cert(self, body=({})):
        """
        Operation: Create a Self-Signed Certificate
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['certificate_type', 'server', 'type', 'subject_CN', 'private_key_password', 'private_key_type', 'digest_algorithm']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "certificate_type" : "", #Certificate Type. Object Type: string
        "server" : "", #Server hostname. Object Type: string
        "type" : "", #Service Type. Object Type: string
        "subject_CN" : "", #Common Name (CN). Object Type: string
        "subject_O" : "", #Organization (O). Object Type: string
        "subject_OU" : "", #Organizational Unit (OU). Object Type: string
        "subject_L" : "", #Location (L). Object Type: string
        "subject_ST" : "", #State (ST). Object Type: string
        "subject_C" : "", #Country (C). Object Type: string
        "subject_SAN" : "", #Subject Alternate Name (SAN). Object Type: string
        "private_key_password" : "", #Private Key Password. Object Type: string
        "private_key_type" : "", #Private Key Type. Object Type: string
        "digest_algorithm" : "", #Digest Algorithm. Object Type: string
        }
        """
        url_path = "/self-signed-cert"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Manage Server Certificates
    def get_server_cert(self):
        """
        Operation: Get a list of server certificates
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/server-cert"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_server_cert_by_service_id(self, service_id=""):
        """
        Operation: Get server certificate
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: service_id, Description: Unique ID for the service
        """
        url_path = "/server-cert/{service_id}"
        dict_path = {"service_id": service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_server_cert_by_service_id(self, service_id="", body=({})):
        """
        Operation: Update a server certificate
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: service_id, Description: URL parameter service_id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "service_id" : 0, #Service ID of the server certificate(1-RADIUS server cert, 2-HTTPS(ECC) server cert, 7-HTTPS(RSA) server cert,21-RadSec server cert and 106-Database server cert). Object Type: integer
        "service_name" : "", #Service Name of the server certificate(RADIUS, HTTPS(ECC), HTTPS(RSA), RadSec or Database). Object Type: string
        "certificate_type" : "", #Type of the server certificate. Object Type: string
        "subject" : "", #Subject of the server certificate . Object Type: string
        "expiry_date" : "", #Expiry date of the server certificate . Object Type: string
        "issue_date" : "", #Issue date of the server certificate. Object Type: string
        "issue_by" : "", #server certificate issued by. Object Type: string
        "validity" : "", #Validity of the server certificate . Object Type: string
        "public_key_algorithm" : "", #Public Key Algorithm of Certificate.. Object Type: string
        "enabled" : False, #Enabled State of the certificate.. Object Type: boolean
        "root_ca_cert" : {}, #Root CA Certificate. Object Type: object
        "intermediate_ca_cert" : [{"":""}], #Intermediate CA Certificate. Object Type: array
        "cert_file" : "", #Certificate File. Object Type: string
        "certificate_url" : "", #Certificate File URL. Object Type: string
        "pkcs12_file_url" : "", #PKCS12 File URL. Object Type: string
        "pkcs12_passphrase" : "", #PKCS12 passphrase. Object Type: string
        }
        """
        url_path = "/server-cert/{service_id}"
        dict_path = {"service_id": service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def get_server_cert_name_by_server_uuid_service_name(
        self, server_uuid="", service_name=""
    ):
        """
        Operation: Get a server certificate
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: service_name, Description: Service name (RADIUS, HTTPS(RSA), HTTPS(ECC) or RadSec)
        """
        url_path = "/server-cert/name/{server_uuid}/{service_name}"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def replace_server_cert_name_by_server_uuid_service_name(
        self, server_uuid="", service_name="", body=({})
    ):
        """
        Operation: Add a server certificate
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: service_name, Description: Service name (RADIUS, HTTPS(RSA), HTTPS(ECC) or RadSec)
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "certificate_url" : "", #Certificate File URL. Object Type: string
        "pkcs12_file_url" : "", #PKCS12 File URL. Object Type: string
        "pkcs12_passphrase" : "", #PKCS12 passphrase. Object Type: string
        }
        """
        url_path = "/server-cert/name/{server_uuid}/{service_name}"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def update_server_cert_name_by_server_uuid_service_name_enable(
        self, server_uuid="", service_name=""
    ):
        """
        Operation: Update a server certificate
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: service_name, Description: Service name (HTTPS(RSA) or HTTPS(ECC))
        """
        url_path = "/server-cert/name/{server_uuid}/{service_name}/enable"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_server_cert_name_by_server_uuid_service_name_disable(
        self, server_uuid="", service_name=""
    ):
        """
        Operation: Update a server certificate
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: server_uuid, Description: UUID of the server
        Parameter Type: path, Name: service_name, Description: Service name (HTTPS(RSA) or HTTPS(ECC))
        """
        url_path = "/server-cert/name/{server_uuid}/{service_name}/disable"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # API Service: Manage Service Certificates
    def get_service_cert(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of service certificates
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/service-cert"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_service_cert(self, body=({})):
        """
        Operation: Add a service certificate
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "certificate_url" : "", #Certificate File URL. Object Type: string
        "pkcs12_file_url" : "", #PKCS12 File URL. Object Type: string
        "pkcs12_passphrase" : "", #PKCS12 passphrase. Object Type: string
        }
        """
        url_path = "/service-cert"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_service_cert_by_service_cert_id(self, service_cert_id=""):
        """
        Operation: Get a service certificate
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: service_cert_id, Description: URL parameter service_cert_id
        """
        url_path = "/service-cert/{service_cert_id}"
        dict_path = {"service_cert_id": service_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_service_cert_by_service_cert_id(self, service_cert_id=""):
        """
        Operation: Delete a service certificate
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: service_cert_id, Description: URL parameter service_cert_id
        """
        url_path = "/service-cert/{service_cert_id}"
        dict_path = {"service_cert_id": service_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
