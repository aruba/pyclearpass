from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_certificateauthority_v1.py


class ApiCertificateAuthority(ClearPassAPILogin):
    # Function Section Name:Certificate
    # Function Section Description: Manage Onboard certificates

    def get_certificate(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of certificates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/certificate"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_certificate_by_certificate_id(self, certificate_id=""):
        """
        Operation: Get a certificate or certificate signing request
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: certificate_id, Description: Numeric ID of the certificate
        """
        url_path = "/certificate/{certificate_id}"
        dict_path = {"certificate_id": certificate_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_certificate_by_certificate_id(self, certificate_id=""):
        """
        Operation: Delete a certificate or certificate signing request
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: certificate_id, Description: Numeric ID of the certificate
        """
        url_path = "/certificate/{certificate_id}"
        dict_path = {"certificate_id": certificate_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:CertificateChain
    # Function Section Description: Get a certificate and its trust chain

    def get_certificate_by_cert_id_chain(self, cert_id=""):
        """
        Operation: Get a certificate and its trust chain
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: cert_id, Description: Numeric ID of the certificate
        """
        url_path = "/certificate/{cert_id}/chain"
        dict_path = {"cert_id": cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:CertificateExport
    # Function Section Description: Export a certificate or certificate signing request

    def new_certificate_by_cert_id_export(self, cert_id="", body=({})):
        """
                Operation: Export a certificate or certificate signing request
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: cert_id, Description: Numeric ID of the certificate
                Required Body Parameters (body description)- CertificateExport {export_format (string) = ['p7b' or 'pem' or 'crt' or 'txt' or 'p12']: Select the file format for the exported item,include_chain (boolean, optional): Select this option to include the certificates for the CA and any intermediate certificate authorities,include_ca (string, optional) = ['all' or 'intermediate']: Select which certificate authorities to include.,export_password (string, optional): Passphrase to protect the PKCS#12 file,export_password2 (string, optional): Re-enter the passphrase}
                Required Body Parameters (type(dict) body example)- {
          "export_format": "",
          "include_chain": false,
          "include_ca": "",
          "export_password": "",
          "export_password2": ""
        }
        """
        url_path = "/certificate/{cert_id}/export"
        dict_path = {"cert_id": cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertificateImport
    # Function Section Description: Import a code-signing, trusted, or CA certificate

    def new_certificate_import(self, body=({})):
        """
                Operation: Import a code-signing, trusted, or CA certificate
                HTTP Status Response Codes: 200 OK, 400 Client Error, 401 Unprocessable Entity, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Client Error, 401 Unprocessable Entity, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- CertificateImport {ca_id (integer, optional) = ['1']: Numeric ID of the certificate authority,type (string) = ['trusted' or 'ca' or 'code-signing']: Type of certificate to import,certificate_file (string): Contents of certificate to import,certificate_file_encoding (string) = ['base64' or 'text']: Encoding used for 'certificate_file' parameter,key_file (string, optional): Contents of private key to import,key_file_encoding (string, optional) = ['base64' or 'text']: Encoding used for 'key_file' parameter,key_passphrase (string, optional): Enter the passphrase that was used to encrypt the private key. If the private key is not encrypted, leave this field blank}
                Required Body Parameters (type(dict) body example)- {
          "ca_id": 0,
          "type": "",
          "certificate_file": "",
          "certificate_file_encoding": "",
          "key_file": "",
          "key_file_encoding": "",
          "key_passphrase": ""
        }
        """
        url_path = "/certificate/import"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertificateNew
    # Function Section Description: Create a new certificate signing request and private key

    def new_certificate_new(self, body=({})):
        """
                Operation: Create a new certificate signing request and private key
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- CertificateNew {ca_id (integer) = ['1']: Select the certificate authority that will be used to sign this request,cert_type (string) = ['tls-client' or 'trusted' or 'ca' or 'code-signing' or 'https']: Select the type of certificate to create from this signing request,country (string): Enter the 2-letter ISO country code of your country,state (string): Enter the full name of your state or province,locality (string): Enter the name of your locality (town or city),organization (string): Enter the name of your organization or company,organizational_unit (string, optional): Enter the name of your organizational unit (e.g. section or division of the company),common_name (string): Enter a name for the certificate. This is the ‘common name’ of the digital certificate,email_address (string): Enter an email address,key_type (string) = ['rsa_1024' or 'rsa_2048' or 'rsa_4096' or 'ec_prime256v1' or 'ec_secp384r1']: Select the type of private key to create for the certificate,device_type (string, optional): Device type to store in certificate subject alternative name,device_udid (string, optional): Device UDID to store in certificate subject alternative name,device_imei (string, optional): Device IMEI to store in certificate subject alternative name,device_iccid (string, optional): Device ICCID to store in certificate subject alternative name,device_serial (string, optional): Device serial to store in certificate subject alternative name,mac_address (string, optional): List of MAC addresses to store in certificate subject alternative name,product_name (string, optional): Product name to store in certificate subject alternative name,product_version (string, optional): Product version to store in certificate subject alternative name,user_name (string, optional): Username to store in certificate subject alternative name,dns_name (string, optional): Host names to include in the Subject Alt Name extension.
        Multiple values can be included, one per line,issue_cert (boolean, optional): Issue this certificate immediately,days (string, optional): The number of days before the certificate will expire,device_name (string, optional): Device name to store in certificate subject alternative name,custom_field (string, optional): Custom fields to store in certificate subject alternative name,user_email_address (string, optional): User’s email address to store in certificate subject alternative name}
                Required Body Parameters (type(dict) body example)- {
          "ca_id": 0,
          "cert_type": "",
          "country": "",
          "state": "",
          "locality": "",
          "organization": "",
          "organizational_unit": "",
          "common_name": "",
          "email_address": "",
          "key_type": "",
          "device_type": "",
          "device_udid": "",
          "device_imei": "",
          "device_iccid": "",
          "device_serial": "",
          "mac_address": "",
          "product_name": "",
          "product_version": "",
          "user_name": "",
          "dns_name": "",
          "issue_cert": false,
          "days": "",
          "device_name": "",
          "custom_field": "",
          "user_email_address": ""
        }
        """
        url_path = "/certificate/new"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertificateReject
    # Function Section Description: Reject a certificate signing request

    def new_certificate_by_cert_id_reject(self, cert_id="", body=({})):
        """
                Operation: Reject a certificate signing request
                HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: cert_id, Description: Numeric ID of the certificate signing request
                Required Body Parameters (body description)- CertificateReject {confirm_reject (boolean, optional): Select this checkbox to confirm the rejection of this request}
                Required Body Parameters (type(dict) body example)- {
          "confirm_reject": false
        }
        """
        url_path = "/certificate/{cert_id}/reject"
        dict_path = {"cert_id": cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertificateRequest
    # Function Section Description: Import a certificate signing request

    def new_certificate_request(self, body=({})):
        """
                Operation: Import a certificate signing request
                HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- CertificateRequest {ca_id (integer) = ['1']: Select the certificate authority that will be used to sign this request,file_csr_encoding (string, optional) = ['base64' or 'text']: Encoding used for 'file_csr' parameter,file_csr (string): Choose a digital certificate signing request to upload. This should be a PEM encoded PKCS#10 certificate request file,cert_type (string) = ['tls-client' or 'trusted' or 'ca' or 'code-signing' or 'https']: Select the type of certificate to create from this signing request,issue_cert (boolean, optional): To modify the subject of the certificate before signing, do not select this checkbox,days (string, optional): The number of days before the certificate will expire}
                Required Body Parameters (type(dict) body example)- {
          "ca_id": 0,
          "file_csr_encoding": "",
          "file_csr": "",
          "cert_type": "",
          "issue_cert": false,
          "days": ""
        }
        """
        url_path = "/certificate/request"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertificateRevoke
    # Function Section Description: Revoke a certificate

    def new_certificate_by_cert_id_revoke(self, cert_id="", body=({})):
        """
                Operation: Revoke a certificate
                HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: cert_id, Description: Numeric ID of the certificate
                Required Body Parameters (body description)- CertificateRevoke {ca_id (integer) = ['1']: Numeric ID of the certificate authority,confirm_revoke (boolean): Select this checkbox to confirm the certificate revocation}
                Required Body Parameters (type(dict) body example)- {
          "ca_id": 0,
          "confirm_revoke": false
        }
        """
        url_path = "/certificate/{cert_id}/revoke"
        dict_path = {"cert_id": cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:CertificateSignRequest
    # Function Section Description: Sign a certificate signing request

    def new_certificate_by_cert_id_sign(self, cert_id="", body=({})):
        """
                Operation: Sign a certificate signing request
                HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: cert_id, Description: Numeric ID of the certificate signing request
                Required Body Parameters (body description)- CertificateSignRequest {ca_id (integer) = ['1']: Numeric ID of the certificate authority,days (integer): The number of days before the certificate will expire,confirm_sign (boolean): Select this checkbox to sign the request and issue a certificate,custom_subject (array[SubjectField], optional): If specified, a list of field/value pairs for the subject of the issued certificate,custom_subject_alt_name (array[SubjectAltNameField], optional): If specified, a list of field/value pairs for the subjectAltName of the issued certificate}SubjectField {field (string) = ['C' or 'ST' or 'L' or 'O' or 'OU' or 'CN' or 'emailAddress' or 'mdpsDeviceName' or 'mdpsDeviceType' or 'mdpsMacAddress' or 'mdpsDeviceSerial' or 'mdpsDeviceImei' or 'mdpsDeviceIccid' or 'mdpsDeviceUdid' or 'mdpsProductName' or 'mdpsProductVersion' or 'mdpsUserName' or 'mdpsEmailAddress' or 'mdpsCustomField']: Field within the subject,value (string): Value of the field}SubjectAltNameField {field (string) = ['DNS' or 'email' or 'IP' or 'URI' or 'userPrincipalName']: Field within the subject alt name,value (string): Value of the field}
                Required Body Parameters (type(dict) body example)- {
          "ca_id": 0,
          "days": 0,
          "confirm_sign": false,
          "custom_subject": [
            {
              "field": "",
              "value": ""
            }
          ],
          "custom_subject_alt_name": [
            {
              "field": "",
              "value": ""
            }
          ]
        }
        """
        url_path = "/certificate/{cert_id}/sign"
        dict_path = {"cert_id": cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # Function Section Name:OnboardDevice
    # Function Section Description: Manage Onboard devices

    def get_onboard_device(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of devices
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/onboard/device"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_onboard_device_by_id(self, id=""):
        """
        Operation: Get a device
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: id, Description: Numeric ID of the device
        """
        url_path = "/onboard/device/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onboard_device_by_id(self, id="", body=({})):
        """
                Operation: Update settings for a device
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: Numeric ID of the device
                Required Body Parameters (body description)- OnboardDevice {id (integer, optional): Numeric ID of the device,status (string, optional) = ['allowed' or 'pending' or 'denied']: Determines whether the device is able to enroll and access the network,device_type (string, optional) = ['Other' or 'Android' or 'iOS' or 'OS X' or 'Windows' or 'Ubuntu' or 'Chromebook' or 'Web' or 'External']: Device type,device_name (string, optional): Device name,device_udid (string, optional): Unique device identifier,device_imei (string, optional): International Mobile Station Equipment Identity, if available,device_iccid (string, optional): SIM card unique serial number, if available,device_serial (string, optional): Serial number of the device, if available,product_name (string, optional): Product name of the device, if available,product_version (string, optional): Product version string of the device, if available,mac_address (array[string], optional): List of MAC addresses associated with the device,serial_number (string, optional): Serial number of device certificate, if device type is "External",usernames (string, optional): Usernames that have enrolled this device,enrolled (boolean, optional): Flag indicating device has been provisioned and currently has a valid certificate,expanded_type (string, optional): Marketing name for the product,mdm_managed (string, optional): Mobile device management (MDM) vendor name, if an endpoint context server reports the device as managed,device_identifier (string, optional): Unique identifier string }
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "status": "",
          "device_type": "",
          "device_name": "",
          "device_udid": "",
          "device_imei": "",
          "device_iccid": "",
          "device_serial": "",
          "product_name": "",
          "product_version": "",
          "mac_address": [
            ""
          ],
          "serial_number": "",
          "usernames": "",
          "enrolled": false,
          "expanded_type": "",
          "mdm_managed": "",
          "device_identifier": ""
        }
        """
        url_path = "/onboard/device/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def delete_onboard_device_by_id(
        self, id="", disconnect_active_sessions="", ignore_disconnect_errors=""
    ):
        """
                Operation: Delete a device
                HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: Numeric ID of the device
                Optional Query Parameter Name: disconnect_active_sessions, Description: true: Disconnects the device from the network (default)false: No action is taken
                Optional Query Parameter Name: ignore_disconnect_errors, Description: true: Optional Disconnect — failure to disconnect will be ignored and the device will be forcibly deleted
        false: Require Disconnect (Recommended) — failure to disconnect will stop the device from being deleted (default)
        When false (‘Require Disconnect’), the device will only be deleted if all other sessions can be disconnected,
        which ensures that the device does not retain access to the network through a currently active session.
        You should only select true (‘Optional Disconnect’) if necessary.
        This parameter is ignored if disconnect_active_sessions is false.
        """
        url_path = "/onboard/device/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {
            "disconnect_active_sessions": disconnect_active_sessions,
            "ignore_disconnect_errors": ignore_disconnect_errors,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
