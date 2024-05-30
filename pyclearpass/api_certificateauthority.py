from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: CertificateAuthority
# FileName: api_certificateauthority.py


class ApiCertificateAuthority(ClearPassAPILogin):

    # API Service: Manage Onboard certificates
    def get_certificate(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of certificates
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: certificate_id, Description: Numeric ID of the certificate
        """
        url_path = "/certificate/{certificate_id}"
        dict_path = {"certificate_id": certificate_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def delete_certificate_by_certificate_id(self, certificate_id=""):
        """
        Operation: Delete a certificate or certificate signing request
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: certificate_id, Description: Numeric ID of the certificate
        """
        url_path = "/certificate/{certificate_id}"
        dict_path = {"certificate_id": certificate_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Get a certificate and its trust chain
    def get_certificate_by_cert_id_chain(self, cert_id=""):
        """
        Operation: Get a certificate and its trust chain
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: cert_id, Description: Numeric ID of the certificate
        """
        url_path = "/certificate/{cert_id}/chain"
        dict_path = {"cert_id": cert_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Export a certificate or certificate signing request
    def new_certificate_by_cert_id_export(self, cert_id="", body=({})):
        """
        Operation: Export a certificate or certificate signing request
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: cert_id, Description: Numeric ID of the certificate
        Required Body Parameters:['export_format']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "export_format" : "", #Select the file format for the exported item. Object Type: string
        "include_chain" : False, #Select this option to include the certificates for the CA and any intermediate certificate authorities. Object Type: boolean
        "include_ca" : "", #Select which certificate authorities to include.. Object Type: string
        "export_password" : "", #Passphrase to protect the PKCS#12 file. Object Type: string
        "export_password2" : "", #Re-enter the passphrase. Object Type: string

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

    # API Service: Import a code-signing, trusted, or CA certificate
    def new_certificate_import(self, body=({})):
        """
        Operation: Import a code-signing, trusted, or CA certificate
        HTTP Response Codes: 200 OK, 400 Client Error, 401 Unprocessable Entity, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['type', 'certificate_file', 'certificate_file_encoding']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "ca_id" : 0, #Numeric ID of the certificate authority. Object Type: integer
        "type" : "", #Type of certificate to import. Object Type: string
        "certificate_file" : "", #Contents of certificate to import. Object Type: string
        "certificate_file_encoding" : "", #Encoding used for 'certificate_file' parameter. Object Type: string
        "key_file" : "", #Contents of private key to import. Object Type: string
        "key_file_encoding" : "", #Encoding used for 'key_file' parameter. Object Type: string
        "key_passphrase" : "", #Enter the passphrase that was used to encrypt the private key. If the private key is not encrypted, leave this field blank. Object Type: string

        }
        """
        url_path = "/certificate/import"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Create a new certificate signing request and private key
    def new_certificate_new(self, body=({})):
        """
        Operation: Create a new certificate signing request and private key
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['ca_id', 'cert_type', 'country', 'state', 'locality', 'organization', 'common_name', 'email_address', 'key_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "ca_id" : 0, #Select the certificate authority that will be used to sign this request. Object Type: integer
        "cert_type" : "", #Select the type of certificate to create from this signing request. Object Type: string
        "country" : "", #Enter the 2-letter ISO country code of your country. Object Type: string
        "state" : "", #Enter the full name of your state or province. Object Type: string
        "locality" : "", #Enter the name of your locality (town or city). Object Type: string
        "organization" : "", #Enter the name of your organization or company. Object Type: string
        "organizational_unit" : "", #Enter the name of your organizational unit (e.g. section or division of the company). Object Type: string
        "common_name" : "", #Enter a name for the certificate. This is the ‘common name’ of the digital certificate. Object Type: string
        "email_address" : "", #Enter an email address. Object Type: string
        "key_type" : "", #Select the type of private key to create for the certificate. Object Type: string
        "device_type" : "", #Device type to store in certificate subject alternative name. Object Type: string
        "device_udid" : "", #Device UDID to store in certificate subject alternative name. Object Type: string
        "device_imei" : "", #Device IMEI to store in certificate subject alternative name. Object Type: string
        "device_iccid" : "", #Device ICCID to store in certificate subject alternative name. Object Type: string
        "device_serial" : "", #Device serial to store in certificate subject alternative name. Object Type: string
        "mac_address" : "", #List of MAC addresses to store in certificate subject alternative name. Object Type: string
        "product_name" : "", #Product name to store in certificate subject alternative name. Object Type: string
        "product_version" : "", #Product version to store in certificate subject alternative name. Object Type: string
        "user_name" : "", #Username to store in certificate subject alternative name. Object Type: string
        "dns_name" : "", #Host names to include in the Subject Alt Name extension.Multiple values can be included, one per line. Object Type: string
        "issue_cert" : False, #Issue this certificate immediately. Object Type: boolean
        "days" : "", #The number of days before the certificate will expire. Object Type: string
        "device_name" : "", #Device name to store in certificate subject alternative name. Object Type: string
        "custom_field" : "", #Custom fields to store in certificate subject alternative name. Object Type: string
        "user_email_address" : "", #User’s email address to store in certificate subject alternative name. Object Type: string

        }
        """
        url_path = "/certificate/new"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Reject a certificate signing request
    def new_certificate_by_cert_id_reject(self, cert_id="", body=({})):
        """
        Operation: Reject a certificate signing request
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: cert_id, Description: Numeric ID of the certificate signing request
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "confirm_reject" : False, #Select this checkbox to confirm the rejection of this request. Object Type: boolean

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

    # API Service: Import a certificate signing request
    def new_certificate_request(self, body=({})):
        """
        Operation: Import a certificate signing request
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['ca_id', 'file_csr', 'cert_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "ca_id" : 0, #Select the certificate authority that will be used to sign this request. Object Type: integer
        "file_csr_encoding" : "", #Encoding used for 'file_csr' parameter. Object Type: string
        "file_csr" : "", #Choose a digital certificate signing request to upload. This should be a PEM encoded PKCS#10 certificate request file. Object Type: string
        "cert_type" : "", #Select the type of certificate to create from this signing request. Object Type: string
        "issue_cert" : False, #To modify the subject of the certificate before signing, do not select this checkbox. Object Type: boolean
        "days" : "", #The number of days before the certificate will expire. Object Type: string

        }
        """
        url_path = "/certificate/request"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Revoke a certificate
    def new_certificate_by_cert_id_revoke(self, cert_id="", body=({})):
        """
        Operation: Revoke a certificate
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: cert_id, Description: Numeric ID of the certificate
        Required Body Parameters:['ca_id', 'confirm_revoke']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "ca_id" : 0, #Numeric ID of the certificate authority. Object Type: integer
        "confirm_revoke" : False, #Select this checkbox to confirm the certificate revocation. Object Type: boolean

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

    # API Service: Sign a certificate signing request
    def new_certificate_by_cert_id_sign(self, cert_id="", body=({})):
        """
                Operation: Sign a certificate signing request
                HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: cert_id, Description: Numeric ID of the certificate signing request
                Required Body Parameters:['ca_id', 'days', 'confirm_sign']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "ca_id" : 0, #Numeric ID of the certificate authority. Object Type: integer
                "days" : 0, #The number of days before the certificate will expire. Object Type: integer
                "confirm_sign" : False, #Select this checkbox to sign the request and issue a certificate. Object Type: boolean
                "custom_subject" : [{
             "field":"", #Field within the subject. Object Type: string
             "value":"", #Value of the field. Object Type: string
        }], #If specified, a list of field/value pairs for the subject of the issued certificate. Object Type: array
                "custom_subject_alt_name" : [{
             "field":"", #Field within the subject alt name. Object Type: string
             "value":"", #Value of the field. Object Type: string
        }], #If specified, a list of field/value pairs for the subjectAltName of the issued certificate. Object Type: array

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

    # API Service: Manage Onboard devices
    def get_onboard_device(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of devices
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the device
        """
        url_path = "/onboard/device/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_onboard_device_by_id(self, id="", body=({})):
        """
        Operation: Update settings for a device
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the device
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #Numeric ID of the device. Object Type: integer
        "status" : "", #Determines whether the device is able to enroll and access the network. Object Type: string
        "device_type" : "", #Device type. Object Type: string
        "device_name" : "", #Device name. Object Type: string
        "device_udid" : "", #Unique device identifier. Object Type: string
        "device_imei" : "", #International Mobile Station Equipment Identity, if available. Object Type: string
        "device_iccid" : "", #SIM card unique serial number, if available. Object Type: string
        "device_serial" : "", #Serial number of the device, if available. Object Type: string
        "product_name" : "", #Product name of the device, if available. Object Type: string
        "product_version" : "", #Product version string of the device, if available. Object Type: string
        "mac_address" : "", #List of MAC addresses associated with the device. Object Type: array
        "serial_number" : "", #Serial number of device certificate, if device type is "External". Object Type: string
        "usernames" : "", #Usernames that have enrolled this device. Object Type: string
        "enrolled" : False, #Flag indicating device has been provisioned and currently has a valid certificate. Object Type: boolean
        "expanded_type" : "", #Marketing name for the product. Object Type: string
        "mdm_managed" : "", #Mobile device management (MDM) vendor name, if an endpoint context server reports the device as managed. Object Type: string
        "device_identifier" : "", #Unique identifier string . Object Type: string

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
        self, disconnect_active_sessions="", ignore_disconnect_errors="", id=""
    ):
        """
                Operation: Delete a device
                HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type (Optional): query, Name: disconnect_active_sessions, Description: <b>true:</b> Disconnects the device from the network (default)<br/><b>false:</b> No action is taken
                Parameter Type (Optional): query, Name: ignore_disconnect_errors, Description:
        <b>true:</b> Optional Disconnect — failure to disconnect will be ignored and the device will be forcibly deleted<br/>
        <b>false:</b> Require Disconnect (Recommended) — failure to disconnect will stop the device from being deleted (default)<br/>
        When false (‘Require Disconnect’), the device will only be deleted if all other sessions can be disconnected,
        which ensures that the device does not retain access to the network through a currently active session.
        You should only select true (‘Optional Disconnect’) if necessary.<br/>
        This parameter is ignored if <span class="code">disconnect_active_sessions</span> is false.
                Parameter Type: path, Name: id, Description: Numeric ID of the device
        """
        url_path = "/onboard/device/{id}"
        dict_query = {
            "disconnect_active_sessions": disconnect_active_sessions,
            "ignore_disconnect_errors": ignore_disconnect_errors,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Onboard users
    def get_user(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of users
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/user"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_user_by_id(self, id=""):
        """
        Operation: Get a user
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the user
        """
        url_path = "/user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_user_by_id(self, id="", body=({})):
        """
        Operation: Update settings for a user
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the user
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "id" : 0, #Numeric ID of the user. Object Type: integer
        "status" : "", #Determines whether the user can enroll devices. Object Type: string
        "username" : "", #Username of the user. Object Type: string
        "device_count" : "", #Number of devices enrolled by this user. Object Type: string

        }
        """
        url_path = "/user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def delete_user_by_id(self, id=""):
        """
        Operation: Delete a user
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: Numeric ID of the user
        """
        url_path = "/user/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
