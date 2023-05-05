from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_platformcertificates_v1.py


class ApiPlatformCertificates(ClearPassAPILogin):
    # Function Section Name:CertSignRequest
    # Function Section Description: Manage Certificate Signing Requests

    def new_cert_sign_request(self, body=({})):
        """
                Operation: Post a certificate sign request
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- CertSignRequestCreate {subject_CN (string): Common Name (CN),subject_O (string, optional): Organization (O),subject_OU (string, optional): Organizational Unit (OU),subject_L (string, optional): Location (L),subject_ST (string, optional): State (ST),subject_C (string, optional): Country (C),subject_SAN (string, optional): Subject Alternate Name (SAN),private_key_password (string): Private Key Password,private_key_type (string) = ['2048-bit rsa' or '3072-bit rsa' or '4096-bit rsa' or 'nist/secg curve over a 256 bit prime field' or 'nist/secg curve over a 384 bit prime field' or 'nist/secg curve over a 521 bit prime field']: null,digest_algorithm (string) = ['SHA-1' or 'SHA-224' or 'SHA-256' or 'SHA-384' or 'SHA-512']: Digest Algorithm}
                Required Body Parameters (type(dict) body example)- {
          "subject_CN": "",
          "subject_O": "",
          "subject_OU": "",
          "subject_L": "",
          "subject_ST": "",
          "subject_C": "",
          "subject_SAN": "",
          "private_key_password": "",
          "private_key_type": "",
          "digest_algorithm": ""
        }
        """
        url_path = "/cert-sign-request"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertTrustList
    # Function Section Description: Manage Certificate Trust List

    def get_cert_trust_list(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of certificate trust list
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- CertTrustListCreate {cert_file (string): Certificate trust list file,enabled (boolean, optional): Enable certificate trust list,cert_usage (array[string]) = ['AD/LDAP Servers' or 'Aruba Infrastructure' or 'Aruba Services' or 'Database' or 'EAP' or 'Endpoint Context Servers' or 'RadSec' or 'SAML' or 'SMTP' or 'EST' or 'Others']: Usage of the certificate}
                Required Body Parameters (type(dict) body example)- {
          "cert_file": "",
          "enabled": false,
          "cert_usage": [
            ""
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
                Required Body Parameters (body description)- CertTrustListUpdate {cert_file (string, optional): Certificate trust list file,enabled (boolean, optional): Enable certificate trust list,cert_usage (array[string], optional) = ['AD/LDAP Servers' or 'Aruba Infrastructure' or 'Aruba Services' or 'Database' or 'EAP' or 'Endpoint Context Servers' or 'RadSec' or 'SAML' or 'SMTP' or 'EST' or 'Others']: Usage of the certificate}
                Required Body Parameters (type(dict) body example)- {
          "cert_file": "",
          "enabled": false,
          "cert_usage": [
            ""
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: cert_trust_list_id, Description: URL parameter cert_trust_list_id
        """
        url_path = "/cert-trust-list/{cert_trust_list_id}"
        dict_path = {"cert_trust_list_id": cert_trust_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:CertTrustListDetails
    # Function Section Description: Manage Certificate Trust List details

    def get_cert_trust_list_details(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of certificate trust list details
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: cert_trust_list_details_id, Description: URL parameter cert_trust_list_details_id
        """
        url_path = "/cert-trust-list-details/{cert_trust_list_details_id}"
        dict_path = {"cert_trust_list_details_id": cert_trust_list_details_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:ClientCert
    # Function Section Description: Manage Client Certificates

    def get_client_cert(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of client certificates
        HTTP Status Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ClientCertCreate {certificate_url (string, optional): Certificate File URL,pkcs12_file_url (string, optional): PKCS12 File URL,pkcs12_passphrase (string, optional): PKCS12 passphrase}
                Required Body Parameters (type(dict) body example)- {
          "certificate_url": "",
          "pkcs12_file_url": "",
          "pkcs12_passphrase": ""
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
        HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: client_cert_id, Description: URL parameter client_cert_id
        """
        url_path = "/client-cert/{client_cert_id}"
        dict_path = {"client_cert_id": client_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_client_cert_by_client_cert_id(self, client_cert_id=""):
        """
        Operation: Delete a client certificate
        HTTP Status Response Codes: 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: client_cert_id, Description: URL parameter client_cert_id
        """
        url_path = "/client-cert/{client_cert_id}"
        dict_path = {"client_cert_id": client_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:RevocationList
    # Function Section Description: Manage Revocation Certificate List

    def get_revocation_list(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of revocation certificate list
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- RevocationListCreate {url (string): URL of the Certificate,bypass_proxy (boolean, optional): Bypass Proxy status of the Certificate,periodic_update (boolean, optional): Periodic Update status of the Certificate,periodic_update_interval (integer, optional): Periodic update time of the Certificate,last_update_status (string, optional): Last updated status,last_updated_time (string, optional): Last updated time,next_updated_time (string, optional): Next update time}
                Required Body Parameters (type(dict) body example)- {
          "url": "",
          "bypass_proxy": false,
          "periodic_update": false,
          "periodic_update_interval": 0,
          "last_update_status": "",
          "last_updated_time": "",
          "next_updated_time": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: revocation_list_id, Description: URL parameter revocation_list_id
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: revocation_list_id, Description: URL parameter revocation_list_id
                Required Body Parameters (body description)- RevocationListUpdate {url (string, optional): URL of the Certificate,bypass_proxy (boolean, optional): Bypass Proxy status of the Certificate,periodic_update (boolean, optional): Periodic Update status of the Certificate,periodic_update_interval (integer, optional): Periodic update time of the Certificate,last_update_status (string, optional): Last updated status,last_updated_time (string, optional): Last updated time,next_updated_time (string, optional): Next update time}
                Required Body Parameters (type(dict) body example)- {
          "url": "",
          "bypass_proxy": false,
          "periodic_update": false,
          "periodic_update_interval": 0,
          "last_update_status": "",
          "last_updated_time": "",
          "next_updated_time": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: revocation_list_id, Description: URL parameter revocation_list_id
        """
        url_path = "/revocation-list/{revocation_list_id}"
        dict_path = {"revocation_list_id": revocation_list_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:SelfSignedCert
    # Function Section Description: Manage Self-Signed Certificates

    def new_self_signed_cert(self, body=({})):
        """
                Operation: Create a Self-Signed Certificate
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- SelfSignedCertCreate {certificate_type (string) = ['SERVER' or 'SERVICE']: Certificate Type,server (string): Server hostname,type (string) = ['RADIUS/EAP Server Certificate' or 'HTTPS(ECC) Server Certificate' or 'HTTPS(RSA) Server Certificate' or 'RadSec Server Certificate' or 'Database Server Certificate']: Service Type,subject_CN (string): Common Name (CN),subject_O (string, optional): Organization (O),subject_OU (string, optional): Organizational Unit (OU),subject_L (string, optional): Location (L),subject_ST (string, optional): State (ST),subject_C (string, optional): Country (C),subject_SAN (string, optional): Subject Alternate Name (SAN),private_key_password (string): Private Key Password,private_key_type (string) = ['2048-bit rsa' or '3072-bit rsa' or '4096-bit rsa' or 'nist/secg curve over a 256 bit prime field' or 'nist/secg curve over a 384 bit prime field' or 'nist/secg curve over a 521 bit prime field']: Private Key Type,digest_algorithm (string) = ['SHA-1' or 'SHA-224' or 'SHA-256' or 'SHA-384' or 'SHA-512']: Digest Algorithm}
                Required Body Parameters (type(dict) body example)- {
          "certificate_type": "",
          "server": "",
          "type": "",
          "subject_CN": "",
          "subject_O": "",
          "subject_OU": "",
          "subject_L": "",
          "subject_ST": "",
          "subject_C": "",
          "subject_SAN": "",
          "private_key_password": "",
          "private_key_type": "",
          "digest_algorithm": ""
        }
        """
        url_path = "/self-signed-cert"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:ServerCert
    # Function Section Description: Manage Server Certificates

    def get_server_cert(self, body=({})):
        """
                Operation: Get a list of server certificates
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- SelfSignedCertCreate {certificate_type (string) = ['SERVER' or 'SERVICE']: Certificate Type,server (string): Server hostname,type (string) = ['RADIUS/EAP Server Certificate' or 'HTTPS(ECC) Server Certificate' or 'HTTPS(RSA) Server Certificate' or 'RadSec Server Certificate' or 'Database Server Certificate']: Service Type,subject_CN (string): Common Name (CN),subject_O (string, optional): Organization (O),subject_OU (string, optional): Organizational Unit (OU),subject_L (string, optional): Location (L),subject_ST (string, optional): State (ST),subject_C (string, optional): Country (C),subject_SAN (string, optional): Subject Alternate Name (SAN),private_key_password (string): Private Key Password,private_key_type (string) = ['2048-bit rsa' or '3072-bit rsa' or '4096-bit rsa' or 'nist/secg curve over a 256 bit prime field' or 'nist/secg curve over a 384 bit prime field' or 'nist/secg curve over a 521 bit prime field']: Private Key Type,digest_algorithm (string) = ['SHA-1' or 'SHA-224' or 'SHA-256' or 'SHA-384' or 'SHA-512']: Digest Algorithm}
                Required Body Parameters (type(dict) body example)- {
          "certificate_type": "",
          "server": "",
          "type": "",
          "subject_CN": "",
          "subject_O": "",
          "subject_OU": "",
          "subject_L": "",
          "subject_ST": "",
          "subject_C": "",
          "subject_SAN": "",
          "private_key_password": "",
          "private_key_type": "",
          "digest_algorithm": ""
        }
        """
        url_path = "/server-cert"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def get_server_cert_name_by_server_uuid_service_name(
        self, server_uuid="", service_name=""
    ):
        """
        Operation: Get a server certificate
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (RADIUS, HTTPS(RSA), HTTPS(ECC) or RadSec)
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: server_uuid, Description: UUID of the server
                Required Path Parameter Name: service_name, Description: Service name (RADIUS, HTTPS(RSA), HTTPS(ECC) or RadSec)
                Required Body Parameters (body description)- ServerCertReplace {certificate_url (string, optional): Certificate File URL,pkcs12_file_url (string, optional): PKCS12 File URL,pkcs12_passphrase (string, optional): PKCS12 passphrase}
                Required Body Parameters (type(dict) body example)- {
          "certificate_url": "",
          "pkcs12_file_url": "",
          "pkcs12_passphrase": ""
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
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (HTTPS(RSA) or HTTPS(ECC))
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
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: server_uuid, Description: UUID of the server
        Required Path Parameter Name: service_name, Description: Service name (HTTPS(RSA) or HTTPS(ECC))
        """
        url_path = "/server-cert/name/{server_uuid}/{service_name}/disable"
        dict_path = {"server_uuid": server_uuid, "service_name": service_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # Function Section Name:ServiceCert
    # Function Section Description: Manage Service Certificates

    def get_service_cert(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of service certificates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- ServiceCertCreate {certificate_url (string, optional): Certificate File URL,pkcs12_file_url (string, optional): PKCS12 File URL,pkcs12_passphrase (string, optional): PKCS12 passphrase}
                Required Body Parameters (type(dict) body example)- {
          "certificate_url": "",
          "pkcs12_file_url": "",
          "pkcs12_passphrase": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: service_cert_id, Description: URL parameter service_cert_id
        """
        url_path = "/service-cert/{service_cert_id}"
        dict_path = {"service_cert_id": service_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_service_cert_by_service_cert_id(self, service_cert_id=""):
        """
        Operation: Delete a service certificate
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: service_cert_id, Description: URL parameter service_cert_id
        """
        url_path = "/service-cert/{service_cert_id}"
        dict_path = {"service_cert_id": service_cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
