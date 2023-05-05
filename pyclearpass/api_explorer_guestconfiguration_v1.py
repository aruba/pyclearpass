from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_guestconfiguration_v1.py


class ApiGuestConfiguration(ClearPassAPILogin):
    # Function Section Name:DigitalPassTemplate
    # Function Section Description: Manage pass templates

    def get_template_pass(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of pass templates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default -id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/template/pass"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_template_pass(self, body=({})):
        """
                Operation: Create a new pass template
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- DigitalPassTemplate {id (integer, optional),name (string, optional),description (string, optional),background_color (string, optional),foreground_color (string, optional),reset (string, optional),label_color (string, optional),summary_template (string, optional),pass_style (string, optional),transit_type (string, optional),icon_image (string, optional),logo_image (string, optional),logo_text_template (string, optional),background_image (integer, optional),thumbnail_image (integer, optional),strip_image (integer, optional),strip_shine (string, optional),footer_image (integer, optional),pass_fields (array[string], optional),relevant_locations (boolean, optional),pass_locations (array[string], optional),relevant_date (boolean, optional),relevant_date_mode (string, optional),relevant_date_rank (integer, optional),relevant_date_template (string, optional),associated_apps (boolean, optional),pass_apps (array[string], optional)}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "description": "",
          "background_color": "",
          "foreground_color": "",
          "reset": "",
          "label_color": "",
          "summary_template": "",
          "pass_style": "",
          "transit_type": "",
          "icon_image": "",
          "logo_image": "",
          "logo_text_template": "",
          "background_image": 0,
          "thumbnail_image": 0,
          "strip_image": 0,
          "strip_shine": "",
          "footer_image": 0,
          "pass_fields": [
            ""
          ],
          "relevant_locations": false,
          "pass_locations": [
            ""
          ],
          "relevant_date": false,
          "relevant_date_mode": "",
          "relevant_date_rank": 0,
          "relevant_date_template": "",
          "associated_apps": false,
          "pass_apps": [
            ""
          ]
        }
        """
        url_path = "/template/pass"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_template_pass_by_id(self, id=""):
        """
        Operation: Get a pass template
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/template/pass/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_template_pass_by_id(self, id="", body=({})):
        """
                Operation: Update some fields of a pass template
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: URL parameter id
                Required Body Parameters (body description)- DigitalPassTemplate {id (integer, optional),name (string, optional),description (string, optional),background_color (string, optional),foreground_color (string, optional),reset (string, optional),label_color (string, optional),summary_template (string, optional),pass_style (string, optional),transit_type (string, optional),icon_image (string, optional),logo_image (string, optional),logo_text_template (string, optional),background_image (integer, optional),thumbnail_image (integer, optional),strip_image (integer, optional),strip_shine (string, optional),footer_image (integer, optional),pass_fields (array[string], optional),relevant_locations (boolean, optional),pass_locations (array[string], optional),relevant_date (boolean, optional),relevant_date_mode (string, optional),relevant_date_rank (integer, optional),relevant_date_template (string, optional),associated_apps (boolean, optional),pass_apps (array[string], optional)}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "description": "",
          "background_color": "",
          "foreground_color": "",
          "reset": "",
          "label_color": "",
          "summary_template": "",
          "pass_style": "",
          "transit_type": "",
          "icon_image": "",
          "logo_image": "",
          "logo_text_template": "",
          "background_image": 0,
          "thumbnail_image": 0,
          "strip_image": 0,
          "strip_shine": "",
          "footer_image": 0,
          "pass_fields": [
            ""
          ],
          "relevant_locations": false,
          "pass_locations": [
            ""
          ],
          "relevant_date": false,
          "relevant_date_mode": "",
          "relevant_date_rank": 0,
          "relevant_date_template": "",
          "associated_apps": false,
          "pass_apps": [
            ""
          ]
        }
        """
        url_path = "/template/pass/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_template_pass_by_id(self, id="", body=({})):
        """
                Operation: Replace a pass template
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: URL parameter id
                Required Body Parameters (body description)- DigitalPassTemplate {id (integer, optional),name (string, optional),description (string, optional),background_color (string, optional),foreground_color (string, optional),reset (string, optional),label_color (string, optional),summary_template (string, optional),pass_style (string, optional),transit_type (string, optional),icon_image (string, optional),logo_image (string, optional),logo_text_template (string, optional),background_image (integer, optional),thumbnail_image (integer, optional),strip_image (integer, optional),strip_shine (string, optional),footer_image (integer, optional),pass_fields (array[string], optional),relevant_locations (boolean, optional),pass_locations (array[string], optional),relevant_date (boolean, optional),relevant_date_mode (string, optional),relevant_date_rank (integer, optional),relevant_date_template (string, optional),associated_apps (boolean, optional),pass_apps (array[string], optional)}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "description": "",
          "background_color": "",
          "foreground_color": "",
          "reset": "",
          "label_color": "",
          "summary_template": "",
          "pass_style": "",
          "transit_type": "",
          "icon_image": "",
          "logo_image": "",
          "logo_text_template": "",
          "background_image": 0,
          "thumbnail_image": 0,
          "strip_image": 0,
          "strip_shine": "",
          "footer_image": 0,
          "pass_fields": [
            ""
          ],
          "relevant_locations": false,
          "pass_locations": [
            ""
          ],
          "relevant_date": false,
          "relevant_date_mode": "",
          "relevant_date_rank": 0,
          "relevant_date_template": "",
          "associated_apps": false,
          "pass_apps": [
            ""
          ]
        }
        """
        url_path = "/template/pass/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_template_pass_by_id(self, id=""):
        """
        Operation: Delete a pass template
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/template/pass/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:GuestAuthenticationConfiguration
    # Function Section Description: Manage settings in Configuration -> Authentication

    def get_guest_authentication(self, id=""):
        """
        Operation: Return settings from Configuration -> Authentication
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/guest/authentication"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_guest_authentication(self, body=({})):
        """
                Operation: Modify settings at Configuration -> Authentication
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- GuestAuthenticationConfiguration {g_admin_access_guest_require_https (boolean, optional): If checked, HTTP access by guests will be redirected to use HTTPS instead,change_of_authorization (boolean, optional): Global to automatically send disconnects when enabled/role values change.
        Requires a NAS Type supporting RFC-3576,g_radius_default_vendor (string, optional) = ['other' or 'rfc3576' or 'coa_3576' or 'appauth_3576' or 'appauthz_3576' or 'aerohive_3576' or 'alu_3576' or 'alu' or 'arista_3576' or 'arista_nr_3576' or 'aruba_3576' or 'aruba' or 'bluesocket' or 'chillispot_3576' or 'cisco_3576' or 'cisco' or 'colubris' or 'consentry' or 'enterasys' or 'dell_3576' or 'dell' or 'extreme' or 'extricom' or 'fortinet_3576' or 'fortinet' or 'hpe_3576' or 'hpe_msm_3576' or 'hpe_uww_3576' or 'juniper' or 'meraki' or 'meraki_splash' or 'meru' or 'motorola_3576' or 'ruckus_3576' or 'ruckus' or 'saml' or 'saml_authorize_only' or 'saml_via' or 'trapeze_3576' or 'trendnet' or 'xirrus']: Select the default type for network access servers,g_radius_server_bind_3576 (string, optional): Force a specific bind address for RFC-3576 requests.  This may be needed in an AirGroup environment.
        Defaults to '0.0.0.0' or '::' depending on your network,g_radius_internal_auth_type (string) = ['pap' or 'chap' or 'mschap']: Controls the RADIUS authentication type used for internal RADIUS authentication requests}
                Required Body Parameters (type(dict) body example)- {
          "g_admin_access_guest_require_https": false,
          "change_of_authorization": false,
          "g_radius_default_vendor": "",
          "g_radius_server_bind_3576": "",
          "g_radius_internal_auth_type": ""
        }
        """
        url_path = "/guest/authentication"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def update_guest_authentication(self, body=({})):
        """
                Operation: Modify settings at Configuration -> Authentication
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- GuestAuthenticationConfiguration {g_admin_access_guest_require_https (boolean, optional): If checked, HTTP access by guests will be redirected to use HTTPS instead,change_of_authorization (boolean, optional): Global to automatically send disconnects when enabled/role values change.
        Requires a NAS Type supporting RFC-3576,g_radius_default_vendor (string, optional) = ['other' or 'rfc3576' or 'coa_3576' or 'appauth_3576' or 'appauthz_3576' or 'aerohive_3576' or 'alu_3576' or 'alu' or 'arista_3576' or 'arista_nr_3576' or 'aruba_3576' or 'aruba' or 'bluesocket' or 'chillispot_3576' or 'cisco_3576' or 'cisco' or 'colubris' or 'consentry' or 'enterasys' or 'dell_3576' or 'dell' or 'extreme' or 'extricom' or 'fortinet_3576' or 'fortinet' or 'hpe_3576' or 'hpe_msm_3576' or 'hpe_uww_3576' or 'juniper' or 'meraki' or 'meraki_splash' or 'meru' or 'motorola_3576' or 'ruckus_3576' or 'ruckus' or 'saml' or 'saml_authorize_only' or 'saml_via' or 'trapeze_3576' or 'trendnet' or 'xirrus']: Select the default type for network access servers,g_radius_server_bind_3576 (string, optional): Force a specific bind address for RFC-3576 requests.  This may be needed in an AirGroup environment.
        Defaults to '0.0.0.0' or '::' depending on your network,g_radius_internal_auth_type (string) = ['pap' or 'chap' or 'mschap']: Controls the RADIUS authentication type used for internal RADIUS authentication requests}
                Required Body Parameters (type(dict) body example)- {
          "g_admin_access_guest_require_https": false,
          "change_of_authorization": false,
          "g_radius_default_vendor": "",
          "g_radius_server_bind_3576": "",
          "g_radius_internal_auth_type": ""
        }
        """
        url_path = "/guest/authentication"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # Function Section Name:GuestManager
    # Function Section Description: Manage settings in Configuration -> Guest Manager

    def get_guestmanager(self, body=({})):
        """
                Operation: Return settings from Configuration -> Guest Manager
                HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
                Required Body Parameters (body description)- GuestAuthenticationConfiguration {g_admin_access_guest_require_https (boolean, optional): If checked, HTTP access by guests will be redirected to use HTTPS instead,change_of_authorization (boolean, optional): Global to automatically send disconnects when enabled/role values change.
        Requires a NAS Type supporting RFC-3576,g_radius_default_vendor (string, optional) = ['other' or 'rfc3576' or 'coa_3576' or 'appauth_3576' or 'appauthz_3576' or 'aerohive_3576' or 'alu_3576' or 'alu' or 'arista_3576' or 'arista_nr_3576' or 'aruba_3576' or 'aruba' or 'bluesocket' or 'chillispot_3576' or 'cisco_3576' or 'cisco' or 'colubris' or 'consentry' or 'enterasys' or 'dell_3576' or 'dell' or 'extreme' or 'extricom' or 'fortinet_3576' or 'fortinet' or 'hpe_3576' or 'hpe_msm_3576' or 'hpe_uww_3576' or 'juniper' or 'meraki' or 'meraki_splash' or 'meru' or 'motorola_3576' or 'ruckus_3576' or 'ruckus' or 'saml' or 'saml_authorize_only' or 'saml_via' or 'trapeze_3576' or 'trendnet' or 'xirrus']: Select the default type for network access servers,g_radius_server_bind_3576 (string, optional): Force a specific bind address for RFC-3576 requests.  This may be needed in an AirGroup environment.
        Defaults to '0.0.0.0' or '::' depending on your network,g_radius_internal_auth_type (string) = ['pap' or 'chap' or 'mschap']: Controls the RADIUS authentication type used for internal RADIUS authentication requests}
                Required Body Parameters (type(dict) body example)- {
          "g_admin_access_guest_require_https": false,
          "change_of_authorization": false,
          "g_radius_default_vendor": "",
          "g_radius_server_bind_3576": "",
          "g_radius_internal_auth_type": ""
        }
        """
        url_path = "/guestmanager"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="get", query=body
        )

    def new_guestmanager(self, body=({})):
        """
                Operation: Modify settings at Configuration -> Guest Manager
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- GuestManager {random_username_method (string) = ['nwa_digits_password' or 'nwa_letters_password' or 'nwa_novowels_password' or 'nwa_lettersdigits_password' or 'nwa_picture_password' or 'nwa_sequence']: The method used to generate random account usernames,random_username_multi_prefix (string, optional): Identifier string to prepend to usernames.
        Dynamic entries based on a user attribute can be entered as '_' + attribute.  For example '_role_name'.
        The username length will determine the length of the numeric sequence only.  Recommend 4,random_username_picture (string, optional): Format picture (see below) describing the usernames that will be created for visitors.

         • Alphanumeric characters are passed through without modification.
         • ‘#’ is replaced with a random digit [0-9].
         • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z]
         • ‘_’ is replaced with a random lowercase letter [a-z]
         • ‘^’ is replaced with a random uppercase letter [A-Z]
         • ‘*’ is replaced with a random letter or digit [A-Za-z0-9].
         • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes]
         • ‘&’ is replaced with a random character (union of sets ! and *)
         • ‘@’ is replaced with a random letter or digit, excluding vowels
         • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2),random_username_length (integer): The length, in characters, of generated account usernames,guest_initial_sequence_options (object, optional): Create multi next available sequence number.  These values will be used when multi_initial_sequence is set to -1,random_password_method (string) = ['nwa_digits_password' or 'nwa_letters_password' or 'nwa_novowels_password' or 'nwa_lettersdigits_password' or 'nwa_alnum_password' or 'nwa_strong_password' or 'nwa_complex_password' or 'nwa_complexity_password' or 'nwa_words_password' or 'nwa_picture_password']: The method used to generate a random account password,random_password_picture (string, optional): Format picture (see below) describing the passwords that will be created for visitors.

         • Alphanumeric characters are passed through without modification.
         • ‘#’ is replaced with a random digit [0-9].
         • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z]
         • ‘_’ is replaced with a random lowercase letter [a-z]
         • ‘^’ is replaced with a random uppercase letter [A-Z]
         • ‘*’ is replaced with a random letter or digit [A-Za-z0-9].
         • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes]
         • ‘&’ is replaced with a random character (union of sets ! and *)
         • ‘@’ is replaced with a random letter or digit, excluding vowels
         • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2),random_password_length (integer): Number of characters to include in randomly-generated account passwords,guest_password_complexity (string) = ['none' or 'case' or 'number' or 'alphanumeric' or 'casenumeric' or 'punctuation' or 'complex']: Password complexity to enforce for manually-entered guest passwords.
        Requires the random password type ‘A password matching the password complexity requirements’
        and the field validator ‘NwaIsValidPasswordComplexity’ for manual password entry,guest_password_minimum (integer): The minimum number of characters that a guest password must contain,guest_password_disallowed (string, optional): Characters which cannot appear in a user-generated password,guest_password_disallowed_words (string, optional): Comma separated list of words disallowed in the random words password generator,guest_view_account_password (boolean, optional): If selected, guest and device Wi-Fi passwords may be displayed to an operator.
        This is only possible if operators have the View Passwords privilege as well,guest_do_expire (integer) = ['4' or '3' or '2' or '1']: Default action to take when the expire_time is reached.
        Note that a logout can only occur if the NAS is RFC-3576 compliant,guest_account_expiry_options (object): The available options to select from when choosing the expiration time of a guest account (expire_after).
        Expiration times are specified in hours,guest_modify_expire_time_options (object): The available options to select from when modifying an account's expiration (modify_expire_time).
        Note some items may be dynamically removed based on the state of the account,guest_lifetime_options (object): The available options to select from when choosing the lifetime of a guest account (expire_postlogin).
        Lifetime values are specified in minutes,g_action_notify_account_expire_enabled (boolean, optional): If checked, users will receive an email notification when their device’s network credentials are due to expire.
        Accounts must contain the ’expired_notify_status’ field with a value of ’1’.  Once a notification is sent, this field will show as ’0’,g_action_notify_account_expiration_duration (integer, optional): Account expiration emails are sent this many days before the account expires.
        Enter a value between 1 and 30,g_action_notify_account_expire_email_unknown (string, optional) = ['none' or 'fixed' or 'domain']: Specify where to send emails if the user’s account doesn’t have an email address recorded,g_action_notify_account_expire_email_unknown_fixed (string, optional): Address used when no email address is known for a user,g_action_notify_account_expire_email_unknown_domain (string, optional): Domain to append to the username to form an email address,g_action_notify_account_expire_subject (string, optional): Enter a subject for the notification email,g_action_notify_account_expire_message (integer, optional) = ['2' or '13' or '7' or '12' or '5' or '6' or '1' or '3' or '8' or '9' or '11' or '10' or '14' or '4']: The plain text or HTML print template to use when generating an email message,g_action_notify_account_expire_skin (string, optional) = ['' or 'plaintext' or 'html_embedded' or 'receipt' or 'default' or 'Aruba Amigopod Skin' or 'Blank Skin' or 'ClearPass Guest Skin' or 'Custom Skin 1' or 'Custom Skin 2' or 'Galleria Skin' or 'Galleria Skin 2']: The format in which to send email receipts,g_action_notify_account_expire_copies (string, optional) = ['never' or 'always_cc' or 'always_bcc']: Specify when to send to the recipients in the Copies To list,g_action_notify_account_expire_copies_to (string, optional): An optional list of email addresses to which copies of expiry notifications will be sent,g_action_notify_device_expire_email_unknown (string, optional) = ['none' or 'fixed']: Specify where to send emails if the user’s account doesn’t have an email or sponsor_email address recorded,g_action_notify_device_expire_email_unknown_fixed (string, optional): Address used when no email address is known for a device,g_action_notify_device_expire_subject (string, optional): Enter a subject for the notification email,g_action_notify_device_expire_message (integer, optional) = ['2' or '13' or '7' or '12' or '5' or '6' or '1' or '3' or '8' or '9' or '11' or '10' or '14' or '4']: The plain text or HTML print template to use when generating an email message,g_action_notify_device_expire_skin (string, optional) = ['' or 'plaintext' or 'html_embedded' or 'receipt' or 'default' or 'Aruba Amigopod Skin' or 'Blank Skin' or 'ClearPass Guest Skin' or 'Custom Skin 1' or 'Custom Skin 2' or 'Galleria Skin' or 'Galleria Skin 2']: The format in which to send email receipts,g_action_notify_device_expire_copies (string, optional) = ['never' or 'always_cc' or 'always_bcc']: Specify when to send to the recipients in the Copies To list,g_action_notify_device_expire_copies_to (string, optional): An optional list of email addresses to which copies of expiry notifications will be sent,site_ssid (string, optional): The SSID of the wireless LAN, if applicable.  This will appear on guest account print receipts,site_wpa_key (string, optional): The WPA key for the wireless LAN, if applicable.  This will appear on guest account print receipts,guest_receipt_print_button (boolean, optional): Guest receipts can print simply by selecting the template in the dropdown, or by clicking a link,guest_account_terms_of_use_url (string, optional): The URL of a terms and conditions page.  The URL will appear in any terms checkbox with:
        {nwa_global name=guest_account_terms_of_use_url}
        It is recommended to upload your terms in Content Manager, where the files will be referenced with the "public/" prefix.
        Alternatively, you can edit Terms and Conditions under Configuration > Pages > Web Pages.
        If your site is hosted externally, be sure the proper access control lists (ACLs) are in place.
        If terms are not required, it is recommended to edit the terms field on your forms to a UI type "hidden" and an Initial Value of 1,guest_active_sessions (integer, optional): Enable limiting the number of active sessions a guest account may have.
        Enter 0 to allow an unlimited number of sessions,guest_about_guest_network_access (string, optional): Template code to display on the Guest Manager start page, under the
        “About Guest Network Access” heading.  Leave blank to use the default text,
        or enter a hyphen (“-”) to remove the default text and the heading}
                Required Body Parameters (type(dict) body example)- {
          "random_username_method": "",
          "random_username_multi_prefix": "",
          "random_username_picture": "",
          "random_username_length": 0,
          "guest_initial_sequence_options": "object",
          "random_password_method": "",
          "random_password_picture": "",
          "random_password_length": 0,
          "guest_password_complexity": "",
          "guest_password_minimum": 0,
          "guest_password_disallowed": "",
          "guest_password_disallowed_words": "",
          "guest_view_account_password": false,
          "guest_do_expire": 0,
          "guest_account_expiry_options": "object",
          "guest_modify_expire_time_options": "object",
          "guest_lifetime_options": "object",
          "g_action_notify_account_expire_enabled": false,
          "g_action_notify_account_expiration_duration": 0,
          "g_action_notify_account_expire_email_unknown": "",
          "g_action_notify_account_expire_email_unknown_fixed": "",
          "g_action_notify_account_expire_email_unknown_domain": "",
          "g_action_notify_account_expire_subject": "",
          "g_action_notify_account_expire_message": 0,
          "g_action_notify_account_expire_skin": "",
          "g_action_notify_account_expire_copies": "",
          "g_action_notify_account_expire_copies_to": "",
          "g_action_notify_device_expire_email_unknown": "",
          "g_action_notify_device_expire_email_unknown_fixed": "",
          "g_action_notify_device_expire_subject": "",
          "g_action_notify_device_expire_message": 0,
          "g_action_notify_device_expire_skin": "",
          "g_action_notify_device_expire_copies": "",
          "g_action_notify_device_expire_copies_to": "",
          "site_ssid": "",
          "site_wpa_key": "",
          "guest_receipt_print_button": false,
          "guest_account_terms_of_use_url": "",
          "guest_active_sessions": 0,
          "guest_about_guest_network_access": ""
        }
        """
        url_path = "/guestmanager"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def update_guestmanager(self, body=({})):
        """
                Operation: Modify settings at Configuration -> Guest Manager
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- GuestManager {random_username_method (string) = ['nwa_digits_password' or 'nwa_letters_password' or 'nwa_novowels_password' or 'nwa_lettersdigits_password' or 'nwa_picture_password' or 'nwa_sequence']: The method used to generate random account usernames,random_username_multi_prefix (string, optional): Identifier string to prepend to usernames.
        Dynamic entries based on a user attribute can be entered as '_' + attribute.  For example '_role_name'.
        The username length will determine the length of the numeric sequence only.  Recommend 4,random_username_picture (string, optional): Format picture (see below) describing the usernames that will be created for visitors.

         • Alphanumeric characters are passed through without modification.
         • ‘#’ is replaced with a random digit [0-9].
         • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z]
         • ‘_’ is replaced with a random lowercase letter [a-z]
         • ‘^’ is replaced with a random uppercase letter [A-Z]
         • ‘*’ is replaced with a random letter or digit [A-Za-z0-9].
         • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes]
         • ‘&’ is replaced with a random character (union of sets ! and *)
         • ‘@’ is replaced with a random letter or digit, excluding vowels
         • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2),random_username_length (integer): The length, in characters, of generated account usernames,guest_initial_sequence_options (object, optional): Create multi next available sequence number.  These values will be used when multi_initial_sequence is set to -1,random_password_method (string) = ['nwa_digits_password' or 'nwa_letters_password' or 'nwa_novowels_password' or 'nwa_lettersdigits_password' or 'nwa_alnum_password' or 'nwa_strong_password' or 'nwa_complex_password' or 'nwa_complexity_password' or 'nwa_words_password' or 'nwa_picture_password']: The method used to generate a random account password,random_password_picture (string, optional): Format picture (see below) describing the passwords that will be created for visitors.

         • Alphanumeric characters are passed through without modification.
         • ‘#’ is replaced with a random digit [0-9].
         • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z]
         • ‘_’ is replaced with a random lowercase letter [a-z]
         • ‘^’ is replaced with a random uppercase letter [A-Z]
         • ‘*’ is replaced with a random letter or digit [A-Za-z0-9].
         • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes]
         • ‘&’ is replaced with a random character (union of sets ! and *)
         • ‘@’ is replaced with a random letter or digit, excluding vowels
         • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2),random_password_length (integer): Number of characters to include in randomly-generated account passwords,guest_password_complexity (string) = ['none' or 'case' or 'number' or 'alphanumeric' or 'casenumeric' or 'punctuation' or 'complex']: Password complexity to enforce for manually-entered guest passwords.
        Requires the random password type ‘A password matching the password complexity requirements’
        and the field validator ‘NwaIsValidPasswordComplexity’ for manual password entry,guest_password_minimum (integer): The minimum number of characters that a guest password must contain,guest_password_disallowed (string, optional): Characters which cannot appear in a user-generated password,guest_password_disallowed_words (string, optional): Comma separated list of words disallowed in the random words password generator,guest_view_account_password (boolean, optional): If selected, guest and device Wi-Fi passwords may be displayed to an operator.
        This is only possible if operators have the View Passwords privilege as well,guest_do_expire (integer) = ['4' or '3' or '2' or '1']: Default action to take when the expire_time is reached.
        Note that a logout can only occur if the NAS is RFC-3576 compliant,guest_account_expiry_options (object): The available options to select from when choosing the expiration time of a guest account (expire_after).
        Expiration times are specified in hours,guest_modify_expire_time_options (object): The available options to select from when modifying an account's expiration (modify_expire_time).
        Note some items may be dynamically removed based on the state of the account,guest_lifetime_options (object): The available options to select from when choosing the lifetime of a guest account (expire_postlogin).
        Lifetime values are specified in minutes,g_action_notify_account_expire_enabled (boolean, optional): If checked, users will receive an email notification when their device’s network credentials are due to expire.
        Accounts must contain the ’expired_notify_status’ field with a value of ’1’.  Once a notification is sent, this field will show as ’0’,g_action_notify_account_expiration_duration (integer, optional): Account expiration emails are sent this many days before the account expires.
        Enter a value between 1 and 30,g_action_notify_account_expire_email_unknown (string, optional) = ['none' or 'fixed' or 'domain']: Specify where to send emails if the user’s account doesn’t have an email address recorded,g_action_notify_account_expire_email_unknown_fixed (string, optional): Address used when no email address is known for a user,g_action_notify_account_expire_email_unknown_domain (string, optional): Domain to append to the username to form an email address,g_action_notify_account_expire_subject (string, optional): Enter a subject for the notification email,g_action_notify_account_expire_message (integer, optional) = ['2' or '13' or '7' or '12' or '5' or '6' or '1' or '3' or '8' or '9' or '11' or '10' or '14' or '4']: The plain text or HTML print template to use when generating an email message,g_action_notify_account_expire_skin (string, optional) = ['' or 'plaintext' or 'html_embedded' or 'receipt' or 'default' or 'Aruba Amigopod Skin' or 'Blank Skin' or 'ClearPass Guest Skin' or 'Custom Skin 1' or 'Custom Skin 2' or 'Galleria Skin' or 'Galleria Skin 2']: The format in which to send email receipts,g_action_notify_account_expire_copies (string, optional) = ['never' or 'always_cc' or 'always_bcc']: Specify when to send to the recipients in the Copies To list,g_action_notify_account_expire_copies_to (string, optional): An optional list of email addresses to which copies of expiry notifications will be sent,g_action_notify_device_expire_email_unknown (string, optional) = ['none' or 'fixed']: Specify where to send emails if the user’s account doesn’t have an email or sponsor_email address recorded,g_action_notify_device_expire_email_unknown_fixed (string, optional): Address used when no email address is known for a device,g_action_notify_device_expire_subject (string, optional): Enter a subject for the notification email,g_action_notify_device_expire_message (integer, optional) = ['2' or '13' or '7' or '12' or '5' or '6' or '1' or '3' or '8' or '9' or '11' or '10' or '14' or '4']: The plain text or HTML print template to use when generating an email message,g_action_notify_device_expire_skin (string, optional) = ['' or 'plaintext' or 'html_embedded' or 'receipt' or 'default' or 'Aruba Amigopod Skin' or 'Blank Skin' or 'ClearPass Guest Skin' or 'Custom Skin 1' or 'Custom Skin 2' or 'Galleria Skin' or 'Galleria Skin 2']: The format in which to send email receipts,g_action_notify_device_expire_copies (string, optional) = ['never' or 'always_cc' or 'always_bcc']: Specify when to send to the recipients in the Copies To list,g_action_notify_device_expire_copies_to (string, optional): An optional list of email addresses to which copies of expiry notifications will be sent,site_ssid (string, optional): The SSID of the wireless LAN, if applicable.  This will appear on guest account print receipts,site_wpa_key (string, optional): The WPA key for the wireless LAN, if applicable.  This will appear on guest account print receipts,guest_receipt_print_button (boolean, optional): Guest receipts can print simply by selecting the template in the dropdown, or by clicking a link,guest_account_terms_of_use_url (string, optional): The URL of a terms and conditions page.  The URL will appear in any terms checkbox with:
        {nwa_global name=guest_account_terms_of_use_url}
        It is recommended to upload your terms in Content Manager, where the files will be referenced with the "public/" prefix.
        Alternatively, you can edit Terms and Conditions under Configuration > Pages > Web Pages.
        If your site is hosted externally, be sure the proper access control lists (ACLs) are in place.
        If terms are not required, it is recommended to edit the terms field on your forms to a UI type "hidden" and an Initial Value of 1,guest_active_sessions (integer, optional): Enable limiting the number of active sessions a guest account may have.
        Enter 0 to allow an unlimited number of sessions,guest_about_guest_network_access (string, optional): Template code to display on the Guest Manager start page, under the
        “About Guest Network Access” heading.  Leave blank to use the default text,
        or enter a hyphen (“-”) to remove the default text and the heading}
                Required Body Parameters (type(dict) body example)- {
          "random_username_method": "",
          "random_username_multi_prefix": "",
          "random_username_picture": "",
          "random_username_length": 0,
          "guest_initial_sequence_options": "object",
          "random_password_method": "",
          "random_password_picture": "",
          "random_password_length": 0,
          "guest_password_complexity": "",
          "guest_password_minimum": 0,
          "guest_password_disallowed": "",
          "guest_password_disallowed_words": "",
          "guest_view_account_password": false,
          "guest_do_expire": 0,
          "guest_account_expiry_options": "object",
          "guest_modify_expire_time_options": "object",
          "guest_lifetime_options": "object",
          "g_action_notify_account_expire_enabled": false,
          "g_action_notify_account_expiration_duration": 0,
          "g_action_notify_account_expire_email_unknown": "",
          "g_action_notify_account_expire_email_unknown_fixed": "",
          "g_action_notify_account_expire_email_unknown_domain": "",
          "g_action_notify_account_expire_subject": "",
          "g_action_notify_account_expire_message": 0,
          "g_action_notify_account_expire_skin": "",
          "g_action_notify_account_expire_copies": "",
          "g_action_notify_account_expire_copies_to": "",
          "g_action_notify_device_expire_email_unknown": "",
          "g_action_notify_device_expire_email_unknown_fixed": "",
          "g_action_notify_device_expire_subject": "",
          "g_action_notify_device_expire_message": 0,
          "g_action_notify_device_expire_skin": "",
          "g_action_notify_device_expire_copies": "",
          "g_action_notify_device_expire_copies_to": "",
          "site_ssid": "",
          "site_wpa_key": "",
          "guest_receipt_print_button": false,
          "guest_account_terms_of_use_url": "",
          "guest_active_sessions": 0,
          "guest_about_guest_network_access": ""
        }
        """
        url_path = "/guestmanager"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # Function Section Name:PrintTemplate
    # Function Section Description: Manage print templates

    def get_template_print(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of print templates
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default -id)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/template/print"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_template_print(self, body=({})):
        """
                Operation: Create a new print template
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- PrintTemplate {id (integer, optional): Numeric ID of the template,name (string, optional): Name of the template,enabled (boolean, optional): Flag indicating if the template is enabled,columns (integer, optional): Columns in a template.,per_account (string, optional): HTML template code used to generate a single account receipt,header (string, optional): HTML template code used at the beginning of the document,footer (string, optional): HTML template code used at the end of the document,wizard_template (string, optional): Style of print template to use,wizard_logo (string, optional): Image to use on the template,wizard_title (string, optional): Title which will be displayed on the template,wizard_subtitle (string, optional): Subtitle to display on the template,wizard_field_header (string, optional): Field header for the details displayed on the template,wizard_fields (string, optional): Visitor account fields,wizard_notes (string, optional): Notes to display on the template,wizard_footer (string, optional): Footer text to display on the template}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "enabled": false,
          "columns": 0,
          "per_account": "",
          "header": "",
          "footer": "",
          "wizard_template": "",
          "wizard_logo": "",
          "wizard_title": "",
          "wizard_subtitle": "",
          "wizard_field_header": "",
          "wizard_fields": "",
          "wizard_notes": "",
          "wizard_footer": ""
        }
        """
        url_path = "/template/print"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_template_print_by_id(self, id=""):
        """
        Operation: Get a print template
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/template/print/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_template_print_by_id(self, id="", body=({})):
        """
                Operation: Update some fields of a print template
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: URL parameter id
                Required Body Parameters (body description)- PrintTemplate {id (integer, optional): Numeric ID of the template,name (string, optional): Name of the template,enabled (boolean, optional): Flag indicating if the template is enabled,columns (integer, optional): Columns in a template.,per_account (string, optional): HTML template code used to generate a single account receipt,header (string, optional): HTML template code used at the beginning of the document,footer (string, optional): HTML template code used at the end of the document,wizard_template (string, optional): Style of print template to use,wizard_logo (string, optional): Image to use on the template,wizard_title (string, optional): Title which will be displayed on the template,wizard_subtitle (string, optional): Subtitle to display on the template,wizard_field_header (string, optional): Field header for the details displayed on the template,wizard_fields (string, optional): Visitor account fields,wizard_notes (string, optional): Notes to display on the template,wizard_footer (string, optional): Footer text to display on the template}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "enabled": false,
          "columns": 0,
          "per_account": "",
          "header": "",
          "footer": "",
          "wizard_template": "",
          "wizard_logo": "",
          "wizard_title": "",
          "wizard_subtitle": "",
          "wizard_field_header": "",
          "wizard_fields": "",
          "wizard_notes": "",
          "wizard_footer": ""
        }
        """
        url_path = "/template/print/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_template_print_by_id(self, id="", body=({})):
        """
                Operation: Replace a print template
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: URL parameter id
                Required Body Parameters (body description)- PrintTemplate {id (integer, optional): Numeric ID of the template,name (string, optional): Name of the template,enabled (boolean, optional): Flag indicating if the template is enabled,columns (integer, optional): Columns in a template.,per_account (string, optional): HTML template code used to generate a single account receipt,header (string, optional): HTML template code used at the beginning of the document,footer (string, optional): HTML template code used at the end of the document,wizard_template (string, optional): Style of print template to use,wizard_logo (string, optional): Image to use on the template,wizard_title (string, optional): Title which will be displayed on the template,wizard_subtitle (string, optional): Subtitle to display on the template,wizard_field_header (string, optional): Field header for the details displayed on the template,wizard_fields (string, optional): Visitor account fields,wizard_notes (string, optional): Notes to display on the template,wizard_footer (string, optional): Footer text to display on the template}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "enabled": false,
          "columns": 0,
          "per_account": "",
          "header": "",
          "footer": "",
          "wizard_template": "",
          "wizard_logo": "",
          "wizard_title": "",
          "wizard_subtitle": "",
          "wizard_field_header": "",
          "wizard_fields": "",
          "wizard_notes": "",
          "wizard_footer": ""
        }
        """
        url_path = "/template/print/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_template_print_by_id(self, id=""):
        """
        Operation: Delete a print template
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/template/print/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # Function Section Name:WebLogin
    # Function Section Description: Manage web logins

    def get_weblogin(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of web login pages
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Optional Query Parameter Name: filter, Description: JSON filter expression specifying the items to return
        Optional Query Parameter Name: sort, Description: Sort ordering for returned items (default +name)
        Optional Query Parameter Name: offset, Description: Zero based offset to start from
        Optional Query Parameter Name: limit, Description: Maximum number of items to return (1 – 1000)
        Optional Query Parameter Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/weblogin"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_weblogin(self, body=({})):
        """
                Operation: Create a new web login page
                HTTP Status Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters (body description)- WebLogin {id (integer, optional): Unique ID of the web login,name (string): Enter a name for this web login page,page_name (string, optional): Enter a page name for this web login.
        The web login will be accessible from “/guest/page_name.php”,description (string, optional): Comments or descriptive text about the web login,vendor_preset (string): Select a predefined group of settings suitable for standard network configurations,vendor_ip (string, optional): Enter the hostname (FQDN) of the vendor’s product here.
        When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device,require_https (string, optional): Select a security option to apply to the web login process,webauth (string, optional): Select how the user’s network login will be handled.
        Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process,form_action (string): The URL of the NAS device’s login form,form_method (string): Choose the method to use when submitting the login form to the NAS,form_username_label (string, optional): The form label for the username field.
        Leave blank to use the default (Username:),form_username (string): The name of the username field for the login form. This will be passed to the NAS device when the form is submitted,form_username_suffix (string, optional): The suffix is automatically appended to the username before submitting the login form to the NAS,form_password_label (string, optional): The form label for the password field.
        Leave blank to use the default (Password:),form_password (string): The name of the password field for the login form. This will be passed to the NAS device when the form is submitted,form_extra (string, optional): Specify any additional field names and values to send to the NAS device as name=value pairs, one per line,submit_label (string, optional): The form label for the log in button.
        Leave blank to use the default (Log In),form_password_encryption (string): Choose the type of password encryption to use when submitting the login form,uam_secret (string, optional): Enter the shared secret between the NAS device and the web login form,url (string, optional): The name of the destination field required by the NAS,default_url (string, optional): Enter the default URL to redirect clients.
        Please ensure you prepend "http://" for any external domain,default_url_override (boolean, optional): If selected, the client’s default destination will be overridden regardless of its value,dynamic_address (boolean, optional): In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.
        The address above will be used whenever the parameter is not available or fails the requirements below,dynamic_allowlist (string, optional): Enter the IP addresses and networks from which dynamic addresses are permitted,dynamic_denylist (string, optional): Enter the IP addresses and networks from which dynamic addresses are denied,access_allowlist (string, optional): Enter the IP addresses and networks from which logins are permitted,access_denylist (string, optional): Enter the IP addresses and networks that are denied login access,access_if_denied (string): Select the response of the system to a request that is not permitted,login_title (string, optional): The title to display on the web login page.
        Leave blank to use the default (Login),login_header (string, optional): HTML template code displayed before the login form,login_footer (string, optional): HTML template code displayed after the login form,login_message (string, optional): HTML template code displayed while the login attempt is in progress,login_delay (number): The time in seconds to delay while displaying the login message,login_skin (string): Choose the skin to use when this web login page is displayed,login_terms_require (boolean, optional): If checked, the user will be forced to accept a Terms and Conditions checkbox,login_terms_label (string, optional): The form label for the terms checkbox.
        Leave blank to use the default (Terms:),login_terms_text (string, optional): HTML code containing your Terms and Conditions.
        Leave blank to use the default (I accept the terms of use),login_terms_layout (string, optional): Select the layout for the terms and conditions text,login_terms_error (string, optional): The text to display if the terms are not accepted.
        Leave blank to use the default (In order to log in, you must accept the terms and conditions.),login_captcha (string, optional): Select a CAPTCHA mode,username_auth (string, optional): Select the authentication requirement.
        Access Code requires a single code (username) to be entered.
        Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.
        Auto is similar to anonymous but the page is automatically submitted.
        Access Code and Anonymous require the account to have the Username Authentication field set,certificate_request (string, optional): Choose whether the user should select a client certificate when authenticating,username_auth_username (string, optional): The account to use for anonymous authentication.
        The password will be visible within the HTML.
        It is recommended to increase the account Session Limit to the number of guests you wish to support,certificate_auth (string, optional): Choose whether other credentials must also be provided in addition to a certificate,register_policy_manager (boolean, optional): If selected, the endpoint’s attributes will also be updated with other details from the user account,register_policy_manager_adv (boolean, optional): Customize attributes stored with the endpoint,register_policy_manager_attrs (string, optional): List of name|value pairs to pass along.
        user_field | Endpoint Attribute,hash_url (string, optional): Select the level of checking to apply to URL parameters passed to the web login page.
        Use this option to detect when URL parameters have been modified by the user, for example their MAC address,hash_secret (string, optional): The redirection URL will be hashed using this shared secret,bypass_cna (boolean, optional): The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.
        Note that this option may not work with all vendors, depending on how the captive portal is implemented,capport_venue_url (string, optional): Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.
        https://www.rfc-editor.org/rfc/rfc8908.html,onguard_healthcheck (boolean, optional): If selected, the guest will be required to pass a health check prior to accessing the network,onguard_agents (string, optional): Select the agent options for client scanning.
        Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java,onguard_header (string, optional): HTML template code displayed before the health check text,onguard_footer (string, optional): HTML template code displayed after the health check text,oauth_enabled (boolean, optional): Enable logins with cloud identity / social network credentials,oauth_debug (boolean, optional): Log debugging data,oauth_providers (object, optional): Configuration for cloud identity authentication providers,login_custom_form (boolean, optional): If selected, you must supply your own HTML login form in the Header or Footer HTML areas,login_pre_auth_check (string): Select how the username and password should be checked before proceeding to the NAS authentication,login_pre_auth_error (string, optional): The text to display if the username and password lookup fails.
        Leave blank to use the default (Invalid username or password),mfa_enabled (string, optional),mfa_first (string, optional): All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device,mfa_duo_ikey (string, optional),mfa_duo_skey (string, optional),mfa_duo_host (string, optional),mfa_fn_client_id (string, optional),mfa_fn_client_secret (string, optional),mfa_fn_factors (string, optional): Enter the number of factors to require,mfa_fn_email (boolean, optional): If disabled, the user must scan the QR code,mfa_iws_tenant (string, optional),mfa_iws_app (string, optional),mfa_iws_hostname (string, optional): Enter the hostname of the ImageWare server,mfa_mc_scope (string, optional): OAuth 2.0 scope value. Only mc_authn is supported for this release,mfa_mc_context (string, optional): Message which will be displayed on the authorization device,mfa_mc_binding_message (string, optional): Plain text reference to interlock the consumption device and authorization device,mfa_mc_acr_values (string, optional): Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6,mfa_mc_display (string, optional): User interface display for Authentication,mfa_mc_prompt (string, optional): Value to specify to the Authorisation server about type of prompt,mfa_mc_max_age (integer, optional): Maximum elapsed time in secs since last authenticaiton,mfa_mc_login_hint (string, optional): An indication to IDP on what ID to use for login,mfa_mc_version (string, optional),mfa_mc_discovery_service_endpoint (string, optional): Provide the endpoint URL provided by Mobile Connect during configuration,mfa_mc_redirect_url (string, optional): Mobile Connect Redirect URL provided during configuration,mfa_mc_client_id (string, optional),mfa_mc_client_secret (string, optional),mfa_header_html (string, optional): HTML template code displayed before the provider’s vendor-specific authentication area,mfa_footer_html (string, optional): HTML template code displayed after the provider’s vendor-specific authentication area}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "page_name": "",
          "description": "",
          "vendor_preset": "",
          "vendor_ip": "",
          "require_https": "",
          "webauth": "",
          "form_action": "",
          "form_method": "",
          "form_username_label": "",
          "form_username": "",
          "form_username_suffix": "",
          "form_password_label": "",
          "form_password": "",
          "form_extra": "",
          "submit_label": "",
          "form_password_encryption": "",
          "uam_secret": "",
          "url": "",
          "default_url": "",
          "default_url_override": false,
          "dynamic_address": false,
          "dynamic_allowlist": "",
          "dynamic_denylist": "",
          "access_allowlist": "",
          "access_denylist": "",
          "access_if_denied": "",
          "login_title": "",
          "login_header": "",
          "login_footer": "",
          "login_message": "",
          "login_delay": 0,
          "login_skin": "",
          "login_terms_require": false,
          "login_terms_label": "",
          "login_terms_text": "",
          "login_terms_layout": "",
          "login_terms_error": "",
          "login_captcha": "",
          "username_auth": "",
          "certificate_request": "",
          "username_auth_username": "",
          "certificate_auth": "",
          "register_policy_manager": false,
          "register_policy_manager_adv": false,
          "register_policy_manager_attrs": "",
          "hash_url": "",
          "hash_secret": "",
          "bypass_cna": false,
          "capport_venue_url": "",
          "onguard_healthcheck": false,
          "onguard_agents": "",
          "onguard_header": "",
          "onguard_footer": "",
          "oauth_enabled": false,
          "oauth_debug": false,
          "oauth_providers": "object",
          "login_custom_form": false,
          "login_pre_auth_check": "",
          "login_pre_auth_error": "",
          "mfa_enabled": "",
          "mfa_first": "",
          "mfa_duo_ikey": "",
          "mfa_duo_skey": "",
          "mfa_duo_host": "",
          "mfa_fn_client_id": "",
          "mfa_fn_client_secret": "",
          "mfa_fn_factors": "",
          "mfa_fn_email": false,
          "mfa_iws_tenant": "",
          "mfa_iws_app": "",
          "mfa_iws_hostname": "",
          "mfa_mc_scope": "",
          "mfa_mc_context": "",
          "mfa_mc_binding_message": "",
          "mfa_mc_acr_values": "",
          "mfa_mc_display": "",
          "mfa_mc_prompt": "",
          "mfa_mc_max_age": 0,
          "mfa_mc_login_hint": "",
          "mfa_mc_version": "",
          "mfa_mc_discovery_service_endpoint": "",
          "mfa_mc_redirect_url": "",
          "mfa_mc_client_id": "",
          "mfa_mc_client_secret": "",
          "mfa_header_html": "",
          "mfa_footer_html": ""
        }
        """
        url_path = "/weblogin"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_weblogin_by_id(self, id=""):
        """
        Operation: Get a web login page
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/weblogin/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_weblogin_by_id(self, id="", body=({})):
        """
                Operation: Update some fields of a web login page
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: URL parameter id
                Required Body Parameters (body description)- WebLogin {id (integer, optional): Unique ID of the web login,name (string): Enter a name for this web login page,page_name (string, optional): Enter a page name for this web login.
        The web login will be accessible from “/guest/page_name.php”,description (string, optional): Comments or descriptive text about the web login,vendor_preset (string): Select a predefined group of settings suitable for standard network configurations,vendor_ip (string, optional): Enter the hostname (FQDN) of the vendor’s product here.
        When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device,require_https (string, optional): Select a security option to apply to the web login process,webauth (string, optional): Select how the user’s network login will be handled.
        Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process,form_action (string): The URL of the NAS device’s login form,form_method (string): Choose the method to use when submitting the login form to the NAS,form_username_label (string, optional): The form label for the username field.
        Leave blank to use the default (Username:),form_username (string): The name of the username field for the login form. This will be passed to the NAS device when the form is submitted,form_username_suffix (string, optional): The suffix is automatically appended to the username before submitting the login form to the NAS,form_password_label (string, optional): The form label for the password field.
        Leave blank to use the default (Password:),form_password (string): The name of the password field for the login form. This will be passed to the NAS device when the form is submitted,form_extra (string, optional): Specify any additional field names and values to send to the NAS device as name=value pairs, one per line,submit_label (string, optional): The form label for the log in button.
        Leave blank to use the default (Log In),form_password_encryption (string): Choose the type of password encryption to use when submitting the login form,uam_secret (string, optional): Enter the shared secret between the NAS device and the web login form,url (string, optional): The name of the destination field required by the NAS,default_url (string, optional): Enter the default URL to redirect clients.
        Please ensure you prepend "http://" for any external domain,default_url_override (boolean, optional): If selected, the client’s default destination will be overridden regardless of its value,dynamic_address (boolean, optional): In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.
        The address above will be used whenever the parameter is not available or fails the requirements below,dynamic_allowlist (string, optional): Enter the IP addresses and networks from which dynamic addresses are permitted,dynamic_denylist (string, optional): Enter the IP addresses and networks from which dynamic addresses are denied,access_allowlist (string, optional): Enter the IP addresses and networks from which logins are permitted,access_denylist (string, optional): Enter the IP addresses and networks that are denied login access,access_if_denied (string): Select the response of the system to a request that is not permitted,login_title (string, optional): The title to display on the web login page.
        Leave blank to use the default (Login),login_header (string, optional): HTML template code displayed before the login form,login_footer (string, optional): HTML template code displayed after the login form,login_message (string, optional): HTML template code displayed while the login attempt is in progress,login_delay (number): The time in seconds to delay while displaying the login message,login_skin (string): Choose the skin to use when this web login page is displayed,login_terms_require (boolean, optional): If checked, the user will be forced to accept a Terms and Conditions checkbox,login_terms_label (string, optional): The form label for the terms checkbox.
        Leave blank to use the default (Terms:),login_terms_text (string, optional): HTML code containing your Terms and Conditions.
        Leave blank to use the default (I accept the terms of use),login_terms_layout (string, optional): Select the layout for the terms and conditions text,login_terms_error (string, optional): The text to display if the terms are not accepted.
        Leave blank to use the default (In order to log in, you must accept the terms and conditions.),login_captcha (string, optional): Select a CAPTCHA mode,username_auth (string, optional): Select the authentication requirement.
        Access Code requires a single code (username) to be entered.
        Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.
        Auto is similar to anonymous but the page is automatically submitted.
        Access Code and Anonymous require the account to have the Username Authentication field set,certificate_request (string, optional): Choose whether the user should select a client certificate when authenticating,username_auth_username (string, optional): The account to use for anonymous authentication.
        The password will be visible within the HTML.
        It is recommended to increase the account Session Limit to the number of guests you wish to support,certificate_auth (string, optional): Choose whether other credentials must also be provided in addition to a certificate,register_policy_manager (boolean, optional): If selected, the endpoint’s attributes will also be updated with other details from the user account,register_policy_manager_adv (boolean, optional): Customize attributes stored with the endpoint,register_policy_manager_attrs (string, optional): List of name|value pairs to pass along.
        user_field | Endpoint Attribute,hash_url (string, optional): Select the level of checking to apply to URL parameters passed to the web login page.
        Use this option to detect when URL parameters have been modified by the user, for example their MAC address,hash_secret (string, optional): The redirection URL will be hashed using this shared secret,bypass_cna (boolean, optional): The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.
        Note that this option may not work with all vendors, depending on how the captive portal is implemented,capport_venue_url (string, optional): Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.
        https://www.rfc-editor.org/rfc/rfc8908.html,onguard_healthcheck (boolean, optional): If selected, the guest will be required to pass a health check prior to accessing the network,onguard_agents (string, optional): Select the agent options for client scanning.
        Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java,onguard_header (string, optional): HTML template code displayed before the health check text,onguard_footer (string, optional): HTML template code displayed after the health check text,oauth_enabled (boolean, optional): Enable logins with cloud identity / social network credentials,oauth_debug (boolean, optional): Log debugging data,oauth_providers (object, optional): Configuration for cloud identity authentication providers,login_custom_form (boolean, optional): If selected, you must supply your own HTML login form in the Header or Footer HTML areas,login_pre_auth_check (string): Select how the username and password should be checked before proceeding to the NAS authentication,login_pre_auth_error (string, optional): The text to display if the username and password lookup fails.
        Leave blank to use the default (Invalid username or password),mfa_enabled (string, optional),mfa_first (string, optional): All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device,mfa_duo_ikey (string, optional),mfa_duo_skey (string, optional),mfa_duo_host (string, optional),mfa_fn_client_id (string, optional),mfa_fn_client_secret (string, optional),mfa_fn_factors (string, optional): Enter the number of factors to require,mfa_fn_email (boolean, optional): If disabled, the user must scan the QR code,mfa_iws_tenant (string, optional),mfa_iws_app (string, optional),mfa_iws_hostname (string, optional): Enter the hostname of the ImageWare server,mfa_mc_scope (string, optional): OAuth 2.0 scope value. Only mc_authn is supported for this release,mfa_mc_context (string, optional): Message which will be displayed on the authorization device,mfa_mc_binding_message (string, optional): Plain text reference to interlock the consumption device and authorization device,mfa_mc_acr_values (string, optional): Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6,mfa_mc_display (string, optional): User interface display for Authentication,mfa_mc_prompt (string, optional): Value to specify to the Authorisation server about type of prompt,mfa_mc_max_age (integer, optional): Maximum elapsed time in secs since last authenticaiton,mfa_mc_login_hint (string, optional): An indication to IDP on what ID to use for login,mfa_mc_version (string, optional),mfa_mc_discovery_service_endpoint (string, optional): Provide the endpoint URL provided by Mobile Connect during configuration,mfa_mc_redirect_url (string, optional): Mobile Connect Redirect URL provided during configuration,mfa_mc_client_id (string, optional),mfa_mc_client_secret (string, optional),mfa_header_html (string, optional): HTML template code displayed before the provider’s vendor-specific authentication area,mfa_footer_html (string, optional): HTML template code displayed after the provider’s vendor-specific authentication area}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "page_name": "",
          "description": "",
          "vendor_preset": "",
          "vendor_ip": "",
          "require_https": "",
          "webauth": "",
          "form_action": "",
          "form_method": "",
          "form_username_label": "",
          "form_username": "",
          "form_username_suffix": "",
          "form_password_label": "",
          "form_password": "",
          "form_extra": "",
          "submit_label": "",
          "form_password_encryption": "",
          "uam_secret": "",
          "url": "",
          "default_url": "",
          "default_url_override": false,
          "dynamic_address": false,
          "dynamic_allowlist": "",
          "dynamic_denylist": "",
          "access_allowlist": "",
          "access_denylist": "",
          "access_if_denied": "",
          "login_title": "",
          "login_header": "",
          "login_footer": "",
          "login_message": "",
          "login_delay": 0,
          "login_skin": "",
          "login_terms_require": false,
          "login_terms_label": "",
          "login_terms_text": "",
          "login_terms_layout": "",
          "login_terms_error": "",
          "login_captcha": "",
          "username_auth": "",
          "certificate_request": "",
          "username_auth_username": "",
          "certificate_auth": "",
          "register_policy_manager": false,
          "register_policy_manager_adv": false,
          "register_policy_manager_attrs": "",
          "hash_url": "",
          "hash_secret": "",
          "bypass_cna": false,
          "capport_venue_url": "",
          "onguard_healthcheck": false,
          "onguard_agents": "",
          "onguard_header": "",
          "onguard_footer": "",
          "oauth_enabled": false,
          "oauth_debug": false,
          "oauth_providers": "object",
          "login_custom_form": false,
          "login_pre_auth_check": "",
          "login_pre_auth_error": "",
          "mfa_enabled": "",
          "mfa_first": "",
          "mfa_duo_ikey": "",
          "mfa_duo_skey": "",
          "mfa_duo_host": "",
          "mfa_fn_client_id": "",
          "mfa_fn_client_secret": "",
          "mfa_fn_factors": "",
          "mfa_fn_email": false,
          "mfa_iws_tenant": "",
          "mfa_iws_app": "",
          "mfa_iws_hostname": "",
          "mfa_mc_scope": "",
          "mfa_mc_context": "",
          "mfa_mc_binding_message": "",
          "mfa_mc_acr_values": "",
          "mfa_mc_display": "",
          "mfa_mc_prompt": "",
          "mfa_mc_max_age": 0,
          "mfa_mc_login_hint": "",
          "mfa_mc_version": "",
          "mfa_mc_discovery_service_endpoint": "",
          "mfa_mc_redirect_url": "",
          "mfa_mc_client_id": "",
          "mfa_mc_client_secret": "",
          "mfa_header_html": "",
          "mfa_footer_html": ""
        }
        """
        url_path = "/weblogin/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_weblogin_by_id(self, id="", body=({})):
        """
                Operation: Replace a web login page
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: id, Description: URL parameter id
                Required Body Parameters (body description)- WebLogin {id (integer, optional): Unique ID of the web login,name (string): Enter a name for this web login page,page_name (string, optional): Enter a page name for this web login.
        The web login will be accessible from “/guest/page_name.php”,description (string, optional): Comments or descriptive text about the web login,vendor_preset (string): Select a predefined group of settings suitable for standard network configurations,vendor_ip (string, optional): Enter the hostname (FQDN) of the vendor’s product here.
        When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device,require_https (string, optional): Select a security option to apply to the web login process,webauth (string, optional): Select how the user’s network login will be handled.
        Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process,form_action (string): The URL of the NAS device’s login form,form_method (string): Choose the method to use when submitting the login form to the NAS,form_username_label (string, optional): The form label for the username field.
        Leave blank to use the default (Username:),form_username (string): The name of the username field for the login form. This will be passed to the NAS device when the form is submitted,form_username_suffix (string, optional): The suffix is automatically appended to the username before submitting the login form to the NAS,form_password_label (string, optional): The form label for the password field.
        Leave blank to use the default (Password:),form_password (string): The name of the password field for the login form. This will be passed to the NAS device when the form is submitted,form_extra (string, optional): Specify any additional field names and values to send to the NAS device as name=value pairs, one per line,submit_label (string, optional): The form label for the log in button.
        Leave blank to use the default (Log In),form_password_encryption (string): Choose the type of password encryption to use when submitting the login form,uam_secret (string, optional): Enter the shared secret between the NAS device and the web login form,url (string, optional): The name of the destination field required by the NAS,default_url (string, optional): Enter the default URL to redirect clients.
        Please ensure you prepend "http://" for any external domain,default_url_override (boolean, optional): If selected, the client’s default destination will be overridden regardless of its value,dynamic_address (boolean, optional): In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.
        The address above will be used whenever the parameter is not available or fails the requirements below,dynamic_allowlist (string, optional): Enter the IP addresses and networks from which dynamic addresses are permitted,dynamic_denylist (string, optional): Enter the IP addresses and networks from which dynamic addresses are denied,access_allowlist (string, optional): Enter the IP addresses and networks from which logins are permitted,access_denylist (string, optional): Enter the IP addresses and networks that are denied login access,access_if_denied (string): Select the response of the system to a request that is not permitted,login_title (string, optional): The title to display on the web login page.
        Leave blank to use the default (Login),login_header (string, optional): HTML template code displayed before the login form,login_footer (string, optional): HTML template code displayed after the login form,login_message (string, optional): HTML template code displayed while the login attempt is in progress,login_delay (number): The time in seconds to delay while displaying the login message,login_skin (string): Choose the skin to use when this web login page is displayed,login_terms_require (boolean, optional): If checked, the user will be forced to accept a Terms and Conditions checkbox,login_terms_label (string, optional): The form label for the terms checkbox.
        Leave blank to use the default (Terms:),login_terms_text (string, optional): HTML code containing your Terms and Conditions.
        Leave blank to use the default (I accept the terms of use),login_terms_layout (string, optional): Select the layout for the terms and conditions text,login_terms_error (string, optional): The text to display if the terms are not accepted.
        Leave blank to use the default (In order to log in, you must accept the terms and conditions.),login_captcha (string, optional): Select a CAPTCHA mode,username_auth (string, optional): Select the authentication requirement.
        Access Code requires a single code (username) to be entered.
        Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.
        Auto is similar to anonymous but the page is automatically submitted.
        Access Code and Anonymous require the account to have the Username Authentication field set,certificate_request (string, optional): Choose whether the user should select a client certificate when authenticating,username_auth_username (string, optional): The account to use for anonymous authentication.
        The password will be visible within the HTML.
        It is recommended to increase the account Session Limit to the number of guests you wish to support,certificate_auth (string, optional): Choose whether other credentials must also be provided in addition to a certificate,register_policy_manager (boolean, optional): If selected, the endpoint’s attributes will also be updated with other details from the user account,register_policy_manager_adv (boolean, optional): Customize attributes stored with the endpoint,register_policy_manager_attrs (string, optional): List of name|value pairs to pass along.
        user_field | Endpoint Attribute,hash_url (string, optional): Select the level of checking to apply to URL parameters passed to the web login page.
        Use this option to detect when URL parameters have been modified by the user, for example their MAC address,hash_secret (string, optional): The redirection URL will be hashed using this shared secret,bypass_cna (boolean, optional): The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.
        Note that this option may not work with all vendors, depending on how the captive portal is implemented,capport_venue_url (string, optional): Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.
        https://www.rfc-editor.org/rfc/rfc8908.html,onguard_healthcheck (boolean, optional): If selected, the guest will be required to pass a health check prior to accessing the network,onguard_agents (string, optional): Select the agent options for client scanning.
        Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java,onguard_header (string, optional): HTML template code displayed before the health check text,onguard_footer (string, optional): HTML template code displayed after the health check text,oauth_enabled (boolean, optional): Enable logins with cloud identity / social network credentials,oauth_debug (boolean, optional): Log debugging data,oauth_providers (object, optional): Configuration for cloud identity authentication providers,login_custom_form (boolean, optional): If selected, you must supply your own HTML login form in the Header or Footer HTML areas,login_pre_auth_check (string): Select how the username and password should be checked before proceeding to the NAS authentication,login_pre_auth_error (string, optional): The text to display if the username and password lookup fails.
        Leave blank to use the default (Invalid username or password),mfa_enabled (string, optional),mfa_first (string, optional): All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device,mfa_duo_ikey (string, optional),mfa_duo_skey (string, optional),mfa_duo_host (string, optional),mfa_fn_client_id (string, optional),mfa_fn_client_secret (string, optional),mfa_fn_factors (string, optional): Enter the number of factors to require,mfa_fn_email (boolean, optional): If disabled, the user must scan the QR code,mfa_iws_tenant (string, optional),mfa_iws_app (string, optional),mfa_iws_hostname (string, optional): Enter the hostname of the ImageWare server,mfa_mc_scope (string, optional): OAuth 2.0 scope value. Only mc_authn is supported for this release,mfa_mc_context (string, optional): Message which will be displayed on the authorization device,mfa_mc_binding_message (string, optional): Plain text reference to interlock the consumption device and authorization device,mfa_mc_acr_values (string, optional): Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6,mfa_mc_display (string, optional): User interface display for Authentication,mfa_mc_prompt (string, optional): Value to specify to the Authorisation server about type of prompt,mfa_mc_max_age (integer, optional): Maximum elapsed time in secs since last authenticaiton,mfa_mc_login_hint (string, optional): An indication to IDP on what ID to use for login,mfa_mc_version (string, optional),mfa_mc_discovery_service_endpoint (string, optional): Provide the endpoint URL provided by Mobile Connect during configuration,mfa_mc_redirect_url (string, optional): Mobile Connect Redirect URL provided during configuration,mfa_mc_client_id (string, optional),mfa_mc_client_secret (string, optional),mfa_header_html (string, optional): HTML template code displayed before the provider’s vendor-specific authentication area,mfa_footer_html (string, optional): HTML template code displayed after the provider’s vendor-specific authentication area}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "page_name": "",
          "description": "",
          "vendor_preset": "",
          "vendor_ip": "",
          "require_https": "",
          "webauth": "",
          "form_action": "",
          "form_method": "",
          "form_username_label": "",
          "form_username": "",
          "form_username_suffix": "",
          "form_password_label": "",
          "form_password": "",
          "form_extra": "",
          "submit_label": "",
          "form_password_encryption": "",
          "uam_secret": "",
          "url": "",
          "default_url": "",
          "default_url_override": false,
          "dynamic_address": false,
          "dynamic_allowlist": "",
          "dynamic_denylist": "",
          "access_allowlist": "",
          "access_denylist": "",
          "access_if_denied": "",
          "login_title": "",
          "login_header": "",
          "login_footer": "",
          "login_message": "",
          "login_delay": 0,
          "login_skin": "",
          "login_terms_require": false,
          "login_terms_label": "",
          "login_terms_text": "",
          "login_terms_layout": "",
          "login_terms_error": "",
          "login_captcha": "",
          "username_auth": "",
          "certificate_request": "",
          "username_auth_username": "",
          "certificate_auth": "",
          "register_policy_manager": false,
          "register_policy_manager_adv": false,
          "register_policy_manager_attrs": "",
          "hash_url": "",
          "hash_secret": "",
          "bypass_cna": false,
          "capport_venue_url": "",
          "onguard_healthcheck": false,
          "onguard_agents": "",
          "onguard_header": "",
          "onguard_footer": "",
          "oauth_enabled": false,
          "oauth_debug": false,
          "oauth_providers": "object",
          "login_custom_form": false,
          "login_pre_auth_check": "",
          "login_pre_auth_error": "",
          "mfa_enabled": "",
          "mfa_first": "",
          "mfa_duo_ikey": "",
          "mfa_duo_skey": "",
          "mfa_duo_host": "",
          "mfa_fn_client_id": "",
          "mfa_fn_client_secret": "",
          "mfa_fn_factors": "",
          "mfa_fn_email": false,
          "mfa_iws_tenant": "",
          "mfa_iws_app": "",
          "mfa_iws_hostname": "",
          "mfa_mc_scope": "",
          "mfa_mc_context": "",
          "mfa_mc_binding_message": "",
          "mfa_mc_acr_values": "",
          "mfa_mc_display": "",
          "mfa_mc_prompt": "",
          "mfa_mc_max_age": 0,
          "mfa_mc_login_hint": "",
          "mfa_mc_version": "",
          "mfa_mc_discovery_service_endpoint": "",
          "mfa_mc_redirect_url": "",
          "mfa_mc_client_id": "",
          "mfa_mc_client_secret": "",
          "mfa_header_html": "",
          "mfa_footer_html": ""
        }
        """
        url_path = "/weblogin/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_weblogin_by_id(self, id=""):
        """
        Operation: Delete a web login page
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: id, Description: URL parameter id
        """
        url_path = "/weblogin/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_weblogin_page_name_by_page_name(self, page__name=""):
        """
        Operation: Get a web login page by page-name
        HTTP Status Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: page-name, Description: Unique page name of the web login
        """
        url_path = "/weblogin/page-name/{page__name}"
        dict_path = {"page__name": page__name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_weblogin_page_name_by_page_name(self, page__name="", body=({})):
        """
                Operation: Update some fields of a web login page by page-name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: page-name, Description: Unique page name of the web login
                Required Body Parameters (body description)- WebLogin {id (integer, optional): Unique ID of the web login,name (string): Enter a name for this web login page,page_name (string, optional): Enter a page name for this web login.
        The web login will be accessible from “/guest/page_name.php”,description (string, optional): Comments or descriptive text about the web login,vendor_preset (string): Select a predefined group of settings suitable for standard network configurations,vendor_ip (string, optional): Enter the hostname (FQDN) of the vendor’s product here.
        When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device,require_https (string, optional): Select a security option to apply to the web login process,webauth (string, optional): Select how the user’s network login will be handled.
        Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process,form_action (string): The URL of the NAS device’s login form,form_method (string): Choose the method to use when submitting the login form to the NAS,form_username_label (string, optional): The form label for the username field.
        Leave blank to use the default (Username:),form_username (string): The name of the username field for the login form. This will be passed to the NAS device when the form is submitted,form_username_suffix (string, optional): The suffix is automatically appended to the username before submitting the login form to the NAS,form_password_label (string, optional): The form label for the password field.
        Leave blank to use the default (Password:),form_password (string): The name of the password field for the login form. This will be passed to the NAS device when the form is submitted,form_extra (string, optional): Specify any additional field names and values to send to the NAS device as name=value pairs, one per line,submit_label (string, optional): The form label for the log in button.
        Leave blank to use the default (Log In),form_password_encryption (string): Choose the type of password encryption to use when submitting the login form,uam_secret (string, optional): Enter the shared secret between the NAS device and the web login form,url (string, optional): The name of the destination field required by the NAS,default_url (string, optional): Enter the default URL to redirect clients.
        Please ensure you prepend "http://" for any external domain,default_url_override (boolean, optional): If selected, the client’s default destination will be overridden regardless of its value,dynamic_address (boolean, optional): In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.
        The address above will be used whenever the parameter is not available or fails the requirements below,dynamic_allowlist (string, optional): Enter the IP addresses and networks from which dynamic addresses are permitted,dynamic_denylist (string, optional): Enter the IP addresses and networks from which dynamic addresses are denied,access_allowlist (string, optional): Enter the IP addresses and networks from which logins are permitted,access_denylist (string, optional): Enter the IP addresses and networks that are denied login access,access_if_denied (string): Select the response of the system to a request that is not permitted,login_title (string, optional): The title to display on the web login page.
        Leave blank to use the default (Login),login_header (string, optional): HTML template code displayed before the login form,login_footer (string, optional): HTML template code displayed after the login form,login_message (string, optional): HTML template code displayed while the login attempt is in progress,login_delay (number): The time in seconds to delay while displaying the login message,login_skin (string): Choose the skin to use when this web login page is displayed,login_terms_require (boolean, optional): If checked, the user will be forced to accept a Terms and Conditions checkbox,login_terms_label (string, optional): The form label for the terms checkbox.
        Leave blank to use the default (Terms:),login_terms_text (string, optional): HTML code containing your Terms and Conditions.
        Leave blank to use the default (I accept the terms of use),login_terms_layout (string, optional): Select the layout for the terms and conditions text,login_terms_error (string, optional): The text to display if the terms are not accepted.
        Leave blank to use the default (In order to log in, you must accept the terms and conditions.),login_captcha (string, optional): Select a CAPTCHA mode,username_auth (string, optional): Select the authentication requirement.
        Access Code requires a single code (username) to be entered.
        Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.
        Auto is similar to anonymous but the page is automatically submitted.
        Access Code and Anonymous require the account to have the Username Authentication field set,certificate_request (string, optional): Choose whether the user should select a client certificate when authenticating,username_auth_username (string, optional): The account to use for anonymous authentication.
        The password will be visible within the HTML.
        It is recommended to increase the account Session Limit to the number of guests you wish to support,certificate_auth (string, optional): Choose whether other credentials must also be provided in addition to a certificate,register_policy_manager (boolean, optional): If selected, the endpoint’s attributes will also be updated with other details from the user account,register_policy_manager_adv (boolean, optional): Customize attributes stored with the endpoint,register_policy_manager_attrs (string, optional): List of name|value pairs to pass along.
        user_field | Endpoint Attribute,hash_url (string, optional): Select the level of checking to apply to URL parameters passed to the web login page.
        Use this option to detect when URL parameters have been modified by the user, for example their MAC address,hash_secret (string, optional): The redirection URL will be hashed using this shared secret,bypass_cna (boolean, optional): The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.
        Note that this option may not work with all vendors, depending on how the captive portal is implemented,capport_venue_url (string, optional): Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.
        https://www.rfc-editor.org/rfc/rfc8908.html,onguard_healthcheck (boolean, optional): If selected, the guest will be required to pass a health check prior to accessing the network,onguard_agents (string, optional): Select the agent options for client scanning.
        Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java,onguard_header (string, optional): HTML template code displayed before the health check text,onguard_footer (string, optional): HTML template code displayed after the health check text,oauth_enabled (boolean, optional): Enable logins with cloud identity / social network credentials,oauth_debug (boolean, optional): Log debugging data,oauth_providers (object, optional): Configuration for cloud identity authentication providers,login_custom_form (boolean, optional): If selected, you must supply your own HTML login form in the Header or Footer HTML areas,login_pre_auth_check (string): Select how the username and password should be checked before proceeding to the NAS authentication,login_pre_auth_error (string, optional): The text to display if the username and password lookup fails.
        Leave blank to use the default (Invalid username or password),mfa_enabled (string, optional),mfa_first (string, optional): All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device,mfa_duo_ikey (string, optional),mfa_duo_skey (string, optional),mfa_duo_host (string, optional),mfa_fn_client_id (string, optional),mfa_fn_client_secret (string, optional),mfa_fn_factors (string, optional): Enter the number of factors to require,mfa_fn_email (boolean, optional): If disabled, the user must scan the QR code,mfa_iws_tenant (string, optional),mfa_iws_app (string, optional),mfa_iws_hostname (string, optional): Enter the hostname of the ImageWare server,mfa_mc_scope (string, optional): OAuth 2.0 scope value. Only mc_authn is supported for this release,mfa_mc_context (string, optional): Message which will be displayed on the authorization device,mfa_mc_binding_message (string, optional): Plain text reference to interlock the consumption device and authorization device,mfa_mc_acr_values (string, optional): Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6,mfa_mc_display (string, optional): User interface display for Authentication,mfa_mc_prompt (string, optional): Value to specify to the Authorisation server about type of prompt,mfa_mc_max_age (integer, optional): Maximum elapsed time in secs since last authenticaiton,mfa_mc_login_hint (string, optional): An indication to IDP on what ID to use for login,mfa_mc_version (string, optional),mfa_mc_discovery_service_endpoint (string, optional): Provide the endpoint URL provided by Mobile Connect during configuration,mfa_mc_redirect_url (string, optional): Mobile Connect Redirect URL provided during configuration,mfa_mc_client_id (string, optional),mfa_mc_client_secret (string, optional),mfa_header_html (string, optional): HTML template code displayed before the provider’s vendor-specific authentication area,mfa_footer_html (string, optional): HTML template code displayed after the provider’s vendor-specific authentication area}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "page_name": "",
          "description": "",
          "vendor_preset": "",
          "vendor_ip": "",
          "require_https": "",
          "webauth": "",
          "form_action": "",
          "form_method": "",
          "form_username_label": "",
          "form_username": "",
          "form_username_suffix": "",
          "form_password_label": "",
          "form_password": "",
          "form_extra": "",
          "submit_label": "",
          "form_password_encryption": "",
          "uam_secret": "",
          "url": "",
          "default_url": "",
          "default_url_override": false,
          "dynamic_address": false,
          "dynamic_allowlist": "",
          "dynamic_denylist": "",
          "access_allowlist": "",
          "access_denylist": "",
          "access_if_denied": "",
          "login_title": "",
          "login_header": "",
          "login_footer": "",
          "login_message": "",
          "login_delay": 0,
          "login_skin": "",
          "login_terms_require": false,
          "login_terms_label": "",
          "login_terms_text": "",
          "login_terms_layout": "",
          "login_terms_error": "",
          "login_captcha": "",
          "username_auth": "",
          "certificate_request": "",
          "username_auth_username": "",
          "certificate_auth": "",
          "register_policy_manager": false,
          "register_policy_manager_adv": false,
          "register_policy_manager_attrs": "",
          "hash_url": "",
          "hash_secret": "",
          "bypass_cna": false,
          "capport_venue_url": "",
          "onguard_healthcheck": false,
          "onguard_agents": "",
          "onguard_header": "",
          "onguard_footer": "",
          "oauth_enabled": false,
          "oauth_debug": false,
          "oauth_providers": "object",
          "login_custom_form": false,
          "login_pre_auth_check": "",
          "login_pre_auth_error": "",
          "mfa_enabled": "",
          "mfa_first": "",
          "mfa_duo_ikey": "",
          "mfa_duo_skey": "",
          "mfa_duo_host": "",
          "mfa_fn_client_id": "",
          "mfa_fn_client_secret": "",
          "mfa_fn_factors": "",
          "mfa_fn_email": false,
          "mfa_iws_tenant": "",
          "mfa_iws_app": "",
          "mfa_iws_hostname": "",
          "mfa_mc_scope": "",
          "mfa_mc_context": "",
          "mfa_mc_binding_message": "",
          "mfa_mc_acr_values": "",
          "mfa_mc_display": "",
          "mfa_mc_prompt": "",
          "mfa_mc_max_age": 0,
          "mfa_mc_login_hint": "",
          "mfa_mc_version": "",
          "mfa_mc_discovery_service_endpoint": "",
          "mfa_mc_redirect_url": "",
          "mfa_mc_client_id": "",
          "mfa_mc_client_secret": "",
          "mfa_header_html": "",
          "mfa_footer_html": ""
        }
        """
        url_path = "/weblogin/page-name/{page__name}"
        dict_path = {"page__name": page__name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_weblogin_page_name_by_page_name(self, page__name="", body=({})):
        """
                Operation: Replace a web login page by page-name
                HTTP Status Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: page-name, Description: Unique page name of the web login
                Required Body Parameters (body description)- WebLogin {id (integer, optional): Unique ID of the web login,name (string): Enter a name for this web login page,page_name (string, optional): Enter a page name for this web login.
        The web login will be accessible from “/guest/page_name.php”,description (string, optional): Comments or descriptive text about the web login,vendor_preset (string): Select a predefined group of settings suitable for standard network configurations,vendor_ip (string, optional): Enter the hostname (FQDN) of the vendor’s product here.
        When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device,require_https (string, optional): Select a security option to apply to the web login process,webauth (string, optional): Select how the user’s network login will be handled.
        Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process,form_action (string): The URL of the NAS device’s login form,form_method (string): Choose the method to use when submitting the login form to the NAS,form_username_label (string, optional): The form label for the username field.
        Leave blank to use the default (Username:),form_username (string): The name of the username field for the login form. This will be passed to the NAS device when the form is submitted,form_username_suffix (string, optional): The suffix is automatically appended to the username before submitting the login form to the NAS,form_password_label (string, optional): The form label for the password field.
        Leave blank to use the default (Password:),form_password (string): The name of the password field for the login form. This will be passed to the NAS device when the form is submitted,form_extra (string, optional): Specify any additional field names and values to send to the NAS device as name=value pairs, one per line,submit_label (string, optional): The form label for the log in button.
        Leave blank to use the default (Log In),form_password_encryption (string): Choose the type of password encryption to use when submitting the login form,uam_secret (string, optional): Enter the shared secret between the NAS device and the web login form,url (string, optional): The name of the destination field required by the NAS,default_url (string, optional): Enter the default URL to redirect clients.
        Please ensure you prepend "http://" for any external domain,default_url_override (boolean, optional): If selected, the client’s default destination will be overridden regardless of its value,dynamic_address (boolean, optional): In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.
        The address above will be used whenever the parameter is not available or fails the requirements below,dynamic_allowlist (string, optional): Enter the IP addresses and networks from which dynamic addresses are permitted,dynamic_denylist (string, optional): Enter the IP addresses and networks from which dynamic addresses are denied,access_allowlist (string, optional): Enter the IP addresses and networks from which logins are permitted,access_denylist (string, optional): Enter the IP addresses and networks that are denied login access,access_if_denied (string): Select the response of the system to a request that is not permitted,login_title (string, optional): The title to display on the web login page.
        Leave blank to use the default (Login),login_header (string, optional): HTML template code displayed before the login form,login_footer (string, optional): HTML template code displayed after the login form,login_message (string, optional): HTML template code displayed while the login attempt is in progress,login_delay (number): The time in seconds to delay while displaying the login message,login_skin (string): Choose the skin to use when this web login page is displayed,login_terms_require (boolean, optional): If checked, the user will be forced to accept a Terms and Conditions checkbox,login_terms_label (string, optional): The form label for the terms checkbox.
        Leave blank to use the default (Terms:),login_terms_text (string, optional): HTML code containing your Terms and Conditions.
        Leave blank to use the default (I accept the terms of use),login_terms_layout (string, optional): Select the layout for the terms and conditions text,login_terms_error (string, optional): The text to display if the terms are not accepted.
        Leave blank to use the default (In order to log in, you must accept the terms and conditions.),login_captcha (string, optional): Select a CAPTCHA mode,username_auth (string, optional): Select the authentication requirement.
        Access Code requires a single code (username) to be entered.
        Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.
        Auto is similar to anonymous but the page is automatically submitted.
        Access Code and Anonymous require the account to have the Username Authentication field set,certificate_request (string, optional): Choose whether the user should select a client certificate when authenticating,username_auth_username (string, optional): The account to use for anonymous authentication.
        The password will be visible within the HTML.
        It is recommended to increase the account Session Limit to the number of guests you wish to support,certificate_auth (string, optional): Choose whether other credentials must also be provided in addition to a certificate,register_policy_manager (boolean, optional): If selected, the endpoint’s attributes will also be updated with other details from the user account,register_policy_manager_adv (boolean, optional): Customize attributes stored with the endpoint,register_policy_manager_attrs (string, optional): List of name|value pairs to pass along.
        user_field | Endpoint Attribute,hash_url (string, optional): Select the level of checking to apply to URL parameters passed to the web login page.
        Use this option to detect when URL parameters have been modified by the user, for example their MAC address,hash_secret (string, optional): The redirection URL will be hashed using this shared secret,bypass_cna (boolean, optional): The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.
        Note that this option may not work with all vendors, depending on how the captive portal is implemented,capport_venue_url (string, optional): Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.
        https://www.rfc-editor.org/rfc/rfc8908.html,onguard_healthcheck (boolean, optional): If selected, the guest will be required to pass a health check prior to accessing the network,onguard_agents (string, optional): Select the agent options for client scanning.
        Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java,onguard_header (string, optional): HTML template code displayed before the health check text,onguard_footer (string, optional): HTML template code displayed after the health check text,oauth_enabled (boolean, optional): Enable logins with cloud identity / social network credentials,oauth_debug (boolean, optional): Log debugging data,oauth_providers (object, optional): Configuration for cloud identity authentication providers,login_custom_form (boolean, optional): If selected, you must supply your own HTML login form in the Header or Footer HTML areas,login_pre_auth_check (string): Select how the username and password should be checked before proceeding to the NAS authentication,login_pre_auth_error (string, optional): The text to display if the username and password lookup fails.
        Leave blank to use the default (Invalid username or password),mfa_enabled (string, optional),mfa_first (string, optional): All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device,mfa_duo_ikey (string, optional),mfa_duo_skey (string, optional),mfa_duo_host (string, optional),mfa_fn_client_id (string, optional),mfa_fn_client_secret (string, optional),mfa_fn_factors (string, optional): Enter the number of factors to require,mfa_fn_email (boolean, optional): If disabled, the user must scan the QR code,mfa_iws_tenant (string, optional),mfa_iws_app (string, optional),mfa_iws_hostname (string, optional): Enter the hostname of the ImageWare server,mfa_mc_scope (string, optional): OAuth 2.0 scope value. Only mc_authn is supported for this release,mfa_mc_context (string, optional): Message which will be displayed on the authorization device,mfa_mc_binding_message (string, optional): Plain text reference to interlock the consumption device and authorization device,mfa_mc_acr_values (string, optional): Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6,mfa_mc_display (string, optional): User interface display for Authentication,mfa_mc_prompt (string, optional): Value to specify to the Authorisation server about type of prompt,mfa_mc_max_age (integer, optional): Maximum elapsed time in secs since last authenticaiton,mfa_mc_login_hint (string, optional): An indication to IDP on what ID to use for login,mfa_mc_version (string, optional),mfa_mc_discovery_service_endpoint (string, optional): Provide the endpoint URL provided by Mobile Connect during configuration,mfa_mc_redirect_url (string, optional): Mobile Connect Redirect URL provided during configuration,mfa_mc_client_id (string, optional),mfa_mc_client_secret (string, optional),mfa_header_html (string, optional): HTML template code displayed before the provider’s vendor-specific authentication area,mfa_footer_html (string, optional): HTML template code displayed after the provider’s vendor-specific authentication area}
                Required Body Parameters (type(dict) body example)- {
          "id": 0,
          "name": "",
          "page_name": "",
          "description": "",
          "vendor_preset": "",
          "vendor_ip": "",
          "require_https": "",
          "webauth": "",
          "form_action": "",
          "form_method": "",
          "form_username_label": "",
          "form_username": "",
          "form_username_suffix": "",
          "form_password_label": "",
          "form_password": "",
          "form_extra": "",
          "submit_label": "",
          "form_password_encryption": "",
          "uam_secret": "",
          "url": "",
          "default_url": "",
          "default_url_override": false,
          "dynamic_address": false,
          "dynamic_allowlist": "",
          "dynamic_denylist": "",
          "access_allowlist": "",
          "access_denylist": "",
          "access_if_denied": "",
          "login_title": "",
          "login_header": "",
          "login_footer": "",
          "login_message": "",
          "login_delay": 0,
          "login_skin": "",
          "login_terms_require": false,
          "login_terms_label": "",
          "login_terms_text": "",
          "login_terms_layout": "",
          "login_terms_error": "",
          "login_captcha": "",
          "username_auth": "",
          "certificate_request": "",
          "username_auth_username": "",
          "certificate_auth": "",
          "register_policy_manager": false,
          "register_policy_manager_adv": false,
          "register_policy_manager_attrs": "",
          "hash_url": "",
          "hash_secret": "",
          "bypass_cna": false,
          "capport_venue_url": "",
          "onguard_healthcheck": false,
          "onguard_agents": "",
          "onguard_header": "",
          "onguard_footer": "",
          "oauth_enabled": false,
          "oauth_debug": false,
          "oauth_providers": "object",
          "login_custom_form": false,
          "login_pre_auth_check": "",
          "login_pre_auth_error": "",
          "mfa_enabled": "",
          "mfa_first": "",
          "mfa_duo_ikey": "",
          "mfa_duo_skey": "",
          "mfa_duo_host": "",
          "mfa_fn_client_id": "",
          "mfa_fn_client_secret": "",
          "mfa_fn_factors": "",
          "mfa_fn_email": false,
          "mfa_iws_tenant": "",
          "mfa_iws_app": "",
          "mfa_iws_hostname": "",
          "mfa_mc_scope": "",
          "mfa_mc_context": "",
          "mfa_mc_binding_message": "",
          "mfa_mc_acr_values": "",
          "mfa_mc_display": "",
          "mfa_mc_prompt": "",
          "mfa_mc_max_age": 0,
          "mfa_mc_login_hint": "",
          "mfa_mc_version": "",
          "mfa_mc_discovery_service_endpoint": "",
          "mfa_mc_redirect_url": "",
          "mfa_mc_client_id": "",
          "mfa_mc_client_secret": "",
          "mfa_header_html": "",
          "mfa_footer_html": ""
        }
        """
        url_path = "/weblogin/page-name/{page__name}"
        dict_path = {"page__name": page__name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_weblogin_page_name_by_page_name(self, page__name=""):
        """
        Operation: Delete a web login page by page-name
        HTTP Status Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Required Path Parameter Name: page-name, Description: Unique page name of the web login
        """
        url_path = "/weblogin/page-name/{page__name}"
        dict_path = {"page__name": page__name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
