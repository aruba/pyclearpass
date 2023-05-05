from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_enforcementprofile_v1.py


class ApiEnforcementProfiles(ClearPassAPILogin):
    # Function Section Name:CaptivePortalProfile
    # Function Section Description: Manage Captive Portal Profile

    def get_enforcement_profile_dur_captive_portal_profile_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Captive Portal Profiles
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- CaptivePortalProfilePost {name (string): Name of the Captive Portal Profile,url (string): URL for ArubaOS-Switch and AOS-CX Captive Portal Profile,url_hashkey (string, optional): URL HashKey for ArubaOS-Switch Captive Portal Profile,aos_attributes (AosAttributes, optional): Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile}AosAttributes {server_group (string, optional): Server Group,default_role (string, optional): Default Role,default_guest_role (string, optional): Default Guest Role,redirect_pause (integer, optional): Redirect Pause (0-60 sec),user_login (string, optional) = ['Yes' or 'No']: User Login,guest_login (string, optional) = ['Yes' or 'No']: Guest Login,logout_popup_window (string, optional) = ['Yes' or 'No']: Logout Popup Window,use_http_for_auth (string, optional) = ['Yes' or 'No']: Use HTTP for Authentication,logon_wait_min_delay (integer, optional): Logon Wait Minimum Delay (1-10 sec),logon_wait_max_delay (integer, optional): Logon Wait Maximum Delay (1-10 sec),logon_wait_cpu_util_threshold (integer, optional): Logon Wait CPU Utilization Threshold (1-100 %),max_auth_failures (integer, optional): Max Authentication Failures (0-10),show_fqdn (string, optional) = ['Yes' or 'No']: Show FQDN,use_chap (string, optional) = ['Yes' or 'No']: Use CHAP (Non-standard),login_page (string, optional): Login Page,welcome_page (string, optional): Welcome Page,show_welcome_page (string, optional) = ['Yes' or 'No']: Show Welcome Page,add_switch_ip_add_in_redirection_url (string, optional) = ['Yes' or 'No']: Adding Switch IP Address in Redirection URL,allow_one_active_user_session (string, optional) = ['Yes' or 'No']: Allow only one Active User Session,show_acceptable_use_policy_page (string, optional) = ['Yes' or 'No']: Show the Acceptable Use Policy Page,add_ip_interface_in_redirection_url (string, optional): Add an IP Interface in the Redirection URL,add_user_vlan_in_redirection_url (string, optional) = ['Yes' or 'No']: Add User VLAN in Redirection URL,allowed_net_destinations (array[string], optional): Allowlist Net Destinations}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "url": "",
          "url_hashkey": "",
          "aos_attributes": {
            "server_group": "",
            "default_role": "",
            "default_guest_role": "",
            "redirect_pause": 0,
            "user_login": "",
            "guest_login": "",
            "logout_popup_window": "",
            "use_http_for_auth": "",
            "logon_wait_min_delay": 0,
            "logon_wait_max_delay": 0,
            "logon_wait_cpu_util_threshold": 0,
            "max_auth_failures": 0,
            "show_fqdn": "",
            "use_chap": "",
            "login_page": "",
            "welcome_page": "",
            "show_welcome_page": "",
            "add_switch_ip_add_in_redirection_url": "",
            "allow_one_active_user_session": "",
            "show_acceptable_use_policy_page": "",
            "add_ip_interface_in_redirection_url": "",
            "add_user_vlan_in_redirection_url": "",
            "allowed_net_destinations": [
              ""
            ]
          }
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
                Required Body Parameters (body description)- CaptivePortalProfileUpdate {name (string, optional): Name of the Captive Portal Profile,url (string, optional): URL for ArubaOS-Switch and AOS-CX Captive Portal Profile,url_hashkey (string, optional): URL HashKey for ArubaOS-Switch Captive Portal Profile,aos_attributes (AosAttributes, optional): Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile}AosAttributes {server_group (string, optional): Server Group,default_role (string, optional): Default Role,default_guest_role (string, optional): Default Guest Role,redirect_pause (integer, optional): Redirect Pause (0-60 sec),user_login (string, optional) = ['Yes' or 'No']: User Login,guest_login (string, optional) = ['Yes' or 'No']: Guest Login,logout_popup_window (string, optional) = ['Yes' or 'No']: Logout Popup Window,use_http_for_auth (string, optional) = ['Yes' or 'No']: Use HTTP for Authentication,logon_wait_min_delay (integer, optional): Logon Wait Minimum Delay (1-10 sec),logon_wait_max_delay (integer, optional): Logon Wait Maximum Delay (1-10 sec),logon_wait_cpu_util_threshold (integer, optional): Logon Wait CPU Utilization Threshold (1-100 %),max_auth_failures (integer, optional): Max Authentication Failures (0-10),show_fqdn (string, optional) = ['Yes' or 'No']: Show FQDN,use_chap (string, optional) = ['Yes' or 'No']: Use CHAP (Non-standard),login_page (string, optional): Login Page,welcome_page (string, optional): Welcome Page,show_welcome_page (string, optional) = ['Yes' or 'No']: Show Welcome Page,add_switch_ip_add_in_redirection_url (string, optional) = ['Yes' or 'No']: Adding Switch IP Address in Redirection URL,allow_one_active_user_session (string, optional) = ['Yes' or 'No']: Allow only one Active User Session,show_acceptable_use_policy_page (string, optional) = ['Yes' or 'No']: Show the Acceptable Use Policy Page,add_ip_interface_in_redirection_url (string, optional): Add an IP Interface in the Redirection URL,add_user_vlan_in_redirection_url (string, optional) = ['Yes' or 'No']: Add User VLAN in Redirection URL,allowed_net_destinations (array[string], optional): Allowlist Net Destinations}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "url": "",
          "url_hashkey": "",
          "aos_attributes": {
            "server_group": "",
            "default_role": "",
            "default_guest_role": "",
            "redirect_pause": 0,
            "user_login": "",
            "guest_login": "",
            "logout_popup_window": "",
            "use_http_for_auth": "",
            "logon_wait_min_delay": 0,
            "logon_wait_max_delay": 0,
            "logon_wait_cpu_util_threshold": 0,
            "max_auth_failures": 0,
            "show_fqdn": "",
            "use_chap": "",
            "login_page": "",
            "welcome_page": "",
            "show_welcome_page": "",
            "add_switch_ip_add_in_redirection_url": "",
            "allow_one_active_user_session": "",
            "show_acceptable_use_policy_page": "",
            "add_ip_interface_in_redirection_url": "",
            "add_user_vlan_in_redirection_url": "",
            "allowed_net_destinations": [
              ""
            ]
          }
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
                Required Body Parameters (body description)- CaptivePortalProfileReplace {name (string, optional): Name of the Captive Portal Profile,url (string, optional): URL for ArubaOS-Switch and AOS-CX Captive Portal Profile,url_hashkey (string, optional): URL HashKey for ArubaOS-Switch Captive Portal Profile,aos_attributes (AosAttributes, optional): Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile}AosAttributes {server_group (string, optional): Server Group,default_role (string, optional): Default Role,default_guest_role (string, optional): Default Guest Role,redirect_pause (integer, optional): Redirect Pause (0-60 sec),user_login (string, optional) = ['Yes' or 'No']: User Login,guest_login (string, optional) = ['Yes' or 'No']: Guest Login,logout_popup_window (string, optional) = ['Yes' or 'No']: Logout Popup Window,use_http_for_auth (string, optional) = ['Yes' or 'No']: Use HTTP for Authentication,logon_wait_min_delay (integer, optional): Logon Wait Minimum Delay (1-10 sec),logon_wait_max_delay (integer, optional): Logon Wait Maximum Delay (1-10 sec),logon_wait_cpu_util_threshold (integer, optional): Logon Wait CPU Utilization Threshold (1-100 %),max_auth_failures (integer, optional): Max Authentication Failures (0-10),show_fqdn (string, optional) = ['Yes' or 'No']: Show FQDN,use_chap (string, optional) = ['Yes' or 'No']: Use CHAP (Non-standard),login_page (string, optional): Login Page,welcome_page (string, optional): Welcome Page,show_welcome_page (string, optional) = ['Yes' or 'No']: Show Welcome Page,add_switch_ip_add_in_redirection_url (string, optional) = ['Yes' or 'No']: Adding Switch IP Address in Redirection URL,allow_one_active_user_session (string, optional) = ['Yes' or 'No']: Allow only one Active User Session,show_acceptable_use_policy_page (string, optional) = ['Yes' or 'No']: Show the Acceptable Use Policy Page,add_ip_interface_in_redirection_url (string, optional): Add an IP Interface in the Redirection URL,add_user_vlan_in_redirection_url (string, optional) = ['Yes' or 'No']: Add User VLAN in Redirection URL,allowed_net_destinations (array[string], optional): Allowlist Net Destinations}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "url": "",
          "url_hashkey": "",
          "aos_attributes": {
            "server_group": "",
            "default_role": "",
            "default_guest_role": "",
            "redirect_pause": 0,
            "user_login": "",
            "guest_login": "",
            "logout_popup_window": "",
            "use_http_for_auth": "",
            "logon_wait_min_delay": 0,
            "logon_wait_max_delay": 0,
            "logon_wait_cpu_util_threshold": 0,
            "max_auth_failures": 0,
            "show_fqdn": "",
            "use_chap": "",
            "login_page": "",
            "welcome_page": "",
            "show_welcome_page": "",
            "add_switch_ip_add_in_redirection_url": "",
            "allow_one_active_user_session": "",
            "show_acceptable_use_policy_page": "",
            "add_ip_interface_in_redirection_url": "",
            "add_user_vlan_in_redirection_url": "",
            "allowed_net_destinations": [
              ""
            ]
          }
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: captive_portal_profile_id, Description: Numeric ID of the Captive Portal Profile
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Captive Portal Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Captive Portal Profile
                Required Body Parameters (body description)- CaptivePortalProfileUpdate {name (string, optional): Name of the Captive Portal Profile,url (string, optional): URL for ArubaOS-Switch and AOS-CX Captive Portal Profile,url_hashkey (string, optional): URL HashKey for ArubaOS-Switch Captive Portal Profile,aos_attributes (AosAttributes, optional): Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile}AosAttributes {server_group (string, optional): Server Group,default_role (string, optional): Default Role,default_guest_role (string, optional): Default Guest Role,redirect_pause (integer, optional): Redirect Pause (0-60 sec),user_login (string, optional) = ['Yes' or 'No']: User Login,guest_login (string, optional) = ['Yes' or 'No']: Guest Login,logout_popup_window (string, optional) = ['Yes' or 'No']: Logout Popup Window,use_http_for_auth (string, optional) = ['Yes' or 'No']: Use HTTP for Authentication,logon_wait_min_delay (integer, optional): Logon Wait Minimum Delay (1-10 sec),logon_wait_max_delay (integer, optional): Logon Wait Maximum Delay (1-10 sec),logon_wait_cpu_util_threshold (integer, optional): Logon Wait CPU Utilization Threshold (1-100 %),max_auth_failures (integer, optional): Max Authentication Failures (0-10),show_fqdn (string, optional) = ['Yes' or 'No']: Show FQDN,use_chap (string, optional) = ['Yes' or 'No']: Use CHAP (Non-standard),login_page (string, optional): Login Page,welcome_page (string, optional): Welcome Page,show_welcome_page (string, optional) = ['Yes' or 'No']: Show Welcome Page,add_switch_ip_add_in_redirection_url (string, optional) = ['Yes' or 'No']: Adding Switch IP Address in Redirection URL,allow_one_active_user_session (string, optional) = ['Yes' or 'No']: Allow only one Active User Session,show_acceptable_use_policy_page (string, optional) = ['Yes' or 'No']: Show the Acceptable Use Policy Page,add_ip_interface_in_redirection_url (string, optional): Add an IP Interface in the Redirection URL,add_user_vlan_in_redirection_url (string, optional) = ['Yes' or 'No']: Add User VLAN in Redirection URL,allowed_net_destinations (array[string], optional): Allowlist Net Destinations}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "url": "",
          "url_hashkey": "",
          "aos_attributes": {
            "server_group": "",
            "default_role": "",
            "default_guest_role": "",
            "redirect_pause": 0,
            "user_login": "",
            "guest_login": "",
            "logout_popup_window": "",
            "use_http_for_auth": "",
            "logon_wait_min_delay": 0,
            "logon_wait_max_delay": 0,
            "logon_wait_cpu_util_threshold": 0,
            "max_auth_failures": 0,
            "show_fqdn": "",
            "use_chap": "",
            "login_page": "",
            "welcome_page": "",
            "show_welcome_page": "",
            "add_switch_ip_add_in_redirection_url": "",
            "allow_one_active_user_session": "",
            "show_acceptable_use_policy_page": "",
            "add_ip_interface_in_redirection_url": "",
            "add_user_vlan_in_redirection_url": "",
            "allowed_net_destinations": [
              ""
            ]
          }
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Captive Portal Profile
                Required Body Parameters (body description)- CaptivePortalProfileReplace {name (string, optional): Name of the Captive Portal Profile,url (string, optional): URL for ArubaOS-Switch and AOS-CX Captive Portal Profile,url_hashkey (string, optional): URL HashKey for ArubaOS-Switch Captive Portal Profile,aos_attributes (AosAttributes, optional): Attributes for Mobility Access Switch and Mobility Controller Captive Portal Profile}AosAttributes {server_group (string, optional): Server Group,default_role (string, optional): Default Role,default_guest_role (string, optional): Default Guest Role,redirect_pause (integer, optional): Redirect Pause (0-60 sec),user_login (string, optional) = ['Yes' or 'No']: User Login,guest_login (string, optional) = ['Yes' or 'No']: Guest Login,logout_popup_window (string, optional) = ['Yes' or 'No']: Logout Popup Window,use_http_for_auth (string, optional) = ['Yes' or 'No']: Use HTTP for Authentication,logon_wait_min_delay (integer, optional): Logon Wait Minimum Delay (1-10 sec),logon_wait_max_delay (integer, optional): Logon Wait Maximum Delay (1-10 sec),logon_wait_cpu_util_threshold (integer, optional): Logon Wait CPU Utilization Threshold (1-100 %),max_auth_failures (integer, optional): Max Authentication Failures (0-10),show_fqdn (string, optional) = ['Yes' or 'No']: Show FQDN,use_chap (string, optional) = ['Yes' or 'No']: Use CHAP (Non-standard),login_page (string, optional): Login Page,welcome_page (string, optional): Welcome Page,show_welcome_page (string, optional) = ['Yes' or 'No']: Show Welcome Page,add_switch_ip_add_in_redirection_url (string, optional) = ['Yes' or 'No']: Adding Switch IP Address in Redirection URL,allow_one_active_user_session (string, optional) = ['Yes' or 'No']: Allow only one Active User Session,show_acceptable_use_policy_page (string, optional) = ['Yes' or 'No']: Show the Acceptable Use Policy Page,add_ip_interface_in_redirection_url (string, optional): Add an IP Interface in the Redirection URL,add_user_vlan_in_redirection_url (string, optional) = ['Yes' or 'No']: Add User VLAN in Redirection URL,allowed_net_destinations (array[string], optional): Allowlist Net Destinations}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "url": "",
          "url_hashkey": "",
          "aos_attributes": {
            "server_group": "",
            "default_role": "",
            "default_guest_role": "",
            "redirect_pause": 0,
            "user_login": "",
            "guest_login": "",
            "logout_popup_window": "",
            "use_http_for_auth": "",
            "logon_wait_min_delay": 0,
            "logon_wait_max_delay": 0,
            "logon_wait_cpu_util_threshold": 0,
            "max_auth_failures": 0,
            "show_fqdn": "",
            "use_chap": "",
            "login_page": "",
            "welcome_page": "",
            "show_welcome_page": "",
            "add_switch_ip_add_in_redirection_url": "",
            "allow_one_active_user_session": "",
            "show_acceptable_use_policy_page": "",
            "add_ip_interface_in_redirection_url": "",
            "add_user_vlan_in_redirection_url": "",
            "allowed_net_destinations": [
              ""
            ]
          }
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Captive Portal Profile
        """
        url_path = (
            "/enforcement-profile-dur/captive-portal-profile/{product_name}/name/{name}"
        )
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:DURClass
    # Function Section Description: Manage DUR Class

    def get_enforcement_profile_dur_dur_class_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Policies
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- DURClassPost {name (string): Name of the DUR Class,traffic (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Traffic of the DUR Class,hpe_rules (array[HPERulesPost]): Rules for ArubaOS-Switch DUR Class,aos_cx_rules (array[AosCxRulesPost]): Rules for AOS-CX DUR Class}HPERulesPost {number (integer): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,traffic_match_type (string, optional) = ['netsource' or 'protocol']: Traffic Match Type,net_source (string, optional) = ['any']: Net Source for netsource traffic_match_type,net_destination (string, optional): Net Destination for netsource traffic_match_type,net_service (string, optional): Net Service for netsource traffic_match_type,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'vrrp' or 'pim' or 'ospf' or 'ipv6_in_ip' or 'ip_in_ip' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'gre' or 'esp' or 'ah' or '255']: Protocol for protocol traffic_match_type,source (string, optional) = ['any']: Source for protocol traffic_match_type,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Source Port for protocol traffic_match_type,source_port_value (string, optional): Source Port Value for protocol traffic_match_type,protocol_number (integer): Protocol Number (0-255) for 255 protocol,destination (string, optional) = ['any' or 'host' or 'ipsubnet']: Destnation for protocol traffic_match_type,destination_value (string, optional): Destination Value for protocol traffic_match_type,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Destination Port for protocol traffic_match_type,destination_port_value (string, optional): Destination Port Value for protocol traffic_match_type,ip_dscp (integer, optional): IP DSCP (0-63) for protocol traffic_match_type,vlan_id (integer, optional): VLAN ID (1-4094) for protocol traffic_match_type,ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence for protocol traffic_match_type,ip_service_type (string, optional) = ['normal' or 'max reliability' or 'max throughput' or 'minimize delay']: IP Type of Service for protocol traffic_match_type,established (boolean, optional): Established for tcp protocol,fin (boolean, optional): Fin for tcp protocol,rst (boolean, optional): Rst for tcp protocol,syn (boolean, optional): Syn for tcp protocol}AosCxRulesPost {number (integer, optional): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'pim' or 'ospf' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'icmpv6' or 'gre' or 'esp' or 'ah' or 'number' or 'any']: Protocol,protocol_number (integer): Protocol Number for number protocol,source (string, optional) = ['any' or 'ip']: Source,source_ip_address (string): Source IP Address for ip source,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Source Port,source_port_value (string): Source Port Value,destination (string, optional) = ['any' or 'ip']: Destination,destination_ip_address (string): Destination IP Address for ip destination,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Destination Port,destination_port_value (string): Destination Port Value,dscp (integer, optional): DSCP (0-63),vlan_id (integer, optional): VLAN ID (1-4094),ecn (integer, optional): ECN (0-3),ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence,service_type (integer, optional): Type of Service (0-31),ttl (integer, optional): Time to Live (0-255),fragment (boolean, optional): Fragment,count_packet (boolean, optional): Count Packet,cwr (boolean, optional): cwr for tcp protocol,ece (boolean, optional): ece for tcp protocol,urg (boolean, optional): urg for tcp protocol,ack (boolean, optional): ack for tcp protocol,psh (boolean, optional): psh for tcp protocol,rst (boolean, optional): rst for tcp protocol,syn (boolean, optional): syn for tcp protocol,fin (boolean, optional): fin for tcp protocol,established (boolean, optional): established for tcp protocol,icmp_type (string, optional) = ['echo' or 'echo-reply' or 'number']: ICMP Type for icmp protocol,icmp_type_value (integer): ICMP Type Value (0-255) for number icmp_type,icmp_code (integer, optional): ICMP Code (0-255) for icmp protocol}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic": "",
          "hpe_rules": [
            {
              "number": 0,
              "packet_match": "",
              "traffic_match_type": "",
              "net_source": "",
              "net_destination": "",
              "net_service": "",
              "protocol": "",
              "source": "",
              "source_port": "",
              "source_port_value": "",
              "protocol_number": 0,
              "destination": "",
              "destination_value": "",
              "destination_port": "",
              "destination_port_value": "",
              "ip_dscp": 0,
              "vlan_id": 0,
              "ip_precedence": "",
              "ip_service_type": "",
              "established": false,
              "fin": false,
              "rst": false,
              "syn": false
            }
          ],
          "aos_cx_rules": [
            {
              "number": 0,
              "packet_match": "",
              "protocol": "",
              "protocol_number": 0,
              "source": "",
              "source_ip_address": "",
              "source_port": "",
              "source_port_value": "",
              "destination": "",
              "destination_ip_address": "",
              "destination_port": "",
              "destination_port_value": "",
              "dscp": 0,
              "vlan_id": 0,
              "ecn": 0,
              "ip_precedence": "",
              "service_type": 0,
              "ttl": 0,
              "fragment": false,
              "count_packet": false,
              "cwr": false,
              "ece": false,
              "urg": false,
              "ack": false,
              "psh": false,
              "rst": false,
              "syn": false,
              "fin": false,
              "established": false,
              "icmp_type": "",
              "icmp_type_value": 0,
              "icmp_code": 0
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: dur_class_id, Description: Numeric ID of the DURClass
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: dur_class_id, Description: Numeric ID of the DURClass
                Required Body Parameters (body description)- DURClassUpdate {name (string, optional): Name of the DUR Class,traffic (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Traffic of the DUR Class,hpe_rules (array[HPERulesPost], optional): Rules for ArubaOS-Switch DUR Class,aos_cx_rules (array[AosCxRulesPost], optional): Rules for AOS-CX DUR Class}HPERulesPost {number (integer): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,traffic_match_type (string, optional) = ['netsource' or 'protocol']: Traffic Match Type,net_source (string, optional) = ['any']: Net Source for netsource traffic_match_type,net_destination (string, optional): Net Destination for netsource traffic_match_type,net_service (string, optional): Net Service for netsource traffic_match_type,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'vrrp' or 'pim' or 'ospf' or 'ipv6_in_ip' or 'ip_in_ip' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'gre' or 'esp' or 'ah' or '255']: Protocol for protocol traffic_match_type,source (string, optional) = ['any']: Source for protocol traffic_match_type,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Source Port for protocol traffic_match_type,source_port_value (string, optional): Source Port Value for protocol traffic_match_type,protocol_number (integer): Protocol Number (0-255) for 255 protocol,destination (string, optional) = ['any' or 'host' or 'ipsubnet']: Destnation for protocol traffic_match_type,destination_value (string, optional): Destination Value for protocol traffic_match_type,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Destination Port for protocol traffic_match_type,destination_port_value (string, optional): Destination Port Value for protocol traffic_match_type,ip_dscp (integer, optional): IP DSCP (0-63) for protocol traffic_match_type,vlan_id (integer, optional): VLAN ID (1-4094) for protocol traffic_match_type,ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence for protocol traffic_match_type,ip_service_type (string, optional) = ['normal' or 'max reliability' or 'max throughput' or 'minimize delay']: IP Type of Service for protocol traffic_match_type,established (boolean, optional): Established for tcp protocol,fin (boolean, optional): Fin for tcp protocol,rst (boolean, optional): Rst for tcp protocol,syn (boolean, optional): Syn for tcp protocol}AosCxRulesPost {number (integer, optional): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'pim' or 'ospf' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'icmpv6' or 'gre' or 'esp' or 'ah' or 'number' or 'any']: Protocol,protocol_number (integer): Protocol Number for number protocol,source (string, optional) = ['any' or 'ip']: Source,source_ip_address (string): Source IP Address for ip source,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Source Port,source_port_value (string): Source Port Value,destination (string, optional) = ['any' or 'ip']: Destination,destination_ip_address (string): Destination IP Address for ip destination,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Destination Port,destination_port_value (string): Destination Port Value,dscp (integer, optional): DSCP (0-63),vlan_id (integer, optional): VLAN ID (1-4094),ecn (integer, optional): ECN (0-3),ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence,service_type (integer, optional): Type of Service (0-31),ttl (integer, optional): Time to Live (0-255),fragment (boolean, optional): Fragment,count_packet (boolean, optional): Count Packet,cwr (boolean, optional): cwr for tcp protocol,ece (boolean, optional): ece for tcp protocol,urg (boolean, optional): urg for tcp protocol,ack (boolean, optional): ack for tcp protocol,psh (boolean, optional): psh for tcp protocol,rst (boolean, optional): rst for tcp protocol,syn (boolean, optional): syn for tcp protocol,fin (boolean, optional): fin for tcp protocol,established (boolean, optional): established for tcp protocol,icmp_type (string, optional) = ['echo' or 'echo-reply' or 'number']: ICMP Type for icmp protocol,icmp_type_value (integer): ICMP Type Value (0-255) for number icmp_type,icmp_code (integer, optional): ICMP Code (0-255) for icmp protocol}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic": "",
          "hpe_rules": [
            {
              "number": 0,
              "packet_match": "",
              "traffic_match_type": "",
              "net_source": "",
              "net_destination": "",
              "net_service": "",
              "protocol": "",
              "source": "",
              "source_port": "",
              "source_port_value": "",
              "protocol_number": 0,
              "destination": "",
              "destination_value": "",
              "destination_port": "",
              "destination_port_value": "",
              "ip_dscp": 0,
              "vlan_id": 0,
              "ip_precedence": "",
              "ip_service_type": "",
              "established": false,
              "fin": false,
              "rst": false,
              "syn": false
            }
          ],
          "aos_cx_rules": [
            {
              "number": 0,
              "packet_match": "",
              "protocol": "",
              "protocol_number": 0,
              "source": "",
              "source_ip_address": "",
              "source_port": "",
              "source_port_value": "",
              "destination": "",
              "destination_ip_address": "",
              "destination_port": "",
              "destination_port_value": "",
              "dscp": 0,
              "vlan_id": 0,
              "ecn": 0,
              "ip_precedence": "",
              "service_type": 0,
              "ttl": 0,
              "fragment": false,
              "count_packet": false,
              "cwr": false,
              "ece": false,
              "urg": false,
              "ack": false,
              "psh": false,
              "rst": false,
              "syn": false,
              "fin": false,
              "established": false,
              "icmp_type": "",
              "icmp_type_value": 0,
              "icmp_code": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: dur_class_id, Description: Numeric ID of the DURClass
                Required Body Parameters (body description)- DURClassReplace {name (string): Name of the DUR Class,traffic (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Traffic of the DUR Class,hpe_rules (array[HPERulesPost]): Rules for ArubaOS-Switch DUR Class,aos_cx_rules (array[AosCxRulesPost]): Rules for AOS-CX DUR Class}HPERulesPost {number (integer): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,traffic_match_type (string, optional) = ['netsource' or 'protocol']: Traffic Match Type,net_source (string, optional) = ['any']: Net Source for netsource traffic_match_type,net_destination (string, optional): Net Destination for netsource traffic_match_type,net_service (string, optional): Net Service for netsource traffic_match_type,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'vrrp' or 'pim' or 'ospf' or 'ipv6_in_ip' or 'ip_in_ip' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'gre' or 'esp' or 'ah' or '255']: Protocol for protocol traffic_match_type,source (string, optional) = ['any']: Source for protocol traffic_match_type,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Source Port for protocol traffic_match_type,source_port_value (string, optional): Source Port Value for protocol traffic_match_type,protocol_number (integer): Protocol Number (0-255) for 255 protocol,destination (string, optional) = ['any' or 'host' or 'ipsubnet']: Destnation for protocol traffic_match_type,destination_value (string, optional): Destination Value for protocol traffic_match_type,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Destination Port for protocol traffic_match_type,destination_port_value (string, optional): Destination Port Value for protocol traffic_match_type,ip_dscp (integer, optional): IP DSCP (0-63) for protocol traffic_match_type,vlan_id (integer, optional): VLAN ID (1-4094) for protocol traffic_match_type,ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence for protocol traffic_match_type,ip_service_type (string, optional) = ['normal' or 'max reliability' or 'max throughput' or 'minimize delay']: IP Type of Service for protocol traffic_match_type,established (boolean, optional): Established for tcp protocol,fin (boolean, optional): Fin for tcp protocol,rst (boolean, optional): Rst for tcp protocol,syn (boolean, optional): Syn for tcp protocol}AosCxRulesPost {number (integer, optional): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'pim' or 'ospf' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'icmpv6' or 'gre' or 'esp' or 'ah' or 'number' or 'any']: Protocol,protocol_number (integer): Protocol Number for number protocol,source (string, optional) = ['any' or 'ip']: Source,source_ip_address (string): Source IP Address for ip source,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Source Port,source_port_value (string): Source Port Value,destination (string, optional) = ['any' or 'ip']: Destination,destination_ip_address (string): Destination IP Address for ip destination,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Destination Port,destination_port_value (string): Destination Port Value,dscp (integer, optional): DSCP (0-63),vlan_id (integer, optional): VLAN ID (1-4094),ecn (integer, optional): ECN (0-3),ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence,service_type (integer, optional): Type of Service (0-31),ttl (integer, optional): Time to Live (0-255),fragment (boolean, optional): Fragment,count_packet (boolean, optional): Count Packet,cwr (boolean, optional): cwr for tcp protocol,ece (boolean, optional): ece for tcp protocol,urg (boolean, optional): urg for tcp protocol,ack (boolean, optional): ack for tcp protocol,psh (boolean, optional): psh for tcp protocol,rst (boolean, optional): rst for tcp protocol,syn (boolean, optional): syn for tcp protocol,fin (boolean, optional): fin for tcp protocol,established (boolean, optional): established for tcp protocol,icmp_type (string, optional) = ['echo' or 'echo-reply' or 'number']: ICMP Type for icmp protocol,icmp_type_value (integer): ICMP Type Value (0-255) for number icmp_type,icmp_code (integer, optional): ICMP Code (0-255) for icmp protocol}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic": "",
          "hpe_rules": [
            {
              "number": 0,
              "packet_match": "",
              "traffic_match_type": "",
              "net_source": "",
              "net_destination": "",
              "net_service": "",
              "protocol": "",
              "source": "",
              "source_port": "",
              "source_port_value": "",
              "protocol_number": 0,
              "destination": "",
              "destination_value": "",
              "destination_port": "",
              "destination_port_value": "",
              "ip_dscp": 0,
              "vlan_id": 0,
              "ip_precedence": "",
              "ip_service_type": "",
              "established": false,
              "fin": false,
              "rst": false,
              "syn": false
            }
          ],
          "aos_cx_rules": [
            {
              "number": 0,
              "packet_match": "",
              "protocol": "",
              "protocol_number": 0,
              "source": "",
              "source_ip_address": "",
              "source_port": "",
              "source_port_value": "",
              "destination": "",
              "destination_ip_address": "",
              "destination_port": "",
              "destination_port_value": "",
              "dscp": 0,
              "vlan_id": 0,
              "ecn": 0,
              "ip_precedence": "",
              "service_type": 0,
              "ttl": 0,
              "fragment": false,
              "count_packet": false,
              "cwr": false,
              "ece": false,
              "urg": false,
              "ack": false,
              "psh": false,
              "rst": false,
              "syn": false,
              "fin": false,
              "established": false,
              "icmp_type": "",
              "icmp_type_value": 0,
              "icmp_code": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: dur_class_id, Description: Numeric ID of the DURClass
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the DURClass
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the DURClass
                Required Body Parameters (body description)- DURClassUpdate {name (string, optional): Name of the DUR Class,traffic (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Traffic of the DUR Class,hpe_rules (array[HPERulesPost], optional): Rules for ArubaOS-Switch DUR Class,aos_cx_rules (array[AosCxRulesPost], optional): Rules for AOS-CX DUR Class}HPERulesPost {number (integer): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,traffic_match_type (string, optional) = ['netsource' or 'protocol']: Traffic Match Type,net_source (string, optional) = ['any']: Net Source for netsource traffic_match_type,net_destination (string, optional): Net Destination for netsource traffic_match_type,net_service (string, optional): Net Service for netsource traffic_match_type,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'vrrp' or 'pim' or 'ospf' or 'ipv6_in_ip' or 'ip_in_ip' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'gre' or 'esp' or 'ah' or '255']: Protocol for protocol traffic_match_type,source (string, optional) = ['any']: Source for protocol traffic_match_type,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Source Port for protocol traffic_match_type,source_port_value (string, optional): Source Port Value for protocol traffic_match_type,protocol_number (integer): Protocol Number (0-255) for 255 protocol,destination (string, optional) = ['any' or 'host' or 'ipsubnet']: Destnation for protocol traffic_match_type,destination_value (string, optional): Destination Value for protocol traffic_match_type,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Destination Port for protocol traffic_match_type,destination_port_value (string, optional): Destination Port Value for protocol traffic_match_type,ip_dscp (integer, optional): IP DSCP (0-63) for protocol traffic_match_type,vlan_id (integer, optional): VLAN ID (1-4094) for protocol traffic_match_type,ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence for protocol traffic_match_type,ip_service_type (string, optional) = ['normal' or 'max reliability' or 'max throughput' or 'minimize delay']: IP Type of Service for protocol traffic_match_type,established (boolean, optional): Established for tcp protocol,fin (boolean, optional): Fin for tcp protocol,rst (boolean, optional): Rst for tcp protocol,syn (boolean, optional): Syn for tcp protocol}AosCxRulesPost {number (integer, optional): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'pim' or 'ospf' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'icmpv6' or 'gre' or 'esp' or 'ah' or 'number' or 'any']: Protocol,protocol_number (integer): Protocol Number for number protocol,source (string, optional) = ['any' or 'ip']: Source,source_ip_address (string): Source IP Address for ip source,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Source Port,source_port_value (string): Source Port Value,destination (string, optional) = ['any' or 'ip']: Destination,destination_ip_address (string): Destination IP Address for ip destination,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Destination Port,destination_port_value (string): Destination Port Value,dscp (integer, optional): DSCP (0-63),vlan_id (integer, optional): VLAN ID (1-4094),ecn (integer, optional): ECN (0-3),ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence,service_type (integer, optional): Type of Service (0-31),ttl (integer, optional): Time to Live (0-255),fragment (boolean, optional): Fragment,count_packet (boolean, optional): Count Packet,cwr (boolean, optional): cwr for tcp protocol,ece (boolean, optional): ece for tcp protocol,urg (boolean, optional): urg for tcp protocol,ack (boolean, optional): ack for tcp protocol,psh (boolean, optional): psh for tcp protocol,rst (boolean, optional): rst for tcp protocol,syn (boolean, optional): syn for tcp protocol,fin (boolean, optional): fin for tcp protocol,established (boolean, optional): established for tcp protocol,icmp_type (string, optional) = ['echo' or 'echo-reply' or 'number']: ICMP Type for icmp protocol,icmp_type_value (integer): ICMP Type Value (0-255) for number icmp_type,icmp_code (integer, optional): ICMP Code (0-255) for icmp protocol}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic": "",
          "hpe_rules": [
            {
              "number": 0,
              "packet_match": "",
              "traffic_match_type": "",
              "net_source": "",
              "net_destination": "",
              "net_service": "",
              "protocol": "",
              "source": "",
              "source_port": "",
              "source_port_value": "",
              "protocol_number": 0,
              "destination": "",
              "destination_value": "",
              "destination_port": "",
              "destination_port_value": "",
              "ip_dscp": 0,
              "vlan_id": 0,
              "ip_precedence": "",
              "ip_service_type": "",
              "established": false,
              "fin": false,
              "rst": false,
              "syn": false
            }
          ],
          "aos_cx_rules": [
            {
              "number": 0,
              "packet_match": "",
              "protocol": "",
              "protocol_number": 0,
              "source": "",
              "source_ip_address": "",
              "source_port": "",
              "source_port_value": "",
              "destination": "",
              "destination_ip_address": "",
              "destination_port": "",
              "destination_port_value": "",
              "dscp": 0,
              "vlan_id": 0,
              "ecn": 0,
              "ip_precedence": "",
              "service_type": 0,
              "ttl": 0,
              "fragment": false,
              "count_packet": false,
              "cwr": false,
              "ece": false,
              "urg": false,
              "ack": false,
              "psh": false,
              "rst": false,
              "syn": false,
              "fin": false,
              "established": false,
              "icmp_type": "",
              "icmp_type_value": 0,
              "icmp_code": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the DURClass
                Required Body Parameters (body description)- DURClassReplace {name (string): Name of the DUR Class,traffic (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Traffic of the DUR Class,hpe_rules (array[HPERulesPost]): Rules for ArubaOS-Switch DUR Class,aos_cx_rules (array[AosCxRulesPost]): Rules for AOS-CX DUR Class}HPERulesPost {number (integer): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,traffic_match_type (string, optional) = ['netsource' or 'protocol']: Traffic Match Type,net_source (string, optional) = ['any']: Net Source for netsource traffic_match_type,net_destination (string, optional): Net Destination for netsource traffic_match_type,net_service (string, optional): Net Service for netsource traffic_match_type,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'vrrp' or 'pim' or 'ospf' or 'ipv6_in_ip' or 'ip_in_ip' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'gre' or 'esp' or 'ah' or '255']: Protocol for protocol traffic_match_type,source (string, optional) = ['any']: Source for protocol traffic_match_type,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Source Port for protocol traffic_match_type,source_port_value (string, optional): Source Port Value for protocol traffic_match_type,protocol_number (integer): Protocol Number (0-255) for 255 protocol,destination (string, optional) = ['any' or 'host' or 'ipsubnet']: Destnation for protocol traffic_match_type,destination_value (string, optional): Destination Value for protocol traffic_match_type,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'neg' or 'range']: Destination Port for protocol traffic_match_type,destination_port_value (string, optional): Destination Port Value for protocol traffic_match_type,ip_dscp (integer, optional): IP DSCP (0-63) for protocol traffic_match_type,vlan_id (integer, optional): VLAN ID (1-4094) for protocol traffic_match_type,ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence for protocol traffic_match_type,ip_service_type (string, optional) = ['normal' or 'max reliability' or 'max throughput' or 'minimize delay']: IP Type of Service for protocol traffic_match_type,established (boolean, optional): Established for tcp protocol,fin (boolean, optional): Fin for tcp protocol,rst (boolean, optional): Rst for tcp protocol,syn (boolean, optional): Syn for tcp protocol}AosCxRulesPost {number (integer, optional): Number (1-2147483647),packet_match (string, optional) = ['match' or 'ignore']: Packet Match,protocol (string, optional) = ['tcp' or 'udp' or 'sctp' or 'pim' or 'ospf' or 'ip' or 'ipv6' or 'igmp' or 'icmp' or 'icmpv6' or 'gre' or 'esp' or 'ah' or 'number' or 'any']: Protocol,protocol_number (integer): Protocol Number for number protocol,source (string, optional) = ['any' or 'ip']: Source,source_ip_address (string): Source IP Address for ip source,source_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Source Port,source_port_value (string): Source Port Value,destination (string, optional) = ['any' or 'ip']: Destination,destination_ip_address (string): Destination IP Address for ip destination,destination_port (string, optional) = ['eq' or 'gt' or 'lt' or 'range']: Destination Port,destination_port_value (string): Destination Port Value,dscp (integer, optional): DSCP (0-63),vlan_id (integer, optional): VLAN ID (1-4094),ecn (integer, optional): ECN (0-3),ip_precedence (string, optional) = ['routine' or 'priority' or 'immediate' or 'flash' or 'flash override' or 'critical' or 'internet' or 'network']: IP Precedence,service_type (integer, optional): Type of Service (0-31),ttl (integer, optional): Time to Live (0-255),fragment (boolean, optional): Fragment,count_packet (boolean, optional): Count Packet,cwr (boolean, optional): cwr for tcp protocol,ece (boolean, optional): ece for tcp protocol,urg (boolean, optional): urg for tcp protocol,ack (boolean, optional): ack for tcp protocol,psh (boolean, optional): psh for tcp protocol,rst (boolean, optional): rst for tcp protocol,syn (boolean, optional): syn for tcp protocol,fin (boolean, optional): fin for tcp protocol,established (boolean, optional): established for tcp protocol,icmp_type (string, optional) = ['echo' or 'echo-reply' or 'number']: ICMP Type for icmp protocol,icmp_type_value (integer): ICMP Type Value (0-255) for number icmp_type,icmp_code (integer, optional): ICMP Code (0-255) for icmp protocol}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic": "",
          "hpe_rules": [
            {
              "number": 0,
              "packet_match": "",
              "traffic_match_type": "",
              "net_source": "",
              "net_destination": "",
              "net_service": "",
              "protocol": "",
              "source": "",
              "source_port": "",
              "source_port_value": "",
              "protocol_number": 0,
              "destination": "",
              "destination_value": "",
              "destination_port": "",
              "destination_port_value": "",
              "ip_dscp": 0,
              "vlan_id": 0,
              "ip_precedence": "",
              "ip_service_type": "",
              "established": false,
              "fin": false,
              "rst": false,
              "syn": false
            }
          ],
          "aos_cx_rules": [
            {
              "number": 0,
              "packet_match": "",
              "protocol": "",
              "protocol_number": 0,
              "source": "",
              "source_ip_address": "",
              "source_port": "",
              "source_port_value": "",
              "destination": "",
              "destination_ip_address": "",
              "destination_port": "",
              "destination_port_value": "",
              "dscp": 0,
              "vlan_id": 0,
              "ecn": 0,
              "ip_precedence": "",
              "service_type": 0,
              "ttl": 0,
              "fragment": false,
              "count_packet": false,
              "cwr": false,
              "ece": false,
              "urg": false,
              "ack": false,
              "psh": false,
              "rst": false,
              "syn": false,
              "fin": false,
              "established": false,
              "icmp_type": "",
              "icmp_type_value": 0,
              "icmp_code": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the DURClass
        """
        url_path = "/enforcement-profile-dur/dur-class/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:EnforcementProfile
    # Function Section Description: Manage Enforcement Profiles

    def get_enforcement_profile(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of Enforcement Profiles
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- EnforcementProfileCreate {name (string): Name of the Enforcement Profile,description (string, optional): Description of the Enforcement Profile,type (string) = ['RADIUS' or 'TACACS' or 'SNMP' or 'Application' or 'Agent' or 'CLI' or 'HTTP' or 'RADIUS_DynAuthZ' or 'Post_Authentication' or 'Aruba_DUR']: Enforcement Profile Type,agent_template (string, optional) = ['Agent' or 'AgentScript']: Agent Enforcement Profile Template,post_auth_template (string, optional) = ['EntityUpdate' or 'SessionRestriction' or 'SessionNotify']: Post Authentication Enforcement Profile Template,radius_dyn_authz_template (string, optional): Post Authentication Enforcement Profile Template,action (string, optional) = ['Accept' or 'Reject' or 'Drop']: Enforcement Profile Action,device_group_list (array[string], optional): Device Group List,attributes (array[Attributes], optional): Attributes,tacacs_service_params (TacacsServiceParam, optional): Tacacs+ Service Params,dur_config (DURConfig, optional): Downloadable User Role Configuration}Attributes {type (string, optional): Type of the Attribute,name (string, optional): Name of the Attribute,value (string, optional): Value of the Attribute}TacacsServiceParam {privilege_level (integer, optional): Privilege Level <0-15>,services (array[string], optional): Selected Services,authorize_attribute_status (string, optional) = ['ADD' or 'REPLACE' or 'FAIL']: Authorize Attribute Status,tacacs_command_config (TacacsCommandConfig, optional): Commands}TacacsCommandConfig {service_type (string, optional) = ['Shell' or 'PIX Shell']: Service Type,permit_unmatched_cmds (boolean, optional): Enable to permit unmatched commands,commands (array[TacacsCommand], optional): Specify which commands with arguments are permitted/denied}TacacsCommand {command (string, optional): Shell Command,permit_unmatched_args (boolean, optional): Enable to permit unmatched arguments,command_args (array[TacacsCommandArgs], optional): List of Command Arguments}TacacsCommandArgs {argument (string, optional): Command Argument,permit_action (boolean, optional): Enable to permit unmatched action}DURConfig {config_mode (string, optional) = ['Standard' or 'Advanced']: Role Configuration Mode for Aruba Downloadable Role Enforcement profile,product (string, optional) = ['AOS-CX' or 'Mobility Controller' or 'ArubaOS-Switch' or 'Mobility Access Switch']: Product Name for Aruba Downloadable Role Enforcement profile,aruba_os_switch_config (ArubaOSSwitchConfig, optional): ArubaOS-Switch Downloadable Role Configuration,mobility_access_switch_config (MASConfig, optional): Mobility Access Switch Downloadable Role Configuration,mobility_controller_config (AMCConfig, optional): Mobility Controller Downloadable Role Configuration,aos_cx_config (AOSCXConfig, optional): AOS-CX Downloadable Role Configuration}ArubaOSSwitchConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policy_name (string, optional): Policy name,controller_static_role (string, optional): Controller Static Role,controller_downloadable_role (string, optional): Controller Downloadable Role,vlan_id (string, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,vlan_tagged_id (string, optional): VLAN ID Tagged,vlan_tagged_name (string, optional): VLAN Name Tagged,reauth_period (string, optional): Re-Authentication Period <0-999999999>,logoff_period (string, optional): Logoff Period <0(mac-pin) OR 60-9999999>,cached_reauth_period (string, optional): Cached Re-Authentication Period <60-2147483647>,enable_device_config (boolean, optional): Enable Device Configuration,enable_poe_allocate_by_class (boolean, optional): Enable POE Allocate By Class,poe_priority (string, optional) = ['low' or 'high' or 'critical']: POE Priority,enable_admin_edge_port (boolean, optional): Enable Admin Edge Port,enable_port_mode (boolean, optional): Enable Port Mode}MASConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policer_profile_name (string, optional): Policer Profile name,qos_profile_name (string, optional): QoS Profile name,voip_profile_name (string, optional): VoIP Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,acl_list (array[acl], optional): Access Control List}acl {name (string, optional): Name of the ACL,type (string, optional) = ['Ethertype' or 'MAC' or 'Stateless' or 'Session']: Type of the ACL}AMCConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,parameterized_vlan (string, optional): Parameterized VLAN,acl_list (array[acl], optional): Access Control List}AOSCXConfig {role_name (string, optional): Role name,description (string, optional): Description,captive_portal_name (string, optional): Captive Portal name,authentication_mode (string, optional) = ['' or 'client-mode' or 'device-mode' or 'multi-domain-mode']: Authentication Mode,device_traffic_class (string, optional) = ['None' or 'Voice']: Device Traffic Class,session_timeout_type (string, optional) = ['Static' or 'Parameterized']: Session Timeout Type,session_timeout (string, optional): Session Timeout <1-4294967295>,parameterized_session_timeout (string, optional): Parameterized Session Timeout,cached_reauth_period (string, optional): Cached Re-authentication period <30-4294967295>,reauth_period_type (string, optional) = ['Manual' or 'Random' or 'Parameterized']: Re-Authentication Period Type,reauth_period (string, optional): Re-Authentication Period <1-4294967295>,minimum_reauth_period (string, optional): Minimum re-authentication period <1-4294967295>,parameterized_reauth (string, optional): Parameterized Re-Authentication,client_inactivity_timeout_type (string, optional) = ['Value' or 'None' or 'Parameterized']: Client Inactivity Timeout Type,client_inactivity_timeout (string, optional): Client Inactivity Timeout value <300-4294967295>,parameterized_client_inactivity_timeout (string, optional): Parameterized Client Inactivity Timeout,allowed_vlan_ids_trunk (string, optional): Allowed VLANs on Trunk <1-4094>,allowed_vlan_names_trunk (string, optional): List of Allowed VLAN Names on Trunk,parameterized_allowed_vlan_type (string, optional) = ['Id' or 'Name']: Parameterized Allowed VLAN Type,parameterized_allowed_vlan (string, optional): Parameterized Allowed VLAN,native_trunk_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Native Trunk VLAN Type,native_trunk_vlan_id (string, optional): Native Trunk VLAN <1-4094>,native_trunk_vlan_name (string, optional): Native Trunk VLAN Name,parameterized_native_trunk_vlan (string, optional): Parameterized Native Trunk VLAN,access_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Access VLAN Type,access_vlan_id (string, optional): Access VLAN <1-4094>,access_vlan_name (string, optional): Access VLAN Name,parameterized_access_vlan (string, optional): Parameterized Access VLAN,gateway_zone (string, optional): Gateway Zone,secondary_role_type (string, optional) = ['None' or 'Static' or 'Dynamic']: Secondary Role Type,gateway_static_role (string, optional): Gateway Static Role,gateway_downloadable_role (string, optional): Gateway Downloadable Role,mtu (string, optional): MTU <68-9198>,trust_mode (string, optional) = ['' or 'none' or 'cos' or 'dscp']: Trust Mode,poe_priority (string, optional) = ['' or 'low' or 'high' or 'critical']: PoE Priority,private_vlan_port_type (string, optional) = ['' or 'promiscuous' or 'secondary']: Private VLAN Port Type,policy_name (string, optional): Policy name}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "agent_template": "",
          "post_auth_template": "",
          "radius_dyn_authz_template": "",
          "action": "",
          "device_group_list": [
            ""
          ],
          "attributes": [
            {
              "type": "",
              "name": "",
              "value": ""
            }
          ],
          "tacacs_service_params": {
            "privilege_level": 0,
            "services": [
              ""
            ],
            "authorize_attribute_status": "",
            "tacacs_command_config": {
              "service_type": "",
              "permit_unmatched_cmds": false,
              "commands": [
                {
                  "command": "",
                  "permit_unmatched_args": false,
                  "command_args": [
                    {
                      "argument": "",
                      "permit_action": false
                    }
                  ]
                }
              ]
            }
          },
          "dur_config": {
            "config_mode": "",
            "product": "",
            "aruba_os_switch_config": {
              "captive_portal_profile_name": "",
              "policy_name": "",
              "controller_static_role": "",
              "controller_downloadable_role": "",
              "vlan_id": "",
              "vlan_name": "",
              "vlan_tagged_id": "",
              "vlan_tagged_name": "",
              "reauth_period": "",
              "logoff_period": "",
              "cached_reauth_period": "",
              "enable_device_config": false,
              "enable_poe_allocate_by_class": false,
              "poe_priority": "",
              "enable_admin_edge_port": false,
              "enable_port_mode": false
            },
            "mobility_access_switch_config": {
              "captive_portal_profile_name": "",
              "policer_profile_name": "",
              "qos_profile_name": "",
              "voip_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "mobility_controller_config": {
              "captive_portal_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "vlan_name": "",
              "parameterized_vlan": "",
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "aos_cx_config": {
              "role_name": "",
              "description": "",
              "captive_portal_name": "",
              "authentication_mode": "",
              "device_traffic_class": "",
              "session_timeout_type": "",
              "session_timeout": "",
              "parameterized_session_timeout": "",
              "cached_reauth_period": "",
              "reauth_period_type": "",
              "reauth_period": "",
              "minimum_reauth_period": "",
              "parameterized_reauth": "",
              "client_inactivity_timeout_type": "",
              "client_inactivity_timeout": "",
              "parameterized_client_inactivity_timeout": "",
              "allowed_vlan_ids_trunk": "",
              "allowed_vlan_names_trunk": "",
              "parameterized_allowed_vlan_type": "",
              "parameterized_allowed_vlan": "",
              "native_trunk_vlan_type": "",
              "native_trunk_vlan_id": "",
              "native_trunk_vlan_name": "",
              "parameterized_native_trunk_vlan": "",
              "access_vlan_type": "",
              "access_vlan_id": "",
              "access_vlan_name": "",
              "parameterized_access_vlan": "",
              "gateway_zone": "",
              "secondary_role_type": "",
              "gateway_static_role": "",
              "gateway_downloadable_role": "",
              "mtu": "",
              "trust_mode": "",
              "poe_priority": "",
              "private_vlan_port_type": "",
              "policy_name": ""
            }
          }
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
                Required Body Parameters (body description)- EnforcementProfileUpdate {name (string, optional): Name of the Enforcement Profile,description (string, optional): Description of the Enforcement Profile,type (string, optional) = ['RADIUS' or 'TACACS' or 'SNMP' or 'Application' or 'Agent' or 'CLI' or 'HTTP' or 'RADIUS_DynAuthZ' or 'Post_Authentication' or 'Aruba_DUR']: Enforcement Profile Type,agent_template (string, optional) = ['Agent' or 'AgentScript']: Agent Enforcement Profile Template,post_auth_template (string, optional) = ['EntityUpdate' or 'SessionRestriction' or 'SessionNotify']: Post Authentication Enforcement Profile Template,radius_dyn_authz_template (string, optional): Post Authentication Enforcement Profile Template,action (string, optional) = ['Accept' or 'Reject' or 'Drop']: Enforcement Profile Action,device_group_list (array[string], optional): Device Group List,attributes (array[Attributes], optional): Attributes,tacacs_service_params (TacacsServiceParam, optional): Tacacs+ Service Params,dur_config (DURConfig, optional): Downloadable User Role Configuration}Attributes {type (string, optional): Type of the Attribute,name (string, optional): Name of the Attribute,value (string, optional): Value of the Attribute}TacacsServiceParam {privilege_level (integer, optional): Privilege Level <0-15>,services (array[string], optional): Selected Services,authorize_attribute_status (string, optional) = ['ADD' or 'REPLACE' or 'FAIL']: Authorize Attribute Status,tacacs_command_config (TacacsCommandConfig, optional): Commands}TacacsCommandConfig {service_type (string, optional) = ['Shell' or 'PIX Shell']: Service Type,permit_unmatched_cmds (boolean, optional): Enable to permit unmatched commands,commands (array[TacacsCommand], optional): Specify which commands with arguments are permitted/denied}TacacsCommand {command (string, optional): Shell Command,permit_unmatched_args (boolean, optional): Enable to permit unmatched arguments,command_args (array[TacacsCommandArgs], optional): List of Command Arguments}TacacsCommandArgs {argument (string, optional): Command Argument,permit_action (boolean, optional): Enable to permit unmatched action}DURConfig {config_mode (string, optional) = ['Standard' or 'Advanced']: Role Configuration Mode for Aruba Downloadable Role Enforcement profile,product (string, optional) = ['AOS-CX' or 'Mobility Controller' or 'ArubaOS-Switch' or 'Mobility Access Switch']: Product Name for Aruba Downloadable Role Enforcement profile,aruba_os_switch_config (ArubaOSSwitchConfig, optional): ArubaOS-Switch Downloadable Role Configuration,mobility_access_switch_config (MASConfig, optional): Mobility Access Switch Downloadable Role Configuration,mobility_controller_config (AMCConfig, optional): Mobility Controller Downloadable Role Configuration,aos_cx_config (AOSCXConfig, optional): AOS-CX Downloadable Role Configuration}ArubaOSSwitchConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policy_name (string, optional): Policy name,controller_static_role (string, optional): Controller Static Role,controller_downloadable_role (string, optional): Controller Downloadable Role,vlan_id (string, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,vlan_tagged_id (string, optional): VLAN ID Tagged,vlan_tagged_name (string, optional): VLAN Name Tagged,reauth_period (string, optional): Re-Authentication Period <0-999999999>,logoff_period (string, optional): Logoff Period <0(mac-pin) OR 60-9999999>,cached_reauth_period (string, optional): Cached Re-Authentication Period <60-2147483647>,enable_device_config (boolean, optional): Enable Device Configuration,enable_poe_allocate_by_class (boolean, optional): Enable POE Allocate By Class,poe_priority (string, optional) = ['low' or 'high' or 'critical']: POE Priority,enable_admin_edge_port (boolean, optional): Enable Admin Edge Port,enable_port_mode (boolean, optional): Enable Port Mode}MASConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policer_profile_name (string, optional): Policer Profile name,qos_profile_name (string, optional): QoS Profile name,voip_profile_name (string, optional): VoIP Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,acl_list (array[acl], optional): Access Control List}acl {name (string, optional): Name of the ACL,type (string, optional) = ['Ethertype' or 'MAC' or 'Stateless' or 'Session']: Type of the ACL}AMCConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,parameterized_vlan (string, optional): Parameterized VLAN,acl_list (array[acl], optional): Access Control List}AOSCXConfig {role_name (string, optional): Role name,description (string, optional): Description,captive_portal_name (string, optional): Captive Portal name,authentication_mode (string, optional) = ['' or 'client-mode' or 'device-mode' or 'multi-domain-mode']: Authentication Mode,device_traffic_class (string, optional) = ['None' or 'Voice']: Device Traffic Class,session_timeout_type (string, optional) = ['Static' or 'Parameterized']: Session Timeout Type,session_timeout (string, optional): Session Timeout <1-4294967295>,parameterized_session_timeout (string, optional): Parameterized Session Timeout,cached_reauth_period (string, optional): Cached Re-authentication period <30-4294967295>,reauth_period_type (string, optional) = ['Manual' or 'Random' or 'Parameterized']: Re-Authentication Period Type,reauth_period (string, optional): Re-Authentication Period <1-4294967295>,minimum_reauth_period (string, optional): Minimum re-authentication period <1-4294967295>,parameterized_reauth (string, optional): Parameterized Re-Authentication,client_inactivity_timeout_type (string, optional) = ['Value' or 'None' or 'Parameterized']: Client Inactivity Timeout Type,client_inactivity_timeout (string, optional): Client Inactivity Timeout value <300-4294967295>,parameterized_client_inactivity_timeout (string, optional): Parameterized Client Inactivity Timeout,allowed_vlan_ids_trunk (string, optional): Allowed VLANs on Trunk <1-4094>,allowed_vlan_names_trunk (string, optional): List of Allowed VLAN Names on Trunk,parameterized_allowed_vlan_type (string, optional) = ['Id' or 'Name']: Parameterized Allowed VLAN Type,parameterized_allowed_vlan (string, optional): Parameterized Allowed VLAN,native_trunk_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Native Trunk VLAN Type,native_trunk_vlan_id (string, optional): Native Trunk VLAN <1-4094>,native_trunk_vlan_name (string, optional): Native Trunk VLAN Name,parameterized_native_trunk_vlan (string, optional): Parameterized Native Trunk VLAN,access_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Access VLAN Type,access_vlan_id (string, optional): Access VLAN <1-4094>,access_vlan_name (string, optional): Access VLAN Name,parameterized_access_vlan (string, optional): Parameterized Access VLAN,gateway_zone (string, optional): Gateway Zone,secondary_role_type (string, optional) = ['None' or 'Static' or 'Dynamic']: Secondary Role Type,gateway_static_role (string, optional): Gateway Static Role,gateway_downloadable_role (string, optional): Gateway Downloadable Role,mtu (string, optional): MTU <68-9198>,trust_mode (string, optional) = ['' or 'none' or 'cos' or 'dscp']: Trust Mode,poe_priority (string, optional) = ['' or 'low' or 'high' or 'critical']: PoE Priority,private_vlan_port_type (string, optional) = ['' or 'promiscuous' or 'secondary']: Private VLAN Port Type,policy_name (string, optional): Policy name}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "agent_template": "",
          "post_auth_template": "",
          "radius_dyn_authz_template": "",
          "action": "",
          "device_group_list": [
            ""
          ],
          "attributes": [
            {
              "type": "",
              "name": "",
              "value": ""
            }
          ],
          "tacacs_service_params": {
            "privilege_level": 0,
            "services": [
              ""
            ],
            "authorize_attribute_status": "",
            "tacacs_command_config": {
              "service_type": "",
              "permit_unmatched_cmds": false,
              "commands": [
                {
                  "command": "",
                  "permit_unmatched_args": false,
                  "command_args": [
                    {
                      "argument": "",
                      "permit_action": false
                    }
                  ]
                }
              ]
            }
          },
          "dur_config": {
            "config_mode": "",
            "product": "",
            "aruba_os_switch_config": {
              "captive_portal_profile_name": "",
              "policy_name": "",
              "controller_static_role": "",
              "controller_downloadable_role": "",
              "vlan_id": "",
              "vlan_name": "",
              "vlan_tagged_id": "",
              "vlan_tagged_name": "",
              "reauth_period": "",
              "logoff_period": "",
              "cached_reauth_period": "",
              "enable_device_config": false,
              "enable_poe_allocate_by_class": false,
              "poe_priority": "",
              "enable_admin_edge_port": false,
              "enable_port_mode": false
            },
            "mobility_access_switch_config": {
              "captive_portal_profile_name": "",
              "policer_profile_name": "",
              "qos_profile_name": "",
              "voip_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "mobility_controller_config": {
              "captive_portal_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "vlan_name": "",
              "parameterized_vlan": "",
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "aos_cx_config": {
              "role_name": "",
              "description": "",
              "captive_portal_name": "",
              "authentication_mode": "",
              "device_traffic_class": "",
              "session_timeout_type": "",
              "session_timeout": "",
              "parameterized_session_timeout": "",
              "cached_reauth_period": "",
              "reauth_period_type": "",
              "reauth_period": "",
              "minimum_reauth_period": "",
              "parameterized_reauth": "",
              "client_inactivity_timeout_type": "",
              "client_inactivity_timeout": "",
              "parameterized_client_inactivity_timeout": "",
              "allowed_vlan_ids_trunk": "",
              "allowed_vlan_names_trunk": "",
              "parameterized_allowed_vlan_type": "",
              "parameterized_allowed_vlan": "",
              "native_trunk_vlan_type": "",
              "native_trunk_vlan_id": "",
              "native_trunk_vlan_name": "",
              "parameterized_native_trunk_vlan": "",
              "access_vlan_type": "",
              "access_vlan_id": "",
              "access_vlan_name": "",
              "parameterized_access_vlan": "",
              "gateway_zone": "",
              "secondary_role_type": "",
              "gateway_static_role": "",
              "gateway_downloadable_role": "",
              "mtu": "",
              "trust_mode": "",
              "poe_priority": "",
              "private_vlan_port_type": "",
              "policy_name": ""
            }
          }
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
                Required Body Parameters (body description)- EnforcementProfileReplace {name (string): Name of the Enforcement Profile,description (string, optional): Description of the Enforcement Profile,type (string) = ['RADIUS' or 'TACACS' or 'SNMP' or 'Application' or 'Agent' or 'CLI' or 'HTTP' or 'RADIUS_DynAuthZ' or 'Post_Authentication' or 'Aruba_DUR']: Enforcement Profile Type,agent_template (string, optional) = ['Agent' or 'AgentScript']: Agent Enforcement Profile Template,post_auth_template (string, optional) = ['EntityUpdate' or 'SessionRestriction' or 'SessionNotify']: Post Authentication Enforcement Profile Template,radius_dyn_authz_template (string, optional): Post Authentication Enforcement Profile Template,action (string, optional) = ['Accept' or 'Reject' or 'Drop']: Enforcement Profile Action,device_group_list (array[string], optional): Device Group List,attributes (array[Attributes], optional): Attributes,tacacs_service_params (TacacsServiceParam, optional): Tacacs+ Service Params,dur_config (DURConfig, optional): Downloadable User Role Configuration}Attributes {type (string, optional): Type of the Attribute,name (string, optional): Name of the Attribute,value (string, optional): Value of the Attribute}TacacsServiceParam {privilege_level (integer, optional): Privilege Level <0-15>,services (array[string], optional): Selected Services,authorize_attribute_status (string, optional) = ['ADD' or 'REPLACE' or 'FAIL']: Authorize Attribute Status,tacacs_command_config (TacacsCommandConfig, optional): Commands}TacacsCommandConfig {service_type (string, optional) = ['Shell' or 'PIX Shell']: Service Type,permit_unmatched_cmds (boolean, optional): Enable to permit unmatched commands,commands (array[TacacsCommand], optional): Specify which commands with arguments are permitted/denied}TacacsCommand {command (string, optional): Shell Command,permit_unmatched_args (boolean, optional): Enable to permit unmatched arguments,command_args (array[TacacsCommandArgs], optional): List of Command Arguments}TacacsCommandArgs {argument (string, optional): Command Argument,permit_action (boolean, optional): Enable to permit unmatched action}DURConfig {config_mode (string, optional) = ['Standard' or 'Advanced']: Role Configuration Mode for Aruba Downloadable Role Enforcement profile,product (string, optional) = ['AOS-CX' or 'Mobility Controller' or 'ArubaOS-Switch' or 'Mobility Access Switch']: Product Name for Aruba Downloadable Role Enforcement profile,aruba_os_switch_config (ArubaOSSwitchConfig, optional): ArubaOS-Switch Downloadable Role Configuration,mobility_access_switch_config (MASConfig, optional): Mobility Access Switch Downloadable Role Configuration,mobility_controller_config (AMCConfig, optional): Mobility Controller Downloadable Role Configuration,aos_cx_config (AOSCXConfig, optional): AOS-CX Downloadable Role Configuration}ArubaOSSwitchConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policy_name (string, optional): Policy name,controller_static_role (string, optional): Controller Static Role,controller_downloadable_role (string, optional): Controller Downloadable Role,vlan_id (string, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,vlan_tagged_id (string, optional): VLAN ID Tagged,vlan_tagged_name (string, optional): VLAN Name Tagged,reauth_period (string, optional): Re-Authentication Period <0-999999999>,logoff_period (string, optional): Logoff Period <0(mac-pin) OR 60-9999999>,cached_reauth_period (string, optional): Cached Re-Authentication Period <60-2147483647>,enable_device_config (boolean, optional): Enable Device Configuration,enable_poe_allocate_by_class (boolean, optional): Enable POE Allocate By Class,poe_priority (string, optional) = ['low' or 'high' or 'critical']: POE Priority,enable_admin_edge_port (boolean, optional): Enable Admin Edge Port,enable_port_mode (boolean, optional): Enable Port Mode}MASConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policer_profile_name (string, optional): Policer Profile name,qos_profile_name (string, optional): QoS Profile name,voip_profile_name (string, optional): VoIP Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,acl_list (array[acl], optional): Access Control List}acl {name (string, optional): Name of the ACL,type (string, optional) = ['Ethertype' or 'MAC' or 'Stateless' or 'Session']: Type of the ACL}AMCConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,parameterized_vlan (string, optional): Parameterized VLAN,acl_list (array[acl], optional): Access Control List}AOSCXConfig {role_name (string, optional): Role name,description (string, optional): Description,captive_portal_name (string, optional): Captive Portal name,authentication_mode (string, optional) = ['' or 'client-mode' or 'device-mode' or 'multi-domain-mode']: Authentication Mode,device_traffic_class (string, optional) = ['None' or 'Voice']: Device Traffic Class,session_timeout_type (string, optional) = ['Static' or 'Parameterized']: Session Timeout Type,session_timeout (string, optional): Session Timeout <1-4294967295>,parameterized_session_timeout (string, optional): Parameterized Session Timeout,cached_reauth_period (string, optional): Cached Re-authentication period <30-4294967295>,reauth_period_type (string, optional) = ['Manual' or 'Random' or 'Parameterized']: Re-Authentication Period Type,reauth_period (string, optional): Re-Authentication Period <1-4294967295>,minimum_reauth_period (string, optional): Minimum re-authentication period <1-4294967295>,parameterized_reauth (string, optional): Parameterized Re-Authentication,client_inactivity_timeout_type (string, optional) = ['Value' or 'None' or 'Parameterized']: Client Inactivity Timeout Type,client_inactivity_timeout (string, optional): Client Inactivity Timeout value <300-4294967295>,parameterized_client_inactivity_timeout (string, optional): Parameterized Client Inactivity Timeout,allowed_vlan_ids_trunk (string, optional): Allowed VLANs on Trunk <1-4094>,allowed_vlan_names_trunk (string, optional): List of Allowed VLAN Names on Trunk,parameterized_allowed_vlan_type (string, optional) = ['Id' or 'Name']: Parameterized Allowed VLAN Type,parameterized_allowed_vlan (string, optional): Parameterized Allowed VLAN,native_trunk_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Native Trunk VLAN Type,native_trunk_vlan_id (string, optional): Native Trunk VLAN <1-4094>,native_trunk_vlan_name (string, optional): Native Trunk VLAN Name,parameterized_native_trunk_vlan (string, optional): Parameterized Native Trunk VLAN,access_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Access VLAN Type,access_vlan_id (string, optional): Access VLAN <1-4094>,access_vlan_name (string, optional): Access VLAN Name,parameterized_access_vlan (string, optional): Parameterized Access VLAN,gateway_zone (string, optional): Gateway Zone,secondary_role_type (string, optional) = ['None' or 'Static' or 'Dynamic']: Secondary Role Type,gateway_static_role (string, optional): Gateway Static Role,gateway_downloadable_role (string, optional): Gateway Downloadable Role,mtu (string, optional): MTU <68-9198>,trust_mode (string, optional) = ['' or 'none' or 'cos' or 'dscp']: Trust Mode,poe_priority (string, optional) = ['' or 'low' or 'high' or 'critical']: PoE Priority,private_vlan_port_type (string, optional) = ['' or 'promiscuous' or 'secondary']: Private VLAN Port Type,policy_name (string, optional): Policy name}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "agent_template": "",
          "post_auth_template": "",
          "radius_dyn_authz_template": "",
          "action": "",
          "device_group_list": [
            ""
          ],
          "attributes": [
            {
              "type": "",
              "name": "",
              "value": ""
            }
          ],
          "tacacs_service_params": {
            "privilege_level": 0,
            "services": [
              ""
            ],
            "authorize_attribute_status": "",
            "tacacs_command_config": {
              "service_type": "",
              "permit_unmatched_cmds": false,
              "commands": [
                {
                  "command": "",
                  "permit_unmatched_args": false,
                  "command_args": [
                    {
                      "argument": "",
                      "permit_action": false
                    }
                  ]
                }
              ]
            }
          },
          "dur_config": {
            "config_mode": "",
            "product": "",
            "aruba_os_switch_config": {
              "captive_portal_profile_name": "",
              "policy_name": "",
              "controller_static_role": "",
              "controller_downloadable_role": "",
              "vlan_id": "",
              "vlan_name": "",
              "vlan_tagged_id": "",
              "vlan_tagged_name": "",
              "reauth_period": "",
              "logoff_period": "",
              "cached_reauth_period": "",
              "enable_device_config": false,
              "enable_poe_allocate_by_class": false,
              "poe_priority": "",
              "enable_admin_edge_port": false,
              "enable_port_mode": false
            },
            "mobility_access_switch_config": {
              "captive_portal_profile_name": "",
              "policer_profile_name": "",
              "qos_profile_name": "",
              "voip_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "mobility_controller_config": {
              "captive_portal_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "vlan_name": "",
              "parameterized_vlan": "",
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "aos_cx_config": {
              "role_name": "",
              "description": "",
              "captive_portal_name": "",
              "authentication_mode": "",
              "device_traffic_class": "",
              "session_timeout_type": "",
              "session_timeout": "",
              "parameterized_session_timeout": "",
              "cached_reauth_period": "",
              "reauth_period_type": "",
              "reauth_period": "",
              "minimum_reauth_period": "",
              "parameterized_reauth": "",
              "client_inactivity_timeout_type": "",
              "client_inactivity_timeout": "",
              "parameterized_client_inactivity_timeout": "",
              "allowed_vlan_ids_trunk": "",
              "allowed_vlan_names_trunk": "",
              "parameterized_allowed_vlan_type": "",
              "parameterized_allowed_vlan": "",
              "native_trunk_vlan_type": "",
              "native_trunk_vlan_id": "",
              "native_trunk_vlan_name": "",
              "parameterized_native_trunk_vlan": "",
              "access_vlan_type": "",
              "access_vlan_id": "",
              "access_vlan_name": "",
              "parameterized_access_vlan": "",
              "gateway_zone": "",
              "secondary_role_type": "",
              "gateway_static_role": "",
              "gateway_downloadable_role": "",
              "mtu": "",
              "trust_mode": "",
              "poe_priority": "",
              "private_vlan_port_type": "",
              "policy_name": ""
            }
          }
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: enforcement_profile_id, Description: Numeric ID of the Enforcement Profile
        """
        url_path = "/enforcement-profile/{enforcement_profile_id}"
        dict_path = {"enforcement_profile_id": enforcement_profile_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_enforcement_profile_name_by_name(self, name=""):
        """
        Operation: Get an Enforcement Profile by name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: name of the enforcement profile
        """
        url_path = "/enforcement-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_enforcement_profile_name_by_name(self, name="", body=({})):
        """
                Operation: Update an Enforcement Profile by name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: name of the enforcement profile
                Required Body Parameters (body description)- EnforcementProfileUpdate {name (string, optional): Name of the Enforcement Profile,description (string, optional): Description of the Enforcement Profile,type (string, optional) = ['RADIUS' or 'TACACS' or 'SNMP' or 'Application' or 'Agent' or 'CLI' or 'HTTP' or 'RADIUS_DynAuthZ' or 'Post_Authentication' or 'Aruba_DUR']: Enforcement Profile Type,agent_template (string, optional) = ['Agent' or 'AgentScript']: Agent Enforcement Profile Template,post_auth_template (string, optional) = ['EntityUpdate' or 'SessionRestriction' or 'SessionNotify']: Post Authentication Enforcement Profile Template,radius_dyn_authz_template (string, optional): Post Authentication Enforcement Profile Template,action (string, optional) = ['Accept' or 'Reject' or 'Drop']: Enforcement Profile Action,device_group_list (array[string], optional): Device Group List,attributes (array[Attributes], optional): Attributes,tacacs_service_params (TacacsServiceParam, optional): Tacacs+ Service Params,dur_config (DURConfig, optional): Downloadable User Role Configuration}Attributes {type (string, optional): Type of the Attribute,name (string, optional): Name of the Attribute,value (string, optional): Value of the Attribute}TacacsServiceParam {privilege_level (integer, optional): Privilege Level <0-15>,services (array[string], optional): Selected Services,authorize_attribute_status (string, optional) = ['ADD' or 'REPLACE' or 'FAIL']: Authorize Attribute Status,tacacs_command_config (TacacsCommandConfig, optional): Commands}TacacsCommandConfig {service_type (string, optional) = ['Shell' or 'PIX Shell']: Service Type,permit_unmatched_cmds (boolean, optional): Enable to permit unmatched commands,commands (array[TacacsCommand], optional): Specify which commands with arguments are permitted/denied}TacacsCommand {command (string, optional): Shell Command,permit_unmatched_args (boolean, optional): Enable to permit unmatched arguments,command_args (array[TacacsCommandArgs], optional): List of Command Arguments}TacacsCommandArgs {argument (string, optional): Command Argument,permit_action (boolean, optional): Enable to permit unmatched action}DURConfig {config_mode (string, optional) = ['Standard' or 'Advanced']: Role Configuration Mode for Aruba Downloadable Role Enforcement profile,product (string, optional) = ['AOS-CX' or 'Mobility Controller' or 'ArubaOS-Switch' or 'Mobility Access Switch']: Product Name for Aruba Downloadable Role Enforcement profile,aruba_os_switch_config (ArubaOSSwitchConfig, optional): ArubaOS-Switch Downloadable Role Configuration,mobility_access_switch_config (MASConfig, optional): Mobility Access Switch Downloadable Role Configuration,mobility_controller_config (AMCConfig, optional): Mobility Controller Downloadable Role Configuration,aos_cx_config (AOSCXConfig, optional): AOS-CX Downloadable Role Configuration}ArubaOSSwitchConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policy_name (string, optional): Policy name,controller_static_role (string, optional): Controller Static Role,controller_downloadable_role (string, optional): Controller Downloadable Role,vlan_id (string, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,vlan_tagged_id (string, optional): VLAN ID Tagged,vlan_tagged_name (string, optional): VLAN Name Tagged,reauth_period (string, optional): Re-Authentication Period <0-999999999>,logoff_period (string, optional): Logoff Period <0(mac-pin) OR 60-9999999>,cached_reauth_period (string, optional): Cached Re-Authentication Period <60-2147483647>,enable_device_config (boolean, optional): Enable Device Configuration,enable_poe_allocate_by_class (boolean, optional): Enable POE Allocate By Class,poe_priority (string, optional) = ['low' or 'high' or 'critical']: POE Priority,enable_admin_edge_port (boolean, optional): Enable Admin Edge Port,enable_port_mode (boolean, optional): Enable Port Mode}MASConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policer_profile_name (string, optional): Policer Profile name,qos_profile_name (string, optional): QoS Profile name,voip_profile_name (string, optional): VoIP Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,acl_list (array[acl], optional): Access Control List}acl {name (string, optional): Name of the ACL,type (string, optional) = ['Ethertype' or 'MAC' or 'Stateless' or 'Session']: Type of the ACL}AMCConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,parameterized_vlan (string, optional): Parameterized VLAN,acl_list (array[acl], optional): Access Control List}AOSCXConfig {role_name (string, optional): Role name,description (string, optional): Description,captive_portal_name (string, optional): Captive Portal name,authentication_mode (string, optional) = ['' or 'client-mode' or 'device-mode' or 'multi-domain-mode']: Authentication Mode,device_traffic_class (string, optional) = ['None' or 'Voice']: Device Traffic Class,session_timeout_type (string, optional) = ['Static' or 'Parameterized']: Session Timeout Type,session_timeout (string, optional): Session Timeout <1-4294967295>,parameterized_session_timeout (string, optional): Parameterized Session Timeout,cached_reauth_period (string, optional): Cached Re-authentication period <30-4294967295>,reauth_period_type (string, optional) = ['Manual' or 'Random' or 'Parameterized']: Re-Authentication Period Type,reauth_period (string, optional): Re-Authentication Period <1-4294967295>,minimum_reauth_period (string, optional): Minimum re-authentication period <1-4294967295>,parameterized_reauth (string, optional): Parameterized Re-Authentication,client_inactivity_timeout_type (string, optional) = ['Value' or 'None' or 'Parameterized']: Client Inactivity Timeout Type,client_inactivity_timeout (string, optional): Client Inactivity Timeout value <300-4294967295>,parameterized_client_inactivity_timeout (string, optional): Parameterized Client Inactivity Timeout,allowed_vlan_ids_trunk (string, optional): Allowed VLANs on Trunk <1-4094>,allowed_vlan_names_trunk (string, optional): List of Allowed VLAN Names on Trunk,parameterized_allowed_vlan_type (string, optional) = ['Id' or 'Name']: Parameterized Allowed VLAN Type,parameterized_allowed_vlan (string, optional): Parameterized Allowed VLAN,native_trunk_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Native Trunk VLAN Type,native_trunk_vlan_id (string, optional): Native Trunk VLAN <1-4094>,native_trunk_vlan_name (string, optional): Native Trunk VLAN Name,parameterized_native_trunk_vlan (string, optional): Parameterized Native Trunk VLAN,access_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Access VLAN Type,access_vlan_id (string, optional): Access VLAN <1-4094>,access_vlan_name (string, optional): Access VLAN Name,parameterized_access_vlan (string, optional): Parameterized Access VLAN,gateway_zone (string, optional): Gateway Zone,secondary_role_type (string, optional) = ['None' or 'Static' or 'Dynamic']: Secondary Role Type,gateway_static_role (string, optional): Gateway Static Role,gateway_downloadable_role (string, optional): Gateway Downloadable Role,mtu (string, optional): MTU <68-9198>,trust_mode (string, optional) = ['' or 'none' or 'cos' or 'dscp']: Trust Mode,poe_priority (string, optional) = ['' or 'low' or 'high' or 'critical']: PoE Priority,private_vlan_port_type (string, optional) = ['' or 'promiscuous' or 'secondary']: Private VLAN Port Type,policy_name (string, optional): Policy name}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "agent_template": "",
          "post_auth_template": "",
          "radius_dyn_authz_template": "",
          "action": "",
          "device_group_list": [
            ""
          ],
          "attributes": [
            {
              "type": "",
              "name": "",
              "value": ""
            }
          ],
          "tacacs_service_params": {
            "privilege_level": 0,
            "services": [
              ""
            ],
            "authorize_attribute_status": "",
            "tacacs_command_config": {
              "service_type": "",
              "permit_unmatched_cmds": false,
              "commands": [
                {
                  "command": "",
                  "permit_unmatched_args": false,
                  "command_args": [
                    {
                      "argument": "",
                      "permit_action": false
                    }
                  ]
                }
              ]
            }
          },
          "dur_config": {
            "config_mode": "",
            "product": "",
            "aruba_os_switch_config": {
              "captive_portal_profile_name": "",
              "policy_name": "",
              "controller_static_role": "",
              "controller_downloadable_role": "",
              "vlan_id": "",
              "vlan_name": "",
              "vlan_tagged_id": "",
              "vlan_tagged_name": "",
              "reauth_period": "",
              "logoff_period": "",
              "cached_reauth_period": "",
              "enable_device_config": false,
              "enable_poe_allocate_by_class": false,
              "poe_priority": "",
              "enable_admin_edge_port": false,
              "enable_port_mode": false
            },
            "mobility_access_switch_config": {
              "captive_portal_profile_name": "",
              "policer_profile_name": "",
              "qos_profile_name": "",
              "voip_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "mobility_controller_config": {
              "captive_portal_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "vlan_name": "",
              "parameterized_vlan": "",
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "aos_cx_config": {
              "role_name": "",
              "description": "",
              "captive_portal_name": "",
              "authentication_mode": "",
              "device_traffic_class": "",
              "session_timeout_type": "",
              "session_timeout": "",
              "parameterized_session_timeout": "",
              "cached_reauth_period": "",
              "reauth_period_type": "",
              "reauth_period": "",
              "minimum_reauth_period": "",
              "parameterized_reauth": "",
              "client_inactivity_timeout_type": "",
              "client_inactivity_timeout": "",
              "parameterized_client_inactivity_timeout": "",
              "allowed_vlan_ids_trunk": "",
              "allowed_vlan_names_trunk": "",
              "parameterized_allowed_vlan_type": "",
              "parameterized_allowed_vlan": "",
              "native_trunk_vlan_type": "",
              "native_trunk_vlan_id": "",
              "native_trunk_vlan_name": "",
              "parameterized_native_trunk_vlan": "",
              "access_vlan_type": "",
              "access_vlan_id": "",
              "access_vlan_name": "",
              "parameterized_access_vlan": "",
              "gateway_zone": "",
              "secondary_role_type": "",
              "gateway_static_role": "",
              "gateway_downloadable_role": "",
              "mtu": "",
              "trust_mode": "",
              "poe_priority": "",
              "private_vlan_port_type": "",
              "policy_name": ""
            }
          }
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: name, Description: name of the enforcement profile
                Required Body Parameters (body description)- EnforcementProfileReplace {name (string): Name of the Enforcement Profile,description (string, optional): Description of the Enforcement Profile,type (string) = ['RADIUS' or 'TACACS' or 'SNMP' or 'Application' or 'Agent' or 'CLI' or 'HTTP' or 'RADIUS_DynAuthZ' or 'Post_Authentication' or 'Aruba_DUR']: Enforcement Profile Type,agent_template (string, optional) = ['Agent' or 'AgentScript']: Agent Enforcement Profile Template,post_auth_template (string, optional) = ['EntityUpdate' or 'SessionRestriction' or 'SessionNotify']: Post Authentication Enforcement Profile Template,radius_dyn_authz_template (string, optional): Post Authentication Enforcement Profile Template,action (string, optional) = ['Accept' or 'Reject' or 'Drop']: Enforcement Profile Action,device_group_list (array[string], optional): Device Group List,attributes (array[Attributes], optional): Attributes,tacacs_service_params (TacacsServiceParam, optional): Tacacs+ Service Params,dur_config (DURConfig, optional): Downloadable User Role Configuration}Attributes {type (string, optional): Type of the Attribute,name (string, optional): Name of the Attribute,value (string, optional): Value of the Attribute}TacacsServiceParam {privilege_level (integer, optional): Privilege Level <0-15>,services (array[string], optional): Selected Services,authorize_attribute_status (string, optional) = ['ADD' or 'REPLACE' or 'FAIL']: Authorize Attribute Status,tacacs_command_config (TacacsCommandConfig, optional): Commands}TacacsCommandConfig {service_type (string, optional) = ['Shell' or 'PIX Shell']: Service Type,permit_unmatched_cmds (boolean, optional): Enable to permit unmatched commands,commands (array[TacacsCommand], optional): Specify which commands with arguments are permitted/denied}TacacsCommand {command (string, optional): Shell Command,permit_unmatched_args (boolean, optional): Enable to permit unmatched arguments,command_args (array[TacacsCommandArgs], optional): List of Command Arguments}TacacsCommandArgs {argument (string, optional): Command Argument,permit_action (boolean, optional): Enable to permit unmatched action}DURConfig {config_mode (string, optional) = ['Standard' or 'Advanced']: Role Configuration Mode for Aruba Downloadable Role Enforcement profile,product (string, optional) = ['AOS-CX' or 'Mobility Controller' or 'ArubaOS-Switch' or 'Mobility Access Switch']: Product Name for Aruba Downloadable Role Enforcement profile,aruba_os_switch_config (ArubaOSSwitchConfig, optional): ArubaOS-Switch Downloadable Role Configuration,mobility_access_switch_config (MASConfig, optional): Mobility Access Switch Downloadable Role Configuration,mobility_controller_config (AMCConfig, optional): Mobility Controller Downloadable Role Configuration,aos_cx_config (AOSCXConfig, optional): AOS-CX Downloadable Role Configuration}ArubaOSSwitchConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policy_name (string, optional): Policy name,controller_static_role (string, optional): Controller Static Role,controller_downloadable_role (string, optional): Controller Downloadable Role,vlan_id (string, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,vlan_tagged_id (string, optional): VLAN ID Tagged,vlan_tagged_name (string, optional): VLAN Name Tagged,reauth_period (string, optional): Re-Authentication Period <0-999999999>,logoff_period (string, optional): Logoff Period <0(mac-pin) OR 60-9999999>,cached_reauth_period (string, optional): Cached Re-Authentication Period <60-2147483647>,enable_device_config (boolean, optional): Enable Device Configuration,enable_poe_allocate_by_class (boolean, optional): Enable POE Allocate By Class,poe_priority (string, optional) = ['low' or 'high' or 'critical']: POE Priority,enable_admin_edge_port (boolean, optional): Enable Admin Edge Port,enable_port_mode (boolean, optional): Enable Port Mode}MASConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,policer_profile_name (string, optional): Policer Profile name,qos_profile_name (string, optional): QoS Profile name,voip_profile_name (string, optional): VoIP Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,acl_list (array[acl], optional): Access Control List}acl {name (string, optional): Name of the ACL,type (string, optional) = ['Ethertype' or 'MAC' or 'Stateless' or 'Session']: Type of the ACL}AMCConfig {captive_portal_profile_name (string, optional): Captive Portal Profile name,reauth_interval (integer, optional): Re-authentication Interval Time (0-4096),vlan_id (integer, optional): VLAN ID <1-4094>,vlan_name (string, optional): VLAN Name,parameterized_vlan (string, optional): Parameterized VLAN,acl_list (array[acl], optional): Access Control List}AOSCXConfig {role_name (string, optional): Role name,description (string, optional): Description,captive_portal_name (string, optional): Captive Portal name,authentication_mode (string, optional) = ['' or 'client-mode' or 'device-mode' or 'multi-domain-mode']: Authentication Mode,device_traffic_class (string, optional) = ['None' or 'Voice']: Device Traffic Class,session_timeout_type (string, optional) = ['Static' or 'Parameterized']: Session Timeout Type,session_timeout (string, optional): Session Timeout <1-4294967295>,parameterized_session_timeout (string, optional): Parameterized Session Timeout,cached_reauth_period (string, optional): Cached Re-authentication period <30-4294967295>,reauth_period_type (string, optional) = ['Manual' or 'Random' or 'Parameterized']: Re-Authentication Period Type,reauth_period (string, optional): Re-Authentication Period <1-4294967295>,minimum_reauth_period (string, optional): Minimum re-authentication period <1-4294967295>,parameterized_reauth (string, optional): Parameterized Re-Authentication,client_inactivity_timeout_type (string, optional) = ['Value' or 'None' or 'Parameterized']: Client Inactivity Timeout Type,client_inactivity_timeout (string, optional): Client Inactivity Timeout value <300-4294967295>,parameterized_client_inactivity_timeout (string, optional): Parameterized Client Inactivity Timeout,allowed_vlan_ids_trunk (string, optional): Allowed VLANs on Trunk <1-4094>,allowed_vlan_names_trunk (string, optional): List of Allowed VLAN Names on Trunk,parameterized_allowed_vlan_type (string, optional) = ['Id' or 'Name']: Parameterized Allowed VLAN Type,parameterized_allowed_vlan (string, optional): Parameterized Allowed VLAN,native_trunk_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Native Trunk VLAN Type,native_trunk_vlan_id (string, optional): Native Trunk VLAN <1-4094>,native_trunk_vlan_name (string, optional): Native Trunk VLAN Name,parameterized_native_trunk_vlan (string, optional): Parameterized Native Trunk VLAN,access_vlan_type (string, optional) = ['Id' or 'Name' or 'Parameterized']: Access VLAN Type,access_vlan_id (string, optional): Access VLAN <1-4094>,access_vlan_name (string, optional): Access VLAN Name,parameterized_access_vlan (string, optional): Parameterized Access VLAN,gateway_zone (string, optional): Gateway Zone,secondary_role_type (string, optional) = ['None' or 'Static' or 'Dynamic']: Secondary Role Type,gateway_static_role (string, optional): Gateway Static Role,gateway_downloadable_role (string, optional): Gateway Downloadable Role,mtu (string, optional): MTU <68-9198>,trust_mode (string, optional) = ['' or 'none' or 'cos' or 'dscp']: Trust Mode,poe_priority (string, optional) = ['' or 'low' or 'high' or 'critical']: PoE Priority,private_vlan_port_type (string, optional) = ['' or 'promiscuous' or 'secondary']: Private VLAN Port Type,policy_name (string, optional): Policy name}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "type": "",
          "agent_template": "",
          "post_auth_template": "",
          "radius_dyn_authz_template": "",
          "action": "",
          "device_group_list": [
            ""
          ],
          "attributes": [
            {
              "type": "",
              "name": "",
              "value": ""
            }
          ],
          "tacacs_service_params": {
            "privilege_level": 0,
            "services": [
              ""
            ],
            "authorize_attribute_status": "",
            "tacacs_command_config": {
              "service_type": "",
              "permit_unmatched_cmds": false,
              "commands": [
                {
                  "command": "",
                  "permit_unmatched_args": false,
                  "command_args": [
                    {
                      "argument": "",
                      "permit_action": false
                    }
                  ]
                }
              ]
            }
          },
          "dur_config": {
            "config_mode": "",
            "product": "",
            "aruba_os_switch_config": {
              "captive_portal_profile_name": "",
              "policy_name": "",
              "controller_static_role": "",
              "controller_downloadable_role": "",
              "vlan_id": "",
              "vlan_name": "",
              "vlan_tagged_id": "",
              "vlan_tagged_name": "",
              "reauth_period": "",
              "logoff_period": "",
              "cached_reauth_period": "",
              "enable_device_config": false,
              "enable_poe_allocate_by_class": false,
              "poe_priority": "",
              "enable_admin_edge_port": false,
              "enable_port_mode": false
            },
            "mobility_access_switch_config": {
              "captive_portal_profile_name": "",
              "policer_profile_name": "",
              "qos_profile_name": "",
              "voip_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "mobility_controller_config": {
              "captive_portal_profile_name": "",
              "reauth_interval": 0,
              "vlan_id": 0,
              "vlan_name": "",
              "parameterized_vlan": "",
              "acl_list": [
                {
                  "name": "",
                  "type": ""
                }
              ]
            },
            "aos_cx_config": {
              "role_name": "",
              "description": "",
              "captive_portal_name": "",
              "authentication_mode": "",
              "device_traffic_class": "",
              "session_timeout_type": "",
              "session_timeout": "",
              "parameterized_session_timeout": "",
              "cached_reauth_period": "",
              "reauth_period_type": "",
              "reauth_period": "",
              "minimum_reauth_period": "",
              "parameterized_reauth": "",
              "client_inactivity_timeout_type": "",
              "client_inactivity_timeout": "",
              "parameterized_client_inactivity_timeout": "",
              "allowed_vlan_ids_trunk": "",
              "allowed_vlan_names_trunk": "",
              "parameterized_allowed_vlan_type": "",
              "parameterized_allowed_vlan": "",
              "native_trunk_vlan_type": "",
              "native_trunk_vlan_id": "",
              "native_trunk_vlan_name": "",
              "parameterized_native_trunk_vlan": "",
              "access_vlan_type": "",
              "access_vlan_id": "",
              "access_vlan_name": "",
              "parameterized_access_vlan": "",
              "gateway_zone": "",
              "secondary_role_type": "",
              "gateway_static_role": "",
              "gateway_downloadable_role": "",
              "mtu": "",
              "trust_mode": "",
              "poe_priority": "",
              "private_vlan_port_type": "",
              "policy_name": ""
            }
          }
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: name, Description: name of the enforcement profile
        """
        url_path = "/enforcement-profile/name/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:EthertypeAccessControlList
    # Function Section Description: Manage Ethertype Access Control List

    def get_enforcement_profile_dur_ethertype_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Ethertype Access Control Lists
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- EthertypeAccessControlListPost {name (string): Name of the Ethertype Access Control List,rules (array[RulesPost], optional): Rules of the Ethertype Access Control List}RulesPost {action (string, optional) = ['permit' or 'deny']: Action,ethertype_type (string, optional) = ['any' or 'value']: Ethertype Type,ethertype_value (integer, optional): Ethertype Value (0-65535),subnet_bits (integer, optional): Subnet Bits (0-65535)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "ethertype_type": "",
              "ethertype_value": 0,
              "subnet_bits": 0
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
                Required Body Parameters (body description)- EthertypeAccessControlListUpdate {name (string, optional): Name of the Ethertype Access Control List,rules (array[Rules], optional): Rules of the Ethertype Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,ethertype_type (string) = ['any' or 'value']: Ethertype Type,ethertype_value (integer, optional): Ethertype Value (0-65535),subnet_bits (integer, optional): Subnet Bits (0-65535)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "ethertype_type": "",
              "ethertype_value": 0,
              "subnet_bits": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
                Required Body Parameters (body description)- EthertypeAccessControlListReplace {name (string, optional): Name of the Ethertype Access Control List,rules (array[Rules], optional): Rules of the Ethertype Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,ethertype_type (string) = ['any' or 'value']: Ethertype Type,ethertype_value (integer, optional): Ethertype Value (0-65535),subnet_bits (integer, optional): Subnet Bits (0-65535)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "ethertype_type": "",
              "ethertype_value": 0,
              "subnet_bits": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: ethertype_access_control_list_id, Description: Numeric ID of the Ethertype Access Control List
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Ethertype Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Ethertype Access Control List
                Required Body Parameters (body description)- EthertypeAccessControlListUpdate {name (string, optional): Name of the Ethertype Access Control List,rules (array[Rules], optional): Rules of the Ethertype Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,ethertype_type (string) = ['any' or 'value']: Ethertype Type,ethertype_value (integer, optional): Ethertype Value (0-65535),subnet_bits (integer, optional): Subnet Bits (0-65535)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "ethertype_type": "",
              "ethertype_value": 0,
              "subnet_bits": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Ethertype Access Control List
                Required Body Parameters (body description)- EthertypeAccessControlListReplace {name (string, optional): Name of the Ethertype Access Control List,rules (array[Rules], optional): Rules of the Ethertype Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,ethertype_type (string) = ['any' or 'value']: Ethertype Type,ethertype_value (integer, optional): Ethertype Value (0-65535),subnet_bits (integer, optional): Subnet Bits (0-65535)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "ethertype_type": "",
              "ethertype_value": 0,
              "subnet_bits": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Ethertype Access Control List
        """
        url_path = "/enforcement-profile-dur/ethertype-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:MACAccessControlList
    # Function Section Description: Manage MAC Access Control List

    def get_enforcement_profile_dur_mac_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of MAC Access Control Lists
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- MACAccessControlListPost {name (string): Name of the MAC Access Control List,rules (array[RulesPost], optional): Rules of the MAC Access Control List}RulesPost {action (string, optional) = ['permit' or 'deny']: Action,mac_address_type (string, optional) = ['any' or 'host' or 'value']: MAC Address Type,mac_address_value (string, optional): MAC Address Value (eg. AA:BB:CC:DD:EE:FF),subnet_bits (string, optional): Subnet Bits (eg. AA:BB:CC:DD:EE:FF)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "mac_address_type": "",
              "mac_address_value": "",
              "subnet_bits": ""
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
                Required Body Parameters (body description)- MACAccessControlListUpdate {name (string, optional): Name of the MAC Access Control List,rules (array[Rules], optional): Rules of the MAC Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,mac_address_type (string) = ['any' or 'host' or 'value']: MAC Address Type,mac_address_value (string, optional): MAC Address Value (eg. AA:BB:CC:DD:EE:FF),subnet_bits (string, optional): Subnet Bits (eg. AA:BB:CC:DD:EE:FF)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "mac_address_type": "",
              "mac_address_value": "",
              "subnet_bits": ""
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
                Required Body Parameters (body description)- MACAccessControlListReplace {name (string, optional): Name of the MAC Access Control List,rules (array[Rules], optional): Rules of the MAC Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,mac_address_type (string) = ['any' or 'host' or 'value']: MAC Address Type,mac_address_value (string, optional): MAC Address Value (eg. AA:BB:CC:DD:EE:FF),subnet_bits (string, optional): Subnet Bits (eg. AA:BB:CC:DD:EE:FF)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "mac_address_type": "",
              "mac_address_value": "",
              "subnet_bits": ""
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: mac_access_control_list_id, Description: Numeric ID of the MAC Access Control List
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the MAC Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the MAC Access Control List
                Required Body Parameters (body description)- MACAccessControlListUpdate {name (string, optional): Name of the MAC Access Control List,rules (array[Rules], optional): Rules of the MAC Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,mac_address_type (string) = ['any' or 'host' or 'value']: MAC Address Type,mac_address_value (string, optional): MAC Address Value (eg. AA:BB:CC:DD:EE:FF),subnet_bits (string, optional): Subnet Bits (eg. AA:BB:CC:DD:EE:FF)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "mac_address_type": "",
              "mac_address_value": "",
              "subnet_bits": ""
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the MAC Access Control List
                Required Body Parameters (body description)- MACAccessControlListReplace {name (string, optional): Name of the MAC Access Control List,rules (array[Rules], optional): Rules of the MAC Access Control List}Rules {action (string) = ['permit' or 'deny']: Action,mac_address_type (string) = ['any' or 'host' or 'value']: MAC Address Type,mac_address_value (string, optional): MAC Address Value (eg. AA:BB:CC:DD:EE:FF),subnet_bits (string, optional): Subnet Bits (eg. AA:BB:CC:DD:EE:FF)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "action": "",
              "mac_address_type": "",
              "mac_address_value": "",
              "subnet_bits": ""
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the MAC Access Control List
        """
        url_path = "/enforcement-profile-dur/mac-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:NATPool
    # Function Section Description: Manage NAT Pool

    def get_enforcement_profile_dur_nat_pool_by_product_name(self, product_name=""):
        """
        Operation: GET a list of NAT Pools
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- NATPoolPost {name (string): Name of the NAT Pool,start_src_range (string): Start of source NAT range,end_src_range (string): End of source NAT range,destination_nat_ip_address (string, optional): Destination NAT IP Address}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "start_src_range": "",
          "end_src_range": "",
          "destination_nat_ip_address": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: nat_pool_id, Description: Numeric ID of the NAT Pool
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: nat_pool_id, Description: Numeric ID of the NAT Pool
                Required Body Parameters (body description)- NATPoolUpdate {name (string, optional): Name of the NAT Pool,start_src_range (string, optional): Start of source NAT range,end_src_range (string, optional): End of source NAT range,destination_nat_ip_address (string, optional): Destination NAT IP Address}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "start_src_range": "",
          "end_src_range": "",
          "destination_nat_ip_address": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: nat_pool_id, Description: Numeric ID of the NAT Pool
                Required Body Parameters (body description)- NATPoolReplace {name (string): Name of the NAT Pool,start_src_range (string): Start of source NAT range,end_src_range (string): End of source NAT range,destination_nat_ip_address (string, optional): Destination NAT IP Address}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "start_src_range": "",
          "end_src_range": "",
          "destination_nat_ip_address": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: nat_pool_id, Description: Numeric ID of the NAT Pool
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the NAT Pool
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the NAT Pool
                Required Body Parameters (body description)- NATPoolUpdate {name (string, optional): Name of the NAT Pool,start_src_range (string, optional): Start of source NAT range,end_src_range (string, optional): End of source NAT range,destination_nat_ip_address (string, optional): Destination NAT IP Address}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "start_src_range": "",
          "end_src_range": "",
          "destination_nat_ip_address": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the NAT Pool
                Required Body Parameters (body description)- NATPoolReplace {name (string): Name of the NAT Pool,start_src_range (string): Start of source NAT range,end_src_range (string): End of source NAT range,destination_nat_ip_address (string, optional): Destination NAT IP Address}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "start_src_range": "",
          "end_src_range": "",
          "destination_nat_ip_address": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the NAT Pool
        """
        url_path = "/enforcement-profile-dur/nat-pool/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:NetDestination
    # Function Section Description: Manage Net Destination

    def get_enforcement_profile_dur_net_destination_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Net Destinations
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- NetDestinationPost {name (string): Name of the Net Destination,invert (boolean, optional): Invert for Mobility Access Switch and Mobility Controller Net Destination,rules (array[RulesPost]): Rules for the Net Destination}RulesPost {rule_type (string, optional) = ['host' or 'network' or 'name' or 'range']: Rule Type,ip_address (string): IP Address,netmask (string): Netmask,end_ip_address (string): End IP Address,host_name (string): Host Name or Domain,position (integer): Position (1-220) for ArubaOS-Switch Net Destination rule}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "invert": false,
          "rules": [
            {
              "rule_type": "",
              "ip_address": "",
              "netmask": "",
              "end_ip_address": "",
              "host_name": "",
              "position": 0
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: net_destination_id, Description: Numeric ID of the Net Destination
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: net_destination_id, Description: Numeric ID of the Net Destination
                Required Body Parameters (body description)- NetDestinationUpdate {name (string, optional): Name of the Net Destination,invert (boolean, optional): Invert for Mobility Access Switch and Mobility Controller Net Destination,rules (array[Rules], optional): Rules for the Net Destination}Rules {rule_type (string) = ['host' or 'network' or 'name' or 'range']: Rule Type,ip_address (string): IP Address,netmask (string): Netmask,end_ip_address (string): End IP Address,host_name (string): Host Name or Domain,position (integer): Position (1-220) for ArubaOS-Switch Net Destination rule}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "invert": false,
          "rules": [
            {
              "rule_type": "",
              "ip_address": "",
              "netmask": "",
              "end_ip_address": "",
              "host_name": "",
              "position": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: net_destination_id, Description: Numeric ID of the Net Destination
                Required Body Parameters (body description)- NetDestinationReplace {name (string, optional): Name of the Net Destination,invert (boolean, optional): Invert for Mobility Access Switch and Mobility Controller Net Destination,rules (array[Rules], optional): Rules for the Net Destination}Rules {rule_type (string) = ['host' or 'network' or 'name' or 'range']: Rule Type,ip_address (string): IP Address,netmask (string): Netmask,end_ip_address (string): End IP Address,host_name (string): Host Name or Domain,position (integer): Position (1-220) for ArubaOS-Switch Net Destination rule}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "invert": false,
          "rules": [
            {
              "rule_type": "",
              "ip_address": "",
              "netmask": "",
              "end_ip_address": "",
              "host_name": "",
              "position": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: net_destination_id, Description: Numeric ID of the Net Destination
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Net Destination
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Net Destination
                Required Body Parameters (body description)- NetDestinationUpdate {name (string, optional): Name of the Net Destination,invert (boolean, optional): Invert for Mobility Access Switch and Mobility Controller Net Destination,rules (array[Rules], optional): Rules for the Net Destination}Rules {rule_type (string) = ['host' or 'network' or 'name' or 'range']: Rule Type,ip_address (string): IP Address,netmask (string): Netmask,end_ip_address (string): End IP Address,host_name (string): Host Name or Domain,position (integer): Position (1-220) for ArubaOS-Switch Net Destination rule}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "invert": false,
          "rules": [
            {
              "rule_type": "",
              "ip_address": "",
              "netmask": "",
              "end_ip_address": "",
              "host_name": "",
              "position": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Net Destination
                Required Body Parameters (body description)- NetDestinationReplace {name (string, optional): Name of the Net Destination,invert (boolean, optional): Invert for Mobility Access Switch and Mobility Controller Net Destination,rules (array[Rules], optional): Rules for the Net Destination}Rules {rule_type (string) = ['host' or 'network' or 'name' or 'range']: Rule Type,ip_address (string): IP Address,netmask (string): Netmask,end_ip_address (string): End IP Address,host_name (string): Host Name or Domain,position (integer): Position (1-220) for ArubaOS-Switch Net Destination rule}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "invert": false,
          "rules": [
            {
              "rule_type": "",
              "ip_address": "",
              "netmask": "",
              "end_ip_address": "",
              "host_name": "",
              "position": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Net Destination
        """
        url_path = "/enforcement-profile-dur/net-destination/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:NetService
    # Function Section Description: Manage Net Services

    def get_enforcement_profile_dur_net_service_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Net Services
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- NetServicePost {name (string): Name of the Net Service,description (string, optional): Description of the Net Service,protocol (string, optional) = ['TCP' or 'UDP' or 'IP']: Protocol of the Net Service,port_selection (string, optional) = ['List' or 'Range' or 'Port']: Port Selection of the Net Service. Port is not applicable for MAS and AMC products,port_list (string, optional): Comma separated Port values of the Net Service,port (integer, optional): Port of the Net Service (1-65535),max_port (integer, optional): Max Port of the Net Service (1-65535),ip_protocol_number (integer, optional): IP Protocol Number of the Net Service (0-255),application_level_gateway (string, optional) = ['dhcp' or 'dns' or 'ftp' or 'noe' or 'rtsp' or 'sccp' or 'sip' or 'sips' or 'svp' or 'tftp' or 'vocera']: Application Level Gateway of the Net Service}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "protocol": "",
          "port_selection": "",
          "port_list": "",
          "port": 0,
          "max_port": 0,
          "ip_protocol_number": 0,
          "application_level_gateway": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: net_service_id, Description: Numeric ID of the Net Service
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: net_service_id, Description: Numeric ID of the Net Service
                Required Body Parameters (body description)- NetServiceUpdate {name (string, optional): Name of the Net Service,description (string, optional): Description of the Net Service,protocol (string, optional) = ['TCP' or 'UDP' or 'IP']: Protocol of the Net Service,port_selection (string, optional) = ['List' or 'Range' or 'Port']: Port Selection of the Net Service. Port is not applicable for MAS and AMC products,port_list (string, optional): Comma separated Port values of the Net Service,port (integer, optional): Port of the Net Service (1-65535),max_port (integer, optional): Max Port of the Net Service (1-65535),ip_protocol_number (integer, optional): IP Protocol Number of the Net Service (0-255),application_level_gateway (string, optional) = ['dhcp' or 'dns' or 'ftp' or 'noe' or 'rtsp' or 'sccp' or 'sip' or 'sips' or 'svp' or 'tftp' or 'vocera']: Application Level Gateway of the Net Service}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "protocol": "",
          "port_selection": "",
          "port_list": "",
          "port": 0,
          "max_port": 0,
          "ip_protocol_number": 0,
          "application_level_gateway": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: net_service_id, Description: Numeric ID of the Net Service
                Required Body Parameters (body description)- NetServiceReplace {name (string): Name of the Net Service,description (string): Description of the Net Service,protocol (string) = ['TCP' or 'UDP' or 'IP']: Protocol of the Net Service,port_selection (string, optional) = ['List' or 'Range' or 'Port']: Port Selection of the Net Service. Port is not applicable for MAS and AMC products,port_list (string, optional): Comma separated Port values of the Net Service,port (integer, optional): Port of the Net Service (1-65535),max_port (integer, optional): Max Port of the Net Service (1-65535),ip_protocol_number (integer, optional): IP Protocol Number of the Net Service (0-255),application_level_gateway (string, optional) = ['dhcp' or 'dns' or 'ftp' or 'noe' or 'rtsp' or 'sccp' or 'sip' or 'sips' or 'svp' or 'tftp' or 'vocera']: Application Level Gateway of the Net Service}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "protocol": "",
          "port_selection": "",
          "port_list": "",
          "port": 0,
          "max_port": 0,
          "ip_protocol_number": 0,
          "application_level_gateway": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: net_service_id, Description: Numeric ID of the Net Service
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Net Service
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Net Service
                Required Body Parameters (body description)- NetServiceUpdate {name (string, optional): Name of the Net Service,description (string, optional): Description of the Net Service,protocol (string, optional) = ['TCP' or 'UDP' or 'IP']: Protocol of the Net Service,port_selection (string, optional) = ['List' or 'Range' or 'Port']: Port Selection of the Net Service. Port is not applicable for MAS and AMC products,port_list (string, optional): Comma separated Port values of the Net Service,port (integer, optional): Port of the Net Service (1-65535),max_port (integer, optional): Max Port of the Net Service (1-65535),ip_protocol_number (integer, optional): IP Protocol Number of the Net Service (0-255),application_level_gateway (string, optional) = ['dhcp' or 'dns' or 'ftp' or 'noe' or 'rtsp' or 'sccp' or 'sip' or 'sips' or 'svp' or 'tftp' or 'vocera']: Application Level Gateway of the Net Service}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "protocol": "",
          "port_selection": "",
          "port_list": "",
          "port": 0,
          "max_port": 0,
          "ip_protocol_number": 0,
          "application_level_gateway": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Net Service
                Required Body Parameters (body description)- NetServiceReplace {name (string): Name of the Net Service,description (string): Description of the Net Service,protocol (string) = ['TCP' or 'UDP' or 'IP']: Protocol of the Net Service,port_selection (string, optional) = ['List' or 'Range' or 'Port']: Port Selection of the Net Service. Port is not applicable for MAS and AMC products,port_list (string, optional): Comma separated Port values of the Net Service,port (integer, optional): Port of the Net Service (1-65535),max_port (integer, optional): Max Port of the Net Service (1-65535),ip_protocol_number (integer, optional): IP Protocol Number of the Net Service (0-255),application_level_gateway (string, optional) = ['dhcp' or 'dns' or 'ftp' or 'noe' or 'rtsp' or 'sccp' or 'sip' or 'sips' or 'svp' or 'tftp' or 'vocera']: Application Level Gateway of the Net Service}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "description": "",
          "protocol": "",
          "port_selection": "",
          "port_list": "",
          "port": 0,
          "max_port": 0,
          "ip_protocol_number": 0,
          "application_level_gateway": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Net Service
        """
        url_path = "/enforcement-profile-dur/net-service/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:PolicerProfile
    # Function Section Description: Manage Policer Profile

    def get_enforcement_profile_dur_policer_profile_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Policer Profiles
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- PolicerProfilePost {name (string): Name of the Policer Profile,cbs (integer, optional): CBS (Bytes) of the Policer Profile,cir (integer, optional): CIR (Kbps) of the Policer Profile,ebs (integer, optional): EBS (Bytes) of the Policer Profile,exceed_action (string, optional): Exceed Action of the Policer Profile,exceed_qos_profile (string, optional): Exceed QoS Profile of the Policer Profile,violate_action (string, optional): Violate Action of the Policer Profile,violate_qos_profile (string, optional): Violate QoS Profile of the Policer Profile}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "cbs": 0,
          "cir": 0,
          "ebs": 0,
          "exceed_action": "",
          "exceed_qos_profile": "",
          "violate_action": "",
          "violate_qos_profile": ""
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: policer_profile_id, Description: Numeric ID of the Policer Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: policer_profile_id, Description: Numeric ID of the Policer Profile
                Required Body Parameters (body description)- PolicerProfileUpdate {name (string, optional): Name of the Policer Profile,cbs (integer, optional): CBS (Bytes) of the Policer Profile,cir (integer, optional): CIR (Kbps) of the Policer Profile,ebs (integer, optional): EBS (Bytes) of the Policer Profile,exceed_action (string, optional): Exceed Action of the Policer Profile,exceed_qos_profile (string, optional): Exceed QoS Profile of the Policer Profile,violate_action (string, optional): Violate Action of the Policer Profile,violate_qos_profile (string, optional): Violate QoS Profile of the Policer Profile}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "cbs": 0,
          "cir": 0,
          "ebs": 0,
          "exceed_action": "",
          "exceed_qos_profile": "",
          "violate_action": "",
          "violate_qos_profile": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: policer_profile_id, Description: Numeric ID of the Policer Profile
                Required Body Parameters (body description)- PolicerProfileReplace {name (string): Name of the Policer Profile,cbs (integer, optional): CBS (Bytes) of the Policer Profile,cir (integer, optional): CIR (Kbps) of the Policer Profile,ebs (integer, optional): EBS (Bytes) of the Policer Profile,exceed_action (string, optional): Exceed Action of the Policer Profile,exceed_qos_profile (string, optional): Exceed QoS Profile of the Policer Profile,violate_action (string, optional): Violate Action of the Policer Profile,violate_qos_profile (string, optional): Violate QoS Profile of the Policer Profile}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "cbs": 0,
          "cir": 0,
          "ebs": 0,
          "exceed_action": "",
          "exceed_qos_profile": "",
          "violate_action": "",
          "violate_qos_profile": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: policer_profile_id, Description: Numeric ID of the Policer Profile
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Policer Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Policer Profile
                Required Body Parameters (body description)- PolicerProfileUpdate {name (string, optional): Name of the Policer Profile,cbs (integer, optional): CBS (Bytes) of the Policer Profile,cir (integer, optional): CIR (Kbps) of the Policer Profile,ebs (integer, optional): EBS (Bytes) of the Policer Profile,exceed_action (string, optional): Exceed Action of the Policer Profile,exceed_qos_profile (string, optional): Exceed QoS Profile of the Policer Profile,violate_action (string, optional): Violate Action of the Policer Profile,violate_qos_profile (string, optional): Violate QoS Profile of the Policer Profile}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "cbs": 0,
          "cir": 0,
          "ebs": 0,
          "exceed_action": "",
          "exceed_qos_profile": "",
          "violate_action": "",
          "violate_qos_profile": ""
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Policer Profile
                Required Body Parameters (body description)- PolicerProfileReplace {name (string): Name of the Policer Profile,cbs (integer, optional): CBS (Bytes) of the Policer Profile,cir (integer, optional): CIR (Kbps) of the Policer Profile,ebs (integer, optional): EBS (Bytes) of the Policer Profile,exceed_action (string, optional): Exceed Action of the Policer Profile,exceed_qos_profile (string, optional): Exceed QoS Profile of the Policer Profile,violate_action (string, optional): Violate Action of the Policer Profile,violate_qos_profile (string, optional): Violate QoS Profile of the Policer Profile}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "cbs": 0,
          "cir": 0,
          "ebs": 0,
          "exceed_action": "",
          "exceed_qos_profile": "",
          "violate_action": "",
          "violate_qos_profile": ""
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Policer Profile
        """
        url_path = "/enforcement-profile-dur/policer-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:Policy
    # Function Section Description: Manage Policy

    def get_enforcement_profile_dur_policy_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Policies
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- PolicyPost {name (string): Name of the Policy,rules (array[RulesPost]): Rules of the Policy}RulesPost {number (integer): Number,class_type (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy,class_name (string): Class Name,action (string, optional) = ['permit' or 'drop' or 'deny' or 'redirect']: Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy,dscp (integer, optional): DSCP (0-63),ip_precedence (integer, optional): IP Precedence (0-7),priority (integer, optional): Priority (0-7),rate_limit (integer, optional): Rate Limit in kbps for ArubaOS-Switch policy (0-10000000),committed_information_rate (integer, optional): Committed Information Rate for AOS-CX policy (1-4294967295),committed_burst_size (integer, optional): Committed Burst Size for AOS-CX policy (1-4294967295),exceed_action (string, optional) = ['drop']: Exceed Action for AOS-CX policy,priority_code_point (integer, optional): Priority Code Point for AOS-CX policy (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "number": 0,
              "class_type": "",
              "class_name": "",
              "action": "",
              "dscp": 0,
              "ip_precedence": 0,
              "priority": 0,
              "rate_limit": 0,
              "committed_information_rate": 0,
              "committed_burst_size": 0,
              "exceed_action": "",
              "priority_code_point": 0
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: policy_id, Description: Numeric ID of the Policy
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: policy_id, Description: Numeric ID of the Policy
                Required Body Parameters (body description)- PolicyUpdate {name (string, optional): Name of the Policy,rules (array[RulesPost], optional): Rules of the Policy}RulesPost {number (integer): Number,class_type (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy,class_name (string): Class Name,action (string, optional) = ['permit' or 'drop' or 'deny' or 'redirect']: Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy,dscp (integer, optional): DSCP (0-63),ip_precedence (integer, optional): IP Precedence (0-7),priority (integer, optional): Priority (0-7),rate_limit (integer, optional): Rate Limit in kbps for ArubaOS-Switch policy (0-10000000),committed_information_rate (integer, optional): Committed Information Rate for AOS-CX policy (1-4294967295),committed_burst_size (integer, optional): Committed Burst Size for AOS-CX policy (1-4294967295),exceed_action (string, optional) = ['drop']: Exceed Action for AOS-CX policy,priority_code_point (integer, optional): Priority Code Point for AOS-CX policy (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "number": 0,
              "class_type": "",
              "class_name": "",
              "action": "",
              "dscp": 0,
              "ip_precedence": 0,
              "priority": 0,
              "rate_limit": 0,
              "committed_information_rate": 0,
              "committed_burst_size": 0,
              "exceed_action": "",
              "priority_code_point": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: policy_id, Description: Numeric ID of the Policy
                Required Body Parameters (body description)- PolicyReplace {name (string): Name of the Policy,rules (array[RulesPost]): Rules of the Policy}RulesPost {number (integer): Number,class_type (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy,class_name (string): Class Name,action (string, optional) = ['permit' or 'drop' or 'deny' or 'redirect']: Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy,dscp (integer, optional): DSCP (0-63),ip_precedence (integer, optional): IP Precedence (0-7),priority (integer, optional): Priority (0-7),rate_limit (integer, optional): Rate Limit in kbps for ArubaOS-Switch policy (0-10000000),committed_information_rate (integer, optional): Committed Information Rate for AOS-CX policy (1-4294967295),committed_burst_size (integer, optional): Committed Burst Size for AOS-CX policy (1-4294967295),exceed_action (string, optional) = ['drop']: Exceed Action for AOS-CX policy,priority_code_point (integer, optional): Priority Code Point for AOS-CX policy (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "number": 0,
              "class_type": "",
              "class_name": "",
              "action": "",
              "dscp": 0,
              "ip_precedence": 0,
              "priority": 0,
              "rate_limit": 0,
              "committed_information_rate": 0,
              "committed_burst_size": 0,
              "exceed_action": "",
              "priority_code_point": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: policy_id, Description: Numeric ID of the Policy
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Policy
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Policy
                Required Body Parameters (body description)- PolicyUpdate {name (string, optional): Name of the Policy,rules (array[RulesPost], optional): Rules of the Policy}RulesPost {number (integer): Number,class_type (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy,class_name (string): Class Name,action (string, optional) = ['permit' or 'drop' or 'deny' or 'redirect']: Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy,dscp (integer, optional): DSCP (0-63),ip_precedence (integer, optional): IP Precedence (0-7),priority (integer, optional): Priority (0-7),rate_limit (integer, optional): Rate Limit in kbps for ArubaOS-Switch policy (0-10000000),committed_information_rate (integer, optional): Committed Information Rate for AOS-CX policy (1-4294967295),committed_burst_size (integer, optional): Committed Burst Size for AOS-CX policy (1-4294967295),exceed_action (string, optional) = ['drop']: Exceed Action for AOS-CX policy,priority_code_point (integer, optional): Priority Code Point for AOS-CX policy (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "number": 0,
              "class_type": "",
              "class_name": "",
              "action": "",
              "dscp": 0,
              "ip_precedence": 0,
              "priority": 0,
              "rate_limit": 0,
              "committed_information_rate": 0,
              "committed_burst_size": 0,
              "exceed_action": "",
              "priority_code_point": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Policy
                Required Body Parameters (body description)- PolicyReplace {name (string): Name of the Policy,rules (array[RulesPost]): Rules of the Policy}RulesPost {number (integer): Number,class_type (string, optional) = ['ipv4' or 'ip' or 'ipv6']: Class Type. ipv4 only applies to ArubaOS-Switch policy and ip only applies to AOS-CX policy,class_name (string): Class Name,action (string, optional) = ['permit' or 'drop' or 'deny' or 'redirect']: Action. deny only applies to ArubaOS-Switch policy and drop only applies to AOS-CX policy,dscp (integer, optional): DSCP (0-63),ip_precedence (integer, optional): IP Precedence (0-7),priority (integer, optional): Priority (0-7),rate_limit (integer, optional): Rate Limit in kbps for ArubaOS-Switch policy (0-10000000),committed_information_rate (integer, optional): Committed Information Rate for AOS-CX policy (1-4294967295),committed_burst_size (integer, optional): Committed Burst Size for AOS-CX policy (1-4294967295),exceed_action (string, optional) = ['drop']: Exceed Action for AOS-CX policy,priority_code_point (integer, optional): Priority Code Point for AOS-CX policy (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "number": 0,
              "class_type": "",
              "class_name": "",
              "action": "",
              "dscp": 0,
              "ip_precedence": 0,
              "priority": 0,
              "rate_limit": 0,
              "committed_information_rate": 0,
              "committed_burst_size": 0,
              "exceed_action": "",
              "priority_code_point": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Policy
        """
        url_path = "/enforcement-profile-dur/policy/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:QoSProfile
    # Function Section Description: Manage QoS Profiles

    def get_enforcement_profile_dur_qos_profile_by_product_name(self, product_name=""):
        """
        Operation: GET a list of QoS Profiles
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- QoSProfilePost {name (string): Name of the QoS Profile,traffic_class (integer, optional): Traffic Class of the QoS Profile (0-7),drop_precedence (string, optional) = ['high' or 'low']: Drop Precedence of the QoS Profile,dscp (integer, optional): DSCP of the QoS Profile (0-63),dot1p (integer, optional): 802.1p of the QoS Profile (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic_class": 0,
          "drop_precedence": "",
          "dscp": 0,
          "dot1p": 0
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: qos_profile_id, Description: Numeric ID of the QoS Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: qos_profile_id, Description: Numeric ID of the QoS Profile
                Required Body Parameters (body description)- QoSProfileUpdate {name (string, optional): Name of the QoS Profile,traffic_class (integer, optional): Traffic Class of the QoS Profile (0-7),drop_precedence (string, optional) = ['high' or 'low']: Drop Precedence of the QoS Profile,dscp (integer, optional): DSCP of the QoS Profile (0-63),dot1p (integer, optional): 802.1p of the QoS Profile (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic_class": 0,
          "drop_precedence": "",
          "dscp": 0,
          "dot1p": 0
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: qos_profile_id, Description: Numeric ID of the QoS Profile
                Required Body Parameters (body description)- QoSProfileReplace {name (string, optional): Name of the QoS Profile,traffic_class (integer, optional): Traffic Class of the QoS Profile (0-7),drop_precedence (string, optional) = ['high' or 'low']: Drop Precedence of the QoS Profile,dscp (integer, optional): DSCP of the QoS Profile (0-63),dot1p (integer, optional): 802.1p of the QoS Profile (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic_class": 0,
          "drop_precedence": "",
          "dscp": 0,
          "dot1p": 0
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: qos_profile_id, Description: Numeric ID of the QoS Profile
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the QoS Profile
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the QoS Profile
                Required Body Parameters (body description)- QoSProfileUpdate {name (string, optional): Name of the QoS Profile,traffic_class (integer, optional): Traffic Class of the QoS Profile (0-7),drop_precedence (string, optional) = ['high' or 'low']: Drop Precedence of the QoS Profile,dscp (integer, optional): DSCP of the QoS Profile (0-63),dot1p (integer, optional): 802.1p of the QoS Profile (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic_class": 0,
          "drop_precedence": "",
          "dscp": 0,
          "dot1p": 0
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the QoS Profile
                Required Body Parameters (body description)- QoSProfileReplace {name (string, optional): Name of the QoS Profile,traffic_class (integer, optional): Traffic Class of the QoS Profile (0-7),drop_precedence (string, optional) = ['high' or 'low']: Drop Precedence of the QoS Profile,dscp (integer, optional): DSCP of the QoS Profile (0-63),dot1p (integer, optional): 802.1p of the QoS Profile (0-7)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "traffic_class": 0,
          "drop_precedence": "",
          "dscp": 0,
          "dot1p": 0
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the QoS Profile
        """
        url_path = "/enforcement-profile-dur/qos-profile/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:SessionAccessControlList
    # Function Section Description: Manage Session Access Control List

    def get_enforcement_profile_dur_session_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Session Access Control Lists
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- SessionAccessControlListPost {name (string): Name of the Session Access Control List,rules (array[RulesPost], optional): Rules of the Session Access Control List}RulesPost {src_traffic_match (string, optional) = ['alias' or 'any' or 'host' or 'network' or 'user']: Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string, optional) = ['alias' or 'any' or 'host' or 'network' or 'user']: Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string, optional) = ['any' or 'protocol' or 'service' or 'tcp' or 'udp']: Service Type,protocol_number (integer, optional): Protocol Number (0-255),service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port (0-65535),tcp_max_port (integer, optional): TCP Max Port (0-65535),udp_min_port (integer, optional): UDP Min Port (0-65535),udp_max_port (integer, optional): UDP Max Port (0-65535),action (string, optional) = ['deny' or 'dst-nat' or 'dual-nat' or 'permit' or 'redirect' or 'src-nat']: Action,dst_nat_ip_address (string, optional): Destination NAT IP Address,dst_nat_port (integer, optional): Destination NAT Port (0-65535),network_name (string, optional): Name of Network in FQDN format,dual_nat_pool (string, optional): Dual NAT Pool,tunnel_id (integer, optional): Tunnel ID (1-50),src_nat_pool (string, optional): Source NAT Pool,deny_list_user_if_acl_applied (string, optional) = ['Yes' or 'No']: Deny List User if ACL gets applied,dot1p_priority (integer, optional): 802.1p Priority (0-7),log_if_acl_applied (string, optional) = ['Yes' or 'No']: Log if ACL gets applied,mirror (string, optional) = ['Yes' or 'No']: Mirror,position (integer, optional): Position (1-2000),queue_priority (string, optional) = ['low' or 'high']: Queue Priority,time_range (string, optional): Time Range,tos (integer, optional): TOS (0-63)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "dst_nat_ip_address": "",
              "dst_nat_port": 0,
              "network_name": "",
              "dual_nat_pool": "",
              "tunnel_id": 0,
              "src_nat_pool": "",
              "deny_list_user_if_acl_applied": "",
              "dot1p_priority": 0,
              "log_if_acl_applied": "",
              "mirror": "",
              "position": 0,
              "queue_priority": "",
              "time_range": "",
              "tos": 0
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
                Required Body Parameters (body description)- SessionAccessControlListUpdate {name (string, optional): Name of the Session Access Control List,rules (array[Rules], optional): Rules of the Session Access Control List}Rules {src_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string) = ['any' or 'protocol' or 'service' or 'tcp' or 'udp']: Service Type,protocol_number (integer, optional): Protocol Number (0-255),service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port (0-65535),tcp_max_port (integer, optional): TCP Max Port (0-65535),udp_min_port (integer, optional): UDP Min Port (0-65535),udp_max_port (integer, optional): UDP Max Port (0-65535),action (string) = ['deny' or 'dst-nat' or 'dual-nat' or 'permit' or 'redirect' or 'src-nat']: Action,dst_nat_ip_address (string, optional): Destination NAT IP Address,dst_nat_port (integer, optional): Destination NAT Port (0-65535),network_name (string, optional): Name of Network in FQDN format,dual_nat_pool (string, optional): Dual NAT Pool,tunnel_id (integer, optional): Tunnel ID (1-50),src_nat_pool (string, optional): Source NAT Pool,deny_list_user_if_acl_applied (string) = ['Yes' or 'No']: Deny List User if ACL gets applied,dot1p_priority (integer, optional): 802.1p Priority (0-7),log_if_acl_applied (string) = ['Yes' or 'No']: Log if ACL gets applied,mirror (string) = ['Yes' or 'No']: Mirror,position (integer, optional): Position (1-2000),queue_priority (string, optional) = ['low' or 'high']: Queue Priority,time_range (string, optional): Time Range,tos (integer, optional): TOS (0-63)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "dst_nat_ip_address": "",
              "dst_nat_port": 0,
              "network_name": "",
              "dual_nat_pool": "",
              "tunnel_id": 0,
              "src_nat_pool": "",
              "deny_list_user_if_acl_applied": "",
              "dot1p_priority": 0,
              "log_if_acl_applied": "",
              "mirror": "",
              "position": 0,
              "queue_priority": "",
              "time_range": "",
              "tos": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
                Required Body Parameters (body description)- SessionAccessControlListReplace {name (string, optional): Name of the Session Access Control List,rules (array[Rules], optional): Rules of the Session Access Control List}Rules {src_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string) = ['any' or 'protocol' or 'service' or 'tcp' or 'udp']: Service Type,protocol_number (integer, optional): Protocol Number (0-255),service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port (0-65535),tcp_max_port (integer, optional): TCP Max Port (0-65535),udp_min_port (integer, optional): UDP Min Port (0-65535),udp_max_port (integer, optional): UDP Max Port (0-65535),action (string) = ['deny' or 'dst-nat' or 'dual-nat' or 'permit' or 'redirect' or 'src-nat']: Action,dst_nat_ip_address (string, optional): Destination NAT IP Address,dst_nat_port (integer, optional): Destination NAT Port (0-65535),network_name (string, optional): Name of Network in FQDN format,dual_nat_pool (string, optional): Dual NAT Pool,tunnel_id (integer, optional): Tunnel ID (1-50),src_nat_pool (string, optional): Source NAT Pool,deny_list_user_if_acl_applied (string) = ['Yes' or 'No']: Deny List User if ACL gets applied,dot1p_priority (integer, optional): 802.1p Priority (0-7),log_if_acl_applied (string) = ['Yes' or 'No']: Log if ACL gets applied,mirror (string) = ['Yes' or 'No']: Mirror,position (integer, optional): Position (1-2000),queue_priority (string, optional) = ['low' or 'high']: Queue Priority,time_range (string, optional): Time Range,tos (integer, optional): TOS (0-63)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "dst_nat_ip_address": "",
              "dst_nat_port": 0,
              "network_name": "",
              "dual_nat_pool": "",
              "tunnel_id": 0,
              "src_nat_pool": "",
              "deny_list_user_if_acl_applied": "",
              "dot1p_priority": 0,
              "log_if_acl_applied": "",
              "mirror": "",
              "position": 0,
              "queue_priority": "",
              "time_range": "",
              "tos": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: session_access_control_list_id, Description: Numeric ID of the Session Access Control List
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Session Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Session Access Control List
                Required Body Parameters (body description)- SessionAccessControlListUpdate {name (string, optional): Name of the Session Access Control List,rules (array[Rules], optional): Rules of the Session Access Control List}Rules {src_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string) = ['any' or 'protocol' or 'service' or 'tcp' or 'udp']: Service Type,protocol_number (integer, optional): Protocol Number (0-255),service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port (0-65535),tcp_max_port (integer, optional): TCP Max Port (0-65535),udp_min_port (integer, optional): UDP Min Port (0-65535),udp_max_port (integer, optional): UDP Max Port (0-65535),action (string) = ['deny' or 'dst-nat' or 'dual-nat' or 'permit' or 'redirect' or 'src-nat']: Action,dst_nat_ip_address (string, optional): Destination NAT IP Address,dst_nat_port (integer, optional): Destination NAT Port (0-65535),network_name (string, optional): Name of Network in FQDN format,dual_nat_pool (string, optional): Dual NAT Pool,tunnel_id (integer, optional): Tunnel ID (1-50),src_nat_pool (string, optional): Source NAT Pool,deny_list_user_if_acl_applied (string) = ['Yes' or 'No']: Deny List User if ACL gets applied,dot1p_priority (integer, optional): 802.1p Priority (0-7),log_if_acl_applied (string) = ['Yes' or 'No']: Log if ACL gets applied,mirror (string) = ['Yes' or 'No']: Mirror,position (integer, optional): Position (1-2000),queue_priority (string, optional) = ['low' or 'high']: Queue Priority,time_range (string, optional): Time Range,tos (integer, optional): TOS (0-63)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "dst_nat_ip_address": "",
              "dst_nat_port": 0,
              "network_name": "",
              "dual_nat_pool": "",
              "tunnel_id": 0,
              "src_nat_pool": "",
              "deny_list_user_if_acl_applied": "",
              "dot1p_priority": 0,
              "log_if_acl_applied": "",
              "mirror": "",
              "position": 0,
              "queue_priority": "",
              "time_range": "",
              "tos": 0
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Session Access Control List
                Required Body Parameters (body description)- SessionAccessControlListReplace {name (string, optional): Name of the Session Access Control List,rules (array[Rules], optional): Rules of the Session Access Control List}Rules {src_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string) = ['alias' or 'any' or 'host' or 'network' or 'user']: Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string) = ['any' or 'protocol' or 'service' or 'tcp' or 'udp']: Service Type,protocol_number (integer, optional): Protocol Number (0-255),service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port (0-65535),tcp_max_port (integer, optional): TCP Max Port (0-65535),udp_min_port (integer, optional): UDP Min Port (0-65535),udp_max_port (integer, optional): UDP Max Port (0-65535),action (string) = ['deny' or 'dst-nat' or 'dual-nat' or 'permit' or 'redirect' or 'src-nat']: Action,dst_nat_ip_address (string, optional): Destination NAT IP Address,dst_nat_port (integer, optional): Destination NAT Port (0-65535),network_name (string, optional): Name of Network in FQDN format,dual_nat_pool (string, optional): Dual NAT Pool,tunnel_id (integer, optional): Tunnel ID (1-50),src_nat_pool (string, optional): Source NAT Pool,deny_list_user_if_acl_applied (string) = ['Yes' or 'No']: Deny List User if ACL gets applied,dot1p_priority (integer, optional): 802.1p Priority (0-7),log_if_acl_applied (string) = ['Yes' or 'No']: Log if ACL gets applied,mirror (string) = ['Yes' or 'No']: Mirror,position (integer, optional): Position (1-2000),queue_priority (string, optional) = ['low' or 'high']: Queue Priority,time_range (string, optional): Time Range,tos (integer, optional): TOS (0-63)}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "dst_nat_ip_address": "",
              "dst_nat_port": 0,
              "network_name": "",
              "dual_nat_pool": "",
              "tunnel_id": 0,
              "src_nat_pool": "",
              "deny_list_user_if_acl_applied": "",
              "dot1p_priority": 0,
              "log_if_acl_applied": "",
              "mirror": "",
              "position": 0,
              "queue_priority": "",
              "time_range": "",
              "tos": 0
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Session Access Control List
        """
        url_path = "/enforcement-profile-dur/session-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:StatelessAccessControlList
    # Function Section Description: Manage Stateless Access Control List

    def get_enforcement_profile_dur_stateless_access_control_list_by_product_name(
        self, product_name=""
    ):
        """
        Operation: GET a list of Stateless Access Control Lists
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- StatelessAccessControlListPost {name (string): Name of the Stateless Access Control List,rules (array[RulesPost], optional): Rules of the Stateless Access Control List}RulesPost {src_traffic_match (string, optional): Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string, optional): Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string, optional): Service Type,protocol_number (integer, optional): Protocol Number,service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port,tcp_max_port (integer, optional): TCP Max Port,udp_min_port (integer, optional): UDP Min Port,udp_max_port (integer, optional): UDP Max Port,action (string, optional): Action,redirect_type (string, optional): Redirect Type,ipsec_map_based_redirect (string, optional): Redirect based on IPsec Map,tunnel_id (integer, optional): Tunnel ID,deny_list_user_if_acl_applied (string, optional): Deny List User if ACL gets applied,log_if_acl_applied (string, optional): Log if ACL gets applied,position (integer, optional): Position,policer_profile (string, optional): Policer Profile,qos_profile (string, optional): QoS Profile,time_range (string, optional): Time Range}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "redirect_type": "",
              "ipsec_map_based_redirect": "",
              "tunnel_id": 0,
              "deny_list_user_if_acl_applied": "",
              "log_if_acl_applied": "",
              "position": 0,
              "policer_profile": "",
              "qos_profile": "",
              "time_range": ""
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
                Required Body Parameters (body description)- StatelessAccessControlListUpdate {name (string, optional): Name of the Stateless Access Control List,rules (array[Rules], optional): Rules of the Stateless Access Control List}Rules {src_traffic_match (string): Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string): Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string): Service Type,protocol_number (integer, optional): Protocol Number,service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port,tcp_max_port (integer, optional): TCP Max Port,udp_min_port (integer, optional): UDP Min Port,udp_max_port (integer, optional): UDP Max Port,action (string): Action,redirect_type (string, optional): Redirect Type,ipsec_map_based_redirect (string, optional): Redirect based on IPsec Map,tunnel_id (integer, optional): Tunnel ID,deny_list_user_if_acl_applied (string): Deny List User if ACL gets applied,log_if_acl_applied (string): Log if ACL gets applied,position (integer, optional): Position,policer_profile (string, optional): Policer Profile,qos_profile (string, optional): QoS Profile,time_range (string, optional): Time Range}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "redirect_type": "",
              "ipsec_map_based_redirect": "",
              "tunnel_id": 0,
              "deny_list_user_if_acl_applied": "",
              "log_if_acl_applied": "",
              "position": 0,
              "policer_profile": "",
              "qos_profile": "",
              "time_range": ""
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
                Required Body Parameters (body description)- StatelessAccessControlListReplace {name (string, optional): Name of the Stateless Access Control List,rules (array[Rules], optional): Rules of the Stateless Access Control List}Rules {src_traffic_match (string): Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string): Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string): Service Type,protocol_number (integer, optional): Protocol Number,service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port,tcp_max_port (integer, optional): TCP Max Port,udp_min_port (integer, optional): UDP Min Port,udp_max_port (integer, optional): UDP Max Port,action (string): Action,redirect_type (string, optional): Redirect Type,ipsec_map_based_redirect (string, optional): Redirect based on IPsec Map,tunnel_id (integer, optional): Tunnel ID,deny_list_user_if_acl_applied (string): Deny List User if ACL gets applied,log_if_acl_applied (string): Log if ACL gets applied,position (integer, optional): Position,policer_profile (string, optional): Policer Profile,qos_profile (string, optional): QoS Profile,time_range (string, optional): Time Range}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "redirect_type": "",
              "ipsec_map_based_redirect": "",
              "tunnel_id": 0,
              "deny_list_user_if_acl_applied": "",
              "log_if_acl_applied": "",
              "position": 0,
              "policer_profile": "",
              "qos_profile": "",
              "time_range": ""
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: stateless_access_control_list_id, Description: Numeric ID of the Stateless Access Control List
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Stateless Access Control List
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Stateless Access Control List
                Required Body Parameters (body description)- StatelessAccessControlListUpdate {name (string, optional): Name of the Stateless Access Control List,rules (array[Rules], optional): Rules of the Stateless Access Control List}Rules {src_traffic_match (string): Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string): Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string): Service Type,protocol_number (integer, optional): Protocol Number,service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port,tcp_max_port (integer, optional): TCP Max Port,udp_min_port (integer, optional): UDP Min Port,udp_max_port (integer, optional): UDP Max Port,action (string): Action,redirect_type (string, optional): Redirect Type,ipsec_map_based_redirect (string, optional): Redirect based on IPsec Map,tunnel_id (integer, optional): Tunnel ID,deny_list_user_if_acl_applied (string): Deny List User if ACL gets applied,log_if_acl_applied (string): Log if ACL gets applied,position (integer, optional): Position,policer_profile (string, optional): Policer Profile,qos_profile (string, optional): QoS Profile,time_range (string, optional): Time Range}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "redirect_type": "",
              "ipsec_map_based_redirect": "",
              "tunnel_id": 0,
              "deny_list_user_if_acl_applied": "",
              "log_if_acl_applied": "",
              "position": 0,
              "policer_profile": "",
              "qos_profile": "",
              "time_range": ""
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Stateless Access Control List
                Required Body Parameters (body description)- StatelessAccessControlListReplace {name (string, optional): Name of the Stateless Access Control List,rules (array[Rules], optional): Rules of the Stateless Access Control List}Rules {src_traffic_match (string): Source Traffic Match,src_alias (string, optional): Source Alias,src_ip_address (string, optional): Source IP Address,src_netmask (string, optional): Source Net Mask,dst_traffic_match (string): Destination Traffic Match,dst_alias (string, optional): Destination Alias,dst_ip_address (string, optional): Destination IP Address,dst_netmask (string, optional): Destination Net Mask,service_type (string): Service Type,protocol_number (integer, optional): Protocol Number,service (string, optional): Service,tcp_min_port (integer, optional): TCP Min Port,tcp_max_port (integer, optional): TCP Max Port,udp_min_port (integer, optional): UDP Min Port,udp_max_port (integer, optional): UDP Max Port,action (string): Action,redirect_type (string, optional): Redirect Type,ipsec_map_based_redirect (string, optional): Redirect based on IPsec Map,tunnel_id (integer, optional): Tunnel ID,deny_list_user_if_acl_applied (string): Deny List User if ACL gets applied,log_if_acl_applied (string): Log if ACL gets applied,position (integer, optional): Position,policer_profile (string, optional): Policer Profile,qos_profile (string, optional): QoS Profile,time_range (string, optional): Time Range}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "rules": [
            {
              "src_traffic_match": "",
              "src_alias": "",
              "src_ip_address": "",
              "src_netmask": "",
              "dst_traffic_match": "",
              "dst_alias": "",
              "dst_ip_address": "",
              "dst_netmask": "",
              "service_type": "",
              "protocol_number": 0,
              "service": "",
              "tcp_min_port": 0,
              "tcp_max_port": 0,
              "udp_min_port": 0,
              "udp_max_port": 0,
              "action": "",
              "redirect_type": "",
              "ipsec_map_based_redirect": "",
              "tunnel_id": 0,
              "deny_list_user_if_acl_applied": "",
              "log_if_acl_applied": "",
              "position": 0,
              "policer_profile": "",
              "qos_profile": "",
              "time_range": ""
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Stateless Access Control List
        """
        url_path = "/enforcement-profile-dur/stateless-access-control-list/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:TimeRange
    # Function Section Description: Manage Time Range

    def get_enforcement_profile_dur_time_range_by_product_name(self, product_name=""):
        """
        Operation: GET a list of Time Ranges
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
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
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Body Parameters (body description)- TimeRangePost {name (string): Name of the Time Range,type (string, optional) = ['Absolute' or 'Periodic']: Type of the Time Range,rules (array[RulesPost]): Rules of the Time Range}RulesPost {start_day_or_date (string) = ['Daily' or 'Weekend' or 'Weekday' or 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: Start day for Periodic Time Range or Start date for Absolute Time Range,end_day_or_date (string) = ['Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: End Day for Periodic Time Range or End date for Absolute Time Range,start_time (string): Start time,end_time (string): End Time}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "type": "",
          "rules": [
            {
              "start_day_or_date": "",
              "end_day_or_date": "",
              "start_time": "",
              "end_time": ""
            }
          ]
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: time_range_id, Description: Numeric ID of the Time Range
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: time_range_id, Description: Numeric ID of the Time Range
                Required Body Parameters (body description)- TimeRangeUpdate {name (string, optional): Name of the Time Range,type (string, optional) = ['Absolute' or 'Periodic']: Type of the Time Range,rules (array[Rules], optional): Rules of the Time Range}Rules {start_day_or_date (string) = ['Daily' or 'Weekend' or 'Weekday' or 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: Start day for Periodic Time Range or Start date for Absolute Time Range,end_day_or_date (string) = ['Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: End Day for Periodic Time Range or End date for Absolute Time Range,start_time (string): Start time,end_time (string): End Time}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "type": "",
          "rules": [
            {
              "start_day_or_date": "",
              "end_day_or_date": "",
              "start_time": "",
              "end_time": ""
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: time_range_id, Description: Numeric ID of the Time Range
                Required Body Parameters (body description)- TimeRangeReplace {name (string, optional): Name of the Time Range,type (string, optional) = ['Absolute' or 'Periodic']: Type of the Time Range,rules (array[Rules], optional): Rules of the Time Range}Rules {start_day_or_date (string) = ['Daily' or 'Weekend' or 'Weekday' or 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: Start day for Periodic Time Range or Start date for Absolute Time Range,end_day_or_date (string) = ['Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: End Day for Periodic Time Range or End date for Absolute Time Range,start_time (string): Start time,end_time (string): End Time}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "type": "",
          "rules": [
            {
              "start_day_or_date": "",
              "end_day_or_date": "",
              "start_time": "",
              "end_time": ""
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: time_range_id, Description: Numeric ID of the Time Range
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
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Time Range
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Time Range
                Required Body Parameters (body description)- TimeRangeUpdate {name (string, optional): Name of the Time Range,type (string, optional) = ['Absolute' or 'Periodic']: Type of the Time Range,rules (array[Rules], optional): Rules of the Time Range}Rules {start_day_or_date (string) = ['Daily' or 'Weekend' or 'Weekday' or 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: Start day for Periodic Time Range or Start date for Absolute Time Range,end_day_or_date (string) = ['Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: End Day for Periodic Time Range or End date for Absolute Time Range,start_time (string): Start time,end_time (string): End Time}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "type": "",
          "rules": [
            {
              "start_day_or_date": "",
              "end_day_or_date": "",
              "start_time": "",
              "end_time": ""
            }
          ]
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
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: product_name, Description: Product Name
                Required Path Parameter Name: name, Description: Name of the Time Range
                Required Body Parameters (body description)- TimeRangeReplace {name (string, optional): Name of the Time Range,type (string, optional) = ['Absolute' or 'Periodic']: Type of the Time Range,rules (array[Rules], optional): Rules of the Time Range}Rules {start_day_or_date (string) = ['Daily' or 'Weekend' or 'Weekday' or 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: Start day for Periodic Time Range or Start date for Absolute Time Range,end_day_or_date (string) = ['Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday']: End Day for Periodic Time Range or End date for Absolute Time Range,start_time (string): Start time,end_time (string): End Time}
                Required Body Parameters (type(dict) body example)- {
          "name": "",
          "type": "",
          "rules": [
            {
              "start_day_or_date": "",
              "end_day_or_date": "",
              "start_time": "",
              "end_time": ""
            }
          ]
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
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: product_name, Description: Product Name
        Required Path Parameter Name: name, Description: Name of the Time Range
        """
        url_path = "/enforcement-profile-dur/time-range/{product_name}/name/{name}"
        dict_path = {"product_name": product_name, "name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
