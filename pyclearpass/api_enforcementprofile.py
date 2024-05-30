from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: EnforcementProfile
# FileName: api_enforcementprofile.py


class ApiEnforcementProfile(ClearPassAPILogin):

    # API Service: Manage Captive Portal Profile
    def get_enforcement_profile_dur_captive_portal_profile_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Captive Portal Profiles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/captive-portal-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_captive_portal_profile_by_product_name(
        self, product_name="", body=({})
    ):
        """
        Operation: Add a Captive Portal Profile
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Required Body Parameters:['name', 'url']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Captive Portal Profile. Object Type: string
        "url" : "", #URL for ArubaOS-Switch and AOS-CX Captive Portal Profile. Object Type: string
        "url_hashkey" : "", #URL HashKey for ArubaOS-Switch Captive Portal Profile. Object Type: string
        "aos_attributes" : "", #Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile. Object Type: AosAttributes

        }
        """
        url_path = "/enforcement-profile-dur/captive-portal-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_captive_portal_profile_by_product_name_captive_portal_profile_id(
        self, product_name="", captive_portal_profile_id=""
    ):
        """
        Operation: Get a Captive Portal Profile
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
        """
        url_path = "/enforcement-profile-dur/captive-portal-profile/{product_name}/{captive_portal_profile_id}"
        dict_path = {
            "product_name": product_name,
            "captive_portal_profile_id": captive_portal_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_captive_portal_profile_by_product_name_captive_portal_profile_id(
        self, product_name="", captive_portal_profile_id="", body=({})
    ):
        """
        Operation: Update some fields of a Captive Portal Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Captive Portal Profile. Object Type: string
        "url" : "", #URL for ArubaOS-Switch and AOS-CX Captive Portal Profile. Object Type: string
        "url_hashkey" : "", #URL HashKey for ArubaOS-Switch Captive Portal Profile. Object Type: string
        "aos_attributes" : "", #Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile. Object Type: AosAttributes

        }
        """
        url_path = "/enforcement-profile-dur/captive-portal-profile/{product_name}/{captive_portal_profile_id}"
        dict_path = {
            "product_name": product_name,
            "captive_portal_profile_id": captive_portal_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_captive_portal_profile_by_product_name_captive_portal_profile_id(
        self, product_name="", captive_portal_profile_id="", body=({})
    ):
        """
        Operation: Replace a Captive Portal Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Captive Portal Profile. Object Type: string
        "url" : "", #URL for ArubaOS-Switch and AOS-CX Captive Portal Profile. Object Type: string
        "url_hashkey" : "", #URL HashKey for ArubaOS-Switch Captive Portal Profile. Object Type: string
        "aos_attributes" : "", #Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile. Object Type: AosAttributes

        }
        """
        url_path = "/enforcement-profile-dur/captive-portal-profile/{product_name}/{captive_portal_profile_id}"
        dict_path = {
            "product_name": product_name,
            "captive_portal_profile_id": captive_portal_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_captive_portal_profile_by_product_name_captive_portal_profile_id(
        self, product_name="", captive_portal_profile_id=""
    ):
        """
        Operation: Delete a Captive Portal Profile
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
        """
        url_path = "/enforcement-profile-dur/captive-portal-profile/{product_name}/{captive_portal_profile_id}"
        dict_path = {
            "product_name": product_name,
            "captive_portal_profile_id": captive_portal_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_captive_portal_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Captive Portal Profile by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Captive Portal Profile
        """
        url_path = (
            "/enforcement-profile-dur/captive-portal-profile/{product_name}/name/{name}"
        )
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_captive_portal_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of a Captive Portal Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Captive Portal Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Captive Portal Profile. Object Type: string
        "url" : "", #URL for ArubaOS-Switch and AOS-CX Captive Portal Profile. Object Type: string
        "url_hashkey" : "", #URL HashKey for ArubaOS-Switch Captive Portal Profile. Object Type: string
        "aos_attributes" : "", #Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile. Object Type: AosAttributes

        }
        """
        url_path = (
            "/enforcement-profile-dur/captive-portal-profile/{product_name}/name/{name}"
        )
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_captive_portal_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Replace a Captive Portal Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Captive Portal Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Captive Portal Profile. Object Type: string
        "url" : "", #URL for ArubaOS-Switch and AOS-CX Captive Portal Profile. Object Type: string
        "url_hashkey" : "", #URL HashKey for ArubaOS-Switch Captive Portal Profile. Object Type: string
        "aos_attributes" : "", #Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile. Object Type: AosAttributes

        }
        """
        url_path = (
            "/enforcement-profile-dur/captive-portal-profile/{product_name}/name/{name}"
        )
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_captive_portal_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Captive Portal Profile by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Captive Portal Profile
        """
        url_path = (
            "/enforcement-profile-dur/captive-portal-profile/{product_name}/name/{name}"
        )
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage DUR Class
    def get_enforcement_profile_dur_dur_class_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Policies
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_dur_class_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a DUR Class
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name', 'hpe_rules', 'aos_cx_rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the DUR Class. Object Type: string
                "traffic" : "", #Traffic of the DUR Class. Object Type: string
                "hpe_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "traffic_match_type":"", #Traffic Match Type. Object Type: string
             "net_source":"", #Net Source for netsource traffic_match_type. Object Type: string
             "net_destination":"", #Net Destination for netsource traffic_match_type. Object Type: string
             "net_service":"", #Net Service for netsource traffic_match_type. Object Type: string
             "protocol":"", #Protocol for protocol traffic_match_type. Object Type: string
             "source":"", #Source for protocol traffic_match_type. Object Type: string
             "source_port":"", #Source Port for protocol traffic_match_type. Object Type: string
             "source_port_value":"", #Source Port Value for protocol traffic_match_type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255) for 255 protocol. Object Type: integer
             "destination":"", #Destnation for protocol traffic_match_type. Object Type: string
             "destination_value":"", #Destination Value for protocol traffic_match_type. Object Type: string
             "destination_port":"", #Destination Port for protocol traffic_match_type. Object Type: string
             "destination_port_value":"", #Destination Port Value for protocol traffic_match_type. Object Type: string
             "ip_dscp":0, #IP DSCP (0-63) for protocol traffic_match_type. Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094) for protocol traffic_match_type. Object Type: integer
             "ip_precedence":"", #IP Precedence for protocol traffic_match_type. Object Type: string
             "ip_service_type":"", #IP Type of Service for protocol traffic_match_type. Object Type: string
             "established":false, #Established for tcp protocol. Object Type: boolean
             "fin":false, #Fin for tcp protocol. Object Type: boolean
             "rst":false, #Rst for tcp protocol. Object Type: boolean
             "syn":false, #Syn for tcp protocol. Object Type: boolean
        }], #Rules for ArubaOS-Switch DUR Class. Object Type: array
                "aos_cx_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "protocol":"", #Protocol. Object Type: string
             "protocol_number":0, #Protocol Number for number protocol. Object Type: integer
             "source":"", #Source. Object Type: string
             "source_ip_address":"", #Source IP Address for ip source. Object Type: string
             "source_port":"", #Source Port. Object Type: string
             "source_port_value":"", #Source Port Value. Object Type: string
             "destination":"", #Destination. Object Type: string
             "destination_ip_address":"", #Destination IP Address for ip destination. Object Type: string
             "destination_port":"", #Destination Port. Object Type: string
             "destination_port_value":"", #Destination Port Value. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094). Object Type: integer
             "ecn":0, #ECN (0-3). Object Type: integer
             "ip_precedence":"", #IP Precedence. Object Type: string
             "service_type":0, #Type of Service (0-31). Object Type: integer
             "ttl":0, #Time to Live (0-255). Object Type: integer
             "fragment":false, #Fragment. Object Type: boolean
             "count_packet":false, #Count Packet. Object Type: boolean
             "cwr":false, #cwr for tcp protocol. Object Type: boolean
             "ece":false, #ece for tcp protocol. Object Type: boolean
             "urg":false, #urg for tcp protocol. Object Type: boolean
             "ack":false, #ack for tcp protocol. Object Type: boolean
             "psh":false, #psh for tcp protocol. Object Type: boolean
             "rst":false, #rst for tcp protocol. Object Type: boolean
             "syn":false, #syn for tcp protocol. Object Type: boolean
             "fin":false, #fin for tcp protocol. Object Type: boolean
             "established":false, #established for tcp protocol. Object Type: boolean
             "icmp_type":"", #ICMP Type for icmp protocol. Object Type: string
             "icmp_type_value":0, #ICMP Type Value (0-255) for number icmp_type. Object Type: integer
             "icmp_code":0, #ICMP Code (0-255) for icmp protocol. Object Type: integer
        }], #Rules for AOS-CX DUR Class. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_dur_class_by_product_name_dur_class_id(
        self, product_name="", dur_class_id=""
    ):
        """
        Operation: Get a DUR Class
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: dur_class_id, Description: Numeric ID of the DURClass
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/{dur_class_id}"
        dict_path = {"product_name": product_name, "dur_class_id": dur_class_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_dur_class_by_product_name_dur_class_id(
        self, product_name="", dur_class_id="", body=({})
    ):
        """
                Operation: Update a DUR Class
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: dur_class_id, Description: Numeric ID of the DURClass
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the DUR Class. Object Type: string
                "traffic" : "", #Traffic of the DUR Class. Object Type: string
                "hpe_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "traffic_match_type":"", #Traffic Match Type. Object Type: string
             "net_source":"", #Net Source for netsource traffic_match_type. Object Type: string
             "net_destination":"", #Net Destination for netsource traffic_match_type. Object Type: string
             "net_service":"", #Net Service for netsource traffic_match_type. Object Type: string
             "protocol":"", #Protocol for protocol traffic_match_type. Object Type: string
             "source":"", #Source for protocol traffic_match_type. Object Type: string
             "source_port":"", #Source Port for protocol traffic_match_type. Object Type: string
             "source_port_value":"", #Source Port Value for protocol traffic_match_type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255) for 255 protocol. Object Type: integer
             "destination":"", #Destnation for protocol traffic_match_type. Object Type: string
             "destination_value":"", #Destination Value for protocol traffic_match_type. Object Type: string
             "destination_port":"", #Destination Port for protocol traffic_match_type. Object Type: string
             "destination_port_value":"", #Destination Port Value for protocol traffic_match_type. Object Type: string
             "ip_dscp":0, #IP DSCP (0-63) for protocol traffic_match_type. Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094) for protocol traffic_match_type. Object Type: integer
             "ip_precedence":"", #IP Precedence for protocol traffic_match_type. Object Type: string
             "ip_service_type":"", #IP Type of Service for protocol traffic_match_type. Object Type: string
             "established":false, #Established for tcp protocol. Object Type: boolean
             "fin":false, #Fin for tcp protocol. Object Type: boolean
             "rst":false, #Rst for tcp protocol. Object Type: boolean
             "syn":false, #Syn for tcp protocol. Object Type: boolean
        }], #Rules for ArubaOS-Switch DUR Class. Object Type: array
                "aos_cx_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "protocol":"", #Protocol. Object Type: string
             "protocol_number":0, #Protocol Number for number protocol. Object Type: integer
             "source":"", #Source. Object Type: string
             "source_ip_address":"", #Source IP Address for ip source. Object Type: string
             "source_port":"", #Source Port. Object Type: string
             "source_port_value":"", #Source Port Value. Object Type: string
             "destination":"", #Destination. Object Type: string
             "destination_ip_address":"", #Destination IP Address for ip destination. Object Type: string
             "destination_port":"", #Destination Port. Object Type: string
             "destination_port_value":"", #Destination Port Value. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094). Object Type: integer
             "ecn":0, #ECN (0-3). Object Type: integer
             "ip_precedence":"", #IP Precedence. Object Type: string
             "service_type":0, #Type of Service (0-31). Object Type: integer
             "ttl":0, #Time to Live (0-255). Object Type: integer
             "fragment":false, #Fragment. Object Type: boolean
             "count_packet":false, #Count Packet. Object Type: boolean
             "cwr":false, #cwr for tcp protocol. Object Type: boolean
             "ece":false, #ece for tcp protocol. Object Type: boolean
             "urg":false, #urg for tcp protocol. Object Type: boolean
             "ack":false, #ack for tcp protocol. Object Type: boolean
             "psh":false, #psh for tcp protocol. Object Type: boolean
             "rst":false, #rst for tcp protocol. Object Type: boolean
             "syn":false, #syn for tcp protocol. Object Type: boolean
             "fin":false, #fin for tcp protocol. Object Type: boolean
             "established":false, #established for tcp protocol. Object Type: boolean
             "icmp_type":"", #ICMP Type for icmp protocol. Object Type: string
             "icmp_type_value":0, #ICMP Type Value (0-255) for number icmp_type. Object Type: integer
             "icmp_code":0, #ICMP Code (0-255) for icmp protocol. Object Type: integer
        }], #Rules for AOS-CX DUR Class. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/{dur_class_id}"
        dict_path = {"product_name": product_name, "dur_class_id": dur_class_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_dur_class_by_product_name_dur_class_id(
        self, product_name="", dur_class_id="", body=({})
    ):
        """
                Operation: Replace a DUR Class
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: dur_class_id, Description: Numeric ID of the DURClass
                Required Body Parameters:['name', 'hpe_rules', 'aos_cx_rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the DUR Class. Object Type: string
                "traffic" : "", #Traffic of the DUR Class. Object Type: string
                "hpe_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "traffic_match_type":"", #Traffic Match Type. Object Type: string
             "net_source":"", #Net Source for netsource traffic_match_type. Object Type: string
             "net_destination":"", #Net Destination for netsource traffic_match_type. Object Type: string
             "net_service":"", #Net Service for netsource traffic_match_type. Object Type: string
             "protocol":"", #Protocol for protocol traffic_match_type. Object Type: string
             "source":"", #Source for protocol traffic_match_type. Object Type: string
             "source_port":"", #Source Port for protocol traffic_match_type. Object Type: string
             "source_port_value":"", #Source Port Value for protocol traffic_match_type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255) for 255 protocol. Object Type: integer
             "destination":"", #Destnation for protocol traffic_match_type. Object Type: string
             "destination_value":"", #Destination Value for protocol traffic_match_type. Object Type: string
             "destination_port":"", #Destination Port for protocol traffic_match_type. Object Type: string
             "destination_port_value":"", #Destination Port Value for protocol traffic_match_type. Object Type: string
             "ip_dscp":0, #IP DSCP (0-63) for protocol traffic_match_type. Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094) for protocol traffic_match_type. Object Type: integer
             "ip_precedence":"", #IP Precedence for protocol traffic_match_type. Object Type: string
             "ip_service_type":"", #IP Type of Service for protocol traffic_match_type. Object Type: string
             "established":false, #Established for tcp protocol. Object Type: boolean
             "fin":false, #Fin for tcp protocol. Object Type: boolean
             "rst":false, #Rst for tcp protocol. Object Type: boolean
             "syn":false, #Syn for tcp protocol. Object Type: boolean
        }], #Rules for ArubaOS-Switch DUR Class. Object Type: array
                "aos_cx_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "protocol":"", #Protocol. Object Type: string
             "protocol_number":0, #Protocol Number for number protocol. Object Type: integer
             "source":"", #Source. Object Type: string
             "source_ip_address":"", #Source IP Address for ip source. Object Type: string
             "source_port":"", #Source Port. Object Type: string
             "source_port_value":"", #Source Port Value. Object Type: string
             "destination":"", #Destination. Object Type: string
             "destination_ip_address":"", #Destination IP Address for ip destination. Object Type: string
             "destination_port":"", #Destination Port. Object Type: string
             "destination_port_value":"", #Destination Port Value. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094). Object Type: integer
             "ecn":0, #ECN (0-3). Object Type: integer
             "ip_precedence":"", #IP Precedence. Object Type: string
             "service_type":0, #Type of Service (0-31). Object Type: integer
             "ttl":0, #Time to Live (0-255). Object Type: integer
             "fragment":false, #Fragment. Object Type: boolean
             "count_packet":false, #Count Packet. Object Type: boolean
             "cwr":false, #cwr for tcp protocol. Object Type: boolean
             "ece":false, #ece for tcp protocol. Object Type: boolean
             "urg":false, #urg for tcp protocol. Object Type: boolean
             "ack":false, #ack for tcp protocol. Object Type: boolean
             "psh":false, #psh for tcp protocol. Object Type: boolean
             "rst":false, #rst for tcp protocol. Object Type: boolean
             "syn":false, #syn for tcp protocol. Object Type: boolean
             "fin":false, #fin for tcp protocol. Object Type: boolean
             "established":false, #established for tcp protocol. Object Type: boolean
             "icmp_type":"", #ICMP Type for icmp protocol. Object Type: string
             "icmp_type_value":0, #ICMP Type Value (0-255) for number icmp_type. Object Type: integer
             "icmp_code":0, #ICMP Code (0-255) for icmp protocol. Object Type: integer
        }], #Rules for AOS-CX DUR Class. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/{dur_class_id}"
        dict_path = {"product_name": product_name, "dur_class_id": dur_class_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_dur_class_by_product_name_dur_class_id(
        self, product_name="", dur_class_id=""
    ):
        """
        Operation: Delete a DUR Class
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: dur_class_id, Description: Numeric ID of the DURClass
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/{dur_class_id}"
        dict_path = {"product_name": product_name, "dur_class_id": dur_class_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_dur_class_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a DUR Class by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the DURClass
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_dur_class_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update a DUR Class by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the DURClass
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the DUR Class. Object Type: string
                "traffic" : "", #Traffic of the DUR Class. Object Type: string
                "hpe_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "traffic_match_type":"", #Traffic Match Type. Object Type: string
             "net_source":"", #Net Source for netsource traffic_match_type. Object Type: string
             "net_destination":"", #Net Destination for netsource traffic_match_type. Object Type: string
             "net_service":"", #Net Service for netsource traffic_match_type. Object Type: string
             "protocol":"", #Protocol for protocol traffic_match_type. Object Type: string
             "source":"", #Source for protocol traffic_match_type. Object Type: string
             "source_port":"", #Source Port for protocol traffic_match_type. Object Type: string
             "source_port_value":"", #Source Port Value for protocol traffic_match_type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255) for 255 protocol. Object Type: integer
             "destination":"", #Destnation for protocol traffic_match_type. Object Type: string
             "destination_value":"", #Destination Value for protocol traffic_match_type. Object Type: string
             "destination_port":"", #Destination Port for protocol traffic_match_type. Object Type: string
             "destination_port_value":"", #Destination Port Value for protocol traffic_match_type. Object Type: string
             "ip_dscp":0, #IP DSCP (0-63) for protocol traffic_match_type. Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094) for protocol traffic_match_type. Object Type: integer
             "ip_precedence":"", #IP Precedence for protocol traffic_match_type. Object Type: string
             "ip_service_type":"", #IP Type of Service for protocol traffic_match_type. Object Type: string
             "established":false, #Established for tcp protocol. Object Type: boolean
             "fin":false, #Fin for tcp protocol. Object Type: boolean
             "rst":false, #Rst for tcp protocol. Object Type: boolean
             "syn":false, #Syn for tcp protocol. Object Type: boolean
        }], #Rules for ArubaOS-Switch DUR Class. Object Type: array
                "aos_cx_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "protocol":"", #Protocol. Object Type: string
             "protocol_number":0, #Protocol Number for number protocol. Object Type: integer
             "source":"", #Source. Object Type: string
             "source_ip_address":"", #Source IP Address for ip source. Object Type: string
             "source_port":"", #Source Port. Object Type: string
             "source_port_value":"", #Source Port Value. Object Type: string
             "destination":"", #Destination. Object Type: string
             "destination_ip_address":"", #Destination IP Address for ip destination. Object Type: string
             "destination_port":"", #Destination Port. Object Type: string
             "destination_port_value":"", #Destination Port Value. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094). Object Type: integer
             "ecn":0, #ECN (0-3). Object Type: integer
             "ip_precedence":"", #IP Precedence. Object Type: string
             "service_type":0, #Type of Service (0-31). Object Type: integer
             "ttl":0, #Time to Live (0-255). Object Type: integer
             "fragment":false, #Fragment. Object Type: boolean
             "count_packet":false, #Count Packet. Object Type: boolean
             "cwr":false, #cwr for tcp protocol. Object Type: boolean
             "ece":false, #ece for tcp protocol. Object Type: boolean
             "urg":false, #urg for tcp protocol. Object Type: boolean
             "ack":false, #ack for tcp protocol. Object Type: boolean
             "psh":false, #psh for tcp protocol. Object Type: boolean
             "rst":false, #rst for tcp protocol. Object Type: boolean
             "syn":false, #syn for tcp protocol. Object Type: boolean
             "fin":false, #fin for tcp protocol. Object Type: boolean
             "established":false, #established for tcp protocol. Object Type: boolean
             "icmp_type":"", #ICMP Type for icmp protocol. Object Type: string
             "icmp_type_value":0, #ICMP Type Value (0-255) for number icmp_type. Object Type: integer
             "icmp_code":0, #ICMP Code (0-255) for icmp protocol. Object Type: integer
        }], #Rules for AOS-CX DUR Class. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_dur_class_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a DUR Class by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the DURClass
                Required Body Parameters:['name', 'hpe_rules', 'aos_cx_rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the DUR Class. Object Type: string
                "traffic" : "", #Traffic of the DUR Class. Object Type: string
                "hpe_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "traffic_match_type":"", #Traffic Match Type. Object Type: string
             "net_source":"", #Net Source for netsource traffic_match_type. Object Type: string
             "net_destination":"", #Net Destination for netsource traffic_match_type. Object Type: string
             "net_service":"", #Net Service for netsource traffic_match_type. Object Type: string
             "protocol":"", #Protocol for protocol traffic_match_type. Object Type: string
             "source":"", #Source for protocol traffic_match_type. Object Type: string
             "source_port":"", #Source Port for protocol traffic_match_type. Object Type: string
             "source_port_value":"", #Source Port Value for protocol traffic_match_type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255) for 255 protocol. Object Type: integer
             "destination":"", #Destnation for protocol traffic_match_type. Object Type: string
             "destination_value":"", #Destination Value for protocol traffic_match_type. Object Type: string
             "destination_port":"", #Destination Port for protocol traffic_match_type. Object Type: string
             "destination_port_value":"", #Destination Port Value for protocol traffic_match_type. Object Type: string
             "ip_dscp":0, #IP DSCP (0-63) for protocol traffic_match_type. Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094) for protocol traffic_match_type. Object Type: integer
             "ip_precedence":"", #IP Precedence for protocol traffic_match_type. Object Type: string
             "ip_service_type":"", #IP Type of Service for protocol traffic_match_type. Object Type: string
             "established":false, #Established for tcp protocol. Object Type: boolean
             "fin":false, #Fin for tcp protocol. Object Type: boolean
             "rst":false, #Rst for tcp protocol. Object Type: boolean
             "syn":false, #Syn for tcp protocol. Object Type: boolean
        }], #Rules for ArubaOS-Switch DUR Class. Object Type: array
                "aos_cx_rules" : [{
             "number":0, #Number (1-2147483647). Object Type: integer
             "packet_match":"", #Packet Match. Object Type: string
             "protocol":"", #Protocol. Object Type: string
             "protocol_number":0, #Protocol Number for number protocol. Object Type: integer
             "source":"", #Source. Object Type: string
             "source_ip_address":"", #Source IP Address for ip source. Object Type: string
             "source_port":"", #Source Port. Object Type: string
             "source_port_value":"", #Source Port Value. Object Type: string
             "destination":"", #Destination. Object Type: string
             "destination_ip_address":"", #Destination IP Address for ip destination. Object Type: string
             "destination_port":"", #Destination Port. Object Type: string
             "destination_port_value":"", #Destination Port Value. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "vlan_id":0, #VLAN ID (1-4094). Object Type: integer
             "ecn":0, #ECN (0-3). Object Type: integer
             "ip_precedence":"", #IP Precedence. Object Type: string
             "service_type":0, #Type of Service (0-31). Object Type: integer
             "ttl":0, #Time to Live (0-255). Object Type: integer
             "fragment":false, #Fragment. Object Type: boolean
             "count_packet":false, #Count Packet. Object Type: boolean
             "cwr":false, #cwr for tcp protocol. Object Type: boolean
             "ece":false, #ece for tcp protocol. Object Type: boolean
             "urg":false, #urg for tcp protocol. Object Type: boolean
             "ack":false, #ack for tcp protocol. Object Type: boolean
             "psh":false, #psh for tcp protocol. Object Type: boolean
             "rst":false, #rst for tcp protocol. Object Type: boolean
             "syn":false, #syn for tcp protocol. Object Type: boolean
             "fin":false, #fin for tcp protocol. Object Type: boolean
             "established":false, #established for tcp protocol. Object Type: boolean
             "icmp_type":"", #ICMP Type for icmp protocol. Object Type: string
             "icmp_type_value":0, #ICMP Type Value (0-255) for number icmp_type. Object Type: integer
             "icmp_code":0, #ICMP Code (0-255) for icmp protocol. Object Type: integer
        }], #Rules for AOS-CX DUR Class. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_dur_class_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a DUR Class by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the DURClass
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Enforcement Profiles
    def get_enforcement_profile(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Enforcement Profiles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/enforcement-profile"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile(self, body=({})):
        """
                Operation: Create a new Enforcement Profile
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['name', 'type']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Enforcement Profile. Object Type: string
                "description" : "", #Description of the Enforcement Profile. Object Type: string
                "type" : "", #Enforcement Profile Type. Object Type: string
                "agent_template" : "", #Agent Enforcement Profile Template. Object Type: string
                "post_auth_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "radius_dyn_authz_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "action" : "", #Enforcement Profile Action. Object Type: string
                "device_group_list" : "", #Device Group List. Object Type: array
                "attributes" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Attributes. Object Type: array
                "tacacs_service_params" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Tacacs+ Service Params. Object Type: TacacsServiceParam
                "dur_config" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Downloadable User Role Configuration. Object Type: DURConfig

                }
        """
        url_path = "/enforcement-profile"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_by_enforcement_profile_id(
        self, enforcement_profile_id=""
    ):
        """
        Operation: Get an Enforcement Profile
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
        """
        url_path = "/enforcement-profile/{enforcement_profile_id}"
        dict_path = {"enforcement_profile_id": enforcement_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_by_enforcement_profile_id(
        self, enforcement_profile_id="", body=({})
    ):
        """
                Operation: Update an Enforcement Profile
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Enforcement Profile. Object Type: string
                "description" : "", #Description of the Enforcement Profile. Object Type: string
                "type" : "", #Enforcement Profile Type. Object Type: string
                "agent_template" : "", #Agent Enforcement Profile Template. Object Type: string
                "post_auth_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "radius_dyn_authz_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "action" : "", #Enforcement Profile Action. Object Type: string
                "device_group_list" : "", #Device Group List. Object Type: array
                "attributes" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Attributes. Object Type: array
                "tacacs_service_params" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Tacacs+ Service Params. Object Type: TacacsServiceParam
                "dur_config" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Downloadable User Role Configuration. Object Type: DURConfig

                }
        """
        url_path = "/enforcement-profile/{enforcement_profile_id}"
        dict_path = {"enforcement_profile_id": enforcement_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_by_enforcement_profile_id(
        self, enforcement_profile_id="", body=({})
    ):
        """
                Operation: Replace an Enforcement Profile
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
                Required Body Parameters:['name', 'type']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Enforcement Profile. Object Type: string
                "description" : "", #Description of the Enforcement Profile. Object Type: string
                "type" : "", #Enforcement Profile Type. Object Type: string
                "agent_template" : "", #Agent Enforcement Profile Template. Object Type: string
                "post_auth_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "radius_dyn_authz_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "action" : "", #Enforcement Profile Action. Object Type: string
                "device_group_list" : "", #Device Group List. Object Type: array
                "attributes" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Attributes. Object Type: array
                "tacacs_service_params" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Tacacs+ Service Params. Object Type: TacacsServiceParam
                "dur_config" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Downloadable User Role Configuration. Object Type: DURConfig

                }
        """
        url_path = "/enforcement-profile/{enforcement_profile_id}"
        dict_path = {"enforcement_profile_id": enforcement_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_by_enforcement_profile_id(
        self, enforcement_profile_id=""
    ):
        """
        Operation: Delete an Enforcement Profile
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
        """
        url_path = "/enforcement-profile/{enforcement_profile_id}"
        dict_path = {"enforcement_profile_id": enforcement_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_name_by_name(self, name=""):
        """
        Operation: Get an Enforcement Profile by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: name of the enforcement profile
        """
        url_path = "/enforcement-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_name_by_name(self, name="", body=({})):
        """
                Operation: Update an Enforcement Profile by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: name of the enforcement profile
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Enforcement Profile. Object Type: string
                "description" : "", #Description of the Enforcement Profile. Object Type: string
                "type" : "", #Enforcement Profile Type. Object Type: string
                "agent_template" : "", #Agent Enforcement Profile Template. Object Type: string
                "post_auth_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "radius_dyn_authz_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "action" : "", #Enforcement Profile Action. Object Type: string
                "device_group_list" : "", #Device Group List. Object Type: array
                "attributes" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Attributes. Object Type: array
                "tacacs_service_params" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Tacacs+ Service Params. Object Type: TacacsServiceParam
                "dur_config" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Downloadable User Role Configuration. Object Type: DURConfig

                }
        """
        url_path = "/enforcement-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_name_by_name(self, name="", body=({})):
        """
                Operation: Replace an Enforcement Profile by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: name, Description: name of the enforcement profile
                Required Body Parameters:['name', 'type']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Enforcement Profile. Object Type: string
                "description" : "", #Description of the Enforcement Profile. Object Type: string
                "type" : "", #Enforcement Profile Type. Object Type: string
                "agent_template" : "", #Agent Enforcement Profile Template. Object Type: string
                "post_auth_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "radius_dyn_authz_template" : "", #Post Authentication Enforcement Profile Template. Object Type: string
                "action" : "", #Enforcement Profile Action. Object Type: string
                "device_group_list" : "", #Device Group List. Object Type: array
                "attributes" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Attributes. Object Type: array
                "tacacs_service_params" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Tacacs+ Service Params. Object Type: TacacsServiceParam
                "dur_config" : [{
             "type":"", #Type of the Attribute. Object Type: string
             "name":"", #Name of the Attribute. Object Type: string
             "value":"", #Value of the Attribute. Object Type: string
        }], #Downloadable User Role Configuration. Object Type: DURConfig

                }
        """
        url_path = "/enforcement-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_name_by_name(self, name=""):
        """
        Operation: Delete an Enforcement Profile by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: name of the enforcement profile
        """
        url_path = "/enforcement-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Ethertype Access Control List
    def get_enforcement_profile_dur_ethertype_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Ethertype Access Control Lists
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = (
            "/enforcement-profile-dur/ethertype-access-control-list/{product_name}"
        )
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_ethertype_access_control_list_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a Ethertype Access Control List
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Ethertype Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "ethertype_type":"", #Ethertype Type. Object Type: string
             "ethertype_value":0, #Ethertype Value (0-65535). Object Type: integer
             "subnet_bits":0, #Subnet Bits (0-65535). Object Type: integer
        }], #Rules of the Ethertype Access Control List. Object Type: array

                }
        """
        url_path = (
            "/enforcement-profile-dur/ethertype-access-control-list/{product_name}"
        )
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_ethertype_access_control_list_by_product_name_ethertype_access_control_list_id(
        self, product_name="", ethertype_access_control_list_id=""
    ):
        """
        Operation: Get a Ethertype Access Control List
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/{ethertype_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "ethertype_access_control_list_id": ethertype_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_ethertype_access_control_list_by_product_name_ethertype_access_control_list_id(
        self, product_name="", ethertype_access_control_list_id="", body=({})
    ):
        """
                Operation: Update a Ethertype Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Ethertype Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "ethertype_type":"", #Ethertype Type. Object Type: string
             "ethertype_value":0, #Ethertype Value (0-65535). Object Type: integer
             "subnet_bits":0, #Subnet Bits (0-65535). Object Type: integer
        }], #Rules of the Ethertype Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/{ethertype_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "ethertype_access_control_list_id": ethertype_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_ethertype_access_control_list_by_product_name_ethertype_access_control_list_id(
        self, product_name="", ethertype_access_control_list_id="", body=({})
    ):
        """
                Operation: Replace a Ethertype Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Ethertype Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "ethertype_type":"", #Ethertype Type. Object Type: string
             "ethertype_value":0, #Ethertype Value (0-65535). Object Type: integer
             "subnet_bits":0, #Subnet Bits (0-65535). Object Type: integer
        }], #Rules of the Ethertype Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/{ethertype_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "ethertype_access_control_list_id": ethertype_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_ethertype_access_control_list_by_product_name_ethertype_access_control_list_id(
        self, product_name="", ethertype_access_control_list_id=""
    ):
        """
        Operation: Delete a Ethertype Access Control List
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/{ethertype_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "ethertype_access_control_list_id": ethertype_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_ethertype_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Ethertype Access Control List by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Ethertype Access Control List
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_ethertype_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update a Ethertype Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Ethertype Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Ethertype Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "ethertype_type":"", #Ethertype Type. Object Type: string
             "ethertype_value":0, #Ethertype Value (0-65535). Object Type: integer
             "subnet_bits":0, #Subnet Bits (0-65535). Object Type: integer
        }], #Rules of the Ethertype Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_ethertype_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a Ethertype Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Ethertype Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Ethertype Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "ethertype_type":"", #Ethertype Type. Object Type: string
             "ethertype_value":0, #Ethertype Value (0-65535). Object Type: integer
             "subnet_bits":0, #Subnet Bits (0-65535). Object Type: integer
        }], #Rules of the Ethertype Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_ethertype_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Ethertype Access Control List by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Ethertype Access Control List
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage MAC Access Control List
    def get_enforcement_profile_dur_mac_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of MAC Access Control Lists
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_mac_access_control_list_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a MAC Access Control List
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the MAC Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "mac_address_type":"", #MAC Address Type. Object Type: string
             "mac_address_value":"", #MAC Address Value (eg. AA:BB:CC:DD:EE:FF). Object Type: string
             "subnet_bits":"", #Subnet Bits (eg. AA:BB:CC:DD:EE:FF). Object Type: string
        }], #Rules of the MAC Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_mac_access_control_list_by_product_name_mac_access_control_list_id(
        self, product_name="", mac_access_control_list_id=""
    ):
        """
        Operation: Get a MAC Access Control List
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/{mac_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "mac_access_control_list_id": mac_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_mac_access_control_list_by_product_name_mac_access_control_list_id(
        self, product_name="", mac_access_control_list_id="", body=({})
    ):
        """
                Operation: Update some fields of a MAC Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the MAC Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "mac_address_type":"", #MAC Address Type. Object Type: string
             "mac_address_value":"", #MAC Address Value (eg. AA:BB:CC:DD:EE:FF). Object Type: string
             "subnet_bits":"", #Subnet Bits (eg. AA:BB:CC:DD:EE:FF). Object Type: string
        }], #Rules of the MAC Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/{mac_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "mac_access_control_list_id": mac_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_mac_access_control_list_by_product_name_mac_access_control_list_id(
        self, product_name="", mac_access_control_list_id="", body=({})
    ):
        """
                Operation: Replace a MAC Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the MAC Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "mac_address_type":"", #MAC Address Type. Object Type: string
             "mac_address_value":"", #MAC Address Value (eg. AA:BB:CC:DD:EE:FF). Object Type: string
             "subnet_bits":"", #Subnet Bits (eg. AA:BB:CC:DD:EE:FF). Object Type: string
        }], #Rules of the MAC Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/{mac_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "mac_access_control_list_id": mac_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_mac_access_control_list_by_product_name_mac_access_control_list_id(
        self, product_name="", mac_access_control_list_id=""
    ):
        """
        Operation: Delete a MAC Access Control List
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/{mac_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "mac_access_control_list_id": mac_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_mac_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a MAC Access Control List by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the MAC Access Control List
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_mac_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update some fields of a MAC Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the MAC Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the MAC Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "mac_address_type":"", #MAC Address Type. Object Type: string
             "mac_address_value":"", #MAC Address Value (eg. AA:BB:CC:DD:EE:FF). Object Type: string
             "subnet_bits":"", #Subnet Bits (eg. AA:BB:CC:DD:EE:FF). Object Type: string
        }], #Rules of the MAC Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_mac_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a MAC Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the MAC Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the MAC Access Control List. Object Type: string
                "rules" : [{
             "action":"", #Action. Object Type: string
             "mac_address_type":"", #MAC Address Type. Object Type: string
             "mac_address_value":"", #MAC Address Value (eg. AA:BB:CC:DD:EE:FF). Object Type: string
             "subnet_bits":"", #Subnet Bits (eg. AA:BB:CC:DD:EE:FF). Object Type: string
        }], #Rules of the MAC Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_mac_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a MAC Access Control List by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the MAC Access Control List
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage NAT Pool
    def get_enforcement_profile_dur_nat_pool_by_product_name(self, product_name=""):
        """
        Operation: GET a list of NAT Pools
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_nat_pool_by_product_name(
        self, product_name="", body=({})
    ):
        """
        Operation: Add a NAT Pool
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Required Body Parameters:['name', 'start_src_range', 'end_src_range']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the NAT Pool. Object Type: string
        "start_src_range" : "", #Start of source NAT range. Object Type: string
        "end_src_range" : "", #End of source NAT range. Object Type: string
        "destination_nat_ip_address" : "", #Destination NAT IP Address. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_nat_pool_by_product_name_nat_pool_id(
        self, product_name="", nat_pool_id=""
    ):
        """
        Operation: Get a NAT Pool
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: nat_pool_id, Description: Numeric ID of the NAT Pool
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/{nat_pool_id}"
        dict_path = {"product_name": product_name, "nat_pool_id": nat_pool_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_nat_pool_by_product_name_nat_pool_id(
        self, product_name="", nat_pool_id="", body=({})
    ):
        """
        Operation: Update some fields of a NAT Pool
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: nat_pool_id, Description: Numeric ID of the NAT Pool
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the NAT Pool. Object Type: string
        "start_src_range" : "", #Start of source NAT range. Object Type: string
        "end_src_range" : "", #End of source NAT range. Object Type: string
        "destination_nat_ip_address" : "", #Destination NAT IP Address. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/{nat_pool_id}"
        dict_path = {"product_name": product_name, "nat_pool_id": nat_pool_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_nat_pool_by_product_name_nat_pool_id(
        self, product_name="", nat_pool_id="", body=({})
    ):
        """
        Operation: Replace a NAT Pool
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: nat_pool_id, Description: Numeric ID of the NAT Pool
        Required Body Parameters:['name', 'start_src_range', 'end_src_range']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the NAT Pool. Object Type: string
        "start_src_range" : "", #Start of source NAT range. Object Type: string
        "end_src_range" : "", #End of source NAT range. Object Type: string
        "destination_nat_ip_address" : "", #Destination NAT IP Address. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/{nat_pool_id}"
        dict_path = {"product_name": product_name, "nat_pool_id": nat_pool_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_nat_pool_by_product_name_nat_pool_id(
        self, product_name="", nat_pool_id=""
    ):
        """
        Operation: Delete a NAT Pool
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: nat_pool_id, Description: Numeric ID of the NAT Pool
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/{nat_pool_id}"
        dict_path = {"product_name": product_name, "nat_pool_id": nat_pool_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_nat_pool_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a NAT Pool by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the NAT Pool
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_nat_pool_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of a NAT Pool by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the NAT Pool
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the NAT Pool. Object Type: string
        "start_src_range" : "", #Start of source NAT range. Object Type: string
        "end_src_range" : "", #End of source NAT range. Object Type: string
        "destination_nat_ip_address" : "", #Destination NAT IP Address. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_nat_pool_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Replace a NAT Pool by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the NAT Pool
        Required Body Parameters:['name', 'start_src_range', 'end_src_range']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the NAT Pool. Object Type: string
        "start_src_range" : "", #Start of source NAT range. Object Type: string
        "end_src_range" : "", #End of source NAT range. Object Type: string
        "destination_nat_ip_address" : "", #Destination NAT IP Address. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_nat_pool_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a NAT Pool by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the NAT Pool
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Net Destination
    def get_enforcement_profile_dur_net_destination_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Net Destinations
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_net_destination_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a Net Destination
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name', 'rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Net Destination. Object Type: string
                "invert" : False, #Invert for Mobility Access Switch and Mobility Controller Net Destination. Object Type: boolean
                "rules" : [{
             "rule_type":"", #Rule Type. Object Type: string
             "ip_address":"", #IP Address. Object Type: string
             "netmask":"", #Netmask. Object Type: string
             "end_ip_address":"", #End IP Address. Object Type: string
             "host_name":"", #Host Name or Domain. Object Type: string
             "position":0, #Position (1-220) for ArubaOS-Switch Net Destination rule. Object Type: integer
        }], #Rules for the Net Destination. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_net_destination_by_product_name_net_destination_id(
        self, product_name="", net_destination_id=""
    ):
        """
        Operation: Get a Net Destination
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: net_destination_id, Description: Numeric ID of the Net Destination
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/{net_destination_id}"
        dict_path = {
            "product_name": product_name,
            "net_destination_id": net_destination_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_net_destination_by_product_name_net_destination_id(
        self, product_name="", net_destination_id="", body=({})
    ):
        """
                Operation: Update some fields of a Net Destination
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: net_destination_id, Description: Numeric ID of the Net Destination
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Net Destination. Object Type: string
                "invert" : False, #Invert for Mobility Access Switch and Mobility Controller Net Destination. Object Type: boolean
                "rules" : [{
             "rule_type":"", #Rule Type. Object Type: string
             "ip_address":"", #IP Address. Object Type: string
             "netmask":"", #Netmask. Object Type: string
             "end_ip_address":"", #End IP Address. Object Type: string
             "host_name":"", #Host Name or Domain. Object Type: string
             "position":0, #Position (1-220) for ArubaOS-Switch Net Destination rule. Object Type: integer
        }], #Rules for the Net Destination. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/{net_destination_id}"
        dict_path = {
            "product_name": product_name,
            "net_destination_id": net_destination_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_net_destination_by_product_name_net_destination_id(
        self, product_name="", net_destination_id="", body=({})
    ):
        """
                Operation: Replace a Net Destination
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: net_destination_id, Description: Numeric ID of the Net Destination
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Net Destination. Object Type: string
                "invert" : False, #Invert for Mobility Access Switch and Mobility Controller Net Destination. Object Type: boolean
                "rules" : [{
             "rule_type":"", #Rule Type. Object Type: string
             "ip_address":"", #IP Address. Object Type: string
             "netmask":"", #Netmask. Object Type: string
             "end_ip_address":"", #End IP Address. Object Type: string
             "host_name":"", #Host Name or Domain. Object Type: string
             "position":0, #Position (1-220) for ArubaOS-Switch Net Destination rule. Object Type: integer
        }], #Rules for the Net Destination. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/{net_destination_id}"
        dict_path = {
            "product_name": product_name,
            "net_destination_id": net_destination_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_net_destination_by_product_name_net_destination_id(
        self, product_name="", net_destination_id=""
    ):
        """
        Operation: Delete a Net Destination
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: net_destination_id, Description: Numeric ID of the Net Destination
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/{net_destination_id}"
        dict_path = {
            "product_name": product_name,
            "net_destination_id": net_destination_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_net_destination_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Net Destination by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Net Destination
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_net_destination_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update some fields of a Net Destination by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Net Destination
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Net Destination. Object Type: string
                "invert" : False, #Invert for Mobility Access Switch and Mobility Controller Net Destination. Object Type: boolean
                "rules" : [{
             "rule_type":"", #Rule Type. Object Type: string
             "ip_address":"", #IP Address. Object Type: string
             "netmask":"", #Netmask. Object Type: string
             "end_ip_address":"", #End IP Address. Object Type: string
             "host_name":"", #Host Name or Domain. Object Type: string
             "position":0, #Position (1-220) for ArubaOS-Switch Net Destination rule. Object Type: integer
        }], #Rules for the Net Destination. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_net_destination_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a Net Destination by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Net Destination
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Net Destination. Object Type: string
                "invert" : False, #Invert for Mobility Access Switch and Mobility Controller Net Destination. Object Type: boolean
                "rules" : [{
             "rule_type":"", #Rule Type. Object Type: string
             "ip_address":"", #IP Address. Object Type: string
             "netmask":"", #Netmask. Object Type: string
             "end_ip_address":"", #End IP Address. Object Type: string
             "host_name":"", #Host Name or Domain. Object Type: string
             "position":0, #Position (1-220) for ArubaOS-Switch Net Destination rule. Object Type: integer
        }], #Rules for the Net Destination. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_net_destination_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Net Destination by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Net Destination
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Net Services
    def get_enforcement_profile_dur_net_service_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Net Services
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_net_service_by_product_name(
        self, product_name="", body=({})
    ):
        """
        Operation: Add a Net Service
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Net Service. Object Type: string
        "description" : "", #Description of the Net Service. Object Type: string
        "protocol" : "", #Protocol of the Net Service. Object Type: string
        "port_selection" : "", #Port Selection of the Net Service. Port is not applicable for MAS and AMC products. Object Type: string
        "port_list" : "", #Comma separated Port values of the Net Service. Object Type: string
        "port" : 0, #Port of the Net Service (1-65535). Object Type: integer
        "max_port" : 0, #Max Port of the Net Service (1-65535). Object Type: integer
        "ip_protocol_number" : 0, #IP Protocol Number of the Net Service (0-255). Object Type: integer
        "application_level_gateway" : "", #Application Level Gateway of the Net Service. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_net_service_by_product_name_net_service_id(
        self, product_name="", net_service_id=""
    ):
        """
        Operation: Get a Net Service
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: net_service_id, Description: Numeric ID of the Net Service
        """
        url_path = (
            "/enforcement-profile-dur/net-service/{product_name}/{net_service_id}"
        )
        dict_path = {"product_name": product_name, "net_service_id": net_service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_net_service_by_product_name_net_service_id(
        self, product_name="", net_service_id="", body=({})
    ):
        """
        Operation: Update some fields of a Net Service
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: net_service_id, Description: Numeric ID of the Net Service
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Net Service. Object Type: string
        "description" : "", #Description of the Net Service. Object Type: string
        "protocol" : "", #Protocol of the Net Service. Object Type: string
        "port_selection" : "", #Port Selection of the Net Service. Port is not applicable for MAS and AMC products. Object Type: string
        "port_list" : "", #Comma separated Port values of the Net Service. Object Type: string
        "port" : 0, #Port of the Net Service (1-65535). Object Type: integer
        "max_port" : 0, #Max Port of the Net Service (1-65535). Object Type: integer
        "ip_protocol_number" : 0, #IP Protocol Number of the Net Service (0-255). Object Type: integer
        "application_level_gateway" : "", #Application Level Gateway of the Net Service. Object Type: string

        }
        """
        url_path = (
            "/enforcement-profile-dur/net-service/{product_name}/{net_service_id}"
        )
        dict_path = {"product_name": product_name, "net_service_id": net_service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_net_service_by_product_name_net_service_id(
        self, product_name="", net_service_id="", body=({})
    ):
        """
        Operation: Replace a Net Service
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: net_service_id, Description: Numeric ID of the Net Service
        Required Body Parameters:['name', 'description', 'protocol']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Net Service. Object Type: string
        "description" : "", #Description of the Net Service. Object Type: string
        "protocol" : "", #Protocol of the Net Service. Object Type: string
        "port_selection" : "", #Port Selection of the Net Service. Port is not applicable for MAS and AMC products. Object Type: string
        "port_list" : "", #Comma separated Port values of the Net Service. Object Type: string
        "port" : 0, #Port of the Net Service (1-65535). Object Type: integer
        "max_port" : 0, #Max Port of the Net Service (1-65535). Object Type: integer
        "ip_protocol_number" : 0, #IP Protocol Number of the Net Service (0-255). Object Type: integer
        "application_level_gateway" : "", #Application Level Gateway of the Net Service. Object Type: string

        }
        """
        url_path = (
            "/enforcement-profile-dur/net-service/{product_name}/{net_service_id}"
        )
        dict_path = {"product_name": product_name, "net_service_id": net_service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_net_service_by_product_name_net_service_id(
        self, product_name="", net_service_id=""
    ):
        """
        Operation: Delete a Net Service
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: net_service_id, Description: Numeric ID of the Net Service
        """
        url_path = (
            "/enforcement-profile-dur/net-service/{product_name}/{net_service_id}"
        )
        dict_path = {"product_name": product_name, "net_service_id": net_service_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_net_service_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Net Service by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Net Service
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_net_service_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of a Net Service by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Net Service
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Net Service. Object Type: string
        "description" : "", #Description of the Net Service. Object Type: string
        "protocol" : "", #Protocol of the Net Service. Object Type: string
        "port_selection" : "", #Port Selection of the Net Service. Port is not applicable for MAS and AMC products. Object Type: string
        "port_list" : "", #Comma separated Port values of the Net Service. Object Type: string
        "port" : 0, #Port of the Net Service (1-65535). Object Type: integer
        "max_port" : 0, #Max Port of the Net Service (1-65535). Object Type: integer
        "ip_protocol_number" : 0, #IP Protocol Number of the Net Service (0-255). Object Type: integer
        "application_level_gateway" : "", #Application Level Gateway of the Net Service. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_net_service_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Replace a Net Service by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Net Service
        Required Body Parameters:['name', 'description', 'protocol']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Net Service. Object Type: string
        "description" : "", #Description of the Net Service. Object Type: string
        "protocol" : "", #Protocol of the Net Service. Object Type: string
        "port_selection" : "", #Port Selection of the Net Service. Port is not applicable for MAS and AMC products. Object Type: string
        "port_list" : "", #Comma separated Port values of the Net Service. Object Type: string
        "port" : 0, #Port of the Net Service (1-65535). Object Type: integer
        "max_port" : 0, #Max Port of the Net Service (1-65535). Object Type: integer
        "ip_protocol_number" : 0, #IP Protocol Number of the Net Service (0-255). Object Type: integer
        "application_level_gateway" : "", #Application Level Gateway of the Net Service. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_net_service_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Net Service by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Net Service
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Policer Profile
    def get_enforcement_profile_dur_policer_profile_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Policer Profiles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_policer_profile_by_product_name(
        self, product_name="", body=({})
    ):
        """
        Operation: Add a Policer Profile
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Policer Profile. Object Type: string
        "cbs" : 0, #CBS (Bytes) of the Policer Profile. Object Type: integer
        "cir" : 0, #CIR (Kbps) of the Policer Profile. Object Type: integer
        "ebs" : 0, #EBS (Bytes) of the Policer Profile. Object Type: integer
        "exceed_action" : "", #Exceed Action of the Policer Profile. Object Type: string
        "exceed_qos_profile" : "", #Exceed QoS Profile of the Policer Profile. Object Type: string
        "violate_action" : "", #Violate Action of the Policer Profile. Object Type: string
        "violate_qos_profile" : "", #Violate QoS Profile of the Policer Profile. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_policer_profile_by_product_name_policer_profile_id(
        self, product_name="", policer_profile_id=""
    ):
        """
        Operation: Get a Policer Profile
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: policer_profile_id, Description: Numeric ID of the Policer Profile
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/{policer_profile_id}"
        dict_path = {
            "product_name": product_name,
            "policer_profile_id": policer_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_policer_profile_by_product_name_policer_profile_id(
        self, product_name="", policer_profile_id="", body=({})
    ):
        """
        Operation: Update some fields of a Policer Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: policer_profile_id, Description: Numeric ID of the Policer Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Policer Profile. Object Type: string
        "cbs" : 0, #CBS (Bytes) of the Policer Profile. Object Type: integer
        "cir" : 0, #CIR (Kbps) of the Policer Profile. Object Type: integer
        "ebs" : 0, #EBS (Bytes) of the Policer Profile. Object Type: integer
        "exceed_action" : "", #Exceed Action of the Policer Profile. Object Type: string
        "exceed_qos_profile" : "", #Exceed QoS Profile of the Policer Profile. Object Type: string
        "violate_action" : "", #Violate Action of the Policer Profile. Object Type: string
        "violate_qos_profile" : "", #Violate QoS Profile of the Policer Profile. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/{policer_profile_id}"
        dict_path = {
            "product_name": product_name,
            "policer_profile_id": policer_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_policer_profile_by_product_name_policer_profile_id(
        self, product_name="", policer_profile_id="", body=({})
    ):
        """
        Operation: Replace a Policer Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: policer_profile_id, Description: Numeric ID of the Policer Profile
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Policer Profile. Object Type: string
        "cbs" : 0, #CBS (Bytes) of the Policer Profile. Object Type: integer
        "cir" : 0, #CIR (Kbps) of the Policer Profile. Object Type: integer
        "ebs" : 0, #EBS (Bytes) of the Policer Profile. Object Type: integer
        "exceed_action" : "", #Exceed Action of the Policer Profile. Object Type: string
        "exceed_qos_profile" : "", #Exceed QoS Profile of the Policer Profile. Object Type: string
        "violate_action" : "", #Violate Action of the Policer Profile. Object Type: string
        "violate_qos_profile" : "", #Violate QoS Profile of the Policer Profile. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/{policer_profile_id}"
        dict_path = {
            "product_name": product_name,
            "policer_profile_id": policer_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_policer_profile_by_product_name_policer_profile_id(
        self, product_name="", policer_profile_id=""
    ):
        """
        Operation: Delete a Policer Profile
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: policer_profile_id, Description: Numeric ID of the Policer Profile
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/{policer_profile_id}"
        dict_path = {
            "product_name": product_name,
            "policer_profile_id": policer_profile_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_policer_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Policer Profile by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Policer Profile
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_policer_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of a Policer Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Policer Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Policer Profile. Object Type: string
        "cbs" : 0, #CBS (Bytes) of the Policer Profile. Object Type: integer
        "cir" : 0, #CIR (Kbps) of the Policer Profile. Object Type: integer
        "ebs" : 0, #EBS (Bytes) of the Policer Profile. Object Type: integer
        "exceed_action" : "", #Exceed Action of the Policer Profile. Object Type: string
        "exceed_qos_profile" : "", #Exceed QoS Profile of the Policer Profile. Object Type: string
        "violate_action" : "", #Violate Action of the Policer Profile. Object Type: string
        "violate_qos_profile" : "", #Violate QoS Profile of the Policer Profile. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_policer_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Replace a Policer Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Policer Profile
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the Policer Profile. Object Type: string
        "cbs" : 0, #CBS (Bytes) of the Policer Profile. Object Type: integer
        "cir" : 0, #CIR (Kbps) of the Policer Profile. Object Type: integer
        "ebs" : 0, #EBS (Bytes) of the Policer Profile. Object Type: integer
        "exceed_action" : "", #Exceed Action of the Policer Profile. Object Type: string
        "exceed_qos_profile" : "", #Exceed QoS Profile of the Policer Profile. Object Type: string
        "violate_action" : "", #Violate Action of the Policer Profile. Object Type: string
        "violate_qos_profile" : "", #Violate QoS Profile of the Policer Profile. Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_policer_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Policer Profile by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Policer Profile
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Policy
    def get_enforcement_profile_dur_policy_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Policies
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_policy_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a Policy
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name', 'rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Policy. Object Type: string
                "rules" : [{
             "number":0, #Number. Object Type: integer
             "class_type":"", #Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy. Object Type: string
             "class_name":"", #Class Name. Object Type: string
             "action":"", #Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "ip_precedence":0, #IP Precedence (0-7). Object Type: integer
             "priority":0, #Priority (0-7). Object Type: integer
             "rate_limit":0, #Rate Limit in kbps for ArubaOS-Switch policy (0-10000000). Object Type: integer
             "committed_information_rate":0, #Committed Information Rate for AOS-CX policy (1-4294967295). Object Type: integer
             "committed_burst_size":0, #Committed Burst Size for AOS-CX policy (1-4294967295). Object Type: integer
             "exceed_action":"", #Exceed Action for AOS-CX policy. Object Type: string
             "priority_code_point":0, #Priority Code Point for AOS-CX policy (0-7). Object Type: integer
        }], #Rules of the Policy. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_policy_by_product_name_policy_id(
        self, product_name="", policy_id=""
    ):
        """
        Operation: Get a Policy
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: policy_id, Description: Numeric ID of the Policy
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/{policy_id}"
        dict_path = {"product_name": product_name, "policy_id": policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_policy_by_product_name_policy_id(
        self, product_name="", policy_id="", body=({})
    ):
        """
                Operation: Update a Policy
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: policy_id, Description: Numeric ID of the Policy
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Policy. Object Type: string
                "rules" : [{
             "number":0, #Number. Object Type: integer
             "class_type":"", #Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy. Object Type: string
             "class_name":"", #Class Name. Object Type: string
             "action":"", #Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "ip_precedence":0, #IP Precedence (0-7). Object Type: integer
             "priority":0, #Priority (0-7). Object Type: integer
             "rate_limit":0, #Rate Limit in kbps for ArubaOS-Switch policy (0-10000000). Object Type: integer
             "committed_information_rate":0, #Committed Information Rate for AOS-CX policy (1-4294967295). Object Type: integer
             "committed_burst_size":0, #Committed Burst Size for AOS-CX policy (1-4294967295). Object Type: integer
             "exceed_action":"", #Exceed Action for AOS-CX policy. Object Type: string
             "priority_code_point":0, #Priority Code Point for AOS-CX policy (0-7). Object Type: integer
        }], #Rules of the Policy. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/{policy_id}"
        dict_path = {"product_name": product_name, "policy_id": policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_policy_by_product_name_policy_id(
        self, product_name="", policy_id="", body=({})
    ):
        """
                Operation: Replace a Policy
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: policy_id, Description: Numeric ID of the Policy
                Required Body Parameters:['name', 'rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Policy. Object Type: string
                "rules" : [{
             "number":0, #Number. Object Type: integer
             "class_type":"", #Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy. Object Type: string
             "class_name":"", #Class Name. Object Type: string
             "action":"", #Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "ip_precedence":0, #IP Precedence (0-7). Object Type: integer
             "priority":0, #Priority (0-7). Object Type: integer
             "rate_limit":0, #Rate Limit in kbps for ArubaOS-Switch policy (0-10000000). Object Type: integer
             "committed_information_rate":0, #Committed Information Rate for AOS-CX policy (1-4294967295). Object Type: integer
             "committed_burst_size":0, #Committed Burst Size for AOS-CX policy (1-4294967295). Object Type: integer
             "exceed_action":"", #Exceed Action for AOS-CX policy. Object Type: string
             "priority_code_point":0, #Priority Code Point for AOS-CX policy (0-7). Object Type: integer
        }], #Rules of the Policy. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/{policy_id}"
        dict_path = {"product_name": product_name, "policy_id": policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_policy_by_product_name_policy_id(
        self, product_name="", policy_id=""
    ):
        """
        Operation: Delete a Policy
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: policy_id, Description: Numeric ID of the Policy
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/{policy_id}"
        dict_path = {"product_name": product_name, "policy_id": policy_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_policy_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Policy by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Policy
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_policy_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update a Policy by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Policy
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Policy. Object Type: string
                "rules" : [{
             "number":0, #Number. Object Type: integer
             "class_type":"", #Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy. Object Type: string
             "class_name":"", #Class Name. Object Type: string
             "action":"", #Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "ip_precedence":0, #IP Precedence (0-7). Object Type: integer
             "priority":0, #Priority (0-7). Object Type: integer
             "rate_limit":0, #Rate Limit in kbps for ArubaOS-Switch policy (0-10000000). Object Type: integer
             "committed_information_rate":0, #Committed Information Rate for AOS-CX policy (1-4294967295). Object Type: integer
             "committed_burst_size":0, #Committed Burst Size for AOS-CX policy (1-4294967295). Object Type: integer
             "exceed_action":"", #Exceed Action for AOS-CX policy. Object Type: string
             "priority_code_point":0, #Priority Code Point for AOS-CX policy (0-7). Object Type: integer
        }], #Rules of the Policy. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_policy_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a Policy by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Policy
                Required Body Parameters:['name', 'rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Policy. Object Type: string
                "rules" : [{
             "number":0, #Number. Object Type: integer
             "class_type":"", #Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy. Object Type: string
             "class_name":"", #Class Name. Object Type: string
             "action":"", #Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy. Object Type: string
             "dscp":0, #DSCP (0-63). Object Type: integer
             "ip_precedence":0, #IP Precedence (0-7). Object Type: integer
             "priority":0, #Priority (0-7). Object Type: integer
             "rate_limit":0, #Rate Limit in kbps for ArubaOS-Switch policy (0-10000000). Object Type: integer
             "committed_information_rate":0, #Committed Information Rate for AOS-CX policy (1-4294967295). Object Type: integer
             "committed_burst_size":0, #Committed Burst Size for AOS-CX policy (1-4294967295). Object Type: integer
             "exceed_action":"", #Exceed Action for AOS-CX policy. Object Type: string
             "priority_code_point":0, #Priority Code Point for AOS-CX policy (0-7). Object Type: integer
        }], #Rules of the Policy. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_policy_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Policy by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Policy
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage QoS Profiles
    def get_enforcement_profile_dur_qos_profile_by_product_name(self, product_name=""):
        """
        Operation: GET a list of QoS Profiles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_qos_profile_by_product_name(
        self, product_name="", body=({})
    ):
        """
        Operation: Add a QoS Profile
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the QoS Profile. Object Type: string
        "traffic_class" : 0, #Traffic Class of the QoS Profile (0-7). Object Type: integer
        "drop_precedence" : "", #Drop Precedence of the QoS Profile. Object Type: string
        "dscp" : 0, #DSCP of the QoS Profile (0-63). Object Type: integer
        "dot1p" : 0, #802.1p of the QoS Profile (0-7). Object Type: integer

        }
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_qos_profile_by_product_name_qos_profile_id(
        self, product_name="", qos_profile_id=""
    ):
        """
        Operation: Get a QoS Profile
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: qos_profile_id, Description: Numeric ID of the QoS Profile
        """
        url_path = (
            "/enforcement-profile-dur/qos-profile/{product_name}/{qos_profile_id}"
        )
        dict_path = {"product_name": product_name, "qos_profile_id": qos_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_qos_profile_by_product_name_qos_profile_id(
        self, product_name="", qos_profile_id="", body=({})
    ):
        """
        Operation: Update some fields of a QoS Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: qos_profile_id, Description: Numeric ID of the QoS Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the QoS Profile. Object Type: string
        "traffic_class" : 0, #Traffic Class of the QoS Profile (0-7). Object Type: integer
        "drop_precedence" : "", #Drop Precedence of the QoS Profile. Object Type: string
        "dscp" : 0, #DSCP of the QoS Profile (0-63). Object Type: integer
        "dot1p" : 0, #802.1p of the QoS Profile (0-7). Object Type: integer

        }
        """
        url_path = (
            "/enforcement-profile-dur/qos-profile/{product_name}/{qos_profile_id}"
        )
        dict_path = {"product_name": product_name, "qos_profile_id": qos_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_qos_profile_by_product_name_qos_profile_id(
        self, product_name="", qos_profile_id="", body=({})
    ):
        """
        Operation: Replace a QoS Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: qos_profile_id, Description: Numeric ID of the QoS Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the QoS Profile. Object Type: string
        "traffic_class" : 0, #Traffic Class of the QoS Profile (0-7). Object Type: integer
        "drop_precedence" : "", #Drop Precedence of the QoS Profile. Object Type: string
        "dscp" : 0, #DSCP of the QoS Profile (0-63). Object Type: integer
        "dot1p" : 0, #802.1p of the QoS Profile (0-7). Object Type: integer

        }
        """
        url_path = (
            "/enforcement-profile-dur/qos-profile/{product_name}/{qos_profile_id}"
        )
        dict_path = {"product_name": product_name, "qos_profile_id": qos_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_qos_profile_by_product_name_qos_profile_id(
        self, product_name="", qos_profile_id=""
    ):
        """
        Operation: Delete a QoS Profile
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: qos_profile_id, Description: Numeric ID of the QoS Profile
        """
        url_path = (
            "/enforcement-profile-dur/qos-profile/{product_name}/{qos_profile_id}"
        )
        dict_path = {"product_name": product_name, "qos_profile_id": qos_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_qos_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a QoS Profile by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the QoS Profile
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_qos_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of a QoS Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the QoS Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the QoS Profile. Object Type: string
        "traffic_class" : 0, #Traffic Class of the QoS Profile (0-7). Object Type: integer
        "drop_precedence" : "", #Drop Precedence of the QoS Profile. Object Type: string
        "dscp" : 0, #DSCP of the QoS Profile (0-63). Object Type: integer
        "dot1p" : 0, #802.1p of the QoS Profile (0-7). Object Type: integer

        }
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_qos_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Replace a QoS Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the QoS Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the QoS Profile. Object Type: string
        "traffic_class" : 0, #Traffic Class of the QoS Profile (0-7). Object Type: integer
        "drop_precedence" : "", #Drop Precedence of the QoS Profile. Object Type: string
        "dscp" : 0, #DSCP of the QoS Profile (0-63). Object Type: integer
        "dot1p" : 0, #802.1p of the QoS Profile (0-7). Object Type: integer

        }
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_qos_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a QoS Profile by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the QoS Profile
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Session Access Control List
    def get_enforcement_profile_dur_session_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Session Access Control Lists
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_session_access_control_list_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a Session Access Control List
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Session Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255). Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port (0-65535). Object Type: integer
             "tcp_max_port":0, #TCP Max Port (0-65535). Object Type: integer
             "udp_min_port":0, #UDP Min Port (0-65535). Object Type: integer
             "udp_max_port":0, #UDP Max Port (0-65535). Object Type: integer
             "action":"", #Action. Object Type: string
             "dst_nat_ip_address":"", #Destination NAT IP Address. Object Type: string
             "dst_nat_port":0, #Destination NAT Port (0-65535). Object Type: integer
             "network_name":"", #Name of Network in FQDN format. Object Type: string
             "dual_nat_pool":"", #Dual NAT Pool. Object Type: string
             "tunnel_id":0, #Tunnel ID (1-50). Object Type: integer
             "src_nat_pool":"", #Source NAT Pool. Object Type: string
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "dot1p_priority":0, #802.1p Priority (0-7). Object Type: integer
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "mirror":"", #Mirror. Object Type: string
             "position":0, #Position (1-2000). Object Type: integer
             "queue_priority":"", #Queue Priority. Object Type: string
             "time_range":"", #Time Range. Object Type: string
             "tos":0, #TOS (0-63). Object Type: integer
        }], #Rules of the Session Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_session_access_control_list_by_product_name_session_access_control_list_id(
        self, product_name="", session_access_control_list_id=""
    ):
        """
        Operation: Get a Session Access Control List
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/{session_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "session_access_control_list_id": session_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_session_access_control_list_by_product_name_session_access_control_list_id(
        self, product_name="", session_access_control_list_id="", body=({})
    ):
        """
                Operation: Update some fields of a Session Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Session Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255). Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port (0-65535). Object Type: integer
             "tcp_max_port":0, #TCP Max Port (0-65535). Object Type: integer
             "udp_min_port":0, #UDP Min Port (0-65535). Object Type: integer
             "udp_max_port":0, #UDP Max Port (0-65535). Object Type: integer
             "action":"", #Action. Object Type: string
             "dst_nat_ip_address":"", #Destination NAT IP Address. Object Type: string
             "dst_nat_port":0, #Destination NAT Port (0-65535). Object Type: integer
             "network_name":"", #Name of Network in FQDN format. Object Type: string
             "dual_nat_pool":"", #Dual NAT Pool. Object Type: string
             "tunnel_id":0, #Tunnel ID (1-50). Object Type: integer
             "src_nat_pool":"", #Source NAT Pool. Object Type: string
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "dot1p_priority":0, #802.1p Priority (0-7). Object Type: integer
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "mirror":"", #Mirror. Object Type: string
             "position":0, #Position (1-2000). Object Type: integer
             "queue_priority":"", #Queue Priority. Object Type: string
             "time_range":"", #Time Range. Object Type: string
             "tos":0, #TOS (0-63). Object Type: integer
        }], #Rules of the Session Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/{session_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "session_access_control_list_id": session_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_session_access_control_list_by_product_name_session_access_control_list_id(
        self, product_name="", session_access_control_list_id="", body=({})
    ):
        """
                Operation: Replace a Session Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Session Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255). Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port (0-65535). Object Type: integer
             "tcp_max_port":0, #TCP Max Port (0-65535). Object Type: integer
             "udp_min_port":0, #UDP Min Port (0-65535). Object Type: integer
             "udp_max_port":0, #UDP Max Port (0-65535). Object Type: integer
             "action":"", #Action. Object Type: string
             "dst_nat_ip_address":"", #Destination NAT IP Address. Object Type: string
             "dst_nat_port":0, #Destination NAT Port (0-65535). Object Type: integer
             "network_name":"", #Name of Network in FQDN format. Object Type: string
             "dual_nat_pool":"", #Dual NAT Pool. Object Type: string
             "tunnel_id":0, #Tunnel ID (1-50). Object Type: integer
             "src_nat_pool":"", #Source NAT Pool. Object Type: string
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "dot1p_priority":0, #802.1p Priority (0-7). Object Type: integer
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "mirror":"", #Mirror. Object Type: string
             "position":0, #Position (1-2000). Object Type: integer
             "queue_priority":"", #Queue Priority. Object Type: string
             "time_range":"", #Time Range. Object Type: string
             "tos":0, #TOS (0-63). Object Type: integer
        }], #Rules of the Session Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/{session_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "session_access_control_list_id": session_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_session_access_control_list_by_product_name_session_access_control_list_id(
        self, product_name="", session_access_control_list_id=""
    ):
        """
        Operation: Delete a Session Access Control List
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/{session_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "session_access_control_list_id": session_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_session_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Session Access Control List by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Session Access Control List
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_session_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update some fields of a Session Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Session Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Session Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255). Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port (0-65535). Object Type: integer
             "tcp_max_port":0, #TCP Max Port (0-65535). Object Type: integer
             "udp_min_port":0, #UDP Min Port (0-65535). Object Type: integer
             "udp_max_port":0, #UDP Max Port (0-65535). Object Type: integer
             "action":"", #Action. Object Type: string
             "dst_nat_ip_address":"", #Destination NAT IP Address. Object Type: string
             "dst_nat_port":0, #Destination NAT Port (0-65535). Object Type: integer
             "network_name":"", #Name of Network in FQDN format. Object Type: string
             "dual_nat_pool":"", #Dual NAT Pool. Object Type: string
             "tunnel_id":0, #Tunnel ID (1-50). Object Type: integer
             "src_nat_pool":"", #Source NAT Pool. Object Type: string
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "dot1p_priority":0, #802.1p Priority (0-7). Object Type: integer
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "mirror":"", #Mirror. Object Type: string
             "position":0, #Position (1-2000). Object Type: integer
             "queue_priority":"", #Queue Priority. Object Type: string
             "time_range":"", #Time Range. Object Type: string
             "tos":0, #TOS (0-63). Object Type: integer
        }], #Rules of the Session Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_session_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a Session Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Session Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Session Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number (0-255). Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port (0-65535). Object Type: integer
             "tcp_max_port":0, #TCP Max Port (0-65535). Object Type: integer
             "udp_min_port":0, #UDP Min Port (0-65535). Object Type: integer
             "udp_max_port":0, #UDP Max Port (0-65535). Object Type: integer
             "action":"", #Action. Object Type: string
             "dst_nat_ip_address":"", #Destination NAT IP Address. Object Type: string
             "dst_nat_port":0, #Destination NAT Port (0-65535). Object Type: integer
             "network_name":"", #Name of Network in FQDN format. Object Type: string
             "dual_nat_pool":"", #Dual NAT Pool. Object Type: string
             "tunnel_id":0, #Tunnel ID (1-50). Object Type: integer
             "src_nat_pool":"", #Source NAT Pool. Object Type: string
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "dot1p_priority":0, #802.1p Priority (0-7). Object Type: integer
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "mirror":"", #Mirror. Object Type: string
             "position":0, #Position (1-2000). Object Type: integer
             "queue_priority":"", #Queue Priority. Object Type: string
             "time_range":"", #Time Range. Object Type: string
             "tos":0, #TOS (0-63). Object Type: integer
        }], #Rules of the Session Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_session_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Session Access Control List by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Session Access Control List
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Stateless Access Control List
    def get_enforcement_profile_dur_stateless_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Stateless Access Control Lists
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = (
            "/enforcement-profile-dur/stateless-access-control-list/{product_name}"
        )
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_stateless_access_control_list_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a Stateless Access Control List
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Stateless Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number. Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port. Object Type: integer
             "tcp_max_port":0, #TCP Max Port. Object Type: integer
             "udp_min_port":0, #UDP Min Port. Object Type: integer
             "udp_max_port":0, #UDP Max Port. Object Type: integer
             "action":"", #Action. Object Type: string
             "redirect_type":"", #Redirect Type. Object Type: string
             "ipsec_map_based_redirect":"", #Redirect based on IPsec Map. Object Type: string
             "tunnel_id":0, #Tunnel ID. Object Type: integer
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "position":0, #Position. Object Type: integer
             "policer_profile":"", #Policer Profile. Object Type: string
             "qos_profile":"", #QoS Profile. Object Type: string
             "time_range":"", #Time Range. Object Type: string
        }], #Rules of the Stateless Access Control List. Object Type: array

                }
        """
        url_path = (
            "/enforcement-profile-dur/stateless-access-control-list/{product_name}"
        )
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_stateless_access_control_list_by_product_name_stateless_access_control_list_id(
        self, product_name="", stateless_access_control_list_id=""
    ):
        """
        Operation: Get a Stateless Access Control List
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/{stateless_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "stateless_access_control_list_id": stateless_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_stateless_access_control_list_by_product_name_stateless_access_control_list_id(
        self, product_name="", stateless_access_control_list_id="", body=({})
    ):
        """
                Operation: Update some fields of a Stateless Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Stateless Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number. Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port. Object Type: integer
             "tcp_max_port":0, #TCP Max Port. Object Type: integer
             "udp_min_port":0, #UDP Min Port. Object Type: integer
             "udp_max_port":0, #UDP Max Port. Object Type: integer
             "action":"", #Action. Object Type: string
             "redirect_type":"", #Redirect Type. Object Type: string
             "ipsec_map_based_redirect":"", #Redirect based on IPsec Map. Object Type: string
             "tunnel_id":0, #Tunnel ID. Object Type: integer
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "position":0, #Position. Object Type: integer
             "policer_profile":"", #Policer Profile. Object Type: string
             "qos_profile":"", #QoS Profile. Object Type: string
             "time_range":"", #Time Range. Object Type: string
        }], #Rules of the Stateless Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/{stateless_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "stateless_access_control_list_id": stateless_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_stateless_access_control_list_by_product_name_stateless_access_control_list_id(
        self, product_name="", stateless_access_control_list_id="", body=({})
    ):
        """
                Operation: Replace a Stateless Access Control List
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Stateless Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number. Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port. Object Type: integer
             "tcp_max_port":0, #TCP Max Port. Object Type: integer
             "udp_min_port":0, #UDP Min Port. Object Type: integer
             "udp_max_port":0, #UDP Max Port. Object Type: integer
             "action":"", #Action. Object Type: string
             "redirect_type":"", #Redirect Type. Object Type: string
             "ipsec_map_based_redirect":"", #Redirect based on IPsec Map. Object Type: string
             "tunnel_id":0, #Tunnel ID. Object Type: integer
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "position":0, #Position. Object Type: integer
             "policer_profile":"", #Policer Profile. Object Type: string
             "qos_profile":"", #QoS Profile. Object Type: string
             "time_range":"", #Time Range. Object Type: string
        }], #Rules of the Stateless Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/{stateless_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "stateless_access_control_list_id": stateless_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_stateless_access_control_list_by_product_name_stateless_access_control_list_id(
        self, product_name="", stateless_access_control_list_id=""
    ):
        """
        Operation: Delete a Stateless Access Control List
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/{stateless_access_control_list_id}"
        dict_path = {
            "product_name": product_name,
            "stateless_access_control_list_id": stateless_access_control_list_id,
        }
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_stateless_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Stateless Access Control List by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Stateless Access Control List
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_stateless_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update some fields of a Stateless Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Stateless Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Stateless Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number. Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port. Object Type: integer
             "tcp_max_port":0, #TCP Max Port. Object Type: integer
             "udp_min_port":0, #UDP Min Port. Object Type: integer
             "udp_max_port":0, #UDP Max Port. Object Type: integer
             "action":"", #Action. Object Type: string
             "redirect_type":"", #Redirect Type. Object Type: string
             "ipsec_map_based_redirect":"", #Redirect based on IPsec Map. Object Type: string
             "tunnel_id":0, #Tunnel ID. Object Type: integer
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "position":0, #Position. Object Type: integer
             "policer_profile":"", #Policer Profile. Object Type: string
             "qos_profile":"", #QoS Profile. Object Type: string
             "time_range":"", #Time Range. Object Type: string
        }], #Rules of the Stateless Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_stateless_access_control_list_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a Stateless Access Control List by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Stateless Access Control List
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Stateless Access Control List. Object Type: string
                "rules" : [{
             "src_traffic_match":"", #Source Traffic Match. Object Type: string
             "src_alias":"", #Source Alias. Object Type: string
             "src_ip_address":"", #Source IP Address. Object Type: string
             "src_netmask":"", #Source Net Mask. Object Type: string
             "dst_traffic_match":"", #Destination Traffic Match. Object Type: string
             "dst_alias":"", #Destination Alias. Object Type: string
             "dst_ip_address":"", #Destination IP Address. Object Type: string
             "dst_netmask":"", #Destination Net Mask. Object Type: string
             "service_type":"", #Service Type. Object Type: string
             "protocol_number":0, #Protocol Number. Object Type: integer
             "service":"", #Service. Object Type: string
             "tcp_min_port":0, #TCP Min Port. Object Type: integer
             "tcp_max_port":0, #TCP Max Port. Object Type: integer
             "udp_min_port":0, #UDP Min Port. Object Type: integer
             "udp_max_port":0, #UDP Max Port. Object Type: integer
             "action":"", #Action. Object Type: string
             "redirect_type":"", #Redirect Type. Object Type: string
             "ipsec_map_based_redirect":"", #Redirect based on IPsec Map. Object Type: string
             "tunnel_id":0, #Tunnel ID. Object Type: integer
             "deny_list_user_if_acl_applied":"", #Deny List User if ACL gets applied. Object Type: string
             "log_if_acl_applied":"", #Log if ACL gets applied. Object Type: string
             "position":0, #Position. Object Type: integer
             "policer_profile":"", #Policer Profile. Object Type: string
             "qos_profile":"", #QoS Profile. Object Type: string
             "time_range":"", #Time Range. Object Type: string
        }], #Rules of the Stateless Access Control List. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_stateless_access_control_list_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Stateless Access Control List by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Stateless Access Control List
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage Time Range
    def get_enforcement_profile_dur_time_range_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Time Ranges
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_time_range_by_product_name(
        self, product_name="", body=({})
    ):
        """
                Operation: Add a Time Range
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Required Body Parameters:['name', 'rules']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Time Range. Object Type: string
                "type" : "", #Type of the Time Range. Object Type: string
                "rules" : [{
             "start_day_or_date":"", #Start day for Periodic Time Range or Start date for Absolute Time Range. Object Type: string
             "end_day_or_date":"", #End Day for Periodic Time Range or End date for Absolute Time Range. Object Type: string
             "start_time":"", #Start time. Object Type: string
             "end_time":"", #End Time. Object Type: string
        }], #Rules of the Time Range. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_time_range_by_product_name_time_range_id(
        self, product_name="", time_range_id=""
    ):
        """
        Operation: Get a Time Range
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: time_range_id, Description: Numeric ID of the Time Range
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/{time_range_id}"
        dict_path = {"product_name": product_name, "time_range_id": time_range_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_time_range_by_product_name_time_range_id(
        self, product_name="", time_range_id="", body=({})
    ):
        """
                Operation: Update some fields of a Time Range
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: time_range_id, Description: Numeric ID of the Time Range
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Time Range. Object Type: string
                "type" : "", #Type of the Time Range. Object Type: string
                "rules" : [{
             "start_day_or_date":"", #Start day for Periodic Time Range or Start date for Absolute Time Range. Object Type: string
             "end_day_or_date":"", #End Day for Periodic Time Range or End date for Absolute Time Range. Object Type: string
             "start_time":"", #Start time. Object Type: string
             "end_time":"", #End Time. Object Type: string
        }], #Rules of the Time Range. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/{time_range_id}"
        dict_path = {"product_name": product_name, "time_range_id": time_range_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_time_range_by_product_name_time_range_id(
        self, product_name="", time_range_id="", body=({})
    ):
        """
                Operation: Replace a Time Range
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: time_range_id, Description: Numeric ID of the Time Range
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Time Range. Object Type: string
                "type" : "", #Type of the Time Range. Object Type: string
                "rules" : [{
             "start_day_or_date":"", #Start day for Periodic Time Range or Start date for Absolute Time Range. Object Type: string
             "end_day_or_date":"", #End Day for Periodic Time Range or End date for Absolute Time Range. Object Type: string
             "start_time":"", #Start time. Object Type: string
             "end_time":"", #End Time. Object Type: string
        }], #Rules of the Time Range. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/{time_range_id}"
        dict_path = {"product_name": product_name, "time_range_id": time_range_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_time_range_by_product_name_time_range_id(
        self, product_name="", time_range_id=""
    ):
        """
        Operation: Delete a Time Range
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: time_range_id, Description: Numeric ID of the Time Range
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/{time_range_id}"
        dict_path = {"product_name": product_name, "time_range_id": time_range_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_time_range_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a Time Range by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Time Range
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_time_range_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Update some fields of a Time Range by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Time Range
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Time Range. Object Type: string
                "type" : "", #Type of the Time Range. Object Type: string
                "rules" : [{
             "start_day_or_date":"", #Start day for Periodic Time Range or Start date for Absolute Time Range. Object Type: string
             "end_day_or_date":"", #End Day for Periodic Time Range or End date for Absolute Time Range. Object Type: string
             "start_time":"", #Start time. Object Type: string
             "end_time":"", #End Time. Object Type: string
        }], #Rules of the Time Range. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_time_range_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
                Operation: Replace a Time Range by name
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Parameter Type: path, Name: product_name, Description: Product Name
                Parameter Type: path, Name: name, Description: Name of the Time Range
                Required Body Parameters: None listed
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):

                body={
                "name" : "", #Name of the Time Range. Object Type: string
                "type" : "", #Type of the Time Range. Object Type: string
                "rules" : [{
             "start_day_or_date":"", #Start day for Periodic Time Range or Start date for Absolute Time Range. Object Type: string
             "end_day_or_date":"", #End Day for Periodic Time Range or End date for Absolute Time Range. Object Type: string
             "start_time":"", #Start time. Object Type: string
             "end_time":"", #End Time. Object Type: string
        }], #Rules of the Time Range. Object Type: array

                }
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_time_range_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a Time Range by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the Time Range
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage VoIP Profile
    def get_enforcement_profile_dur_voip_profile_by_product_name(self, product_name=""):
        """
        Operation: GET a list of VoIP Profiles
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        """
        url_path = "/enforcement-profile-dur/voip-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_enforcement_profile_dur_voip_profile_by_product_name(
        self, product_name="", body=({})
    ):
        """
        Operation: Add a VoIP Profile
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Required Body Parameters:['name']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the VoIP Profile. Object Type: string
        "voip_vlan" : 0, #VoIP VLAN of the VoIP Profile (1-4094). Object Type: integer
        "dscp" : 0, #DSCP of the VoIP Profile (0-63). Object Type: integer
        "dot1p" : "", #802.1p of the VoIP Profile (0-7). Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/voip-profile/{product_name}"
        dict_path = {"product_name": product_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_enforcement_profile_dur_voip_profile_by_product_name_voip_profile_id(
        self, product_name="", voip_profile_id=""
    ):
        """
        Operation: Get a VoIP Profile
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: voip_profile_id, Description: Numeric ID of the VoIP Profile
        """
        url_path = (
            "/enforcement-profile-dur/voip-profile/{product_name}/{voip_profile_id}"
        )
        dict_path = {"product_name": product_name, "voip_profile_id": voip_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_voip_profile_by_product_name_voip_profile_id(
        self, product_name="", voip_profile_id="", body=({})
    ):
        """
        Operation: Update some fields of a VoIP Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: voip_profile_id, Description: Numeric ID of the VoIP Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the VoIP Profile. Object Type: string
        "voip_vlan" : 0, #VoIP VLAN of the VoIP Profile (1-4094). Object Type: integer
        "dscp" : 0, #DSCP of the VoIP Profile (0-63). Object Type: integer
        "dot1p" : "", #802.1p of the VoIP Profile (0-7). Object Type: string

        }
        """
        url_path = (
            "/enforcement-profile-dur/voip-profile/{product_name}/{voip_profile_id}"
        )
        dict_path = {"product_name": product_name, "voip_profile_id": voip_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_voip_profile_by_product_name_voip_profile_id(
        self, product_name="", voip_profile_id="", body=({})
    ):
        """
        Operation: Replace a VoIP Profile
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: voip_profile_id, Description: Numeric ID of the VoIP Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the VoIP Profile. Object Type: string
        "voip_vlan" : 0, #VoIP VLAN of the VoIP Profile (1-4094). Object Type: integer
        "dscp" : 0, #DSCP of the VoIP Profile (0-63). Object Type: integer
        "dot1p" : "", #802.1p of the VoIP Profile (0-7). Object Type: string

        }
        """
        url_path = (
            "/enforcement-profile-dur/voip-profile/{product_name}/{voip_profile_id}"
        )
        dict_path = {"product_name": product_name, "voip_profile_id": voip_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_voip_profile_by_product_name_voip_profile_id(
        self, product_name="", voip_profile_id=""
    ):
        """
        Operation: Delete a VoIP Profile
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: voip_profile_id, Description: Numeric ID of the VoIP Profile
        """
        url_path = (
            "/enforcement-profile-dur/voip-profile/{product_name}/{voip_profile_id}"
        )
        dict_path = {"product_name": product_name, "voip_profile_id": voip_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_dur_voip_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Get a VoIP Profile by name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the VoIP Profile
        """
        url_path = "/enforcement-profile-dur/voip-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_dur_voip_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Update some fields of a VoIP Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the VoIP Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the VoIP Profile. Object Type: string
        "voip_vlan" : 0, #VoIP VLAN of the VoIP Profile (1-4094). Object Type: integer
        "dscp" : 0, #DSCP of the VoIP Profile (0-63). Object Type: integer
        "dot1p" : "", #802.1p of the VoIP Profile (0-7). Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/voip-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_enforcement_profile_dur_voip_profile_by_product_name_name_name(
        self, product_name="", name="", body=({})
    ):
        """
        Operation: Replace a VoIP Profile by name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the VoIP Profile
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "name" : "", #Name of the VoIP Profile. Object Type: string
        "voip_vlan" : 0, #VoIP VLAN of the VoIP Profile (1-4094). Object Type: integer
        "dscp" : 0, #DSCP of the VoIP Profile (0-63). Object Type: integer
        "dot1p" : "", #802.1p of the VoIP Profile (0-7). Object Type: string

        }
        """
        url_path = "/enforcement-profile-dur/voip-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_enforcement_profile_dur_voip_profile_by_product_name_name_name(
        self, product_name="", name=""
    ):
        """
        Operation: Delete a VoIP Profile by name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: product_name, Description: Product Name
        Parameter Type: path, Name: name, Description: Name of the VoIP Profile
        """
        url_path = "/enforcement-profile-dur/voip-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
