from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin
)
#File Name: api_explorer_policyelements_v1.py

class ApiPolicyElements(ClearPassAPILogin):

    #Function Section Name:ApplicationDictionary  
    #Function Section Description: Manage Application Dictionaries

    def get_application_dictionary(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of Application Dictionaries
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/application-dictionary'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_application_dictionary(self,body=({})):
        '''
        Operation: Create a new Application Dictionary
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ApplicationDictionaryCreate {name (string): Name of the Application Dictionary,description (string, optional): Description of the Application Dictionary,attributes (array[Attributes]): List of Application Dictionary Attributes}Attributes {attr_name (string): Application Dictionary Attribute Name,attr_type (string) = ['Integer' or 'String' or 'Boolean' or 'Date-Time' or 'TimeOfDay' or 'Day' or 'Date' or 'List' or 'Text' or 'IPv4Address' or 'IPv6Address' or 'MACAddress']: Application Dictionary Attribute Type,allowed_values (string, optional): Allowed Values for Application Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/application-dictionary'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_application_dictionary_by_application_dictionary_id(self,application_dictionary_id=""):
        '''
        Operation: Get an Application Dictionary
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
        '''
        url_path = '/application-dictionary/{application_dictionary_id}'
        dict_path={'application_dictionary_id': application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_application_dictionary_by_application_dictionary_id(self,application_dictionary_id="",body=({})):
        '''
        Operation: Update an Application Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
        Required Body Parameters (body description)- ApplicationDictionaryUpdate {name (string, optional): Name of the Application Dictionary,description (string, optional): Description of the Application Dictionary,attributes (array[Attributes], optional): List of Application Dictionary Attributes}Attributes {attr_name (string): Application Dictionary Attribute Name,attr_type (string) = ['Integer' or 'String' or 'Boolean' or 'Date-Time' or 'TimeOfDay' or 'Day' or 'Date' or 'List' or 'Text' or 'IPv4Address' or 'IPv6Address' or 'MACAddress']: Application Dictionary Attribute Type,allowed_values (string, optional): Allowed Values for Application Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/application-dictionary/{application_dictionary_id}'
        dict_path={'application_dictionary_id': application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_application_dictionary_by_application_dictionary_id(self,application_dictionary_id="",body=({})):
        '''
        Operation: Replace an Application Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
        Required Body Parameters (body description)- ApplicationDictionaryReplace {name (string): Name of the Application Dictionary,description (string, optional): Description of the Application Dictionary,attributes (array[Attributes]): List of Application Dictionary Attributes}Attributes {attr_name (string): Application Dictionary Attribute Name,attr_type (string) = ['Integer' or 'String' or 'Boolean' or 'Date-Time' or 'TimeOfDay' or 'Day' or 'Date' or 'List' or 'Text' or 'IPv4Address' or 'IPv6Address' or 'MACAddress']: Application Dictionary Attribute Type,allowed_values (string, optional): Allowed Values for Application Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/application-dictionary/{application_dictionary_id}'
        dict_path={'application_dictionary_id': application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_application_dictionary_by_application_dictionary_id(self,application_dictionary_id=""):
        '''
        Operation: Delete an Application Dictionary
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: application_dictionary_id, Description: Numeric ID of the Application Dictionary
        '''
        url_path = '/application-dictionary/{application_dictionary_id}'
        dict_path={'application_dictionary_id': application_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_application_dictionary_name_by_name(self,name=""):
        '''
        Operation: Get an Application Dictionary by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the Application Dictionary
        '''
        url_path = '/application-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_application_dictionary_name_by_name(self,name="",body=({})):
        '''
        Operation: Update an Application Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the Application Dictionary
        Required Body Parameters (body description)- ApplicationDictionaryUpdate {name (string, optional): Name of the Application Dictionary,description (string, optional): Description of the Application Dictionary,attributes (array[Attributes], optional): List of Application Dictionary Attributes}Attributes {attr_name (string): Application Dictionary Attribute Name,attr_type (string) = ['Integer' or 'String' or 'Boolean' or 'Date-Time' or 'TimeOfDay' or 'Day' or 'Date' or 'List' or 'Text' or 'IPv4Address' or 'IPv6Address' or 'MACAddress']: Application Dictionary Attribute Type,allowed_values (string, optional): Allowed Values for Application Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/application-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_application_dictionary_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace an Application Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the Application Dictionary
        Required Body Parameters (body description)- ApplicationDictionaryReplace {name (string): Name of the Application Dictionary,description (string, optional): Description of the Application Dictionary,attributes (array[Attributes]): List of Application Dictionary Attributes}Attributes {attr_name (string): Application Dictionary Attribute Name,attr_type (string) = ['Integer' or 'String' or 'Boolean' or 'Date-Time' or 'TimeOfDay' or 'Day' or 'Date' or 'List' or 'Text' or 'IPv4Address' or 'IPv6Address' or 'MACAddress']: Application Dictionary Attribute Type,allowed_values (string, optional): Allowed Values for Application Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/application-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_application_dictionary_name_by_name(self,name=""):
        '''
        Operation: Delete an Application Dictionary by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the Application Dictionary
        '''
        url_path = '/application-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:AuthMethod  
    #Function Section Description: Manage authentication methods

    def get_auth_method(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of authentication methods
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/auth-method'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_auth_method(self,body=({})):
        '''
        Operation: Create a new authentication method
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- AuthMethodCreate {name (string): Name of the auth method,description (string, optional): Description of the auth method,method_type (string) = ['Authorize' or 'CHAP' or 'EAP-FAST' or 'EAP-GTC' or 'EAP-MD5' or 'EAP-MSCHAPv2' or 'EAP-PEAP' or 'EAP-PEAP-Public' or 'EAP-PWD' or 'EAP-TLS' or 'EAP-TTLS' or 'MAC-AUTH' or 'MSCHAP' or 'PAP' or 'TEAP']: Type of the auth method,details (AuthMethodDetails, optional): Details JSON object of the auth method,inner_methods (array[string], optional): List of inner methods of the auth method}AuthMethodDetails {tunnel_pac_lifetime (integer, optional): Tunnel PAC Expire Time,tunnel_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Tunnel PAC Expire Time Units,user_auth_pac_enable (boolean, optional): Authorization PAC,user_auth_pac_lifetime (integer, optional): Authorization PAC Expire Time,user_auth_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Authorization PAC Expire Time Units,machine_pac_enable (boolean, optional): Machine PAC,machine_pac_lifetime (integer, optional): Machine PAC Expire Time,machine_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Machine PAC Expire Time Units,posture_pac_enable (boolean, optional): Posture PAC,posture_pac_lifetime (integer, optional): Posture PAC Expire Time,posture_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Posture PAC Expire Time Units,allow_anonymous_provisioning (boolean, optional): Allow anonymous mode (requires no server certificate),auth_provisioning_require_client_cert (boolean, optional): Require end-host certificate for provisioning,client_certificate_auth (boolean, optional): End-Host Authentication,allow_authenticated_provisioning (boolean, optional): Allow authenticated mode (requires server certificate),certificate_comparison (string, optional) = ['none' or 'dn' or 'cn' or 'san' or 'cn_or_san' or 'binary']: Certificate Comparison,session_timeout (integer, optional): Session Timeout,session_cache_enable (boolean, optional): Session Resumption,challenge (string, optional): Challenge,allow_fast_reconnect (boolean, optional): Fast Reconnect,nap_support_enable (boolean, optional): Microsoft NAP Support,enforce_crypto_binding (string, optional) = ['none' or 'optional' or 'required']: Cryptobinding,public_password (string, optional): Public Password,public_username (string, optional): Public Username,group_name (string, optional) = ['256-bit random ECP group' or '384-bit random ECP group' or '521-bit random ECP group' or '192-bit random ECP group' or '224-bit random ECP group']: Group,server_id (string, optional): Server Id,autz_required (boolean, optional): Authorization Required,ocsp_enable (string, optional) = ['none' or 'optional' or 'required']: Verify Certificate using OCSP,ocsp_url (string, optional): OCSP URL,override_cert_url (boolean, optional): Override OCSP URL from Client,encryption_scheme (string, optional) = ['auto' or 'sso']: Enable Aruba-SSO,allow_unknown_clients (boolean, optional): Allow Unknown End-Hosts,pass_reset_flow (boolean, optional) = ['Challenge' or 'Reject']: Password reset sends in,no_of_retries (boolean, optional): Number of retries}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "method_type": "",
  "details": {
    "tunnel_pac_lifetime": 0,
    "tunnel_pac_lifetime_units": "",
    "user_auth_pac_enable": false,
    "user_auth_pac_lifetime": 0,
    "user_auth_pac_lifetime_units": "",
    "machine_pac_enable": false,
    "machine_pac_lifetime": 0,
    "machine_pac_lifetime_units": "",
    "posture_pac_enable": false,
    "posture_pac_lifetime": 0,
    "posture_pac_lifetime_units": "",
    "allow_anonymous_provisioning": false,
    "auth_provisioning_require_client_cert": false,
    "client_certificate_auth": false,
    "allow_authenticated_provisioning": false,
    "certificate_comparison": "",
    "session_timeout": 0,
    "session_cache_enable": false,
    "challenge": "",
    "allow_fast_reconnect": false,
    "nap_support_enable": false,
    "enforce_crypto_binding": "",
    "public_password": "",
    "public_username": "",
    "group_name": "",
    "server_id": "",
    "autz_required": false,
    "ocsp_enable": "",
    "ocsp_url": "",
    "override_cert_url": false,
    "encryption_scheme": "",
    "allow_unknown_clients": false,
    "pass_reset_flow": false,
    "no_of_retries": false
  },
  "inner_methods": [
    ""
  ]
}
        '''
        url_path = '/auth-method'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_auth_method_by_auth_method_id(self,auth_method_id=""):
        '''
        Operation: Get an authentication method
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: auth_method_id, Description: Numeric ID of the authentication method
        '''
        url_path = '/auth-method/{auth_method_id}'
        dict_path={'auth_method_id': auth_method_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_auth_method_by_auth_method_id(self,auth_method_id="",body=({})):
        '''
        Operation: Update some fields of an authentication method
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: auth_method_id, Description: Numeric ID of the authentication method
        Required Body Parameters (body description)- AuthMethodUpdate {name (string, optional): Name of the auth method,description (string, optional): Description of the auth method,method_type (string, optional) = ['Authorize' or 'CHAP' or 'EAP-FAST' or 'EAP-GTC' or 'EAP-MD5' or 'EAP-MSCHAPv2' or 'EAP-PEAP' or 'EAP-PEAP-Public' or 'EAP-PWD' or 'EAP-TLS' or 'EAP-TTLS' or 'MAC-AUTH' or 'MSCHAP' or 'PAP' or 'TEAP']: Type of the auth method,details (AuthMethodDetails, optional): Details JSON object of the auth method,inner_methods (array[string], optional): List of inner methods of the auth method}AuthMethodDetails {tunnel_pac_lifetime (integer, optional): Tunnel PAC Expire Time,tunnel_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Tunnel PAC Expire Time Units,user_auth_pac_enable (boolean, optional): Authorization PAC,user_auth_pac_lifetime (integer, optional): Authorization PAC Expire Time,user_auth_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Authorization PAC Expire Time Units,machine_pac_enable (boolean, optional): Machine PAC,machine_pac_lifetime (integer, optional): Machine PAC Expire Time,machine_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Machine PAC Expire Time Units,posture_pac_enable (boolean, optional): Posture PAC,posture_pac_lifetime (integer, optional): Posture PAC Expire Time,posture_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Posture PAC Expire Time Units,allow_anonymous_provisioning (boolean, optional): Allow anonymous mode (requires no server certificate),auth_provisioning_require_client_cert (boolean, optional): Require end-host certificate for provisioning,client_certificate_auth (boolean, optional): End-Host Authentication,allow_authenticated_provisioning (boolean, optional): Allow authenticated mode (requires server certificate),certificate_comparison (string, optional) = ['none' or 'dn' or 'cn' or 'san' or 'cn_or_san' or 'binary']: Certificate Comparison,session_timeout (integer, optional): Session Timeout,session_cache_enable (boolean, optional): Session Resumption,challenge (string, optional): Challenge,allow_fast_reconnect (boolean, optional): Fast Reconnect,nap_support_enable (boolean, optional): Microsoft NAP Support,enforce_crypto_binding (string, optional) = ['none' or 'optional' or 'required']: Cryptobinding,public_password (string, optional): Public Password,public_username (string, optional): Public Username,group_name (string, optional) = ['256-bit random ECP group' or '384-bit random ECP group' or '521-bit random ECP group' or '192-bit random ECP group' or '224-bit random ECP group']: Group,server_id (string, optional): Server Id,autz_required (boolean, optional): Authorization Required,ocsp_enable (string, optional) = ['none' or 'optional' or 'required']: Verify Certificate using OCSP,ocsp_url (string, optional): OCSP URL,override_cert_url (boolean, optional): Override OCSP URL from Client,encryption_scheme (string, optional) = ['auto' or 'sso']: Enable Aruba-SSO,allow_unknown_clients (boolean, optional): Allow Unknown End-Hosts,pass_reset_flow (boolean, optional) = ['Challenge' or 'Reject']: Password reset sends in,no_of_retries (boolean, optional): Number of retries}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "method_type": "",
  "details": {
    "tunnel_pac_lifetime": 0,
    "tunnel_pac_lifetime_units": "",
    "user_auth_pac_enable": false,
    "user_auth_pac_lifetime": 0,
    "user_auth_pac_lifetime_units": "",
    "machine_pac_enable": false,
    "machine_pac_lifetime": 0,
    "machine_pac_lifetime_units": "",
    "posture_pac_enable": false,
    "posture_pac_lifetime": 0,
    "posture_pac_lifetime_units": "",
    "allow_anonymous_provisioning": false,
    "auth_provisioning_require_client_cert": false,
    "client_certificate_auth": false,
    "allow_authenticated_provisioning": false,
    "certificate_comparison": "",
    "session_timeout": 0,
    "session_cache_enable": false,
    "challenge": "",
    "allow_fast_reconnect": false,
    "nap_support_enable": false,
    "enforce_crypto_binding": "",
    "public_password": "",
    "public_username": "",
    "group_name": "",
    "server_id": "",
    "autz_required": false,
    "ocsp_enable": "",
    "ocsp_url": "",
    "override_cert_url": false,
    "encryption_scheme": "",
    "allow_unknown_clients": false,
    "pass_reset_flow": false,
    "no_of_retries": false
  },
  "inner_methods": [
    ""
  ]
}
        '''
        url_path = '/auth-method/{auth_method_id}'
        dict_path={'auth_method_id': auth_method_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_auth_method_by_auth_method_id(self,auth_method_id="",body=({})):
        '''
        Operation: Replace an authentication method
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: auth_method_id, Description: Numeric ID of the authentication method
        Required Body Parameters (body description)- AuthMethodReplace {name (string): Name of the auth method,description (string, optional): Description of the auth method,method_type (string) = ['Authorize' or 'CHAP' or 'EAP-FAST' or 'EAP-GTC' or 'EAP-MD5' or 'EAP-MSCHAPv2' or 'EAP-PEAP' or 'EAP-PEAP-Public' or 'EAP-PWD' or 'EAP-TLS' or 'EAP-TTLS' or 'MAC-AUTH' or 'MSCHAP' or 'PAP' or 'TEAP']: Type of the auth method,details (AuthMethodDetails, optional): Details JSON object of the auth method,inner_methods (array[string], optional): List of inner methods of the auth method}AuthMethodDetails {tunnel_pac_lifetime (integer, optional): Tunnel PAC Expire Time,tunnel_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Tunnel PAC Expire Time Units,user_auth_pac_enable (boolean, optional): Authorization PAC,user_auth_pac_lifetime (integer, optional): Authorization PAC Expire Time,user_auth_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Authorization PAC Expire Time Units,machine_pac_enable (boolean, optional): Machine PAC,machine_pac_lifetime (integer, optional): Machine PAC Expire Time,machine_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Machine PAC Expire Time Units,posture_pac_enable (boolean, optional): Posture PAC,posture_pac_lifetime (integer, optional): Posture PAC Expire Time,posture_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Posture PAC Expire Time Units,allow_anonymous_provisioning (boolean, optional): Allow anonymous mode (requires no server certificate),auth_provisioning_require_client_cert (boolean, optional): Require end-host certificate for provisioning,client_certificate_auth (boolean, optional): End-Host Authentication,allow_authenticated_provisioning (boolean, optional): Allow authenticated mode (requires server certificate),certificate_comparison (string, optional) = ['none' or 'dn' or 'cn' or 'san' or 'cn_or_san' or 'binary']: Certificate Comparison,session_timeout (integer, optional): Session Timeout,session_cache_enable (boolean, optional): Session Resumption,challenge (string, optional): Challenge,allow_fast_reconnect (boolean, optional): Fast Reconnect,nap_support_enable (boolean, optional): Microsoft NAP Support,enforce_crypto_binding (string, optional) = ['none' or 'optional' or 'required']: Cryptobinding,public_password (string, optional): Public Password,public_username (string, optional): Public Username,group_name (string, optional) = ['256-bit random ECP group' or '384-bit random ECP group' or '521-bit random ECP group' or '192-bit random ECP group' or '224-bit random ECP group']: Group,server_id (string, optional): Server Id,autz_required (boolean, optional): Authorization Required,ocsp_enable (string, optional) = ['none' or 'optional' or 'required']: Verify Certificate using OCSP,ocsp_url (string, optional): OCSP URL,override_cert_url (boolean, optional): Override OCSP URL from Client,encryption_scheme (string, optional) = ['auto' or 'sso']: Enable Aruba-SSO,allow_unknown_clients (boolean, optional): Allow Unknown End-Hosts,pass_reset_flow (boolean, optional) = ['Challenge' or 'Reject']: Password reset sends in,no_of_retries (boolean, optional): Number of retries}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "method_type": "",
  "details": {
    "tunnel_pac_lifetime": 0,
    "tunnel_pac_lifetime_units": "",
    "user_auth_pac_enable": false,
    "user_auth_pac_lifetime": 0,
    "user_auth_pac_lifetime_units": "",
    "machine_pac_enable": false,
    "machine_pac_lifetime": 0,
    "machine_pac_lifetime_units": "",
    "posture_pac_enable": false,
    "posture_pac_lifetime": 0,
    "posture_pac_lifetime_units": "",
    "allow_anonymous_provisioning": false,
    "auth_provisioning_require_client_cert": false,
    "client_certificate_auth": false,
    "allow_authenticated_provisioning": false,
    "certificate_comparison": "",
    "session_timeout": 0,
    "session_cache_enable": false,
    "challenge": "",
    "allow_fast_reconnect": false,
    "nap_support_enable": false,
    "enforce_crypto_binding": "",
    "public_password": "",
    "public_username": "",
    "group_name": "",
    "server_id": "",
    "autz_required": false,
    "ocsp_enable": "",
    "ocsp_url": "",
    "override_cert_url": false,
    "encryption_scheme": "",
    "allow_unknown_clients": false,
    "pass_reset_flow": false,
    "no_of_retries": false
  },
  "inner_methods": [
    ""
  ]
}
        '''
        url_path = '/auth-method/{auth_method_id}'
        dict_path={'auth_method_id': auth_method_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_auth_method_by_auth_method_id(self,auth_method_id=""):
        '''
        Operation: Delete an authentication method
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: auth_method_id, Description: Numeric ID of the authentication method
        '''
        url_path = '/auth-method/{auth_method_id}'
        dict_path={'auth_method_id': auth_method_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_auth_method_name_by_name(self,name=""):
        '''
        Operation: Get an authentication method by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the authentication method
        '''
        url_path = '/auth-method/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_auth_method_name_by_name(self,name="",body=({})):
        '''
        Operation: Update some fields of an authentication method by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the authentication method
        Required Body Parameters (body description)- AuthMethodUpdate {name (string, optional): Name of the auth method,description (string, optional): Description of the auth method,method_type (string, optional) = ['Authorize' or 'CHAP' or 'EAP-FAST' or 'EAP-GTC' or 'EAP-MD5' or 'EAP-MSCHAPv2' or 'EAP-PEAP' or 'EAP-PEAP-Public' or 'EAP-PWD' or 'EAP-TLS' or 'EAP-TTLS' or 'MAC-AUTH' or 'MSCHAP' or 'PAP' or 'TEAP']: Type of the auth method,details (AuthMethodDetails, optional): Details JSON object of the auth method,inner_methods (array[string], optional): List of inner methods of the auth method}AuthMethodDetails {tunnel_pac_lifetime (integer, optional): Tunnel PAC Expire Time,tunnel_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Tunnel PAC Expire Time Units,user_auth_pac_enable (boolean, optional): Authorization PAC,user_auth_pac_lifetime (integer, optional): Authorization PAC Expire Time,user_auth_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Authorization PAC Expire Time Units,machine_pac_enable (boolean, optional): Machine PAC,machine_pac_lifetime (integer, optional): Machine PAC Expire Time,machine_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Machine PAC Expire Time Units,posture_pac_enable (boolean, optional): Posture PAC,posture_pac_lifetime (integer, optional): Posture PAC Expire Time,posture_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Posture PAC Expire Time Units,allow_anonymous_provisioning (boolean, optional): Allow anonymous mode (requires no server certificate),auth_provisioning_require_client_cert (boolean, optional): Require end-host certificate for provisioning,client_certificate_auth (boolean, optional): End-Host Authentication,allow_authenticated_provisioning (boolean, optional): Allow authenticated mode (requires server certificate),certificate_comparison (string, optional) = ['none' or 'dn' or 'cn' or 'san' or 'cn_or_san' or 'binary']: Certificate Comparison,session_timeout (integer, optional): Session Timeout,session_cache_enable (boolean, optional): Session Resumption,challenge (string, optional): Challenge,allow_fast_reconnect (boolean, optional): Fast Reconnect,nap_support_enable (boolean, optional): Microsoft NAP Support,enforce_crypto_binding (string, optional) = ['none' or 'optional' or 'required']: Cryptobinding,public_password (string, optional): Public Password,public_username (string, optional): Public Username,group_name (string, optional) = ['256-bit random ECP group' or '384-bit random ECP group' or '521-bit random ECP group' or '192-bit random ECP group' or '224-bit random ECP group']: Group,server_id (string, optional): Server Id,autz_required (boolean, optional): Authorization Required,ocsp_enable (string, optional) = ['none' or 'optional' or 'required']: Verify Certificate using OCSP,ocsp_url (string, optional): OCSP URL,override_cert_url (boolean, optional): Override OCSP URL from Client,encryption_scheme (string, optional) = ['auto' or 'sso']: Enable Aruba-SSO,allow_unknown_clients (boolean, optional): Allow Unknown End-Hosts,pass_reset_flow (boolean, optional) = ['Challenge' or 'Reject']: Password reset sends in,no_of_retries (boolean, optional): Number of retries}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "method_type": "",
  "details": {
    "tunnel_pac_lifetime": 0,
    "tunnel_pac_lifetime_units": "",
    "user_auth_pac_enable": false,
    "user_auth_pac_lifetime": 0,
    "user_auth_pac_lifetime_units": "",
    "machine_pac_enable": false,
    "machine_pac_lifetime": 0,
    "machine_pac_lifetime_units": "",
    "posture_pac_enable": false,
    "posture_pac_lifetime": 0,
    "posture_pac_lifetime_units": "",
    "allow_anonymous_provisioning": false,
    "auth_provisioning_require_client_cert": false,
    "client_certificate_auth": false,
    "allow_authenticated_provisioning": false,
    "certificate_comparison": "",
    "session_timeout": 0,
    "session_cache_enable": false,
    "challenge": "",
    "allow_fast_reconnect": false,
    "nap_support_enable": false,
    "enforce_crypto_binding": "",
    "public_password": "",
    "public_username": "",
    "group_name": "",
    "server_id": "",
    "autz_required": false,
    "ocsp_enable": "",
    "ocsp_url": "",
    "override_cert_url": false,
    "encryption_scheme": "",
    "allow_unknown_clients": false,
    "pass_reset_flow": false,
    "no_of_retries": false
  },
  "inner_methods": [
    ""
  ]
}
        '''
        url_path = '/auth-method/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_auth_method_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace an authentication method by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the authentication method
        Required Body Parameters (body description)- AuthMethodReplace {name (string): Name of the auth method,description (string, optional): Description of the auth method,method_type (string) = ['Authorize' or 'CHAP' or 'EAP-FAST' or 'EAP-GTC' or 'EAP-MD5' or 'EAP-MSCHAPv2' or 'EAP-PEAP' or 'EAP-PEAP-Public' or 'EAP-PWD' or 'EAP-TLS' or 'EAP-TTLS' or 'MAC-AUTH' or 'MSCHAP' or 'PAP' or 'TEAP']: Type of the auth method,details (AuthMethodDetails, optional): Details JSON object of the auth method,inner_methods (array[string], optional): List of inner methods of the auth method}AuthMethodDetails {tunnel_pac_lifetime (integer, optional): Tunnel PAC Expire Time,tunnel_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Tunnel PAC Expire Time Units,user_auth_pac_enable (boolean, optional): Authorization PAC,user_auth_pac_lifetime (integer, optional): Authorization PAC Expire Time,user_auth_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Authorization PAC Expire Time Units,machine_pac_enable (boolean, optional): Machine PAC,machine_pac_lifetime (integer, optional): Machine PAC Expire Time,machine_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Machine PAC Expire Time Units,posture_pac_enable (boolean, optional): Posture PAC,posture_pac_lifetime (integer, optional): Posture PAC Expire Time,posture_pac_lifetime_units (string, optional) = ['hours' or 'days' or 'weeks' or 'months' or 'years']: Posture PAC Expire Time Units,allow_anonymous_provisioning (boolean, optional): Allow anonymous mode (requires no server certificate),auth_provisioning_require_client_cert (boolean, optional): Require end-host certificate for provisioning,client_certificate_auth (boolean, optional): End-Host Authentication,allow_authenticated_provisioning (boolean, optional): Allow authenticated mode (requires server certificate),certificate_comparison (string, optional) = ['none' or 'dn' or 'cn' or 'san' or 'cn_or_san' or 'binary']: Certificate Comparison,session_timeout (integer, optional): Session Timeout,session_cache_enable (boolean, optional): Session Resumption,challenge (string, optional): Challenge,allow_fast_reconnect (boolean, optional): Fast Reconnect,nap_support_enable (boolean, optional): Microsoft NAP Support,enforce_crypto_binding (string, optional) = ['none' or 'optional' or 'required']: Cryptobinding,public_password (string, optional): Public Password,public_username (string, optional): Public Username,group_name (string, optional) = ['256-bit random ECP group' or '384-bit random ECP group' or '521-bit random ECP group' or '192-bit random ECP group' or '224-bit random ECP group']: Group,server_id (string, optional): Server Id,autz_required (boolean, optional): Authorization Required,ocsp_enable (string, optional) = ['none' or 'optional' or 'required']: Verify Certificate using OCSP,ocsp_url (string, optional): OCSP URL,override_cert_url (boolean, optional): Override OCSP URL from Client,encryption_scheme (string, optional) = ['auto' or 'sso']: Enable Aruba-SSO,allow_unknown_clients (boolean, optional): Allow Unknown End-Hosts,pass_reset_flow (boolean, optional) = ['Challenge' or 'Reject']: Password reset sends in,no_of_retries (boolean, optional): Number of retries}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "method_type": "",
  "details": {
    "tunnel_pac_lifetime": 0,
    "tunnel_pac_lifetime_units": "",
    "user_auth_pac_enable": false,
    "user_auth_pac_lifetime": 0,
    "user_auth_pac_lifetime_units": "",
    "machine_pac_enable": false,
    "machine_pac_lifetime": 0,
    "machine_pac_lifetime_units": "",
    "posture_pac_enable": false,
    "posture_pac_lifetime": 0,
    "posture_pac_lifetime_units": "",
    "allow_anonymous_provisioning": false,
    "auth_provisioning_require_client_cert": false,
    "client_certificate_auth": false,
    "allow_authenticated_provisioning": false,
    "certificate_comparison": "",
    "session_timeout": 0,
    "session_cache_enable": false,
    "challenge": "",
    "allow_fast_reconnect": false,
    "nap_support_enable": false,
    "enforce_crypto_binding": "",
    "public_password": "",
    "public_username": "",
    "group_name": "",
    "server_id": "",
    "autz_required": false,
    "ocsp_enable": "",
    "ocsp_url": "",
    "override_cert_url": false,
    "encryption_scheme": "",
    "allow_unknown_clients": false,
    "pass_reset_flow": false,
    "no_of_retries": false
  },
  "inner_methods": [
    ""
  ]
}
        '''
        url_path = '/auth-method/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_auth_method_name_by_name(self,name=""):
        '''
        Operation: Delete an authentication method by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the authentication method
        '''
        url_path = '/auth-method/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:AuthSource  
    #Function Section Description: Manage authentication sources

    def get_auth_source(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of authentication sources
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/auth-source'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_auth_source(self,body=({})):
        '''
        Operation: Create a new authentication source
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- AuthSourceCreate {name (string): Name of the auth source,description (string, optional): Description of the auth source,type (string) = ['AD' or 'Ldap' or 'Sql' or 'HTTP' or 'Kerberos' or 'Local' or 'SHL' or 'TokenServer']: Type of the auth source,use_for_authorization (boolean, optional): Enable to use this Authentication Source,authorization_source_names (array[string], optional): additional auth-sources from which role-mapping attributes to be fetched,cppm_primary_auth_source_connection_details (AuthSourceConnectionDetailsMetadataCreate): details of Authentication source,auth_source_radius_attributes (AuthSourceRadiusAttributeDetailsCreate, optional): details of authSourceRadiusAttributes,cppm_auth_source_connection_backups (AuthSourceBackupConnectionDetailsMetadataCreate, optional): details of authentication source backups,auth_source_filters (AuthSourceFiltersDetailsCreate, optional): details of auth_source_filters,server_timeout (integer): Time out if the Authentication source fails to send a response to an authorization query,cache_timeout (integer): Specify the duration in number of seconds for which the attributes are cached.}AuthSourceConnectionDetailsMetadataCreate {host_name (string, optional): Host Name of Authentication Source,connection_security (string, optional) = ['None' or 'StartTLS' or 'AD_Over_SSL']: Connection Security of Authentication Source,connection_port (integer, optional): Connection port of Authentication Source,verify_server_certificate (boolean, optional): Boolean to verify Server Certificate for secure connection,trusted_certificate_id (integer, optional): Trusted certificate ID used during verification of server certificate,bind_DN (string, optional): Bind DN of Authentication Source,bind_password (string, optional): Bind Password of Authentication Source,net_BIOS_domain_name (string, optional): Net-BIOS-Domain-Name of Authentication Source,base_DN (string, optional): Base DN of Authentication Source,search_scope (string, optional) = ['Base_Object_Search' or 'One_Level_Search' or 'SubTree_Search']: Search Scope of Authentication Source,ldap_referrals (boolean, optional): Follow referrals for Authentication Source,bind_user (boolean, optional): Allow bind using user password,user_certificate (string, optional): User Certificate of Authentication Source,always_use_netBIOS_name (boolean, optional): Boolean to always use NetBIOS name instead of the domain part in username for authentication,replace_special_char (boolean, optional): Enable special character handling for LDAP query,password_attribute (string, optional): Password Attribute of Authentication Source,password_type (string, optional) = ['ClearText' or 'NT_Hash' or 'LM_Hash' or 'SHA1' or 'SHA256' or 'SHA512' or 'MD5' or 'SHA1_Base64' or 'SHA256_Base64' or 'SHA512_Base64']: Type of the Password,password_header (string, optional): Password Header of Authentication Source,server_name (string, optional): Server Name of Authentication Source,port (integer, optional): Port of SQL Server,database_name (string, optional): Name of the database,login_user_name (string, optional): User name to login to the Server,login_password (string, optional): Password to login to SQL Server,timeout (integer, optional): Timeout of the Connection,odbc_type (string, optional) = ['PostgreSQL' or 'Oracle_11g' or 'MariaDB' or 'MSSQL']: ODBC Type of SQL DB,base_URL (string, optional): Base URL of Authentication Source,realm (string, optional): Realm of Authentication Source,server_principal (string, optional): Server Principal of Authentication Source,server_principal_password (string, optional): Server Principal Password of Authentication Source,authorization_token (string, optional): Authorization Token of Authentication Source,protocol (string, optional): Protocol of Authentication Source,secret (string, optional): Secret key of Authentication Source,tenant_id (string, optional): Tenant ID of Authentication Source,client_id (string, optional): Client ID of Authentication Source,client_secret (string, optional): Client Secret of Authentication Source,static_host_lists (array[string], optional): Static Host Lists of Authentication Source,client_certificate (string, optional): Client Certificates id,status_server_messages (string, optional): Boolean to send status-server messages}AuthSourceRadiusAttributeDetailsCreate {vendor_id (integer, optional): vendor ID of AuthSourceRadiusAttribute,attribute_id (integer, optional): attribute ID of AuthSourceRadiusAttribute,attribute_value (string, optional): attribute value of AuthSourceRadiusAttribute,attribute_operation (integer, optional): attribute operation of AuthSourceRadiusAttribute,attribute_display_value (string, optional): attribute display value of AuthSourceRadiusAttribute}AuthSourceBackupConnectionDetailsMetadataCreate {order_no (integer, optional): Priority of the Authentication Source,cppm_auth_source_connection_details (undefined, optional): Connection Details of the Authentication source backup}AuthSourceFiltersDetailsCreate {source_Id (integer, optional): SourceId of AuthSourceFilter,name (string, optional): Name of AuthSourceFilter,param_values (string, optional): Parameter Values of AuthSourceFilter,query (string, optional): Query of AuthSourceFilter,selected_Dn (string, optional): SelectedDn of AuthSourceFilter,attributes (AttributesMetadataCreate, optional): Details of CppmAuthSourceFilterAttributes,details (DetailsMetadataCreate, optional): Details of CppmAuthSourceFilterDetails}AttributesMetadataCreate {attribute_name (string, optional): Attribute name of AuthSourceFilterAttributes,alias_name (string, optional): AliasName of AuthSourceFilterAttributes,attribute_type (string, optional): attribute_type of AuthSourceFilterAttributes,enable_as_role (boolean, optional): EnableAsRole of AuthSourceFilterAttributes,enable_as_user_attribute (boolean, optional): EnableAsUserAttr of AuthSourceFilterAttributes}DetailsMetadataCreate {attribute_name (string, optional): Attribute name of AuthSourceFilterDetails,attribute_value (string, optional): Attribute Value of AuthSourceFilterDetails}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "type": "",
  "use_for_authorization": false,
  "authorization_source_names": [
    ""
  ],
  "cppm_primary_auth_source_connection_details": {
    "host_name": "",
    "connection_security": "",
    "connection_port": 0,
    "verify_server_certificate": false,
    "trusted_certificate_id": 0,
    "bind_DN": "",
    "bind_password": "",
    "net_BIOS_domain_name": "",
    "base_DN": "",
    "search_scope": "",
    "ldap_referrals": false,
    "bind_user": false,
    "user_certificate": "",
    "always_use_netBIOS_name": false,
    "replace_special_char": false,
    "password_attribute": "",
    "password_type": "",
    "password_header": "",
    "server_name": "",
    "port": 0,
    "database_name": "",
    "login_user_name": "",
    "login_password": "",
    "timeout": 0,
    "odbc_type": "",
    "base_URL": "",
    "realm": "",
    "server_principal": "",
    "server_principal_password": "",
    "authorization_token": "",
    "protocol": "",
    "secret": "",
    "tenant_id": "",
    "client_id": "",
    "client_secret": "",
    "static_host_lists": [
      ""
    ],
    "client_certificate": "",
    "status_server_messages": ""
  },
  "auth_source_radius_attributes": {
    "vendor_id": 0,
    "attribute_id": 0,
    "attribute_value": "",
    "attribute_operation": 0,
    "attribute_display_value": ""
  },
  "cppm_auth_source_connection_backups": {
    "order_no": 0
  },
  "auth_source_filters": {
    "source_Id": 0,
    "name": "",
    "param_values": "",
    "query": "",
    "selected_Dn": "",
    "attributes": {
      "attribute_name": "",
      "alias_name": "",
      "attribute_type": "",
      "enable_as_role": false,
      "enable_as_user_attribute": false
    },
    "details": {
      "attribute_name": "",
      "attribute_value": ""
    }
  },
  "server_timeout": 0,
  "cache_timeout": 0
}
        '''
        url_path = '/auth-source'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_auth_source_by_auth_source_id(self,auth_source_id=""):
        '''
        Operation: Get an authentication source
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: auth_source_id, Description: Numeric ID of the authentication source
        '''
        url_path = '/auth-source/{auth_source_id}'
        dict_path={'auth_source_id': auth_source_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_auth_source_by_auth_source_id(self,auth_source_id="",body=({})):
        '''
        Operation: Update some fields of an authentication source
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: auth_source_id, Description: Numeric ID of the authentication source
        Required Body Parameters (body description)- AuthSourceUpdate {name (string, optional): Name of the auth source,description (string, optional): Description of the auth source,type (string, optional) = ['AD' or 'Ldap' or 'Sql' or 'HTTP' or 'Kerberos' or 'Local' or 'SHL' or 'TokenServer']: Type of the auth source,use_for_authorization (boolean, optional): Enable to use this Authentication Source,authorization_source_names (array[string], optional): additional auth-sources from which role-mapping attributes to be fetched,cppm_primary_auth_source_connection_details (AuthSourceConnectionDetailsUpdate, optional): details of Authentication source,auth_source_radius_attributes (AuthSourceRadiusAttributeDetailsUpdate, optional): details of authSourceRadiusAttributes,cppm_auth_source_connection_backups (AuthSourceBackupConnectionDetailsMetadataUpdate, optional): details of authentication source backups,auth_source_filters (AuthSourceFiltersDetailsUpdate, optional): details of auth_source_filters,server_timeout (integer, optional): Time out if the Authentication source fails to send a response to an authorization query,cache_timeout (integer, optional): Specify the duration in number of seconds for which the attributes are cached.}AuthSourceConnectionDetailsUpdate {host_name (string, optional): Host Name of Authentication Source,connection_security (string, optional) = ['None' or 'StartTLS' or 'AD_Over_SSL']: Connection Security of Authentication Source,connection_port (integer, optional): Connection port of Authentication Source,verify_server_certificate (boolean, optional): Boolean to verify Server Certificate for secure connection,trusted_certificate_id (integer, optional): Trusted certificate ID used during verification of server certificate,bind_DN (string, optional): Bind DN of Authentication Source,bind_password (string, optional): Bind Password of Authentication Source,net_BIOS_domain_name (string, optional): Net-BIOS-Domain-Name of Authentication Source,base_DN (string, optional): Base DN of Authentication Source,search_scope (string, optional) = ['Base_Object_Search' or 'One_Level_Search' or 'SubTree_Search']: Search Scope of Authentication Source,ldap_referrals (boolean, optional): Follow referrals for Authentication Source,bind_user (boolean, optional): Allow bind using user password,user_certificate (string, optional): User Certificate of Authentication Source,always_use_netBIOS_name (boolean, optional): Boolean to always use NetBIOS name instead of the domain part in username for authentication,replace_special_char (boolean, optional): Enable special character handling for LDAP query,password_attribute (string, optional): Password Attribute of Authentication Source,password_type (string, optional) = ['ClearText' or 'NT_Hash' or 'LM_Hash' or 'SHA1' or 'SHA256' or 'SHA512' or 'MD5' or 'SHA1_Base64' or 'SHA256_Base64' or 'SHA512_Base64']: Type of the Password,password_header (string, optional): Password Header of Authentication Source,server_name (string, optional): Server Name of Authentication Source,port (integer, optional): Port of SQL Server,database_name (string, optional): Name of the database,login_user_name (string, optional): User name to login to the Server,login_password (string, optional): Password to login to SQL Server,timeout (integer, optional): Timeout of the Connection,odbc_type (string, optional) = ['PostgreSQL' or 'Oracle_11g' or 'MariaDB' or 'MSSQL']: ODBC Type of SQL DB,base_URL (string, optional): Base URL of Authentication Source,realm (string, optional): Realm of Authentication Source,server_principal (string, optional): Server Principal of Authentication Source,server_principal_password (string, optional): Server Principal Password of Authentication Source,authorization_token (string, optional): Authorization Token of Authentication Source,protocol (string, optional): Protocol of Authentication Source,secret (string, optional): Secret key of Authentication Source,tenant_id (string, optional): Tenant ID of Authentication Source,client_id (string, optional): Client ID of Authentication Source,client_secret (string, optional): Client Secret of Authentication Source,static_host_lists (array[string], optional): Static Host Lists of Authentication Source,client_certificate (string, optional): Client Certificates id,status_server_messages (string, optional): Boolean to send status-server messages}AuthSourceRadiusAttributeDetailsUpdate {vendor_id (integer, optional): vendor ID of AuthSourceRadiusAttribute,attribute_id (integer, optional): attribute ID of AuthSourceRadiusAttribute,attribute_value (string, optional): attribute value of AuthSourceRadiusAttribute,attribute_operation (integer, optional): attribute operation of AuthSourceRadiusAttribute,attribute_display_value (string, optional): attribute display value of AuthSourceRadiusAttribute}AuthSourceBackupConnectionDetailsMetadataUpdate {order_no (integer, optional): Priority of the Authentication Source,cppm_auth_source_connection_details (undefined, optional): Connection Details of the Authentication source backup}AuthSourceFiltersDetailsUpdate {source_Id (integer, optional): SourceId of AuthSourceFilter,name (string, optional): Name of AuthSourceFilter,param_values (string, optional): Parameter Values of AuthSourceFilter,query (string, optional): Query of AuthSourceFilter,selected_Dn (string, optional): SelectedDn of AuthSourceFilter,attributes (AttributesMetadataUpdate, optional): Details of CppmAuthSourceFilterAttributes,details (DetailsMetadataUpdate, optional): Details of CppmAuthSourceFilterDetails}AttributesMetadataUpdate {attribute_name (string, optional): Attribute name of AuthSourceFilterAttributes,alias_name (string, optional): AliasName of AuthSourceFilterAttributes,attribute_type (string, optional): attribute_type of AuthSourceFilterAttributes,enable_as_role (boolean, optional): EnableAsRole of AuthSourceFilterAttributes,enable_as_user_attribute (boolean, optional): EnableAsUserAttr of AuthSourceFilterAttributes}DetailsMetadataUpdate {attribute_name (string, optional): Attribute name of AuthSourceFilterDetails,attribute_value (string, optional): Attribute Value of AuthSourceFilterDetails}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "type": "",
  "use_for_authorization": false,
  "authorization_source_names": [
    ""
  ],
  "cppm_primary_auth_source_connection_details": {
    "host_name": "",
    "connection_security": "",
    "connection_port": 0,
    "verify_server_certificate": false,
    "trusted_certificate_id": 0,
    "bind_DN": "",
    "bind_password": "",
    "net_BIOS_domain_name": "",
    "base_DN": "",
    "search_scope": "",
    "ldap_referrals": false,
    "bind_user": false,
    "user_certificate": "",
    "always_use_netBIOS_name": false,
    "replace_special_char": false,
    "password_attribute": "",
    "password_type": "",
    "password_header": "",
    "server_name": "",
    "port": 0,
    "database_name": "",
    "login_user_name": "",
    "login_password": "",
    "timeout": 0,
    "odbc_type": "",
    "base_URL": "",
    "realm": "",
    "server_principal": "",
    "server_principal_password": "",
    "authorization_token": "",
    "protocol": "",
    "secret": "",
    "tenant_id": "",
    "client_id": "",
    "client_secret": "",
    "static_host_lists": [
      ""
    ],
    "client_certificate": "",
    "status_server_messages": ""
  },
  "auth_source_radius_attributes": {
    "vendor_id": 0,
    "attribute_id": 0,
    "attribute_value": "",
    "attribute_operation": 0,
    "attribute_display_value": ""
  },
  "cppm_auth_source_connection_backups": {
    "order_no": 0
  },
  "auth_source_filters": {
    "source_Id": 0,
    "name": "",
    "param_values": "",
    "query": "",
    "selected_Dn": "",
    "attributes": {
      "attribute_name": "",
      "alias_name": "",
      "attribute_type": "",
      "enable_as_role": false,
      "enable_as_user_attribute": false
    },
    "details": {
      "attribute_name": "",
      "attribute_value": ""
    }
  },
  "server_timeout": 0,
  "cache_timeout": 0
}
        '''
        url_path = '/auth-source/{auth_source_id}'
        dict_path={'auth_source_id': auth_source_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_auth_source_by_auth_source_id(self,auth_source_id="",body=({})):
        '''
        Operation: Replace an authentication source
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: auth_source_id, Description: Numeric ID of the authentication source
        Required Body Parameters (body description)- AuthSourceReplace {name (string): Name of the auth source,description (string, optional): Description of the auth source,type (string) = ['AD' or 'Ldap' or 'Sql' or 'HTTP' or 'Kerberos' or 'Local' or 'SHL' or 'TokenServer']: Type of the auth source,use_for_authorization (boolean, optional): Enable to use this Authentication Source,authorization_source_names (array[string], optional): additional auth-sources from which role-mapping attributes to be fetched,cppm_primary_auth_source_connection_details (AuthSourceConnectionDetailsMetadataReplace): details of Authentication source,auth_source_radius_attributes (AuthSourceRadiusAttributeDetailsReplace, optional): details of authSourceRadiusAttributes,cppm_auth_source_connection_backups (AuthSourceBackupConnectionDetailsMetadataReplace, optional): details of authentication source backups,auth_source_filters (AuthSourceFiltersDetailsReplace, optional): details of auth_source_filters,server_timeout (integer): Time out if the Authentication source fails to send a response to an authorization query,cache_timeout (integer): Specify the duration in number of seconds for which the attributes are cached.}AuthSourceConnectionDetailsMetadataReplace {host_name (string, optional): Host Name of Authentication Source,connection_security (string, optional) = ['None' or 'StartTLS' or 'AD_Over_SSL']: Connection Security of Authentication Source,connection_port (integer, optional): Connection port of Authentication Source,verify_server_certificate (boolean, optional): Boolean to verify Server Certificate for secure connection,trusted_certificate_id (integer, optional): Trusted certificate ID used during verification of server certificate,bind_DN (string, optional): Bind DN of Authentication Source,bind_password (string, optional): Bind Password of Authentication Source,net_BIOS_domain_name (string, optional): Net-BIOS-Domain-Name of Authentication Source,base_DN (string, optional): Base DN of Authentication Source,search_scope (string, optional) = ['Base_Object_Search' or 'One_Level_Search' or 'SubTree_Search']: Search Scope of Authentication Source,ldap_referrals (boolean, optional): Follow referrals for Authentication Source,bind_user (boolean, optional): Allow bind using user password,user_certificate (string, optional): User Certificate of Authentication Source,always_use_netBIOS_name (boolean, optional): Boolean to always use NetBIOS name instead of the domain part in username for authentication,replace_special_char (boolean, optional): Enable special character handling for LDAP query,password_attribute (string, optional): Password Attribute of Authentication Source,password_type (string, optional) = ['ClearText' or 'NT_Hash' or 'LM_Hash' or 'SHA1' or 'SHA256' or 'SHA512' or 'MD5' or 'SHA1_Base64' or 'SHA256_Base64' or 'SHA512_Base64']: Type of the Password,password_header (string, optional): Password Header of Authentication Source,server_name (string, optional): Server Name of Authentication Source,port (integer, optional): Port of SQL Server,database_name (string, optional): Name of the database,login_user_name (string, optional): User name to login to the Server,login_password (string, optional): Password to login to SQL Server,timeout (integer, optional): Timeout of the Connection,odbc_type (string, optional) = ['PostgreSQL' or 'Oracle_11g' or 'MariaDB' or 'MSSQL']: ODBC Type of SQL DB,base_URL (string, optional): Base URL of Authentication Source,realm (string, optional): Realm of Authentication Source,server_principal (string, optional): Server Principal of Authentication Source,server_principal_password (string, optional): Server Principal Password of Authentication Source,authorization_token (string, optional): Authorization Token of Authentication Source,protocol (string, optional): Protocol of Authentication Source,secret (string, optional): Secret key of Authentication Source,tenant_id (string, optional): Tenant ID of Authentication Source,client_id (string, optional): Client ID of Authentication Source,client_secret (string, optional): Client Secret of Authentication Source,static_host_lists (array[string], optional): Static Host Lists of Authentication Source,client_certificate (string, optional): Client Certificates id,status_server_messages (string, optional): Boolean to send status-server messages}AuthSourceRadiusAttributeDetailsReplace {vendor_id (integer, optional): vendor ID of AuthSourceRadiusAttribute,attribute_id (integer, optional): attribute ID of AuthSourceRadiusAttribute,attribute_value (string, optional): attribute value of AuthSourceRadiusAttribute,attribute_operation (integer, optional): attribute operation of AuthSourceRadiusAttribute,attribute_display_value (string, optional): attribute display value of AuthSourceRadiusAttribute}AuthSourceBackupConnectionDetailsMetadataReplace {order_no (integer, optional): Priority of the Authentication Source,cppm_auth_source_connection_details (undefined, optional): Connection Details of the Authentication source backup}AuthSourceFiltersDetailsReplace {source_Id (integer, optional): SourceId of AuthSourceFilter,name (string, optional): Name of AuthSourceFilter,param_values (string, optional): Parameter Values of AuthSourceFilter,query (string, optional): Query of AuthSourceFilter,selected_Dn (string, optional): SelectedDn of AuthSourceFilter,attributes (AttributesMetadataReplace, optional): Details of CppmAuthSourceFilterAttributes,details (DetailsMetadataReplace, optional): Details of CppmAuthSourceFilterDetails}AttributesMetadataReplace {attribute_name (string, optional): Attribute name of AuthSourceFilterAttributes,alias_name (string, optional): AliasName of AuthSourceFilterAttributes,attribute_type (string, optional): attribute_type of AuthSourceFilterAttributes,enable_as_role (boolean, optional): EnableAsRole of AuthSourceFilterAttributes,enable_as_user_attribute (boolean, optional): EnableAsUserAttr of AuthSourceFilterAttributes}DetailsMetadataReplace {attribute_name (string, optional): Attribute name of AuthSourceFilterDetails,attribute_value (string, optional): Attribute Value of AuthSourceFilterDetails}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "type": "",
  "use_for_authorization": false,
  "authorization_source_names": [
    ""
  ],
  "cppm_primary_auth_source_connection_details": {
    "host_name": "",
    "connection_security": "",
    "connection_port": 0,
    "verify_server_certificate": false,
    "trusted_certificate_id": 0,
    "bind_DN": "",
    "bind_password": "",
    "net_BIOS_domain_name": "",
    "base_DN": "",
    "search_scope": "",
    "ldap_referrals": false,
    "bind_user": false,
    "user_certificate": "",
    "always_use_netBIOS_name": false,
    "replace_special_char": false,
    "password_attribute": "",
    "password_type": "",
    "password_header": "",
    "server_name": "",
    "port": 0,
    "database_name": "",
    "login_user_name": "",
    "login_password": "",
    "timeout": 0,
    "odbc_type": "",
    "base_URL": "",
    "realm": "",
    "server_principal": "",
    "server_principal_password": "",
    "authorization_token": "",
    "protocol": "",
    "secret": "",
    "tenant_id": "",
    "client_id": "",
    "client_secret": "",
    "static_host_lists": [
      ""
    ],
    "client_certificate": "",
    "status_server_messages": ""
  },
  "auth_source_radius_attributes": {
    "vendor_id": 0,
    "attribute_id": 0,
    "attribute_value": "",
    "attribute_operation": 0,
    "attribute_display_value": ""
  },
  "cppm_auth_source_connection_backups": {
    "order_no": 0
  },
  "auth_source_filters": {
    "source_Id": 0,
    "name": "",
    "param_values": "",
    "query": "",
    "selected_Dn": "",
    "attributes": {
      "attribute_name": "",
      "alias_name": "",
      "attribute_type": "",
      "enable_as_role": false,
      "enable_as_user_attribute": false
    },
    "details": {
      "attribute_name": "",
      "attribute_value": ""
    }
  },
  "server_timeout": 0,
  "cache_timeout": 0
}
        '''
        url_path = '/auth-source/{auth_source_id}'
        dict_path={'auth_source_id': auth_source_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_auth_source_by_auth_source_id(self,auth_source_id=""):
        '''
        Operation: Delete an authentication source
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: auth_source_id, Description: Numeric ID of the authentication source
        '''
        url_path = '/auth-source/{auth_source_id}'
        dict_path={'auth_source_id': auth_source_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_auth_source_name_by_name(self,name=""):
        '''
        Operation: Get an authentication source by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the authentication source
        '''
        url_path = '/auth-source/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_auth_source_name_by_name(self,name="",body=({})):
        '''
        Operation: Update some fields of an authentication source by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the authentication source
        Required Body Parameters (body description)- AuthSourceUpdate {name (string, optional): Name of the auth source,description (string, optional): Description of the auth source,type (string, optional) = ['AD' or 'Ldap' or 'Sql' or 'HTTP' or 'Kerberos' or 'Local' or 'SHL' or 'TokenServer']: Type of the auth source,use_for_authorization (boolean, optional): Enable to use this Authentication Source,authorization_source_names (array[string], optional): additional auth-sources from which role-mapping attributes to be fetched,cppm_primary_auth_source_connection_details (AuthSourceConnectionDetailsUpdate, optional): details of Authentication source,auth_source_radius_attributes (AuthSourceRadiusAttributeDetailsUpdate, optional): details of authSourceRadiusAttributes,cppm_auth_source_connection_backups (AuthSourceBackupConnectionDetailsMetadataUpdate, optional): details of authentication source backups,auth_source_filters (AuthSourceFiltersDetailsUpdate, optional): details of auth_source_filters,server_timeout (integer, optional): Time out if the Authentication source fails to send a response to an authorization query,cache_timeout (integer, optional): Specify the duration in number of seconds for which the attributes are cached.}AuthSourceConnectionDetailsUpdate {host_name (string, optional): Host Name of Authentication Source,connection_security (string, optional) = ['None' or 'StartTLS' or 'AD_Over_SSL']: Connection Security of Authentication Source,connection_port (integer, optional): Connection port of Authentication Source,verify_server_certificate (boolean, optional): Boolean to verify Server Certificate for secure connection,trusted_certificate_id (integer, optional): Trusted certificate ID used during verification of server certificate,bind_DN (string, optional): Bind DN of Authentication Source,bind_password (string, optional): Bind Password of Authentication Source,net_BIOS_domain_name (string, optional): Net-BIOS-Domain-Name of Authentication Source,base_DN (string, optional): Base DN of Authentication Source,search_scope (string, optional) = ['Base_Object_Search' or 'One_Level_Search' or 'SubTree_Search']: Search Scope of Authentication Source,ldap_referrals (boolean, optional): Follow referrals for Authentication Source,bind_user (boolean, optional): Allow bind using user password,user_certificate (string, optional): User Certificate of Authentication Source,always_use_netBIOS_name (boolean, optional): Boolean to always use NetBIOS name instead of the domain part in username for authentication,replace_special_char (boolean, optional): Enable special character handling for LDAP query,password_attribute (string, optional): Password Attribute of Authentication Source,password_type (string, optional) = ['ClearText' or 'NT_Hash' or 'LM_Hash' or 'SHA1' or 'SHA256' or 'SHA512' or 'MD5' or 'SHA1_Base64' or 'SHA256_Base64' or 'SHA512_Base64']: Type of the Password,password_header (string, optional): Password Header of Authentication Source,server_name (string, optional): Server Name of Authentication Source,port (integer, optional): Port of SQL Server,database_name (string, optional): Name of the database,login_user_name (string, optional): User name to login to the Server,login_password (string, optional): Password to login to SQL Server,timeout (integer, optional): Timeout of the Connection,odbc_type (string, optional) = ['PostgreSQL' or 'Oracle_11g' or 'MariaDB' or 'MSSQL']: ODBC Type of SQL DB,base_URL (string, optional): Base URL of Authentication Source,realm (string, optional): Realm of Authentication Source,server_principal (string, optional): Server Principal of Authentication Source,server_principal_password (string, optional): Server Principal Password of Authentication Source,authorization_token (string, optional): Authorization Token of Authentication Source,protocol (string, optional): Protocol of Authentication Source,secret (string, optional): Secret key of Authentication Source,tenant_id (string, optional): Tenant ID of Authentication Source,client_id (string, optional): Client ID of Authentication Source,client_secret (string, optional): Client Secret of Authentication Source,static_host_lists (array[string], optional): Static Host Lists of Authentication Source,client_certificate (string, optional): Client Certificates id,status_server_messages (string, optional): Boolean to send status-server messages}AuthSourceRadiusAttributeDetailsUpdate {vendor_id (integer, optional): vendor ID of AuthSourceRadiusAttribute,attribute_id (integer, optional): attribute ID of AuthSourceRadiusAttribute,attribute_value (string, optional): attribute value of AuthSourceRadiusAttribute,attribute_operation (integer, optional): attribute operation of AuthSourceRadiusAttribute,attribute_display_value (string, optional): attribute display value of AuthSourceRadiusAttribute}AuthSourceBackupConnectionDetailsMetadataUpdate {order_no (integer, optional): Priority of the Authentication Source,cppm_auth_source_connection_details (undefined, optional): Connection Details of the Authentication source backup}AuthSourceFiltersDetailsUpdate {source_Id (integer, optional): SourceId of AuthSourceFilter,name (string, optional): Name of AuthSourceFilter,param_values (string, optional): Parameter Values of AuthSourceFilter,query (string, optional): Query of AuthSourceFilter,selected_Dn (string, optional): SelectedDn of AuthSourceFilter,attributes (AttributesMetadataUpdate, optional): Details of CppmAuthSourceFilterAttributes,details (DetailsMetadataUpdate, optional): Details of CppmAuthSourceFilterDetails}AttributesMetadataUpdate {attribute_name (string, optional): Attribute name of AuthSourceFilterAttributes,alias_name (string, optional): AliasName of AuthSourceFilterAttributes,attribute_type (string, optional): attribute_type of AuthSourceFilterAttributes,enable_as_role (boolean, optional): EnableAsRole of AuthSourceFilterAttributes,enable_as_user_attribute (boolean, optional): EnableAsUserAttr of AuthSourceFilterAttributes}DetailsMetadataUpdate {attribute_name (string, optional): Attribute name of AuthSourceFilterDetails,attribute_value (string, optional): Attribute Value of AuthSourceFilterDetails}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "type": "",
  "use_for_authorization": false,
  "authorization_source_names": [
    ""
  ],
  "cppm_primary_auth_source_connection_details": {
    "host_name": "",
    "connection_security": "",
    "connection_port": 0,
    "verify_server_certificate": false,
    "trusted_certificate_id": 0,
    "bind_DN": "",
    "bind_password": "",
    "net_BIOS_domain_name": "",
    "base_DN": "",
    "search_scope": "",
    "ldap_referrals": false,
    "bind_user": false,
    "user_certificate": "",
    "always_use_netBIOS_name": false,
    "replace_special_char": false,
    "password_attribute": "",
    "password_type": "",
    "password_header": "",
    "server_name": "",
    "port": 0,
    "database_name": "",
    "login_user_name": "",
    "login_password": "",
    "timeout": 0,
    "odbc_type": "",
    "base_URL": "",
    "realm": "",
    "server_principal": "",
    "server_principal_password": "",
    "authorization_token": "",
    "protocol": "",
    "secret": "",
    "tenant_id": "",
    "client_id": "",
    "client_secret": "",
    "static_host_lists": [
      ""
    ],
    "client_certificate": "",
    "status_server_messages": ""
  },
  "auth_source_radius_attributes": {
    "vendor_id": 0,
    "attribute_id": 0,
    "attribute_value": "",
    "attribute_operation": 0,
    "attribute_display_value": ""
  },
  "cppm_auth_source_connection_backups": {
    "order_no": 0
  },
  "auth_source_filters": {
    "source_Id": 0,
    "name": "",
    "param_values": "",
    "query": "",
    "selected_Dn": "",
    "attributes": {
      "attribute_name": "",
      "alias_name": "",
      "attribute_type": "",
      "enable_as_role": false,
      "enable_as_user_attribute": false
    },
    "details": {
      "attribute_name": "",
      "attribute_value": ""
    }
  },
  "server_timeout": 0,
  "cache_timeout": 0
}
        '''
        url_path = '/auth-source/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_auth_source_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace an authentication source by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the authentication source
        Required Body Parameters (body description)- AuthSourceReplace {name (string): Name of the auth source,description (string, optional): Description of the auth source,type (string) = ['AD' or 'Ldap' or 'Sql' or 'HTTP' or 'Kerberos' or 'Local' or 'SHL' or 'TokenServer']: Type of the auth source,use_for_authorization (boolean, optional): Enable to use this Authentication Source,authorization_source_names (array[string], optional): additional auth-sources from which role-mapping attributes to be fetched,cppm_primary_auth_source_connection_details (AuthSourceConnectionDetailsMetadataReplace): details of Authentication source,auth_source_radius_attributes (AuthSourceRadiusAttributeDetailsReplace, optional): details of authSourceRadiusAttributes,cppm_auth_source_connection_backups (AuthSourceBackupConnectionDetailsMetadataReplace, optional): details of authentication source backups,auth_source_filters (AuthSourceFiltersDetailsReplace, optional): details of auth_source_filters,server_timeout (integer): Time out if the Authentication source fails to send a response to an authorization query,cache_timeout (integer): Specify the duration in number of seconds for which the attributes are cached.}AuthSourceConnectionDetailsMetadataReplace {host_name (string, optional): Host Name of Authentication Source,connection_security (string, optional) = ['None' or 'StartTLS' or 'AD_Over_SSL']: Connection Security of Authentication Source,connection_port (integer, optional): Connection port of Authentication Source,verify_server_certificate (boolean, optional): Boolean to verify Server Certificate for secure connection,trusted_certificate_id (integer, optional): Trusted certificate ID used during verification of server certificate,bind_DN (string, optional): Bind DN of Authentication Source,bind_password (string, optional): Bind Password of Authentication Source,net_BIOS_domain_name (string, optional): Net-BIOS-Domain-Name of Authentication Source,base_DN (string, optional): Base DN of Authentication Source,search_scope (string, optional) = ['Base_Object_Search' or 'One_Level_Search' or 'SubTree_Search']: Search Scope of Authentication Source,ldap_referrals (boolean, optional): Follow referrals for Authentication Source,bind_user (boolean, optional): Allow bind using user password,user_certificate (string, optional): User Certificate of Authentication Source,always_use_netBIOS_name (boolean, optional): Boolean to always use NetBIOS name instead of the domain part in username for authentication,replace_special_char (boolean, optional): Enable special character handling for LDAP query,password_attribute (string, optional): Password Attribute of Authentication Source,password_type (string, optional) = ['ClearText' or 'NT_Hash' or 'LM_Hash' or 'SHA1' or 'SHA256' or 'SHA512' or 'MD5' or 'SHA1_Base64' or 'SHA256_Base64' or 'SHA512_Base64']: Type of the Password,password_header (string, optional): Password Header of Authentication Source,server_name (string, optional): Server Name of Authentication Source,port (integer, optional): Port of SQL Server,database_name (string, optional): Name of the database,login_user_name (string, optional): User name to login to the Server,login_password (string, optional): Password to login to SQL Server,timeout (integer, optional): Timeout of the Connection,odbc_type (string, optional) = ['PostgreSQL' or 'Oracle_11g' or 'MariaDB' or 'MSSQL']: ODBC Type of SQL DB,base_URL (string, optional): Base URL of Authentication Source,realm (string, optional): Realm of Authentication Source,server_principal (string, optional): Server Principal of Authentication Source,server_principal_password (string, optional): Server Principal Password of Authentication Source,authorization_token (string, optional): Authorization Token of Authentication Source,protocol (string, optional): Protocol of Authentication Source,secret (string, optional): Secret key of Authentication Source,tenant_id (string, optional): Tenant ID of Authentication Source,client_id (string, optional): Client ID of Authentication Source,client_secret (string, optional): Client Secret of Authentication Source,static_host_lists (array[string], optional): Static Host Lists of Authentication Source,client_certificate (string, optional): Client Certificates id,status_server_messages (string, optional): Boolean to send status-server messages}AuthSourceRadiusAttributeDetailsReplace {vendor_id (integer, optional): vendor ID of AuthSourceRadiusAttribute,attribute_id (integer, optional): attribute ID of AuthSourceRadiusAttribute,attribute_value (string, optional): attribute value of AuthSourceRadiusAttribute,attribute_operation (integer, optional): attribute operation of AuthSourceRadiusAttribute,attribute_display_value (string, optional): attribute display value of AuthSourceRadiusAttribute}AuthSourceBackupConnectionDetailsMetadataReplace {order_no (integer, optional): Priority of the Authentication Source,cppm_auth_source_connection_details (undefined, optional): Connection Details of the Authentication source backup}AuthSourceFiltersDetailsReplace {source_Id (integer, optional): SourceId of AuthSourceFilter,name (string, optional): Name of AuthSourceFilter,param_values (string, optional): Parameter Values of AuthSourceFilter,query (string, optional): Query of AuthSourceFilter,selected_Dn (string, optional): SelectedDn of AuthSourceFilter,attributes (AttributesMetadataReplace, optional): Details of CppmAuthSourceFilterAttributes,details (DetailsMetadataReplace, optional): Details of CppmAuthSourceFilterDetails}AttributesMetadataReplace {attribute_name (string, optional): Attribute name of AuthSourceFilterAttributes,alias_name (string, optional): AliasName of AuthSourceFilterAttributes,attribute_type (string, optional): attribute_type of AuthSourceFilterAttributes,enable_as_role (boolean, optional): EnableAsRole of AuthSourceFilterAttributes,enable_as_user_attribute (boolean, optional): EnableAsUserAttr of AuthSourceFilterAttributes}DetailsMetadataReplace {attribute_name (string, optional): Attribute name of AuthSourceFilterDetails,attribute_value (string, optional): Attribute Value of AuthSourceFilterDetails}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "type": "",
  "use_for_authorization": false,
  "authorization_source_names": [
    ""
  ],
  "cppm_primary_auth_source_connection_details": {
    "host_name": "",
    "connection_security": "",
    "connection_port": 0,
    "verify_server_certificate": false,
    "trusted_certificate_id": 0,
    "bind_DN": "",
    "bind_password": "",
    "net_BIOS_domain_name": "",
    "base_DN": "",
    "search_scope": "",
    "ldap_referrals": false,
    "bind_user": false,
    "user_certificate": "",
    "always_use_netBIOS_name": false,
    "replace_special_char": false,
    "password_attribute": "",
    "password_type": "",
    "password_header": "",
    "server_name": "",
    "port": 0,
    "database_name": "",
    "login_user_name": "",
    "login_password": "",
    "timeout": 0,
    "odbc_type": "",
    "base_URL": "",
    "realm": "",
    "server_principal": "",
    "server_principal_password": "",
    "authorization_token": "",
    "protocol": "",
    "secret": "",
    "tenant_id": "",
    "client_id": "",
    "client_secret": "",
    "static_host_lists": [
      ""
    ],
    "client_certificate": "",
    "status_server_messages": ""
  },
  "auth_source_radius_attributes": {
    "vendor_id": 0,
    "attribute_id": 0,
    "attribute_value": "",
    "attribute_operation": 0,
    "attribute_display_value": ""
  },
  "cppm_auth_source_connection_backups": {
    "order_no": 0
  },
  "auth_source_filters": {
    "source_Id": 0,
    "name": "",
    "param_values": "",
    "query": "",
    "selected_Dn": "",
    "attributes": {
      "attribute_name": "",
      "alias_name": "",
      "attribute_type": "",
      "enable_as_role": false,
      "enable_as_user_attribute": false
    },
    "details": {
      "attribute_name": "",
      "attribute_value": ""
    }
  },
  "server_timeout": 0,
  "cache_timeout": 0
}
        '''
        url_path = '/auth-source/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_auth_source_name_by_name(self,name=""):
        '''
        Operation: Delete an authentication source by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the authentication source
        '''
        url_path = '/auth-source/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:EnforcementPolicy  
    #Function Section Description: Manage Enforcement Policies

    def get_enforcement_policy(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of enforcement policies
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/enforcement-policy'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_enforcement_policy(self,body=({})):
        '''
        Operation: Create a new enforcement policy
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- EnforcementPolicyCreate {name (string): Name of the Enforcement Policy,description (string, optional): Description of the Enforcement Policy,enforcement_type (string) = ['RADIUS' or 'TACACS' or 'WEBAUTH' or 'Application' or 'Event']: Enforcement Type of the Enforcement Policy,default_enforcement_profile (string): Default Enforcement Profile for the Enforcement Policy,rule_eval_algo (string) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm of the Enforcement Policy rules,rules (RulesSettingsCreate): List of Rules for Enforcement Policy}RulesSettingsCreate {enforcement_profile_names (string): List of Enforcement Profile names for a rule,condition (RulesConditionSettingsCreate): Conditions of Enforcement Policy rules}RulesConditionSettingsCreate {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "enforcement_type": "",
  "default_enforcement_profile": "",
  "rule_eval_algo": "",
  "rules": {
    "enforcement_profile_names": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/enforcement-policy'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_enforcement_policy_by_enforcement_policy_id(self,enforcement_policy_id=""):
        '''
        Operation: Get a enforcement policy
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        '''
        url_path = '/enforcement-policy/{enforcement_policy_id}'
        dict_path={'enforcement_policy_id': enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_enforcement_policy_by_enforcement_policy_id(self,enforcement_policy_id="",body=({})):
        '''
        Operation: Update a enforcement policy
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        Required Body Parameters (body description)- EnforcementPolicyUpdate {name (string, optional): Name of the Enforcement Policy,description (string, optional): Description of the Enforcement Policy,enforcement_type (string, optional) = ['RADIUS' or 'TACACS' or 'WEBAUTH' or 'Application' or 'Event']: Enforcement Type of the Enforcement Policy,default_enforcement_profile (string, optional): Default Enforcement Profile for the Enforcement Policy,rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm of the Enforcement Policy rules,rules (RulesSettingsUpdate, optional): List of Rules for Enforcement Policy}RulesSettingsUpdate {enforcement_profile_names (string, optional): List of Enforcement Profile names for a rule,condition (RulesConditionSettingsUpdate, optional): Conditions of Enforcement Policy rules}RulesConditionSettingsUpdate {type (string, optional): Condition type,name (string, optional): Condition name,oper (string, optional): Condition operator,value (string, optional): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "enforcement_type": "",
  "default_enforcement_profile": "",
  "rule_eval_algo": "",
  "rules": {
    "enforcement_profile_names": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/enforcement-policy/{enforcement_policy_id}'
        dict_path={'enforcement_policy_id': enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_enforcement_policy_by_enforcement_policy_id(self,enforcement_policy_id="",body=({})):
        '''
        Operation: Replace a enforcement policy
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        Required Body Parameters (body description)- EnforcementPolicyReplace {name (string): Name of the Enforcement Policy,description (string, optional): Description of the Enforcement Policy,enforcement_type (string) = ['RADIUS' or 'TACACS' or 'WEBAUTH' or 'Application' or 'Event']: Enforcement Type of the Enforcement Policy,default_enforcement_profile (string): Default Enforcement Profile for the Enforcement Policy,rule_eval_algo (string) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm of the Enforcement Policy rules,rules (RulesSettingsReplace): List of Rules for Enforcement Policy}RulesSettingsReplace {enforcement_profile_names (string): List of Enforcement Profile names for a rule,condition (RulesConditionSettingsReplace): Conditions of Enforcement Policy rules}RulesConditionSettingsReplace {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "enforcement_type": "",
  "default_enforcement_profile": "",
  "rule_eval_algo": "",
  "rules": {
    "enforcement_profile_names": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/enforcement-policy/{enforcement_policy_id}'
        dict_path={'enforcement_policy_id': enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_enforcement_policy_by_enforcement_policy_id(self,enforcement_policy_id=""):
        '''
        Operation: Delete a enforcement policy
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: enforcement_policy_id, Description: Numeric ID of the enforcement policy
        '''
        url_path = '/enforcement-policy/{enforcement_policy_id}'
        dict_path={'enforcement_policy_id': enforcement_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_enforcement_policy_name_by_name(self,name=""):
        '''
        Operation: Get a enforcement policy by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the enforcement policy
        '''
        url_path = '/enforcement-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_enforcement_policy_name_by_name(self,name="",body=({})):
        '''
        Operation: Update a enforcement policy by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the enforcement policy
        Required Body Parameters (body description)- EnforcementPolicyUpdate {name (string, optional): Name of the Enforcement Policy,description (string, optional): Description of the Enforcement Policy,enforcement_type (string, optional) = ['RADIUS' or 'TACACS' or 'WEBAUTH' or 'Application' or 'Event']: Enforcement Type of the Enforcement Policy,default_enforcement_profile (string, optional): Default Enforcement Profile for the Enforcement Policy,rule_eval_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm of the Enforcement Policy rules,rules (RulesSettingsUpdate, optional): List of Rules for Enforcement Policy}RulesSettingsUpdate {enforcement_profile_names (string, optional): List of Enforcement Profile names for a rule,condition (RulesConditionSettingsUpdate, optional): Conditions of Enforcement Policy rules}RulesConditionSettingsUpdate {type (string, optional): Condition type,name (string, optional): Condition name,oper (string, optional): Condition operator,value (string, optional): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "enforcement_type": "",
  "default_enforcement_profile": "",
  "rule_eval_algo": "",
  "rules": {
    "enforcement_profile_names": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/enforcement-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_enforcement_policy_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a enforcement policy by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the enforcement policy
        Required Body Parameters (body description)- EnforcementPolicyReplace {name (string): Name of the Enforcement Policy,description (string, optional): Description of the Enforcement Policy,enforcement_type (string) = ['RADIUS' or 'TACACS' or 'WEBAUTH' or 'Application' or 'Event']: Enforcement Type of the Enforcement Policy,default_enforcement_profile (string): Default Enforcement Profile for the Enforcement Policy,rule_eval_algo (string) = ['first-applicable' or 'evaluate-all']: Rule Evaluation Algorithm of the Enforcement Policy rules,rules (RulesSettingsReplace): List of Rules for Enforcement Policy}RulesSettingsReplace {enforcement_profile_names (string): List of Enforcement Profile names for a rule,condition (RulesConditionSettingsReplace): Conditions of Enforcement Policy rules}RulesConditionSettingsReplace {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "enforcement_type": "",
  "default_enforcement_profile": "",
  "rule_eval_algo": "",
  "rules": {
    "enforcement_profile_names": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/enforcement-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_enforcement_policy_name_by_name(self,name=""):
        '''
        Operation: Delete a enforcement policy by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the enforcement policy
        '''
        url_path = '/enforcement-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:NetworkDevice  
    #Function Section Description: Manage network devices

    def get_network_device(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of network devices
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/network-device'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_network_device(self,body=({})):
        '''
        Operation: Create a new network device
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- NetworkDeviceCreate {description (string, optional): Description of the network device,nad_groups (array[string], optional): NAD groups,name (string): Name of the network device,ip_address (string): IP or Subnet Address of the network device,radius_secret (string, optional): RADIUS Shared Secret of the network device,tacacs_secret (string, optional): TACACS+ Shared Secret of the network device,vendor_name (string, optional): Vendor Name of the network device,vendor_id (integer, optional): Vendor Id of the network device,coa_capable (boolean, optional): Flag indicating if the network device is capable of CoA,coa_port (integer, optional): CoA port number of the network device,radsec_enabled (boolean, optional): Flag indicating if the network device is radSec enabled,snmp_read (SNMPReadSettings, optional): SNMP read settings of the network device,snmp_write (SNMPWriteSettings, optional): SNMP write settings of the network device,radsec_config (RadSecSettings, optional): RadSec settings of the network device,cli_config (CLISettings, optional): CLI Configuration details of the network device,onConnect_enforcement (OnConnectEnforcementSettings, optional): OnConnect Enforcement settings of the network device,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the network device}SNMPReadSettings {force_read (boolean, optional): This field is deprecated.,read_arp_info (boolean, optional): Enable to read ARP table from this device,zone_name (string, optional): Policy Manager Zone name to be associated with the network device,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}SNMPWriteSettings {default_vlan (integer, optional): Default VLAN for port when SNMP-enforced session expires,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}RadSecSettings {serial_number (string, optional): Serial Number of a Certificate,validate_cert (string, optional) = ['NONE' or 'CN_OR_SAN' or 'RFC']: Validating a Certificate, the valid inputs are NONE, CN, SAN or CN_OR_SAN.,subject_dn (string, optional): Issuer CA Certificates Subject DN,expiry_date (string, optional): Issuer CA Certificates Expiry Date,cn_regex (string, optional): Common Name Regular Expression String,san_regex (string, optional): Subject Alternate Name Regular Expression String,src_override_ip (string, optional): Source Override IP indicates the actual Source IP Address}CLISettings {type (string, optional) = ['SSH' or 'Telnet']: Access type of the network device,port (integer, optional): SSH/Telnet port number of the network device,username (string, optional): Username of the network device,password (string, optional): Password of the network device,username_prompt_regex (string, optional): Username prompt regex of the network device,password_prompt_regex (string, optional): Password prompt regex of the network device,command_prompt_regex (string, optional): Command prompt regex of the network device,enable_prompt_regex (string, optional): Enable prompt regex of the network device,enable_password (string, optional): Enable password of the network device}OnConnectEnforcementSettings {enabled (boolean, optional): Flag indicating if the network device is enabled with OnConnect Enforcement. SNMP read configuration and Policy Manager Zone is a must for this to work.,ports (string, optional): Port names used in OnConnect Enforcement in CSV format (e.g. FastEthernet 1/0/10). Use empty string to enable for all ports. Ports determined to be uplink or trunk ports will be ignored.}
        Required Body Parameters (type(dict) body example)- {
  "description": "",
  "nad_groups": [
    ""
  ],
  "name": "",
  "ip_address": "",
  "radius_secret": "",
  "tacacs_secret": "",
  "vendor_name": "",
  "vendor_id": 0,
  "coa_capable": false,
  "coa_port": 0,
  "radsec_enabled": false,
  "snmp_read": {
    "force_read": false,
    "read_arp_info": false,
    "zone_name": "",
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "snmp_write": {
    "default_vlan": 0,
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "radsec_config": {
    "serial_number": "",
    "validate_cert": "",
    "subject_dn": "",
    "expiry_date": "",
    "cn_regex": "",
    "san_regex": "",
    "src_override_ip": ""
  },
  "cli_config": {
    "type": "",
    "port": 0,
    "username": "",
    "password": "",
    "username_prompt_regex": "",
    "password_prompt_regex": "",
    "command_prompt_regex": "",
    "enable_prompt_regex": "",
    "enable_password": ""
  },
  "onConnect_enforcement": {
    "enabled": false,
    "ports": ""
  },
  "attributes": "object"
}
        '''
        url_path = '/network-device'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_network_device_by_network_device_id(self,network_device_id=""):
        '''
        Operation: Get a network device
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: network_device_id, Description: Numeric ID of the network device
        '''
        url_path = '/network-device/{network_device_id}'
        dict_path={'network_device_id': network_device_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_network_device_by_network_device_id(self,network_device_id="",body=({})):
        '''
        Operation: Update some fields of a network device
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: network_device_id, Description: Numeric ID of the network device
        Required Body Parameters (body description)- NetworkDeviceUpdate {description (string, optional): Description of the network device,nad_groups (array[string], optional): NAD groups,name (string, optional): Name of the network device,ip_address (string, optional): IP or Subnet Address of the network device,radius_secret (string, optional): RADIUS Shared Secret of the network device,tacacs_secret (string, optional): TACACS+ Shared Secret of the network device,vendor_name (string, optional): Vendor Name of the network device,vendor_id (integer, optional): Vendor Id of the network device,coa_capable (boolean, optional): Flag indicating if the network device is capable of CoA,coa_port (integer, optional): CoA port number of the network device,radsec_enabled (boolean, optional): Flag indicating if the network device is radSec enabled,snmp_read (SNMPReadSettings, optional): SNMP read settings of the network device,snmp_write (SNMPWriteSettings, optional): SNMP write settings of the network device,radsec_config (RadSecSettings, optional): RadSec settings of the network device,cli_config (CLISettings, optional): CLI Configuration details of the network device,onConnect_enforcement (OnConnectEnforcementSettings, optional): OnConnect Enforcement settings of the network device,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the network device}SNMPReadSettings {force_read (boolean, optional): This field is deprecated.,read_arp_info (boolean, optional): Enable to read ARP table from this device,zone_name (string, optional): Policy Manager Zone name to be associated with the network device,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}SNMPWriteSettings {default_vlan (integer, optional): Default VLAN for port when SNMP-enforced session expires,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}RadSecSettings {serial_number (string, optional): Serial Number of a Certificate,validate_cert (string, optional) = ['NONE' or 'CN_OR_SAN' or 'RFC']: Validating a Certificate, the valid inputs are NONE, CN, SAN or CN_OR_SAN.,subject_dn (string, optional): Issuer CA Certificates Subject DN,expiry_date (string, optional): Issuer CA Certificates Expiry Date,cn_regex (string, optional): Common Name Regular Expression String,san_regex (string, optional): Subject Alternate Name Regular Expression String,src_override_ip (string, optional): Source Override IP indicates the actual Source IP Address}CLISettings {type (string, optional) = ['SSH' or 'Telnet']: Access type of the network device,port (integer, optional): SSH/Telnet port number of the network device,username (string, optional): Username of the network device,password (string, optional): Password of the network device,username_prompt_regex (string, optional): Username prompt regex of the network device,password_prompt_regex (string, optional): Password prompt regex of the network device,command_prompt_regex (string, optional): Command prompt regex of the network device,enable_prompt_regex (string, optional): Enable prompt regex of the network device,enable_password (string, optional): Enable password of the network device}OnConnectEnforcementSettings {enabled (boolean, optional): Flag indicating if the network device is enabled with OnConnect Enforcement. SNMP read configuration and Policy Manager Zone is a must for this to work.,ports (string, optional): Port names used in OnConnect Enforcement in CSV format (e.g. FastEthernet 1/0/10). Use empty string to enable for all ports. Ports determined to be uplink or trunk ports will be ignored.}
        Required Body Parameters (type(dict) body example)- {
  "description": "",
  "nad_groups": [
    ""
  ],
  "name": "",
  "ip_address": "",
  "radius_secret": "",
  "tacacs_secret": "",
  "vendor_name": "",
  "vendor_id": 0,
  "coa_capable": false,
  "coa_port": 0,
  "radsec_enabled": false,
  "snmp_read": {
    "force_read": false,
    "read_arp_info": false,
    "zone_name": "",
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "snmp_write": {
    "default_vlan": 0,
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "radsec_config": {
    "serial_number": "",
    "validate_cert": "",
    "subject_dn": "",
    "expiry_date": "",
    "cn_regex": "",
    "san_regex": "",
    "src_override_ip": ""
  },
  "cli_config": {
    "type": "",
    "port": 0,
    "username": "",
    "password": "",
    "username_prompt_regex": "",
    "password_prompt_regex": "",
    "command_prompt_regex": "",
    "enable_prompt_regex": "",
    "enable_password": ""
  },
  "onConnect_enforcement": {
    "enabled": false,
    "ports": ""
  },
  "attributes": "object"
}
        '''
        url_path = '/network-device/{network_device_id}'
        dict_path={'network_device_id': network_device_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_network_device_by_network_device_id(self,network_device_id="",body=({})):
        '''
        Operation: Replace a network device
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: network_device_id, Description: Numeric ID of the network device
        Required Body Parameters (body description)- NetworkDeviceReplace {description (string, optional): Description of the network device,nad_groups (array[string], optional): NAD groups,name (string): Name of the network device,ip_address (string): IP or Subnet Address of the network device,radius_secret (string, optional): RADIUS Shared Secret of the network device,tacacs_secret (string, optional): TACACS+ Shared Secret of the network device,vendor_name (string, optional): Vendor Name of the network device,vendor_id (integer, optional): Vendor Id of the network device,coa_capable (boolean, optional): Flag indicating if the network device is capable of CoA,coa_port (integer, optional): CoA port number of the network device,radsec_enabled (boolean, optional): Flag indicating if the network device is radSec enabled,snmp_read (SNMPReadSettings, optional): SNMP read settings of the network device,snmp_write (SNMPWriteSettings, optional): SNMP write settings of the network device,radsec_config (RadSecSettings, optional): RadSec settings of the network device,cli_config (CLISettings, optional): CLI Configuration details of the network device,onConnect_enforcement (OnConnectEnforcementSettings, optional): OnConnect Enforcement settings of the network device,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the network device}SNMPReadSettings {force_read (boolean, optional): This field is deprecated.,read_arp_info (boolean, optional): Enable to read ARP table from this device,zone_name (string, optional): Policy Manager Zone name to be associated with the network device,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}SNMPWriteSettings {default_vlan (integer, optional): Default VLAN for port when SNMP-enforced session expires,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}RadSecSettings {serial_number (string, optional): Serial Number of a Certificate,validate_cert (string, optional) = ['NONE' or 'CN_OR_SAN' or 'RFC']: Validating a Certificate, the valid inputs are NONE, CN, SAN or CN_OR_SAN.,subject_dn (string, optional): Issuer CA Certificates Subject DN,expiry_date (string, optional): Issuer CA Certificates Expiry Date,cn_regex (string, optional): Common Name Regular Expression String,san_regex (string, optional): Subject Alternate Name Regular Expression String,src_override_ip (string, optional): Source Override IP indicates the actual Source IP Address}CLISettings {type (string, optional) = ['SSH' or 'Telnet']: Access type of the network device,port (integer, optional): SSH/Telnet port number of the network device,username (string, optional): Username of the network device,password (string, optional): Password of the network device,username_prompt_regex (string, optional): Username prompt regex of the network device,password_prompt_regex (string, optional): Password prompt regex of the network device,command_prompt_regex (string, optional): Command prompt regex of the network device,enable_prompt_regex (string, optional): Enable prompt regex of the network device,enable_password (string, optional): Enable password of the network device}OnConnectEnforcementSettings {enabled (boolean, optional): Flag indicating if the network device is enabled with OnConnect Enforcement. SNMP read configuration and Policy Manager Zone is a must for this to work.,ports (string, optional): Port names used in OnConnect Enforcement in CSV format (e.g. FastEthernet 1/0/10). Use empty string to enable for all ports. Ports determined to be uplink or trunk ports will be ignored.}
        Required Body Parameters (type(dict) body example)- {
  "description": "",
  "nad_groups": [
    ""
  ],
  "name": "",
  "ip_address": "",
  "radius_secret": "",
  "tacacs_secret": "",
  "vendor_name": "",
  "vendor_id": 0,
  "coa_capable": false,
  "coa_port": 0,
  "radsec_enabled": false,
  "snmp_read": {
    "force_read": false,
    "read_arp_info": false,
    "zone_name": "",
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "snmp_write": {
    "default_vlan": 0,
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "radsec_config": {
    "serial_number": "",
    "validate_cert": "",
    "subject_dn": "",
    "expiry_date": "",
    "cn_regex": "",
    "san_regex": "",
    "src_override_ip": ""
  },
  "cli_config": {
    "type": "",
    "port": 0,
    "username": "",
    "password": "",
    "username_prompt_regex": "",
    "password_prompt_regex": "",
    "command_prompt_regex": "",
    "enable_prompt_regex": "",
    "enable_password": ""
  },
  "onConnect_enforcement": {
    "enabled": false,
    "ports": ""
  },
  "attributes": "object"
}
        '''
        url_path = '/network-device/{network_device_id}'
        dict_path={'network_device_id': network_device_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_network_device_by_network_device_id(self,network_device_id=""):
        '''
        Operation: Delete a network device
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: network_device_id, Description: Numeric ID of the network device
        '''
        url_path = '/network-device/{network_device_id}'
        dict_path={'network_device_id': network_device_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_network_device_name_by_name(self,name=""):
        '''
        Operation: Get a network device by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the network device
        '''
        url_path = '/network-device/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_network_device_name_by_name(self,name="",body=({})):
        '''
        Operation: Update some fields of a network device by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the network device
        Required Body Parameters (body description)- NetworkDeviceUpdate {description (string, optional): Description of the network device,nad_groups (array[string], optional): NAD groups,name (string, optional): Name of the network device,ip_address (string, optional): IP or Subnet Address of the network device,radius_secret (string, optional): RADIUS Shared Secret of the network device,tacacs_secret (string, optional): TACACS+ Shared Secret of the network device,vendor_name (string, optional): Vendor Name of the network device,vendor_id (integer, optional): Vendor Id of the network device,coa_capable (boolean, optional): Flag indicating if the network device is capable of CoA,coa_port (integer, optional): CoA port number of the network device,radsec_enabled (boolean, optional): Flag indicating if the network device is radSec enabled,snmp_read (SNMPReadSettings, optional): SNMP read settings of the network device,snmp_write (SNMPWriteSettings, optional): SNMP write settings of the network device,radsec_config (RadSecSettings, optional): RadSec settings of the network device,cli_config (CLISettings, optional): CLI Configuration details of the network device,onConnect_enforcement (OnConnectEnforcementSettings, optional): OnConnect Enforcement settings of the network device,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the network device}SNMPReadSettings {force_read (boolean, optional): This field is deprecated.,read_arp_info (boolean, optional): Enable to read ARP table from this device,zone_name (string, optional): Policy Manager Zone name to be associated with the network device,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}SNMPWriteSettings {default_vlan (integer, optional): Default VLAN for port when SNMP-enforced session expires,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}RadSecSettings {serial_number (string, optional): Serial Number of a Certificate,validate_cert (string, optional) = ['NONE' or 'CN_OR_SAN' or 'RFC']: Validating a Certificate, the valid inputs are NONE, CN, SAN or CN_OR_SAN.,subject_dn (string, optional): Issuer CA Certificates Subject DN,expiry_date (string, optional): Issuer CA Certificates Expiry Date,cn_regex (string, optional): Common Name Regular Expression String,san_regex (string, optional): Subject Alternate Name Regular Expression String,src_override_ip (string, optional): Source Override IP indicates the actual Source IP Address}CLISettings {type (string, optional) = ['SSH' or 'Telnet']: Access type of the network device,port (integer, optional): SSH/Telnet port number of the network device,username (string, optional): Username of the network device,password (string, optional): Password of the network device,username_prompt_regex (string, optional): Username prompt regex of the network device,password_prompt_regex (string, optional): Password prompt regex of the network device,command_prompt_regex (string, optional): Command prompt regex of the network device,enable_prompt_regex (string, optional): Enable prompt regex of the network device,enable_password (string, optional): Enable password of the network device}OnConnectEnforcementSettings {enabled (boolean, optional): Flag indicating if the network device is enabled with OnConnect Enforcement. SNMP read configuration and Policy Manager Zone is a must for this to work.,ports (string, optional): Port names used in OnConnect Enforcement in CSV format (e.g. FastEthernet 1/0/10). Use empty string to enable for all ports. Ports determined to be uplink or trunk ports will be ignored.}
        Required Body Parameters (type(dict) body example)- {
  "description": "",
  "nad_groups": [
    ""
  ],
  "name": "",
  "ip_address": "",
  "radius_secret": "",
  "tacacs_secret": "",
  "vendor_name": "",
  "vendor_id": 0,
  "coa_capable": false,
  "coa_port": 0,
  "radsec_enabled": false,
  "snmp_read": {
    "force_read": false,
    "read_arp_info": false,
    "zone_name": "",
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "snmp_write": {
    "default_vlan": 0,
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "radsec_config": {
    "serial_number": "",
    "validate_cert": "",
    "subject_dn": "",
    "expiry_date": "",
    "cn_regex": "",
    "san_regex": "",
    "src_override_ip": ""
  },
  "cli_config": {
    "type": "",
    "port": 0,
    "username": "",
    "password": "",
    "username_prompt_regex": "",
    "password_prompt_regex": "",
    "command_prompt_regex": "",
    "enable_prompt_regex": "",
    "enable_password": ""
  },
  "onConnect_enforcement": {
    "enabled": false,
    "ports": ""
  },
  "attributes": "object"
}
        '''
        url_path = '/network-device/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_network_device_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a network device by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the network device
        Required Body Parameters (body description)- NetworkDeviceReplace {description (string, optional): Description of the network device,nad_groups (array[string], optional): NAD groups,name (string): Name of the network device,ip_address (string): IP or Subnet Address of the network device,radius_secret (string, optional): RADIUS Shared Secret of the network device,tacacs_secret (string, optional): TACACS+ Shared Secret of the network device,vendor_name (string, optional): Vendor Name of the network device,vendor_id (integer, optional): Vendor Id of the network device,coa_capable (boolean, optional): Flag indicating if the network device is capable of CoA,coa_port (integer, optional): CoA port number of the network device,radsec_enabled (boolean, optional): Flag indicating if the network device is radSec enabled,snmp_read (SNMPReadSettings, optional): SNMP read settings of the network device,snmp_write (SNMPWriteSettings, optional): SNMP write settings of the network device,radsec_config (RadSecSettings, optional): RadSec settings of the network device,cli_config (CLISettings, optional): CLI Configuration details of the network device,onConnect_enforcement (OnConnectEnforcementSettings, optional): OnConnect Enforcement settings of the network device,attributes (object, optional): Additional attributes(key/value pairs) may be stored with the network device}SNMPReadSettings {force_read (boolean, optional): This field is deprecated.,read_arp_info (boolean, optional): Enable to read ARP table from this device,zone_name (string, optional): Policy Manager Zone name to be associated with the network device,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}SNMPWriteSettings {default_vlan (integer, optional): Default VLAN for port when SNMP-enforced session expires,snmp_version (string, optional) = ['V1' or 'V2C' or 'V3']: SNMP version of the network device,community_string (string, optional): Community string of the network device,security_level (string, optional) = ['NOAUTH_NOPRIV' or 'AUTH_NOPRIV' or 'AUTH_PRIV']: Security level of the network device,user (string, optional): Username of the network device,auth_protocol (string, optional) = ['MD5' or 'SHA']: Authentication protocol of the network device,auth_key (string, optional): Authentication key of the network device,privacy_protocol (string, optional) = ['DES_CBC' or 'AES_128']: Privacy protocol of the network device,privacy_key (string, optional): Privacy key of the network device}RadSecSettings {serial_number (string, optional): Serial Number of a Certificate,validate_cert (string, optional) = ['NONE' or 'CN_OR_SAN' or 'RFC']: Validating a Certificate, the valid inputs are NONE, CN, SAN or CN_OR_SAN.,subject_dn (string, optional): Issuer CA Certificates Subject DN,expiry_date (string, optional): Issuer CA Certificates Expiry Date,cn_regex (string, optional): Common Name Regular Expression String,san_regex (string, optional): Subject Alternate Name Regular Expression String,src_override_ip (string, optional): Source Override IP indicates the actual Source IP Address}CLISettings {type (string, optional) = ['SSH' or 'Telnet']: Access type of the network device,port (integer, optional): SSH/Telnet port number of the network device,username (string, optional): Username of the network device,password (string, optional): Password of the network device,username_prompt_regex (string, optional): Username prompt regex of the network device,password_prompt_regex (string, optional): Password prompt regex of the network device,command_prompt_regex (string, optional): Command prompt regex of the network device,enable_prompt_regex (string, optional): Enable prompt regex of the network device,enable_password (string, optional): Enable password of the network device}OnConnectEnforcementSettings {enabled (boolean, optional): Flag indicating if the network device is enabled with OnConnect Enforcement. SNMP read configuration and Policy Manager Zone is a must for this to work.,ports (string, optional): Port names used in OnConnect Enforcement in CSV format (e.g. FastEthernet 1/0/10). Use empty string to enable for all ports. Ports determined to be uplink or trunk ports will be ignored.}
        Required Body Parameters (type(dict) body example)- {
  "description": "",
  "nad_groups": [
    ""
  ],
  "name": "",
  "ip_address": "",
  "radius_secret": "",
  "tacacs_secret": "",
  "vendor_name": "",
  "vendor_id": 0,
  "coa_capable": false,
  "coa_port": 0,
  "radsec_enabled": false,
  "snmp_read": {
    "force_read": false,
    "read_arp_info": false,
    "zone_name": "",
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "snmp_write": {
    "default_vlan": 0,
    "snmp_version": "",
    "community_string": "",
    "security_level": "",
    "user": "",
    "auth_protocol": "",
    "auth_key": "",
    "privacy_protocol": "",
    "privacy_key": ""
  },
  "radsec_config": {
    "serial_number": "",
    "validate_cert": "",
    "subject_dn": "",
    "expiry_date": "",
    "cn_regex": "",
    "san_regex": "",
    "src_override_ip": ""
  },
  "cli_config": {
    "type": "",
    "port": 0,
    "username": "",
    "password": "",
    "username_prompt_regex": "",
    "password_prompt_regex": "",
    "command_prompt_regex": "",
    "enable_prompt_regex": "",
    "enable_password": ""
  },
  "onConnect_enforcement": {
    "enabled": false,
    "ports": ""
  },
  "attributes": "object"
}
        '''
        url_path = '/network-device/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_network_device_name_by_name(self,name=""):
        '''
        Operation: Delete a network device by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the network device
        '''
        url_path = '/network-device/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:NetworkDeviceGroup  
    #Function Section Description: Manage network device groups

    def get_network_device_group(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of network device groups
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/network-device-group'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_network_device_group(self,body=({})):
        '''
        Operation: Create a new network device group
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- NetworkDeviceGroupCreate {name (string): Name of the network device group,description (string, optional): Description of the network device group,group_format (string) = ['subnet' or 'regex' or 'list']: Format of the network devices,value (string): Network devices in the specified format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "group_format": "",
  "value": ""
}
        '''
        url_path = '/network-device-group'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_network_device_group_by_network_device_group_id(self,network_device_group_id=""):
        '''
        Operation: Get a network device group
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: network_device_group_id, Description: Numeric ID of the network device group
        '''
        url_path = '/network-device-group/{network_device_group_id}'
        dict_path={'network_device_group_id': network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_network_device_group_by_network_device_group_id(self,network_device_group_id="",body=({})):
        '''
        Operation: Update some fields of a network device group
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: network_device_group_id, Description: Numeric ID of the network device group
        Required Body Parameters (body description)- NetworkDeviceGroupUpdate {name (string, optional): Name of the network device group,description (string, optional): Description of the network device group,group_format (string, optional) = ['subnet' or 'regex' or 'list']: Format of the network devices,value (string, optional): Network devices in the specified format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "group_format": "",
  "value": ""
}
        '''
        url_path = '/network-device-group/{network_device_group_id}'
        dict_path={'network_device_group_id': network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_network_device_group_by_network_device_group_id(self,network_device_group_id="",body=({})):
        '''
        Operation: Replace a network device group
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: network_device_group_id, Description: Numeric ID of the network device group
        Required Body Parameters (body description)- NetworkDeviceGroupReplace {name (string): Name of the network device group,description (string, optional): Description of the network device group,group_format (string) = ['subnet' or 'regex' or 'list']: Format of the network devices,value (string): Network devices in the specified format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "group_format": "",
  "value": ""
}
        '''
        url_path = '/network-device-group/{network_device_group_id}'
        dict_path={'network_device_group_id': network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_network_device_group_by_network_device_group_id(self,network_device_group_id=""):
        '''
        Operation: Delete a network device group
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: network_device_group_id, Description: Numeric ID of the network device group
        '''
        url_path = '/network-device-group/{network_device_group_id}'
        dict_path={'network_device_group_id': network_device_group_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_network_device_group_name_by_name(self,name=""):
        '''
        Operation: Get a network device group by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the network device group
        '''
        url_path = '/network-device-group/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_network_device_group_name_by_name(self,name="",body=({})):
        '''
        Operation: Update some fields of a network device group by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the network device group
        Required Body Parameters (body description)- NetworkDeviceGroupUpdate {name (string, optional): Name of the network device group,description (string, optional): Description of the network device group,group_format (string, optional) = ['subnet' or 'regex' or 'list']: Format of the network devices,value (string, optional): Network devices in the specified format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "group_format": "",
  "value": ""
}
        '''
        url_path = '/network-device-group/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_network_device_group_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a network device group by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the network device group
        Required Body Parameters (body description)- NetworkDeviceGroupReplace {name (string): Name of the network device group,description (string, optional): Description of the network device group,group_format (string) = ['subnet' or 'regex' or 'list']: Format of the network devices,value (string): Network devices in the specified format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "group_format": "",
  "value": ""
}
        '''
        url_path = '/network-device-group/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_network_device_group_name_by_name(self,name=""):
        '''
        Operation: Delete a network device group by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the network device group
        '''
        url_path = '/network-device-group/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:PosturePolicy  
    #Function Section Description: Manage Posture Policies

    def get_posture_policy(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of Posture Policies
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/posture-policy'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_posture_policy(self,body=({})):
        '''
        Operation: Create a new Posture Policy
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- PosturePolicyCreate {name (string): Posture Policy Name,description (string, optional): Description,posture_agent (string) = ['Supplicant' or 'WebAgent']: Posture Agent,host_os (string, optional) = ['Windows' or 'Linux' or 'macOS']: Host Operating System,plugin_version (string, optional): Plugin Version,roles (array[string], optional): Restrict by Roles,policy_xml (string): Posture Policy XML}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "posture_agent": "",
  "host_os": "",
  "plugin_version": "",
  "roles": [
    ""
  ],
  "policy_xml": ""
}
        '''
        url_path = '/posture-policy'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_posture_policy_by_posture_policy_id(self,posture_policy_id=""):
        '''
        Operation: Get a Posture Policy
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        '''
        url_path = '/posture-policy/{posture_policy_id}'
        dict_path={'posture_policy_id': posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_posture_policy_by_posture_policy_id(self,posture_policy_id="",body=({})):
        '''
        Operation: Update a Posture Policy
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        Required Body Parameters (body description)- PosturePolicyUpdate {name (string, optional): Posture Policy Name,description (string, optional): Description,posture_agent (string, optional) = ['Supplicant' or 'WebAgent']: Posture Agent,host_os (string, optional) = ['Windows' or 'Linux' or 'macOS']: Host Operating System,plugin_version (string, optional): Plugin Version,roles (array[string], optional): Restrict by Roles,policy_xml (string, optional): Posture Policy XML}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "posture_agent": "",
  "host_os": "",
  "plugin_version": "",
  "roles": [
    ""
  ],
  "policy_xml": ""
}
        '''
        url_path = '/posture-policy/{posture_policy_id}'
        dict_path={'posture_policy_id': posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_posture_policy_by_posture_policy_id(self,posture_policy_id="",body=({})):
        '''
        Operation: Replace a Posture Policy
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        Required Body Parameters (body description)- PosturePolicyReplace {name (string): Posture Policy Name,description (string, optional): Description,posture_agent (string) = ['Supplicant' or 'WebAgent']: Posture Agent,host_os (string, optional) = ['Windows' or 'Linux' or 'macOS']: Host Operating System,plugin_version (string, optional): Plugin Version,roles (array[string], optional): Restrict by Roles,policy_xml (string): Posture Policy XML}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "posture_agent": "",
  "host_os": "",
  "plugin_version": "",
  "roles": [
    ""
  ],
  "policy_xml": ""
}
        '''
        url_path = '/posture-policy/{posture_policy_id}'
        dict_path={'posture_policy_id': posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_posture_policy_by_posture_policy_id(self,posture_policy_id=""):
        '''
        Operation: Delete a Posture Policy
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: posture_policy_id, Description: Numeric ID of the Posture Policy
        '''
        url_path = '/posture-policy/{posture_policy_id}'
        dict_path={'posture_policy_id': posture_policy_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_posture_policy_name_by_name(self,name=""):
        '''
        Operation: Get a Posture Policy by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the Posture Policy
        '''
        url_path = '/posture-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_posture_policy_name_by_name(self,name="",body=({})):
        '''
        Operation: Update a Posture Policy by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the Posture Policy
        Required Body Parameters (body description)- PosturePolicyUpdate {name (string, optional): Posture Policy Name,description (string, optional): Description,posture_agent (string, optional) = ['Supplicant' or 'WebAgent']: Posture Agent,host_os (string, optional) = ['Windows' or 'Linux' or 'macOS']: Host Operating System,plugin_version (string, optional): Plugin Version,roles (array[string], optional): Restrict by Roles,policy_xml (string, optional): Posture Policy XML}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "posture_agent": "",
  "host_os": "",
  "plugin_version": "",
  "roles": [
    ""
  ],
  "policy_xml": ""
}
        '''
        url_path = '/posture-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_posture_policy_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a Posture Policy by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the Posture Policy
        Required Body Parameters (body description)- PosturePolicyReplace {name (string): Posture Policy Name,description (string, optional): Description,posture_agent (string) = ['Supplicant' or 'WebAgent']: Posture Agent,host_os (string, optional) = ['Windows' or 'Linux' or 'macOS']: Host Operating System,plugin_version (string, optional): Plugin Version,roles (array[string], optional): Restrict by Roles,policy_xml (string): Posture Policy XML}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "posture_agent": "",
  "host_os": "",
  "plugin_version": "",
  "roles": [
    ""
  ],
  "policy_xml": ""
}
        '''
        url_path = '/posture-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_posture_policy_name_by_name(self,name=""):
        '''
        Operation: Delete a Posture Policy by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the Posture Policy
        '''
        url_path = '/posture-policy/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:RADIUSDictionary  
    #Function Section Description: Manage RADIUS Dictionaries

    def get_radius_dictionary(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of RADIUS Dictionaries
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/radius-dictionary'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_radius_dictionary(self,body=({})):
        '''
        Operation: Create a new RADIUS Dictionary
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RADIUSDictionaryCreate {vendor_id (integer): Vendor ID of RADIUS Dictionary,vendor_name (string): Vendor Name of RADIUS Dictionary,prefix (string): Vendor Prefix of RADIUS Dictionary,enabled (boolean, optional): Is RADIUS Dictionary enabled?,attributes (array[Attributes]): Attributes of RADIUS Dictionary}Attributes {attr_id (integer): RADIUS Dictionary Attribute ID,attr_name (string): RADIUS Dictionary Attribute Name,attr_type (string): RADIUS Dictionary Attribute Type,attr_profile (string): ["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile,extra_data (string, optional): RADIUS Dictionary Attribute Extra Data,valid_values (array[ValidValue], optional): RADIUS Dictionary Attribute Valid Values}ValidValue {value_enum (integer): Value of RADIUS Dictionary Attribute Valid Value,value (string): Value Enum of RADIUS Dictionary Attribute Valid Value}
        Required Body Parameters (type(dict) body example)- {
  "vendor_id": 0,
  "vendor_name": "",
  "prefix": "",
  "enabled": false,
  "attributes": [
    {
      "attr_id": 0,
      "attr_name": "",
      "attr_type": "",
      "attr_profile": "",
      "extra_data": "",
      "valid_values": [
        {
          "value_enum": 0,
          "value": ""
        }
      ]
    }
  ]
}
        '''
        url_path = '/radius-dictionary'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_radius_dictionary_by_radius_dictionary_id(self,radius_dictionary_id=""):
        '''
        Operation: Get a RADIUS Dictionary
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        '''
        url_path = '/radius-dictionary/{radius_dictionary_id}'
        dict_path={'radius_dictionary_id': radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_radius_dictionary_by_radius_dictionary_id(self,radius_dictionary_id="",body=({})):
        '''
        Operation: Update a RADIUS Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        Required Body Parameters (body description)- RADIUSDictionaryUpdate {vendor_id (integer, optional): Vendor ID of RADIUS Dictionary,vendor_name (string, optional): Vendor Name of RADIUS Dictionary,prefix (string, optional): Vendor Prefix of RADIUS Dictionary,enabled (boolean, optional): Is RADIUS Dictionary enabled?,attributes (array[Attributes], optional): Attributes of RADIUS Dictionary}Attributes {attr_id (integer): RADIUS Dictionary Attribute ID,attr_name (string): RADIUS Dictionary Attribute Name,attr_type (string): RADIUS Dictionary Attribute Type,attr_profile (string): ["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile,extra_data (string, optional): RADIUS Dictionary Attribute Extra Data,valid_values (array[ValidValue], optional): RADIUS Dictionary Attribute Valid Values}ValidValue {value_enum (integer): Value of RADIUS Dictionary Attribute Valid Value,value (string): Value Enum of RADIUS Dictionary Attribute Valid Value}
        Required Body Parameters (type(dict) body example)- {
  "vendor_id": 0,
  "vendor_name": "",
  "prefix": "",
  "enabled": false,
  "attributes": [
    {
      "attr_id": 0,
      "attr_name": "",
      "attr_type": "",
      "attr_profile": "",
      "extra_data": "",
      "valid_values": [
        {
          "value_enum": 0,
          "value": ""
        }
      ]
    }
  ]
}
        '''
        url_path = '/radius-dictionary/{radius_dictionary_id}'
        dict_path={'radius_dictionary_id': radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_radius_dictionary_by_radius_dictionary_id(self,radius_dictionary_id="",body=({})):
        '''
        Operation: Replace a RADIUS Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        Required Body Parameters (body description)- RADIUSDictionaryReplace {vendor_id (integer): Vendor ID of RADIUS Dictionary,vendor_name (string): Vendor Name of RADIUS Dictionary,prefix (string): Vendor Prefix of RADIUS Dictionary,enabled (boolean, optional): Is RADIUS Dictionary enabled?,attributes (array[Attributes]): Attributes of RADIUS Dictionary}Attributes {attr_id (integer): RADIUS Dictionary Attribute ID,attr_name (string): RADIUS Dictionary Attribute Name,attr_type (string): RADIUS Dictionary Attribute Type,attr_profile (string): ["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile,extra_data (string, optional): RADIUS Dictionary Attribute Extra Data,valid_values (array[ValidValue], optional): RADIUS Dictionary Attribute Valid Values}ValidValue {value_enum (integer): Value of RADIUS Dictionary Attribute Valid Value,value (string): Value Enum of RADIUS Dictionary Attribute Valid Value}
        Required Body Parameters (type(dict) body example)- {
  "vendor_id": 0,
  "vendor_name": "",
  "prefix": "",
  "enabled": false,
  "attributes": [
    {
      "attr_id": 0,
      "attr_name": "",
      "attr_type": "",
      "attr_profile": "",
      "extra_data": "",
      "valid_values": [
        {
          "value_enum": 0,
          "value": ""
        }
      ]
    }
  ]
}
        '''
        url_path = '/radius-dictionary/{radius_dictionary_id}'
        dict_path={'radius_dictionary_id': radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def get_radius_dictionary_name_by_name(self,name=""):
        '''
        Operation: Get a RADIUS Dictionary by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the RADIUS Dictionary
        '''
        url_path = '/radius-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_radius_dictionary_name_by_name(self,name="",body=({})):
        '''
        Operation: Update a RADIUS Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the RADIUS Dictionary
        Required Body Parameters (body description)- RADIUSDictionaryUpdate {vendor_id (integer, optional): Vendor ID of RADIUS Dictionary,vendor_name (string, optional): Vendor Name of RADIUS Dictionary,prefix (string, optional): Vendor Prefix of RADIUS Dictionary,enabled (boolean, optional): Is RADIUS Dictionary enabled?,attributes (array[Attributes], optional): Attributes of RADIUS Dictionary}Attributes {attr_id (integer): RADIUS Dictionary Attribute ID,attr_name (string): RADIUS Dictionary Attribute Name,attr_type (string): RADIUS Dictionary Attribute Type,attr_profile (string): ["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile,extra_data (string, optional): RADIUS Dictionary Attribute Extra Data,valid_values (array[ValidValue], optional): RADIUS Dictionary Attribute Valid Values}ValidValue {value_enum (integer): Value of RADIUS Dictionary Attribute Valid Value,value (string): Value Enum of RADIUS Dictionary Attribute Valid Value}
        Required Body Parameters (type(dict) body example)- {
  "vendor_id": 0,
  "vendor_name": "",
  "prefix": "",
  "enabled": false,
  "attributes": [
    {
      "attr_id": 0,
      "attr_name": "",
      "attr_type": "",
      "attr_profile": "",
      "extra_data": "",
      "valid_values": [
        {
          "value_enum": 0,
          "value": ""
        }
      ]
    }
  ]
}
        '''
        url_path = '/radius-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_radius_dictionary_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a RADIUS Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the RADIUS Dictionary
        Required Body Parameters (body description)- RADIUSDictionaryReplace {vendor_id (integer): Vendor ID of RADIUS Dictionary,vendor_name (string): Vendor Name of RADIUS Dictionary,prefix (string): Vendor Prefix of RADIUS Dictionary,enabled (boolean, optional): Is RADIUS Dictionary enabled?,attributes (array[Attributes]): Attributes of RADIUS Dictionary}Attributes {attr_id (integer): RADIUS Dictionary Attribute ID,attr_name (string): RADIUS Dictionary Attribute Name,attr_type (string): RADIUS Dictionary Attribute Type,attr_profile (string): ["in" or "out" or "in out"] RADIUS Dictionary Attribute Profile,extra_data (string, optional): RADIUS Dictionary Attribute Extra Data,valid_values (array[ValidValue], optional): RADIUS Dictionary Attribute Valid Values}ValidValue {value_enum (integer): Value of RADIUS Dictionary Attribute Valid Value,value (string): Value Enum of RADIUS Dictionary Attribute Valid Value}
        Required Body Parameters (type(dict) body example)- {
  "vendor_id": 0,
  "vendor_name": "",
  "prefix": "",
  "enabled": false,
  "attributes": [
    {
      "attr_id": 0,
      "attr_name": "",
      "attr_type": "",
      "attr_profile": "",
      "extra_data": "",
      "valid_values": [
        {
          "value_enum": 0,
          "value": ""
        }
      ]
    }
  ]
}
        '''
        url_path = '/radius-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def update_radius_dictionary_by_radius_dictionary_id_enable(self,radius_dictionary_id=""):
        '''
        Operation: Enable a RADIUS Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        '''
        url_path = '/radius-dictionary/{radius_dictionary_id}/enable'
        dict_path={'radius_dictionary_id': radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_radius_dictionary_by_radius_dictionary_id_disable(self,radius_dictionary_id=""):
        '''
        Operation: Disable a RADIUS Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: radius_dictionary_id, Description: Numeric ID of the RADIUS Dictionary
        '''
        url_path = '/radius-dictionary/{radius_dictionary_id}/disable'
        dict_path={'radius_dictionary_id': radius_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_radius_dictionary_name_by_name_enable(self,name=""):
        '''
        Operation: Enable a RADIUS Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the RADIUS Dictionary
        '''
        url_path = '/radius-dictionary/name/{name}/enable'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_radius_dictionary_name_by_name_disable(self,name=""):
        '''
        Operation: Disable a RADIUS Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the RADIUS Dictionary
        '''
        url_path = '/radius-dictionary/name/{name}/disable'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        

    #Function Section Name:RADIUSDynamicAuthorizationTemplate  
    #Function Section Description: Manage RADIUS Dynamic Authorization Templates

    def get_radius_dynamic_authorization_template(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of RADIUS Dynamic Authorization Templates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/radius-dynamic-authorization-template'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_radius_dynamic_authorization_template(self,body=({})):
        '''
        Operation: Create a new RADIUS Dynamic Authorization Template
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RADIUSDynamicAuthorizationTemplateCreate {vendor_name (string): Vendor Name of RADIUS Dynamic Authorization Template,template_type (string): Template Type of RADIUS Dynamic Authorization Template,name (string): Name of RADIUS Dynamic Authorization Template,display_name (string): Display Name of RADIUS Dynamic Authorization Template,attributes (array[Attributes]): Attributes of RADIUS Dynamic Authorization Template}Attributes {input_required (string) = ['Not_Required' or 'Optional' or 'Required']: RADIUS Dynamic Authorization Template Attribute Input Required,value (string): RADIUS Dynamic Authorization Template Attribute Value,name (string): RADIUS Dynamic Authorization Template Attribute Name,type (string, optional): RADIUS Dynamic Authorization Template Attribute Type}
        Required Body Parameters (type(dict) body example)- {
  "vendor_name": "",
  "template_type": "",
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "input_required": "",
      "value": "",
      "name": "",
      "type": ""
    }
  ]
}
        '''
        url_path = '/radius-dynamic-authorization-template'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(self,radius_dynamic_authorization_template_id=""):
        '''
        Operation: Get a RADIUS Dynamic Authorization Template
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
        '''
        url_path = '/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}'
        dict_path={'radius_dynamic_authorization_template_id': radius_dynamic_authorization_template_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(self,radius_dynamic_authorization_template_id="",body=({})):
        '''
        Operation: Update a RADIUS Dynamic Authorization Template
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
        Required Body Parameters (body description)- RADIUSDynamicAuthorizationTemplateUpdate {vendor_name (string, optional): Vendor Name of RADIUS Dynamic Authorization Template,template_type (string, optional): Template Type of RADIUS Dynamic Authorization Template,name (string, optional): Name of RADIUS Dynamic Authorization Template,display_name (string, optional): Display Name of RADIUS Dynamic Authorization Template,attributes (array[Attributes], optional): Attributes of RADIUS Dynamic Authorization Template}Attributes {input_required (string) = ['Not_Required' or 'Optional' or 'Required']: RADIUS Dynamic Authorization Template Attribute Input Required,value (string): RADIUS Dynamic Authorization Template Attribute Value,name (string): RADIUS Dynamic Authorization Template Attribute Name,type (string, optional): RADIUS Dynamic Authorization Template Attribute Type}
        Required Body Parameters (type(dict) body example)- {
  "vendor_name": "",
  "template_type": "",
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "input_required": "",
      "value": "",
      "name": "",
      "type": ""
    }
  ]
}
        '''
        url_path = '/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}'
        dict_path={'radius_dynamic_authorization_template_id': radius_dynamic_authorization_template_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(self,radius_dynamic_authorization_template_id="",body=({})):
        '''
        Operation: Replace a RADIUS Dynamic Authorization Template
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
        Required Body Parameters (body description)- RADIUSDynamicAuthorizationTemplateReplace {vendor_name (string): Vendor Name of RADIUS Dynamic Authorization Template,template_type (string): Template Type of RADIUS Dynamic Authorization Template,name (string): Name of RADIUS Dynamic Authorization Template,display_name (string): Display Name of RADIUS Dynamic Authorization Template,attributes (array[Attributes]): Attributes of RADIUS Dynamic Authorization Template}Attributes {input_required (string) = ['Not_Required' or 'Optional' or 'Required']: RADIUS Dynamic Authorization Template Attribute Input Required,value (string): RADIUS Dynamic Authorization Template Attribute Value,name (string): RADIUS Dynamic Authorization Template Attribute Name,type (string, optional): RADIUS Dynamic Authorization Template Attribute Type}
        Required Body Parameters (type(dict) body example)- {
  "vendor_name": "",
  "template_type": "",
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "input_required": "",
      "value": "",
      "name": "",
      "type": ""
    }
  ]
}
        '''
        url_path = '/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}'
        dict_path={'radius_dynamic_authorization_template_id': radius_dynamic_authorization_template_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_radius_dynamic_authorization_template_by_radius_dynamic_authorization_template_id(self,radius_dynamic_authorization_template_id=""):
        '''
        Operation: Delete a RADIUS Dynamic Authorization Template
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: radius_dynamic_authorization_template_id, Description: Numeric ID of RADIUS Dynamic Authorization Template
        '''
        url_path = '/radius-dynamic-authorization-template/{radius_dynamic_authorization_template_id}'
        dict_path={'radius_dynamic_authorization_template_id': radius_dynamic_authorization_template_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_radius_dynamic_authorization_template_name_by_name(self,name=""):
        '''
        Operation: Get a RADIUS Dynamic Authorization Template by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
        '''
        url_path = '/radius-dynamic-authorization-template/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_radius_dynamic_authorization_template_name_by_name(self,name="",body=({})):
        '''
        Operation: Update a RADIUS Dynamic Authorization Template by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
        Required Body Parameters (body description)- RADIUSDynamicAuthorizationTemplateUpdate {vendor_name (string, optional): Vendor Name of RADIUS Dynamic Authorization Template,template_type (string, optional): Template Type of RADIUS Dynamic Authorization Template,name (string, optional): Name of RADIUS Dynamic Authorization Template,display_name (string, optional): Display Name of RADIUS Dynamic Authorization Template,attributes (array[Attributes], optional): Attributes of RADIUS Dynamic Authorization Template}Attributes {input_required (string) = ['Not_Required' or 'Optional' or 'Required']: RADIUS Dynamic Authorization Template Attribute Input Required,value (string): RADIUS Dynamic Authorization Template Attribute Value,name (string): RADIUS Dynamic Authorization Template Attribute Name,type (string, optional): RADIUS Dynamic Authorization Template Attribute Type}
        Required Body Parameters (type(dict) body example)- {
  "vendor_name": "",
  "template_type": "",
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "input_required": "",
      "value": "",
      "name": "",
      "type": ""
    }
  ]
}
        '''
        url_path = '/radius-dynamic-authorization-template/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_radius_dynamic_authorization_template_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a RADIUS Dynamic Authorization Template by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
        Required Body Parameters (body description)- RADIUSDynamicAuthorizationTemplateReplace {vendor_name (string): Vendor Name of RADIUS Dynamic Authorization Template,template_type (string): Template Type of RADIUS Dynamic Authorization Template,name (string): Name of RADIUS Dynamic Authorization Template,display_name (string): Display Name of RADIUS Dynamic Authorization Template,attributes (array[Attributes]): Attributes of RADIUS Dynamic Authorization Template}Attributes {input_required (string) = ['Not_Required' or 'Optional' or 'Required']: RADIUS Dynamic Authorization Template Attribute Input Required,value (string): RADIUS Dynamic Authorization Template Attribute Value,name (string): RADIUS Dynamic Authorization Template Attribute Name,type (string, optional): RADIUS Dynamic Authorization Template Attribute Type}
        Required Body Parameters (type(dict) body example)- {
  "vendor_name": "",
  "template_type": "",
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "input_required": "",
      "value": "",
      "name": "",
      "type": ""
    }
  ]
}
        '''
        url_path = '/radius-dynamic-authorization-template/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_radius_dynamic_authorization_template_name_by_name(self,name=""):
        '''
        Operation: Delete a RADIUS Dynamic Authorization Template by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of RADIUS Dynamic Authorization Template
        '''
        url_path = '/radius-dynamic-authorization-template/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:RADIUSProxyTarget  
    #Function Section Description: Manage proxy targets

    def get_proxy_target(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of proxy targets
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/proxy-target'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_proxy_target(self,body=({})):
        '''
        Operation: Create a new proxy target
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RADIUSProxyTargetCreate {name (string): Name of the proxy target,host_name (string): Host name of the proxy target,description (string, optional): Description of the proxy target,authentication_port (integer, optional): Authentication port of the proxy target,proxy_type (string): The proxy type, either RADIUS or RadSec,accounting_port (integer, optional): Accounting port of the proxy target,secret (string, optional): Shared Secret of the proxy target,radsec_port (integer, optional): The RadSec proxy port number (Should be 2083),radsec_verify_cert (boolean, optional): Enable to verify the server certificate,cert_subject (string, optional): Client Certificate Subject,enable_status_server_msgs (boolean, optional): Enable to send the status-server message}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "host_name": "",
  "description": "",
  "authentication_port": 0,
  "proxy_type": "",
  "accounting_port": 0,
  "secret": "",
  "radsec_port": 0,
  "radsec_verify_cert": false,
  "cert_subject": "",
  "enable_status_server_msgs": false
}
        '''
        url_path = '/proxy-target'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_proxy_target_by_proxy_target_id(self,proxy_target_id=""):
        '''
        Operation: Get a proxy target
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: proxy_target_id, Description: Numeric ID of the proxy target
        '''
        url_path = '/proxy-target/{proxy_target_id}'
        dict_path={'proxy_target_id': proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_proxy_target_by_proxy_target_id(self,proxy_target_id="",body=({})):
        '''
        Operation: Update some fields of a proxy target
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: proxy_target_id, Description: Numeric ID of the proxy target
        Required Body Parameters (body description)- RADIUSProxyTargetUpdate {name (string, optional): Name of the proxy target,host_name (string, optional): Host name of the proxy target,description (string, optional): Description of the proxy target,authentication_port (integer, optional): Authentication port of the proxy target,proxy_type (string, optional): The proxy type, either RADIUS or RadSec,accounting_port (integer, optional): Accounting port of the proxy target,secret (string, optional): Shared Secret of the proxy target,radsec_port (integer, optional): The RadSec proxy port number (Should be 2083),radsec_verify_cert (boolean, optional): Enable to verify the server certificate,cert_subject (string, optional): Client Certificate Subject,enable_status_server_msgs (boolean, optional): Enable to send the status-server message}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "host_name": "",
  "description": "",
  "authentication_port": 0,
  "proxy_type": "",
  "accounting_port": 0,
  "secret": "",
  "radsec_port": 0,
  "radsec_verify_cert": false,
  "cert_subject": "",
  "enable_status_server_msgs": false
}
        '''
        url_path = '/proxy-target/{proxy_target_id}'
        dict_path={'proxy_target_id': proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_proxy_target_by_proxy_target_id(self,proxy_target_id="",body=({})):
        '''
        Operation: Replace a proxy target
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: proxy_target_id, Description: Numeric ID of the proxy target
        Required Body Parameters (body description)- RADIUSProxyTargetReplace {name (string): Name of the proxy target,host_name (string): Host name of the proxy target,description (string, optional): Description of the proxy target,authentication_port (integer, optional): Authentication port of the proxy target,proxy_type (string): The proxy type, either RADIUS or RadSec,accounting_port (integer, optional): Accounting port of the proxy target,secret (string, optional): Shared Secret of the proxy target,radsec_port (integer, optional): The RadSec proxy port number (Should be 2083),radsec_verify_cert (boolean, optional): Enable to verify the server certificate,cert_subject (string, optional): Client Certificate Subject,enable_status_server_msgs (boolean, optional): Enable to send the status-server message}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "host_name": "",
  "description": "",
  "authentication_port": 0,
  "proxy_type": "",
  "accounting_port": 0,
  "secret": "",
  "radsec_port": 0,
  "radsec_verify_cert": false,
  "cert_subject": "",
  "enable_status_server_msgs": false
}
        '''
        url_path = '/proxy-target/{proxy_target_id}'
        dict_path={'proxy_target_id': proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_proxy_target_by_proxy_target_id(self,proxy_target_id=""):
        '''
        Operation: Delete a proxy target
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: proxy_target_id, Description: Numeric ID of the proxy target
        '''
        url_path = '/proxy-target/{proxy_target_id}'
        dict_path={'proxy_target_id': proxy_target_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_proxy_target_name_by_name(self,name=""):
        '''
        Operation: Get a proxy target by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the proxy target
        '''
        url_path = '/proxy-target/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_proxy_target_name_by_name(self,name="",body=({})):
        '''
        Operation: Update some fields of a proxy target by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the proxy target
        Required Body Parameters (body description)- RADIUSProxyTargetUpdate {name (string, optional): Name of the proxy target,host_name (string, optional): Host name of the proxy target,description (string, optional): Description of the proxy target,authentication_port (integer, optional): Authentication port of the proxy target,proxy_type (string, optional): The proxy type, either RADIUS or RadSec,accounting_port (integer, optional): Accounting port of the proxy target,secret (string, optional): Shared Secret of the proxy target,radsec_port (integer, optional): The RadSec proxy port number (Should be 2083),radsec_verify_cert (boolean, optional): Enable to verify the server certificate,cert_subject (string, optional): Client Certificate Subject,enable_status_server_msgs (boolean, optional): Enable to send the status-server message}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "host_name": "",
  "description": "",
  "authentication_port": 0,
  "proxy_type": "",
  "accounting_port": 0,
  "secret": "",
  "radsec_port": 0,
  "radsec_verify_cert": false,
  "cert_subject": "",
  "enable_status_server_msgs": false
}
        '''
        url_path = '/proxy-target/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_proxy_target_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a proxy target by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the proxy target
        Required Body Parameters (body description)- RADIUSProxyTargetReplace {name (string): Name of the proxy target,host_name (string): Host name of the proxy target,description (string, optional): Description of the proxy target,authentication_port (integer, optional): Authentication port of the proxy target,proxy_type (string): The proxy type, either RADIUS or RadSec,accounting_port (integer, optional): Accounting port of the proxy target,secret (string, optional): Shared Secret of the proxy target,radsec_port (integer, optional): The RadSec proxy port number (Should be 2083),radsec_verify_cert (boolean, optional): Enable to verify the server certificate,cert_subject (string, optional): Client Certificate Subject,enable_status_server_msgs (boolean, optional): Enable to send the status-server message}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "host_name": "",
  "description": "",
  "authentication_port": 0,
  "proxy_type": "",
  "accounting_port": 0,
  "secret": "",
  "radsec_port": 0,
  "radsec_verify_cert": false,
  "cert_subject": "",
  "enable_status_server_msgs": false
}
        '''
        url_path = '/proxy-target/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_proxy_target_name_by_name(self,name=""):
        '''
        Operation: Delete a proxy target by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the proxy target
        '''
        url_path = '/proxy-target/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:Role  
    #Function Section Description: Manage roles

    def get_role(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of roles
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/role'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_role(self,body=({})):
        '''
        Operation: Create a new role
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RoleCreate {name (string): Name of the role,description (string, optional): Description of the role}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": ""
}
        '''
        url_path = '/role'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_role_by_role_id(self,role_id=""):
        '''
        Operation: Get a role
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: role_id, Description: Numeric ID of the role
        '''
        url_path = '/role/{role_id}'
        dict_path={'role_id': role_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_role_by_role_id(self,role_id="",body=({})):
        '''
        Operation: Update some fields of a role
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: role_id, Description: Numeric ID of the role
        Required Body Parameters (body description)- RoleUpdate {name (string, optional): Name of the role,description (string, optional): Description of the role}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": ""
}
        '''
        url_path = '/role/{role_id}'
        dict_path={'role_id': role_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_role_by_role_id(self,role_id="",body=({})):
        '''
        Operation: Replace a role
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: role_id, Description: Numeric ID of the role
        Required Body Parameters (body description)- RoleReplace {name (string): Name of the role,description (string, optional): Description of the role}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": ""
}
        '''
        url_path = '/role/{role_id}'
        dict_path={'role_id': role_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_role_by_role_id(self,role_id=""):
        '''
        Operation: Delete a role
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: role_id, Description: Numeric ID of the role
        '''
        url_path = '/role/{role_id}'
        dict_path={'role_id': role_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_role_name_by_name(self,name=""):
        '''
        Operation: Get a role by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the role
        '''
        url_path = '/role/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_role_name_by_name(self,name="",body=({})):
        '''
        Operation: Update some fields of a role by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the role
        Required Body Parameters (body description)- RoleUpdate {name (string, optional): Name of the role,description (string, optional): Description of the role}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": ""
}
        '''
        url_path = '/role/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_role_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a role by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the role
        Required Body Parameters (body description)- RoleReplace {name (string): Name of the role,description (string, optional): Description of the role}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": ""
}
        '''
        url_path = '/role/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_role_name_by_name(self,name=""):
        '''
        Operation: Delete a role by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the role
        '''
        url_path = '/role/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:RoleMapping  
    #Function Section Description: Manage Role Mappings

    def get_role_mapping(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of role mappings
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/role-mapping'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_role_mapping(self,body=({})):
        '''
        Operation: Create a new role mapping
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- RoleMappingCreate {name (string): Role mapping policy name,description (string, optional): Role mapping description,default_role_name (string): Role mapping default role name,rule_combine_algo (string) = ['first-applicable' or 'evaluate-all']: Role mapping rules evaluation algorithm,rules (RulesSettingsCreate): List of role mapping rules}RulesSettingsCreate {match_type (string) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,role_name (string): Role name,condition (RulesConditionSettingsCreate): Conditions of role mapping rules}RulesConditionSettingsCreate {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "default_role_name": "",
  "rule_combine_algo": "",
  "rules": {
    "match_type": "",
    "role_name": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/role-mapping'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_role_mapping_by_role_mapping_id(self,role_mapping_id=""):
        '''
        Operation: Get a role mapping
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: role_mapping_id, Description: Numeric ID of the role mapping
        '''
        url_path = '/role-mapping/{role_mapping_id}'
        dict_path={'role_mapping_id': role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_role_mapping_by_role_mapping_id(self,role_mapping_id="",body=({})):
        '''
        Operation: Update a role mapping
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: role_mapping_id, Description: Numeric ID of the role mapping
        Required Body Parameters (body description)- RoleMappingUpdate {name (string, optional): Role mapping policy name,description (string, optional): Role mapping description,default_role_name (string, optional): Role mapping default role name,rule_combine_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Role mapping rules evaluation algorithm,rules (RulesSettingsUpdate, optional): List of role mapping rules}RulesSettingsUpdate {match_type (string, optional) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,role_name (string, optional): Role name,condition (RulesConditionSettingsUpdate, optional): Conditions of role mapping rules}RulesConditionSettingsUpdate {type (string, optional): Condition type,name (string, optional): Condition name,oper (string, optional): Condition operator,value (string, optional): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "default_role_name": "",
  "rule_combine_algo": "",
  "rules": {
    "match_type": "",
    "role_name": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/role-mapping/{role_mapping_id}'
        dict_path={'role_mapping_id': role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_role_mapping_by_role_mapping_id(self,role_mapping_id="",body=({})):
        '''
        Operation: Replace a role mapping
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: role_mapping_id, Description: Numeric ID of the role mapping
        Required Body Parameters (body description)- RoleMappingReplace {name (string): Role mapping policy name,description (string, optional): Role mapping description,default_role_name (string): Role mapping default role name,rule_combine_algo (string) = ['first-applicable' or 'evaluate-all']: Role mapping rules evaluation algorithm,rules (RulesSettingsReplace): List of role mapping rules}RulesSettingsReplace {match_type (string) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,role_name (string): Role name,condition (RulesConditionSettingsReplace): Conditions of role mapping rules}RulesConditionSettingsReplace {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "default_role_name": "",
  "rule_combine_algo": "",
  "rules": {
    "match_type": "",
    "role_name": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/role-mapping/{role_mapping_id}'
        dict_path={'role_mapping_id': role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_role_mapping_by_role_mapping_id(self,role_mapping_id=""):
        '''
        Operation: Delete a role mapping
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: role_mapping_id, Description: Numeric ID of the role mapping
        '''
        url_path = '/role-mapping/{role_mapping_id}'
        dict_path={'role_mapping_id': role_mapping_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_role_mapping_name_by_name(self,name=""):
        '''
        Operation: Get a role mapping by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the role mapping
        '''
        url_path = '/role-mapping/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_role_mapping_name_by_name(self,name="",body=({})):
        '''
        Operation: Update a role mapping by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the role mapping
        Required Body Parameters (body description)- RoleMappingUpdate {name (string, optional): Role mapping policy name,description (string, optional): Role mapping description,default_role_name (string, optional): Role mapping default role name,rule_combine_algo (string, optional) = ['first-applicable' or 'evaluate-all']: Role mapping rules evaluation algorithm,rules (RulesSettingsUpdate, optional): List of role mapping rules}RulesSettingsUpdate {match_type (string, optional) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,role_name (string, optional): Role name,condition (RulesConditionSettingsUpdate, optional): Conditions of role mapping rules}RulesConditionSettingsUpdate {type (string, optional): Condition type,name (string, optional): Condition name,oper (string, optional): Condition operator,value (string, optional): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "default_role_name": "",
  "rule_combine_algo": "",
  "rules": {
    "match_type": "",
    "role_name": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/role-mapping/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_role_mapping_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a role mapping by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the role mapping
        Required Body Parameters (body description)- RoleMappingReplace {name (string): Role mapping policy name,description (string, optional): Role mapping description,default_role_name (string): Role mapping default role name,rule_combine_algo (string) = ['first-applicable' or 'evaluate-all']: Role mapping rules evaluation algorithm,rules (RulesSettingsReplace): List of role mapping rules}RulesSettingsReplace {match_type (string) = ['AND' or 'OR']: Matches ANY/ALL the conditions specified in the rule,role_name (string): Role name,condition (RulesConditionSettingsReplace): Conditions of role mapping rules}RulesConditionSettingsReplace {type (string): Condition type,name (string): Condition name,oper (string): Condition operator,value (string): Condition value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "description": "",
  "default_role_name": "",
  "rule_combine_algo": "",
  "rules": {
    "match_type": "",
    "role_name": "",
    "condition": {
      "type": "",
      "name": "",
      "oper": "",
      "value": ""
    }
  }
}
        '''
        url_path = '/role-mapping/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_role_mapping_name_by_name(self,name=""):
        '''
        Operation: Delete a role mapping by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the role mapping
        '''
        url_path = '/role-mapping/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        

    #Function Section Name:Service  
    #Function Section Description: Manage Configuration Services

    def get_config_service(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of Services
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/config/service'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_config_service(self,body=({})):
        '''
        Operation: Create a new Service
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ServiceCreate {name (string): Name of the Service,template (string) = ['Aruba 802.1X Wireless' or '802.1X Wireless' or '802.1X Wired' or 'MAC Authentication' or 'Web-based Authentication' or 'Web-based Health Check Only' or 'Web-based Open Network Access' or '802.1X Wireless - Identity Only' or '802.1X Wired - Identity Only' or 'RADIUS Enforcement ( Generic )' or 'RADIUS Proxy' or 'RADIUS Authorization' or 'TACACS+ Enforcement' or 'Aruba Application Authentication' or 'Aruba Application Authorization' or 'Cisco Web Authentication Proxy' or 'Event-based Enforcement' or 'ClearPass OnConnect Enforcement']: Template of the Service,enabled (boolean, optional): Is Service enabled?,order_no (integer, optional): Order number of the Service,description (string, optional): Description of the Service,monitor_mode (boolean, optional): Enable to monitor network access without enforcement,rules_match_type (string, optional) = ['MATCHES_ANY' or 'MATCHES_ALL']: Matches ANY/ALL of the rule conditions,rules_conditions (array[ServiceRules], optional): List of service rules conditions,auth_methods (array[string], optional): List of Authentication Method Names,auth_sources (array[string], optional): List of Authentication Source Names,strip_username (boolean, optional): Enable to specify a comma-separated list of rules to strip username prefixes or suffixes,strip_username_csv (string, optional): Strip Username Rule,service_cert_cn (string, optional): Subject DN of Service Certificate,service_cert_expiry_date (string, optional): Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z),role_mapping_policy (string, optional): Role Mapping Policy Name,enf_policy (string): Enforcement Policy Name,use_cached_policy_results (boolean, optional): Enable to use cached Roles and Posture attributes from previous sessions,authz_sources (array[string], optional): List of Additional authorization sources from which to fetch role-mapping attributes,posture_enabled (boolean, optional): Enable Posture Compliance,posture_policies (array[string], optional): List of Posture Policy Names,default_posture_token (string, optional) = ['HEALTHY' or 'CHECKUP' or 'TRANSITION' or 'QUARANTINE' or 'INFECTED' or 'UNKNOWN']: Default Posture Token,remediate_end_hosts (boolean, optional): Enable auto-remediation of non-compliant end-hosts,remediation_url (string, optional): Remediation URL,audit_enabled (boolean, optional): Enable Audit End-hosts,audit_server (string, optional): Audit Server Name,audit_trigger_condition (string, optional) = ['ALWAYS' or 'NO_POSTURE' or 'MAC_AUTH']: Audit Trigger Conditions,audit_mac_auth_client_type (string, optional) = ['KNOWN' or 'UNKNOWN' or 'BOTH']: Client Type For MAC authentication request Audit Trigger Condition,action_after_audit (string, optional) = ['NONE' or 'SNMP' or 'RADIUS']: Action after audit,audit_coa_acton (string, optional): RADIUS CoA Action to be triggered after audit,profiler_enabled (boolean, optional): Enable Profile Endpoints,profiler_endpoint_classification (array[string], optional): List of Endpoint classification(s) after which an action must be triggered,profiler_coa_action (string, optional): RADIUS CoA Action to be triggered by Profiler ,acct_proxy_enabled (boolean, optional): Enable Accounting Proxy Targets,acct_proxy_targets (array[string], optional): List Accounting Proxy Target names,acct_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be deleted for Accounting proxy,acct_proxy_attrs_to_add (array[AttributesToAdd], optional): RADIUS attributes to be added for Accounting proxy,radius_proxy_scheme (string, optional) = ['Load Balance' or 'Failover']: Proxying Scheme for RADIUS Proxy Service Type,radius_proxy_targets (array[string], optional): List of Proxy Targets for RADIUS Proxy Service Type,radius_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be removed from remote server (proxy target) reply,radius_proxy_enable_for_acct (boolean, optional): Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) }ServiceRules {type (string): Type,name (string): Name,operator (string): Operator,value (string, optional): Value}AttributesToDelete {type (string): Type,name (string): Name}AttributesToAdd {type (string): Type,name (string): Name,value (string): Value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "template": "",
  "enabled": false,
  "order_no": 0,
  "description": "",
  "monitor_mode": false,
  "rules_match_type": "",
  "rules_conditions": [
    {
      "type": "",
      "name": "",
      "operator": "",
      "value": ""
    }
  ],
  "auth_methods": [
    ""
  ],
  "auth_sources": [
    ""
  ],
  "strip_username": false,
  "strip_username_csv": "",
  "service_cert_cn": "",
  "service_cert_expiry_date": "",
  "role_mapping_policy": "",
  "enf_policy": "",
  "use_cached_policy_results": false,
  "authz_sources": [
    ""
  ],
  "posture_enabled": false,
  "posture_policies": [
    ""
  ],
  "default_posture_token": "",
  "remediate_end_hosts": false,
  "remediation_url": "",
  "audit_enabled": false,
  "audit_server": "",
  "audit_trigger_condition": "",
  "audit_mac_auth_client_type": "",
  "action_after_audit": "",
  "audit_coa_acton": "",
  "profiler_enabled": false,
  "profiler_endpoint_classification": [
    ""
  ],
  "profiler_coa_action": "",
  "acct_proxy_enabled": false,
  "acct_proxy_targets": [
    ""
  ],
  "acct_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "acct_proxy_attrs_to_add": [
    {
      "type": "",
      "name": "",
      "value": ""
    }
  ],
  "radius_proxy_scheme": "",
  "radius_proxy_targets": [
    ""
  ],
  "radius_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "radius_proxy_enable_for_acct": false
}
        '''
        url_path = '/config/service'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_config_service_by_services_id(self,services_id=""):
        '''
        Operation: Get a Service
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: services_id, Description: Numeric ID of the service
        '''
        url_path = '/config/service/{services_id}'
        dict_path={'services_id': services_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_config_service_by_services_id(self,services_id="",body=({})):
        '''
        Operation: Update some fields of a Service
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_id, Description: Numeric ID of the service
        Required Body Parameters (body description)- ServiceUpdate {name (string, optional): Name of the Service,template (string, optional) = ['Aruba 802.1X Wireless' or '802.1X Wireless' or '802.1X Wired' or 'MAC Authentication' or 'Web-based Authentication' or 'Web-based Health Check Only' or 'Web-based Open Network Access' or '802.1X Wireless - Identity Only' or '802.1X Wired - Identity Only' or 'RADIUS Enforcement ( Generic )' or 'RADIUS Proxy' or 'RADIUS Authorization' or 'TACACS+ Enforcement' or 'Aruba Application Authentication' or 'Aruba Application Authorization' or 'Cisco Web Authentication Proxy' or 'Event-based Enforcement' or 'ClearPass OnConnect Enforcement']: Template of the Service,enabled (boolean, optional): Is Service enabled?,order_no (integer, optional): Order number of the Service,description (string, optional): Description of the Service,monitor_mode (boolean, optional): Enable to monitor network access without enforcement,rules_match_type (string, optional) = ['MATCHES_ANY' or 'MATCHES_ALL']: Matches ANY/ALL of the rule conditions,rules_conditions (array[ServiceRules], optional): List of service rules conditions,auth_methods (array[string], optional): List of Authentication Method Names,auth_sources (array[string], optional): List of Authentication Source Names,strip_username (boolean, optional): Enable to specify a comma-separated list of rules to strip username prefixes or suffixes,strip_username_csv (string, optional): Strip Username Rule,service_cert_cn (string, optional): Subject DN of Service Certificate,service_cert_expiry_date (string, optional): Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z),role_mapping_policy (string, optional): Role Mapping Policy Name,enf_policy (string, optional): Enforcement Policy Name,use_cached_policy_results (boolean, optional): Enable to use cached Roles and Posture attributes from previous sessions,authz_sources (array[string], optional): List of Additional authorization sources from which to fetch role-mapping attributes,posture_enabled (boolean, optional): Enable Posture Compliance,posture_policies (array[string], optional): List of Posture Policy Names,default_posture_token (string, optional) = ['HEALTHY' or 'CHECKUP' or 'TRANSITION' or 'QUARANTINE' or 'INFECTED' or 'UNKNOWN']: Default Posture Token,remediate_end_hosts (boolean, optional): Enable auto-remediation of non-compliant end-hosts,remediation_url (string, optional): Remediation URL,audit_enabled (boolean, optional): Enable Audit End-hosts,audit_server (string, optional): Audit Server Name,audit_trigger_condition (string, optional) = ['ALWAYS' or 'NO_POSTURE' or 'MAC_AUTH']: Audit Trigger Conditions,audit_mac_auth_client_type (string, optional) = ['KNOWN' or 'UNKNOWN' or 'BOTH']: Client Type For MAC authentication request Audit Trigger Condition,action_after_audit (string, optional) = ['NONE' or 'SNMP' or 'RADIUS']: Action after audit,audit_coa_acton (string, optional): RADIUS CoA Action to be triggered after audit,profiler_enabled (boolean, optional): Enable Profile Endpoints,profiler_endpoint_classification (array[string], optional): List of Endpoint classification(s) after which an action must be triggered,profiler_coa_action (string, optional): RADIUS CoA Action to be triggered by Profiler ,acct_proxy_enabled (boolean, optional): Enable Accounting Proxy Targets,acct_proxy_targets (array[string], optional): List Accounting Proxy Target names,acct_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be deleted for Accounting proxy,acct_proxy_attrs_to_add (array[AttributesToAdd], optional): RADIUS attributes to be added for Accounting proxy,radius_proxy_scheme (string, optional) = ['Load Balance' or 'Failover']: Proxying Scheme for RADIUS Proxy Service Type,radius_proxy_targets (array[string], optional): List of Proxy Targets for RADIUS Proxy Service Type,radius_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be removed from remote server (proxy target) reply,radius_proxy_enable_for_acct (boolean, optional): Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) }ServiceRules {type (string): Type,name (string): Name,operator (string): Operator,value (string, optional): Value}AttributesToDelete {type (string): Type,name (string): Name}AttributesToAdd {type (string): Type,name (string): Name,value (string): Value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "template": "",
  "enabled": false,
  "order_no": 0,
  "description": "",
  "monitor_mode": false,
  "rules_match_type": "",
  "rules_conditions": [
    {
      "type": "",
      "name": "",
      "operator": "",
      "value": ""
    }
  ],
  "auth_methods": [
    ""
  ],
  "auth_sources": [
    ""
  ],
  "strip_username": false,
  "strip_username_csv": "",
  "service_cert_cn": "",
  "service_cert_expiry_date": "",
  "role_mapping_policy": "",
  "enf_policy": "",
  "use_cached_policy_results": false,
  "authz_sources": [
    ""
  ],
  "posture_enabled": false,
  "posture_policies": [
    ""
  ],
  "default_posture_token": "",
  "remediate_end_hosts": false,
  "remediation_url": "",
  "audit_enabled": false,
  "audit_server": "",
  "audit_trigger_condition": "",
  "audit_mac_auth_client_type": "",
  "action_after_audit": "",
  "audit_coa_acton": "",
  "profiler_enabled": false,
  "profiler_endpoint_classification": [
    ""
  ],
  "profiler_coa_action": "",
  "acct_proxy_enabled": false,
  "acct_proxy_targets": [
    ""
  ],
  "acct_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "acct_proxy_attrs_to_add": [
    {
      "type": "",
      "name": "",
      "value": ""
    }
  ],
  "radius_proxy_scheme": "",
  "radius_proxy_targets": [
    ""
  ],
  "radius_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "radius_proxy_enable_for_acct": false
}
        '''
        url_path = '/config/service/{services_id}'
        dict_path={'services_id': services_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_config_service_by_services_id(self,services_id="",body=({})):
        '''
        Operation: Replace a Service
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_id, Description: Numeric ID of the service
        Required Body Parameters (body description)- ServiceReplace {name (string): Name of the Service,template (string) = ['Aruba 802.1X Wireless' or '802.1X Wireless' or '802.1X Wired' or 'MAC Authentication' or 'Web-based Authentication' or 'Web-based Health Check Only' or 'Web-based Open Network Access' or '802.1X Wireless - Identity Only' or '802.1X Wired - Identity Only' or 'RADIUS Enforcement ( Generic )' or 'RADIUS Proxy' or 'RADIUS Authorization' or 'TACACS+ Enforcement' or 'Aruba Application Authentication' or 'Aruba Application Authorization' or 'Cisco Web Authentication Proxy' or 'Event-based Enforcement' or 'ClearPass OnConnect Enforcement']: Template of the Service,enabled (boolean, optional): Is Service enabled?,order_no (integer, optional): Order number of the Service,description (string, optional): Description of the Service,monitor_mode (boolean, optional): Enable to monitor network access without enforcement,rules_match_type (string, optional) = ['MATCHES_ANY' or 'MATCHES_ALL']: Matches ANY/ALL of the rule conditions,rules_conditions (array[ServiceRules], optional): List of service rules conditions,auth_methods (array[string], optional): List of Authentication Method Names,auth_sources (array[string], optional): List of Authentication Source Names,strip_username (boolean, optional): Enable to specify a comma-separated list of rules to strip username prefixes or suffixes,strip_username_csv (string, optional): Strip Username Rule,service_cert_cn (string, optional): Subject DN of Service Certificate,service_cert_expiry_date (string, optional): Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z),role_mapping_policy (string, optional): Role Mapping Policy Name,enf_policy (string): Enforcement Policy Name,use_cached_policy_results (boolean, optional): Enable to use cached Roles and Posture attributes from previous sessions,authz_sources (array[string], optional): List of Additional authorization sources from which to fetch role-mapping attributes,posture_enabled (boolean, optional): Enable Posture Compliance,posture_policies (array[string], optional): List of Posture Policy Names,default_posture_token (string, optional) = ['HEALTHY' or 'CHECKUP' or 'TRANSITION' or 'QUARANTINE' or 'INFECTED' or 'UNKNOWN']: Default Posture Token,remediate_end_hosts (boolean, optional): Enable auto-remediation of non-compliant end-hosts,remediation_url (string, optional): Remediation URL,audit_enabled (boolean, optional): Enable Audit End-hosts,audit_server (string, optional): Audit Server Name,audit_trigger_condition (string, optional) = ['ALWAYS' or 'NO_POSTURE' or 'MAC_AUTH']: Audit Trigger Conditions,audit_mac_auth_client_type (string, optional) = ['KNOWN' or 'UNKNOWN' or 'BOTH']: Client Type For MAC authentication request Audit Trigger Condition,action_after_audit (string, optional) = ['NONE' or 'SNMP' or 'RADIUS']: Action after audit,audit_coa_acton (string, optional): RADIUS CoA Action to be triggered after audit,profiler_enabled (boolean, optional): Enable Profile Endpoints,profiler_endpoint_classification (array[string], optional): List of Endpoint classification(s) after which an action must be triggered,profiler_coa_action (string, optional): RADIUS CoA Action to be triggered by Profiler ,acct_proxy_enabled (boolean, optional): Enable Accounting Proxy Targets,acct_proxy_targets (array[string], optional): List Accounting Proxy Target names,acct_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be deleted for Accounting proxy,acct_proxy_attrs_to_add (array[AttributesToAdd], optional): RADIUS attributes to be added for Accounting proxy,radius_proxy_scheme (string, optional) = ['Load Balance' or 'Failover']: Proxying Scheme for RADIUS Proxy Service Type,radius_proxy_targets (array[string], optional): List of Proxy Targets for RADIUS Proxy Service Type,radius_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be removed from remote server (proxy target) reply,radius_proxy_enable_for_acct (boolean, optional): Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) }ServiceRules {type (string): Type,name (string): Name,operator (string): Operator,value (string, optional): Value}AttributesToDelete {type (string): Type,name (string): Name}AttributesToAdd {type (string): Type,name (string): Name,value (string): Value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "template": "",
  "enabled": false,
  "order_no": 0,
  "description": "",
  "monitor_mode": false,
  "rules_match_type": "",
  "rules_conditions": [
    {
      "type": "",
      "name": "",
      "operator": "",
      "value": ""
    }
  ],
  "auth_methods": [
    ""
  ],
  "auth_sources": [
    ""
  ],
  "strip_username": false,
  "strip_username_csv": "",
  "service_cert_cn": "",
  "service_cert_expiry_date": "",
  "role_mapping_policy": "",
  "enf_policy": "",
  "use_cached_policy_results": false,
  "authz_sources": [
    ""
  ],
  "posture_enabled": false,
  "posture_policies": [
    ""
  ],
  "default_posture_token": "",
  "remediate_end_hosts": false,
  "remediation_url": "",
  "audit_enabled": false,
  "audit_server": "",
  "audit_trigger_condition": "",
  "audit_mac_auth_client_type": "",
  "action_after_audit": "",
  "audit_coa_acton": "",
  "profiler_enabled": false,
  "profiler_endpoint_classification": [
    ""
  ],
  "profiler_coa_action": "",
  "acct_proxy_enabled": false,
  "acct_proxy_targets": [
    ""
  ],
  "acct_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "acct_proxy_attrs_to_add": [
    {
      "type": "",
      "name": "",
      "value": ""
    }
  ],
  "radius_proxy_scheme": "",
  "radius_proxy_targets": [
    ""
  ],
  "radius_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "radius_proxy_enable_for_acct": false
}
        '''
        url_path = '/config/service/{services_id}'
        dict_path={'services_id': services_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_config_service_by_services_id(self,services_id=""):
        '''
        Operation: Delete a Service
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: services_id, Description: Numeric ID of the service
        '''
        url_path = '/config/service/{services_id}'
        dict_path={'services_id': services_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_config_service_name_by_services_name(self,services_name=""):
        '''
        Operation: Get a Service by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: services_name, Description: Name of the Service
        '''
        url_path = '/config/service/name/{services_name}'
        dict_path={'services_name': services_name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_config_service_name_by_services_name(self,services_name="",body=({})):
        '''
        Operation: Update some fields of a Service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_name, Description: Name of the Service
        Required Body Parameters (body description)- ServiceUpdate {name (string, optional): Name of the Service,template (string, optional) = ['Aruba 802.1X Wireless' or '802.1X Wireless' or '802.1X Wired' or 'MAC Authentication' or 'Web-based Authentication' or 'Web-based Health Check Only' or 'Web-based Open Network Access' or '802.1X Wireless - Identity Only' or '802.1X Wired - Identity Only' or 'RADIUS Enforcement ( Generic )' or 'RADIUS Proxy' or 'RADIUS Authorization' or 'TACACS+ Enforcement' or 'Aruba Application Authentication' or 'Aruba Application Authorization' or 'Cisco Web Authentication Proxy' or 'Event-based Enforcement' or 'ClearPass OnConnect Enforcement']: Template of the Service,enabled (boolean, optional): Is Service enabled?,order_no (integer, optional): Order number of the Service,description (string, optional): Description of the Service,monitor_mode (boolean, optional): Enable to monitor network access without enforcement,rules_match_type (string, optional) = ['MATCHES_ANY' or 'MATCHES_ALL']: Matches ANY/ALL of the rule conditions,rules_conditions (array[ServiceRules], optional): List of service rules conditions,auth_methods (array[string], optional): List of Authentication Method Names,auth_sources (array[string], optional): List of Authentication Source Names,strip_username (boolean, optional): Enable to specify a comma-separated list of rules to strip username prefixes or suffixes,strip_username_csv (string, optional): Strip Username Rule,service_cert_cn (string, optional): Subject DN of Service Certificate,service_cert_expiry_date (string, optional): Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z),role_mapping_policy (string, optional): Role Mapping Policy Name,enf_policy (string, optional): Enforcement Policy Name,use_cached_policy_results (boolean, optional): Enable to use cached Roles and Posture attributes from previous sessions,authz_sources (array[string], optional): List of Additional authorization sources from which to fetch role-mapping attributes,posture_enabled (boolean, optional): Enable Posture Compliance,posture_policies (array[string], optional): List of Posture Policy Names,default_posture_token (string, optional) = ['HEALTHY' or 'CHECKUP' or 'TRANSITION' or 'QUARANTINE' or 'INFECTED' or 'UNKNOWN']: Default Posture Token,remediate_end_hosts (boolean, optional): Enable auto-remediation of non-compliant end-hosts,remediation_url (string, optional): Remediation URL,audit_enabled (boolean, optional): Enable Audit End-hosts,audit_server (string, optional): Audit Server Name,audit_trigger_condition (string, optional) = ['ALWAYS' or 'NO_POSTURE' or 'MAC_AUTH']: Audit Trigger Conditions,audit_mac_auth_client_type (string, optional) = ['KNOWN' or 'UNKNOWN' or 'BOTH']: Client Type For MAC authentication request Audit Trigger Condition,action_after_audit (string, optional) = ['NONE' or 'SNMP' or 'RADIUS']: Action after audit,audit_coa_acton (string, optional): RADIUS CoA Action to be triggered after audit,profiler_enabled (boolean, optional): Enable Profile Endpoints,profiler_endpoint_classification (array[string], optional): List of Endpoint classification(s) after which an action must be triggered,profiler_coa_action (string, optional): RADIUS CoA Action to be triggered by Profiler ,acct_proxy_enabled (boolean, optional): Enable Accounting Proxy Targets,acct_proxy_targets (array[string], optional): List Accounting Proxy Target names,acct_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be deleted for Accounting proxy,acct_proxy_attrs_to_add (array[AttributesToAdd], optional): RADIUS attributes to be added for Accounting proxy,radius_proxy_scheme (string, optional) = ['Load Balance' or 'Failover']: Proxying Scheme for RADIUS Proxy Service Type,radius_proxy_targets (array[string], optional): List of Proxy Targets for RADIUS Proxy Service Type,radius_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be removed from remote server (proxy target) reply,radius_proxy_enable_for_acct (boolean, optional): Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) }ServiceRules {type (string): Type,name (string): Name,operator (string): Operator,value (string, optional): Value}AttributesToDelete {type (string): Type,name (string): Name}AttributesToAdd {type (string): Type,name (string): Name,value (string): Value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "template": "",
  "enabled": false,
  "order_no": 0,
  "description": "",
  "monitor_mode": false,
  "rules_match_type": "",
  "rules_conditions": [
    {
      "type": "",
      "name": "",
      "operator": "",
      "value": ""
    }
  ],
  "auth_methods": [
    ""
  ],
  "auth_sources": [
    ""
  ],
  "strip_username": false,
  "strip_username_csv": "",
  "service_cert_cn": "",
  "service_cert_expiry_date": "",
  "role_mapping_policy": "",
  "enf_policy": "",
  "use_cached_policy_results": false,
  "authz_sources": [
    ""
  ],
  "posture_enabled": false,
  "posture_policies": [
    ""
  ],
  "default_posture_token": "",
  "remediate_end_hosts": false,
  "remediation_url": "",
  "audit_enabled": false,
  "audit_server": "",
  "audit_trigger_condition": "",
  "audit_mac_auth_client_type": "",
  "action_after_audit": "",
  "audit_coa_acton": "",
  "profiler_enabled": false,
  "profiler_endpoint_classification": [
    ""
  ],
  "profiler_coa_action": "",
  "acct_proxy_enabled": false,
  "acct_proxy_targets": [
    ""
  ],
  "acct_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "acct_proxy_attrs_to_add": [
    {
      "type": "",
      "name": "",
      "value": ""
    }
  ],
  "radius_proxy_scheme": "",
  "radius_proxy_targets": [
    ""
  ],
  "radius_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "radius_proxy_enable_for_acct": false
}
        '''
        url_path = '/config/service/name/{services_name}'
        dict_path={'services_name': services_name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_config_service_name_by_services_name(self,services_name="",body=({})):
        '''
        Operation: Replace a Service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_name, Description: Name of the Service
        Required Body Parameters (body description)- ServiceReplace {name (string): Name of the Service,template (string) = ['Aruba 802.1X Wireless' or '802.1X Wireless' or '802.1X Wired' or 'MAC Authentication' or 'Web-based Authentication' or 'Web-based Health Check Only' or 'Web-based Open Network Access' or '802.1X Wireless - Identity Only' or '802.1X Wired - Identity Only' or 'RADIUS Enforcement ( Generic )' or 'RADIUS Proxy' or 'RADIUS Authorization' or 'TACACS+ Enforcement' or 'Aruba Application Authentication' or 'Aruba Application Authorization' or 'Cisco Web Authentication Proxy' or 'Event-based Enforcement' or 'ClearPass OnConnect Enforcement']: Template of the Service,enabled (boolean, optional): Is Service enabled?,order_no (integer, optional): Order number of the Service,description (string, optional): Description of the Service,monitor_mode (boolean, optional): Enable to monitor network access without enforcement,rules_match_type (string, optional) = ['MATCHES_ANY' or 'MATCHES_ALL']: Matches ANY/ALL of the rule conditions,rules_conditions (array[ServiceRules], optional): List of service rules conditions,auth_methods (array[string], optional): List of Authentication Method Names,auth_sources (array[string], optional): List of Authentication Source Names,strip_username (boolean, optional): Enable to specify a comma-separated list of rules to strip username prefixes or suffixes,strip_username_csv (string, optional): Strip Username Rule,service_cert_cn (string, optional): Subject DN of Service Certificate,service_cert_expiry_date (string, optional): Expiry Date of Service Certificate (Date Format - MMM dd, yyyy HH:mm:ss Z),role_mapping_policy (string, optional): Role Mapping Policy Name,enf_policy (string): Enforcement Policy Name,use_cached_policy_results (boolean, optional): Enable to use cached Roles and Posture attributes from previous sessions,authz_sources (array[string], optional): List of Additional authorization sources from which to fetch role-mapping attributes,posture_enabled (boolean, optional): Enable Posture Compliance,posture_policies (array[string], optional): List of Posture Policy Names,default_posture_token (string, optional) = ['HEALTHY' or 'CHECKUP' or 'TRANSITION' or 'QUARANTINE' or 'INFECTED' or 'UNKNOWN']: Default Posture Token,remediate_end_hosts (boolean, optional): Enable auto-remediation of non-compliant end-hosts,remediation_url (string, optional): Remediation URL,audit_enabled (boolean, optional): Enable Audit End-hosts,audit_server (string, optional): Audit Server Name,audit_trigger_condition (string, optional) = ['ALWAYS' or 'NO_POSTURE' or 'MAC_AUTH']: Audit Trigger Conditions,audit_mac_auth_client_type (string, optional) = ['KNOWN' or 'UNKNOWN' or 'BOTH']: Client Type For MAC authentication request Audit Trigger Condition,action_after_audit (string, optional) = ['NONE' or 'SNMP' or 'RADIUS']: Action after audit,audit_coa_acton (string, optional): RADIUS CoA Action to be triggered after audit,profiler_enabled (boolean, optional): Enable Profile Endpoints,profiler_endpoint_classification (array[string], optional): List of Endpoint classification(s) after which an action must be triggered,profiler_coa_action (string, optional): RADIUS CoA Action to be triggered by Profiler ,acct_proxy_enabled (boolean, optional): Enable Accounting Proxy Targets,acct_proxy_targets (array[string], optional): List Accounting Proxy Target names,acct_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be deleted for Accounting proxy,acct_proxy_attrs_to_add (array[AttributesToAdd], optional): RADIUS attributes to be added for Accounting proxy,radius_proxy_scheme (string, optional) = ['Load Balance' or 'Failover']: Proxying Scheme for RADIUS Proxy Service Type,radius_proxy_targets (array[string], optional): List of Proxy Targets for RADIUS Proxy Service Type,radius_proxy_attrs_to_delete (array[AttributesToDelete], optional): RADIUS attributes to be removed from remote server (proxy target) reply,radius_proxy_enable_for_acct (boolean, optional): Enable proxy for accounting requests (Applicable only for RADIUS Proxy Service Type) }ServiceRules {type (string): Type,name (string): Name,operator (string): Operator,value (string, optional): Value}AttributesToDelete {type (string): Type,name (string): Name}AttributesToAdd {type (string): Type,name (string): Name,value (string): Value}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "template": "",
  "enabled": false,
  "order_no": 0,
  "description": "",
  "monitor_mode": false,
  "rules_match_type": "",
  "rules_conditions": [
    {
      "type": "",
      "name": "",
      "operator": "",
      "value": ""
    }
  ],
  "auth_methods": [
    ""
  ],
  "auth_sources": [
    ""
  ],
  "strip_username": false,
  "strip_username_csv": "",
  "service_cert_cn": "",
  "service_cert_expiry_date": "",
  "role_mapping_policy": "",
  "enf_policy": "",
  "use_cached_policy_results": false,
  "authz_sources": [
    ""
  ],
  "posture_enabled": false,
  "posture_policies": [
    ""
  ],
  "default_posture_token": "",
  "remediate_end_hosts": false,
  "remediation_url": "",
  "audit_enabled": false,
  "audit_server": "",
  "audit_trigger_condition": "",
  "audit_mac_auth_client_type": "",
  "action_after_audit": "",
  "audit_coa_acton": "",
  "profiler_enabled": false,
  "profiler_endpoint_classification": [
    ""
  ],
  "profiler_coa_action": "",
  "acct_proxy_enabled": false,
  "acct_proxy_targets": [
    ""
  ],
  "acct_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "acct_proxy_attrs_to_add": [
    {
      "type": "",
      "name": "",
      "value": ""
    }
  ],
  "radius_proxy_scheme": "",
  "radius_proxy_targets": [
    ""
  ],
  "radius_proxy_attrs_to_delete": [
    {
      "type": "",
      "name": ""
    }
  ],
  "radius_proxy_enable_for_acct": false
}
        '''
        url_path = '/config/service/name/{services_name}'
        dict_path={'services_name': services_name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_config_service_name_by_services_name(self,services_name=""):
        '''
        Operation: Delete a Service by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: services_name, Description: Name of the Service
        '''
        url_path = '/config/service/name/{services_name}'
        dict_path={'services_name': services_name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def update_config_service_by_services_id_enable(self,services_id=""):
        '''
        Operation: Enable a Service
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_id, Description: Numeric ID of the service
        '''
        url_path = '/config/service/{services_id}/enable'
        dict_path={'services_id': services_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_config_service_name_by_services_name_enable(self,services_name=""):
        '''
        Operation: Enable a Service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_name, Description: Name of the Service
        '''
        url_path = '/config/service/name/{services_name}/enable'
        dict_path={'services_name': services_name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_config_service_by_services_id_disable(self,services_id=""):
        '''
        Operation: Disable a Service
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_id, Description: Numeric ID of the service
        '''
        url_path = '/config/service/{services_id}/disable'
        dict_path={'services_id': services_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_config_service_name_by_services_name_disable(self,services_name=""):
        '''
        Operation: Disable a Service by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: services_name, Description: Name of the Service
        '''
        url_path = '/config/service/name/{services_name}/disable'
        dict_path={'services_name': services_name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='patch')
        
        
    def update_config_service_reorder(self,body=({})):
        '''
        Operation: Reorder Services
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- ServiceReorder {service_orders (array[ServiceOrders]): List of Service Orders to be updated}ServiceOrders {service_name (string): Name of the Service,order_no (integer): Order number of the Service}
        Required Body Parameters (type(dict) body example)- {
  "service_orders": [
    {
      "service_name": "",
      "order_no": 0
    }
  ]
}
        '''
        url_path = '/config/service/reorder'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)

    #Function Section Name:TACACSServiceDictionary  
    #Function Section Description: Manage TACACS+ Service Dictionaries

    def get_tacacs_service_dictionary(self,filter="",sort="",offset="",limit="",calculate_count=""):
        '''
        Operation: Get a list of TACACS+ Service Dictionaries
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        '''
        url_path = '/tacacs-service-dictionary'
        dict_query={'filter': filter, 'sort': sort, 'offset': offset, 'limit': limit, 'calculate_count': calculate_count}
        url_path = _generate_parameterised_url(parameters = dict_query,url = url_path)
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def new_tacacs_service_dictionary(self,body=({})):
        '''
        Operation: Create a new TACACS+ Service Dictionary
        HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters (body description)- TACACSServiceDictionaryCreate {name (string): Name of TACACS+ Service Dictionary,display_name (string): Display Name of TACACS+ Service Dictionary,attributes (array[Attributes]): List of TACACS+ Service Dictionary Attributes}Attributes {attr_name (string): TACACS+ Service Dictionary Attribute Name,attr_display_name (string): TACACS+ Service Dictionary Attribute Display Name,attr_type (string): TACACS+ Service Dictionary Attribute Data Type,allowed_values (string, optional): Allowed Values for TACACS+ Service Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_display_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/tacacs-service-dictionary'
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='post',query = body)
    def get_tacacs_service_dictionary_by_tacacs_service_dictionary_id(self,tacacs_service_dictionary_id=""):
        '''
        Operation: Get a TACACS+ Service Dictionary
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
        '''
        url_path = '/tacacs-service-dictionary/{tacacs_service_dictionary_id}'
        dict_path={'tacacs_service_dictionary_id': tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_tacacs_service_dictionary_by_tacacs_service_dictionary_id(self,tacacs_service_dictionary_id="",body=({})):
        '''
        Operation: Update a TACACS+ Service Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
        Required Body Parameters (body description)- TACACSServiceDictionaryUpdate {name (string, optional): Name of TACACS+ Service Dictionary,display_name (string, optional): Display Name of TACACS+ Service Dictionary,attributes (array[Attributes], optional): List of TACACS+ Service Dictionary Attributes}Attributes {attr_name (string): TACACS+ Service Dictionary Attribute Name,attr_display_name (string): TACACS+ Service Dictionary Attribute Display Name,attr_type (string): TACACS+ Service Dictionary Attribute Data Type,allowed_values (string, optional): Allowed Values for TACACS+ Service Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_display_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/tacacs-service-dictionary/{tacacs_service_dictionary_id}'
        dict_path={'tacacs_service_dictionary_id': tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_tacacs_service_dictionary_by_tacacs_service_dictionary_id(self,tacacs_service_dictionary_id="",body=({})):
        '''
        Operation: Replace a TACACS+ Service Dictionary
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
        Required Body Parameters (body description)- TACACSServiceDictionaryReplace {name (string): Name of TACACS+ Service Dictionary,display_name (string): Display Name of TACACS+ Service Dictionary,attributes (array[Attributes]): List of TACACS+ Service Dictionary Attributes}Attributes {attr_name (string): TACACS+ Service Dictionary Attribute Name,attr_display_name (string): TACACS+ Service Dictionary Attribute Display Name,attr_type (string): TACACS+ Service Dictionary Attribute Data Type,allowed_values (string, optional): Allowed Values for TACACS+ Service Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_display_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/tacacs-service-dictionary/{tacacs_service_dictionary_id}'
        dict_path={'tacacs_service_dictionary_id': tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_tacacs_service_dictionary_by_tacacs_service_dictionary_id(self,tacacs_service_dictionary_id=""):
        '''
        Operation: Delete a TACACS+ Service Dictionary
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: tacacs_service_dictionary_id, Description: Numeric ID of the TACACS+ Service Dictionary
        '''
        url_path = '/tacacs-service-dictionary/{tacacs_service_dictionary_id}'
        dict_path={'tacacs_service_dictionary_id': tacacs_service_dictionary_id}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
    def get_tacacs_service_dictionary_name_by_name(self,name=""):
        '''
        Operation: Get a TACACS+ Service Dictionary by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the TACACS+ Service Dictionary
        '''
        url_path = '/tacacs-service-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='get')
        
        
    def update_tacacs_service_dictionary_name_by_name(self,name="",body=({})):
        '''
        Operation: Update a TACACS+ Service Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the TACACS+ Service Dictionary
        Required Body Parameters (body description)- TACACSServiceDictionaryUpdate {name (string, optional): Name of TACACS+ Service Dictionary,display_name (string, optional): Display Name of TACACS+ Service Dictionary,attributes (array[Attributes], optional): List of TACACS+ Service Dictionary Attributes}Attributes {attr_name (string): TACACS+ Service Dictionary Attribute Name,attr_display_name (string): TACACS+ Service Dictionary Attribute Display Name,attr_type (string): TACACS+ Service Dictionary Attribute Data Type,allowed_values (string, optional): Allowed Values for TACACS+ Service Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_display_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/tacacs-service-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='patch',query = body)
    def replace_tacacs_service_dictionary_name_by_name(self,name="",body=({})):
        '''
        Operation: Replace a TACACS+ Service Dictionary by name
        HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: name, Description: Unique name of the TACACS+ Service Dictionary
        Required Body Parameters (body description)- TACACSServiceDictionaryReplace {name (string): Name of TACACS+ Service Dictionary,display_name (string): Display Name of TACACS+ Service Dictionary,attributes (array[Attributes]): List of TACACS+ Service Dictionary Attributes}Attributes {attr_name (string): TACACS+ Service Dictionary Attribute Name,attr_display_name (string): TACACS+ Service Dictionary Attribute Display Name,attr_type (string): TACACS+ Service Dictionary Attribute Data Type,allowed_values (string, optional): Allowed Values for TACACS+ Service Dictionary Attributes in CSV format}
        Required Body Parameters (type(dict) body example)- {
  "name": "",
  "display_name": "",
  "attributes": [
    {
      "attr_name": "",
      "attr_display_name": "",
      "attr_type": "",
      "allowed_values": ""
    }
  ]
}
        '''
        url_path = '/tacacs-service-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        body = _remove_empty_keys(keys = body)
        return ClearPassAPILogin._send_request(self,url = url_path,method ='put',query = body)
    def delete_tacacs_service_dictionary_name_by_name(self,name=""):
        '''
        Operation: Delete a TACACS+ Service Dictionary by name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: Unique name of the TACACS+ Service Dictionary
        '''
        url_path = '/tacacs-service-dictionary/name/{name}'
        dict_path={'name': name}
        for item in dict_path:
            url_path = url_path.replace('{'+item+'}',dict_path[item])
        return ClearPassAPILogin._send_request(self,url = url_path,method='delete')
        
        
