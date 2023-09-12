from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: GuestConfiguration
# FileName: api_guestconfiguration.py


class ApiGuestConfiguration(ClearPassAPILogin):
    # API Service: Manage pass templates
    def get_template_pass(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of pass templates
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default -id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #No Desc. Object Type: string
        "description" : "", #No Desc. Object Type: string
        "background_color" : "", #No Desc. Object Type: string
        "foreground_color" : "", #No Desc. Object Type: string
        "reset" : "", #No Desc. Object Type: string
        "label_color" : "", #No Desc. Object Type: string
        "summary_template" : "", #No Desc. Object Type: string
        "pass_style" : "", #No Desc. Object Type: string
        "transit_type" : "", #No Desc. Object Type: string
        "icon_image" : "", #No Desc. Object Type: string
        "logo_image" : "", #No Desc. Object Type: string
        "logo_text_template" : "", #No Desc. Object Type: string
        "background_image" : 0, #No Desc. Object Type: integer
        "thumbnail_image" : 0, #No Desc. Object Type: integer
        "strip_image" : 0, #No Desc. Object Type: integer
        "strip_shine" : "", #No Desc. Object Type: string
        "footer_image" : 0, #No Desc. Object Type: integer
        "pass_fields" : 0, #No Desc. Object Type: array
        "relevant_locations" : False, #No Desc. Object Type: boolean
        "pass_locations" : False, #No Desc. Object Type: array
        "relevant_date" : False, #No Desc. Object Type: boolean
        "relevant_date_mode" : "", #No Desc. Object Type: string
        "relevant_date_rank" : 0, #No Desc. Object Type: integer
        "relevant_date_template" : "", #No Desc. Object Type: string
        "associated_apps" : False, #No Desc. Object Type: boolean
        "pass_apps" : False, #No Desc. Object Type: array
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/template/pass/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_template_pass_by_id(self, id="", body=({})):
        """
        Operation: Update some fields of a pass template
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: URL parameter id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #No Desc. Object Type: string
        "description" : "", #No Desc. Object Type: string
        "background_color" : "", #No Desc. Object Type: string
        "foreground_color" : "", #No Desc. Object Type: string
        "reset" : "", #No Desc. Object Type: string
        "label_color" : "", #No Desc. Object Type: string
        "summary_template" : "", #No Desc. Object Type: string
        "pass_style" : "", #No Desc. Object Type: string
        "transit_type" : "", #No Desc. Object Type: string
        "icon_image" : "", #No Desc. Object Type: string
        "logo_image" : "", #No Desc. Object Type: string
        "logo_text_template" : "", #No Desc. Object Type: string
        "background_image" : 0, #No Desc. Object Type: integer
        "thumbnail_image" : 0, #No Desc. Object Type: integer
        "strip_image" : 0, #No Desc. Object Type: integer
        "strip_shine" : "", #No Desc. Object Type: string
        "footer_image" : 0, #No Desc. Object Type: integer
        "pass_fields" : 0, #No Desc. Object Type: array
        "relevant_locations" : False, #No Desc. Object Type: boolean
        "pass_locations" : False, #No Desc. Object Type: array
        "relevant_date" : False, #No Desc. Object Type: boolean
        "relevant_date_mode" : "", #No Desc. Object Type: string
        "relevant_date_rank" : 0, #No Desc. Object Type: integer
        "relevant_date_template" : "", #No Desc. Object Type: string
        "associated_apps" : False, #No Desc. Object Type: boolean
        "pass_apps" : False, #No Desc. Object Type: array
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: URL parameter id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #No Desc. Object Type: integer
        "name" : "", #No Desc. Object Type: string
        "description" : "", #No Desc. Object Type: string
        "background_color" : "", #No Desc. Object Type: string
        "foreground_color" : "", #No Desc. Object Type: string
        "reset" : "", #No Desc. Object Type: string
        "label_color" : "", #No Desc. Object Type: string
        "summary_template" : "", #No Desc. Object Type: string
        "pass_style" : "", #No Desc. Object Type: string
        "transit_type" : "", #No Desc. Object Type: string
        "icon_image" : "", #No Desc. Object Type: string
        "logo_image" : "", #No Desc. Object Type: string
        "logo_text_template" : "", #No Desc. Object Type: string
        "background_image" : 0, #No Desc. Object Type: integer
        "thumbnail_image" : 0, #No Desc. Object Type: integer
        "strip_image" : 0, #No Desc. Object Type: integer
        "strip_shine" : "", #No Desc. Object Type: string
        "footer_image" : 0, #No Desc. Object Type: integer
        "pass_fields" : 0, #No Desc. Object Type: array
        "relevant_locations" : False, #No Desc. Object Type: boolean
        "pass_locations" : False, #No Desc. Object Type: array
        "relevant_date" : False, #No Desc. Object Type: boolean
        "relevant_date_mode" : "", #No Desc. Object Type: string
        "relevant_date_rank" : 0, #No Desc. Object Type: integer
        "relevant_date_template" : "", #No Desc. Object Type: string
        "associated_apps" : False, #No Desc. Object Type: boolean
        "pass_apps" : False, #No Desc. Object Type: array
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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/template/pass/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage settings in Configuration -> Authentication
    def get_guest_authentication(self):
        """
        Operation: Return settings from Configuration -> Authentication
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/guest/authentication"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_guest_authentication(self, body=({})):
        """
        Operation: Modify settings at Configuration -> Authentication
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['g_radius_internal_auth_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "g_admin_access_guest_require_https" : False, #If checked, HTTP access by guests will be redirected to use HTTPS instead. Object Type: boolean
        "change_of_authorization" : False, #Global to automatically send disconnects when enabled/role values change.Requires a NAS Type supporting RFC-3576. Object Type: boolean
        "g_radius_default_vendor" : "", #Select the default type for network access servers. Object Type: string
        "g_radius_server_bind_3576" : "", #Force a specific bind address for RFC-3576 requests.  This may be needed in an AirGroup environment.Defaults to '0.0.0.0' or '::' depending on your network. Object Type: string
        "g_radius_internal_auth_type" : "", #Controls the RADIUS authentication type used for internal RADIUS authentication requests. Object Type: string
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['g_radius_internal_auth_type']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "g_admin_access_guest_require_https" : False, #If checked, HTTP access by guests will be redirected to use HTTPS instead. Object Type: boolean
        "change_of_authorization" : False, #Global to automatically send disconnects when enabled/role values change.Requires a NAS Type supporting RFC-3576. Object Type: boolean
        "g_radius_default_vendor" : "", #Select the default type for network access servers. Object Type: string
        "g_radius_server_bind_3576" : "", #Force a specific bind address for RFC-3576 requests.  This may be needed in an AirGroup environment.Defaults to '0.0.0.0' or '::' depending on your network. Object Type: string
        "g_radius_internal_auth_type" : "", #Controls the RADIUS authentication type used for internal RADIUS authentication requests. Object Type: string
        }
        """
        url_path = "/guest/authentication"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Manage settings in Configuration -> Guest Manager
    def get_guestmanager(self):
        """
        Operation: Return settings from Configuration -> Guest Manager
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        """
        url_path = "/guestmanager"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_guestmanager(self, body=({})):
        """
                Operation: Modify settings at Configuration -> Guest Manager
                HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['random_username_method', 'random_username_length', 'random_password_method', 'random_password_length', 'guest_password_complexity', 'guest_password_minimum', 'guest_do_expire', 'guest_account_expiry_options', 'guest_modify_expire_time_options', 'guest_lifetime_options']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "random_username_method" : "", #The method used to generate random account usernames. Object Type: string
                "random_username_multi_prefix" : "", #Identifier string to prepend to usernames.Dynamic entries based on a user attribute can be entered as '_' + attribute.  For example '_role_name'.The username length will determine the length of the numeric sequence only.  Recommend 4. Object Type: string
                "random_username_picture" : "", #Format picture (see below) describing the usernames that will be created for visitors. • Alphanumeric characters are passed through without modification. • ‘#’ is replaced with a random digit [0-9]. • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z] • ‘_’ is replaced with a random lowercase letter [a-z] • ‘^’ is replaced with a random uppercase letter [A-Z] • ‘*’ is replaced with a random letter or digit [A-Za-z0-9]. • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes] • ‘&’ is replaced with a random character (union of sets ! and *) • ‘@’ is replaced with a random letter or digit, excluding vowels • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2). Object Type: string
                "random_username_length" : 0, #The length, in characters, of generated account usernames. Object Type: integer
                "guest_initial_sequence_options" : {}, #Create multi next available sequence number.  These values will be used when multi_initial_sequence is set to -1. Object Type: object
                "random_password_method" : "", #The method used to generate a random account password. Object Type: string
                "random_password_picture" : "", #Format picture (see below) describing the passwords that will be created for visitors. • Alphanumeric characters are passed through without modification. • ‘#’ is replaced with a random digit [0-9]. • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z] • ‘_’ is replaced with a random lowercase letter [a-z] • ‘^’ is replaced with a random uppercase letter [A-Z] • ‘*’ is replaced with a random letter or digit [A-Za-z0-9]. • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes] • ‘&’ is replaced with a random character (union of sets ! and *) • ‘@’ is replaced with a random letter or digit, excluding vowels • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2). Object Type: string
                "random_password_length" : 0, #Number of characters to include in randomly-generated account passwords. Object Type: integer
                "guest_password_complexity" : "", #Password complexity to enforce for manually-entered guest passwords.Requires the random password type ‘A password matching the password complexity requirements’and the field validator ‘NwaIsValidPasswordComplexity’ for manual password entry. Object Type: string
                "guest_password_minimum" : 0, #The minimum number of characters that a guest password must contain. Object Type: integer
                "guest_password_disallowed" : "", #Characters which cannot appear in a user-generated password. Object Type: string
                "guest_password_disallowed_words" : "", #Comma separated list of words disallowed in the random words password generator. Object Type: string
                "guest_view_account_password" : False, #If selected, guest and device Wi-Fi passwords may be displayed to an operator.This is only possible if operators have the View Passwords privilege as well. Object Type: boolean
                "guest_do_expire" : 0, #Default action to take when the expire_time is reached.
        Note that a logout can only occur if the NAS is RFC-3576 compliant. Object Type: integer
                "guest_account_expiry_options" : {},      The available options to select from when choosing the expiration time of a guest account (expire_after).     #Expiration times are specified in hours. Object Type: object
                "guest_modify_expire_time_options" : {},      The available options to select from when modifying an account's expiration (modify_expire_time).     #Note some items may be dynamically removed based on the state of the account. Object Type: object
                "guest_lifetime_options" : {},      The available options to select from when choosing the lifetime of a guest account (expire_postlogin).     #Lifetime values are specified in minutes. Object Type: object
                "g_action_notify_account_expire_enabled" : False, #If checked, users will receive an email notification when their device’s network credentials are due to expire.Accounts must contain the ’expired_notify_status’ field with a value of ’1’.  Once a notification is sent, this field will show as ’0’. Object Type: boolean
                "g_action_notify_account_expiration_duration" : 0, #Account expiration emails are sent this many days before the account expires.
        Enter a value between 1 and 30. Object Type: integer
                "g_action_notify_account_expire_email_unknown" : "", #Specify where to send emails if the user’s account doesn’t have an email address recorded. Object Type: string
                "g_action_notify_account_expire_email_unknown_fixed" : "", #Address used when no email address is known for a user. Object Type: string
                "g_action_notify_account_expire_email_unknown_domain" : "", #Domain to append to the username to form an email address. Object Type: string
                "g_action_notify_account_expire_subject" : "", #Enter a subject for the notification email. Object Type: string
                "g_action_notify_account_expire_message" : 0, #The plain text or HTML print template to use when generating an email message. Object Type: integer
                "g_action_notify_account_expire_skin" : "", #The format in which to send email receipts. Object Type: string
                "g_action_notify_account_expire_copies" : "", #Specify when to send to the recipients in the Copies To list. Object Type: string
                "g_action_notify_account_expire_copies_to" : "", #An optional list of email addresses to which copies of expiry notifications will be sent. Object Type: string
                "g_action_notify_device_expire_email_unknown" : "", #Specify where to send emails if the user’s account doesn’t have an email or sponsor_email address recorded. Object Type: string
                "g_action_notify_device_expire_email_unknown_fixed" : "", #Address used when no email address is known for a device. Object Type: string
                "g_action_notify_device_expire_subject" : "", #Enter a subject for the notification email. Object Type: string
                "g_action_notify_device_expire_message" : 0, #The plain text or HTML print template to use when generating an email message. Object Type: integer
                "g_action_notify_device_expire_skin" : "", #The format in which to send email receipts. Object Type: string
                "g_action_notify_device_expire_copies" : "", #Specify when to send to the recipients in the Copies To list. Object Type: string
                "g_action_notify_device_expire_copies_to" : "", #An optional list of email addresses to which copies of expiry notifications will be sent. Object Type: string
                "site_ssid" : "", #The SSID of the wireless LAN, if applicable.  This will appear on guest account print receipts. Object Type: string
                "site_wpa_key" : "", #The WPA key for the wireless LAN, if applicable.  This will appear on guest account print receipts. Object Type: string
                "guest_receipt_print_button" : False, #Guest receipts can print simply by selecting the template in the dropdown, or by clicking a link. Object Type: boolean
                "guest_account_terms_of_use_url" : "", #The URL of a terms and conditions page.  The URL will appear in any terms checkbox with:{nwa_global name=guest_account_terms_of_use_url}It is recommended to upload your terms in Content Manager, where the files will be referenced with the "public/" prefix.Alternatively, you can edit Terms and Conditions under Configuration > Pages > Web Pages.If your site is hosted externally, be sure the proper access control lists (ACLs) are in place.If terms are not required, it is recommended to edit the terms field on your forms to a UI type "hidden" and an Initial Value of 1. Object Type: string
                "guest_active_sessions" : 0, #Enable limiting the number of active sessions a guest account may have.
        Enter 0 to allow an unlimited number of sessions. Object Type: integer
                "guest_about_guest_network_access" : "", #Template code to display on the Guest Manager start page, under the“About Guest Network Access” heading.  Leave blank to use the default text,or enter a hyphen (“-”) to remove the default text and the heading. Object Type: string
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
                HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Body Parameters:['random_username_method', 'random_username_length', 'random_password_method', 'random_password_length', 'guest_password_complexity', 'guest_password_minimum', 'guest_do_expire', 'guest_account_expiry_options', 'guest_modify_expire_time_options', 'guest_lifetime_options']
                Parameter Type: body, Name: body
                Body example with descriptions and object types below (type(dict):
                body={
                "random_username_method" : "", #The method used to generate random account usernames. Object Type: string
                "random_username_multi_prefix" : "", #Identifier string to prepend to usernames.Dynamic entries based on a user attribute can be entered as '_' + attribute.  For example '_role_name'.The username length will determine the length of the numeric sequence only.  Recommend 4. Object Type: string
                "random_username_picture" : "", #Format picture (see below) describing the usernames that will be created for visitors. • Alphanumeric characters are passed through without modification. • ‘#’ is replaced with a random digit [0-9]. • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z] • ‘_’ is replaced with a random lowercase letter [a-z] • ‘^’ is replaced with a random uppercase letter [A-Z] • ‘*’ is replaced with a random letter or digit [A-Za-z0-9]. • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes] • ‘&’ is replaced with a random character (union of sets ! and *) • ‘@’ is replaced with a random letter or digit, excluding vowels • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2). Object Type: string
                "random_username_length" : 0, #The length, in characters, of generated account usernames. Object Type: integer
                "guest_initial_sequence_options" : {}, #Create multi next available sequence number.  These values will be used when multi_initial_sequence is set to -1. Object Type: object
                "random_password_method" : "", #The method used to generate a random account password. Object Type: string
                "random_password_picture" : "", #Format picture (see below) describing the passwords that will be created for visitors. • Alphanumeric characters are passed through without modification. • ‘#’ is replaced with a random digit [0-9]. • ‘$’ or ‘?’ is replaced with a random letter [A-Za-z] • ‘_’ is replaced with a random lowercase letter [a-z] • ‘^’ is replaced with a random uppercase letter [A-Z] • ‘*’ is replaced with a random letter or digit [A-Za-z0-9]. • ‘!’ is replaced with a random punctuation symbol [excluding apostrophe, quotes] • ‘&’ is replaced with a random character (union of sets ! and *) • ‘@’ is replaced with a random letter or digit, excluding vowels • '%' is replaced with a random letter or digit, excluding vowels and anything that looks like another (il1, B8, O0, Z2). Object Type: string
                "random_password_length" : 0, #Number of characters to include in randomly-generated account passwords. Object Type: integer
                "guest_password_complexity" : "", #Password complexity to enforce for manually-entered guest passwords.Requires the random password type ‘A password matching the password complexity requirements’and the field validator ‘NwaIsValidPasswordComplexity’ for manual password entry. Object Type: string
                "guest_password_minimum" : 0, #The minimum number of characters that a guest password must contain. Object Type: integer
                "guest_password_disallowed" : "", #Characters which cannot appear in a user-generated password. Object Type: string
                "guest_password_disallowed_words" : "", #Comma separated list of words disallowed in the random words password generator. Object Type: string
                "guest_view_account_password" : False, #If selected, guest and device Wi-Fi passwords may be displayed to an operator.This is only possible if operators have the View Passwords privilege as well. Object Type: boolean
                "guest_do_expire" : 0, #Default action to take when the expire_time is reached.
        Note that a logout can only occur if the NAS is RFC-3576 compliant. Object Type: integer
                "guest_account_expiry_options" : {},      The available options to select from when choosing the expiration time of a guest account (expire_after).     #Expiration times are specified in hours. Object Type: object
                "guest_modify_expire_time_options" : {},      The available options to select from when modifying an account's expiration (modify_expire_time).     #Note some items may be dynamically removed based on the state of the account. Object Type: object
                "guest_lifetime_options" : {},      The available options to select from when choosing the lifetime of a guest account (expire_postlogin).     #Lifetime values are specified in minutes. Object Type: object
                "g_action_notify_account_expire_enabled" : False, #If checked, users will receive an email notification when their device’s network credentials are due to expire.Accounts must contain the ’expired_notify_status’ field with a value of ’1’.  Once a notification is sent, this field will show as ’0’. Object Type: boolean
                "g_action_notify_account_expiration_duration" : 0, #Account expiration emails are sent this many days before the account expires.
        Enter a value between 1 and 30. Object Type: integer
                "g_action_notify_account_expire_email_unknown" : "", #Specify where to send emails if the user’s account doesn’t have an email address recorded. Object Type: string
                "g_action_notify_account_expire_email_unknown_fixed" : "", #Address used when no email address is known for a user. Object Type: string
                "g_action_notify_account_expire_email_unknown_domain" : "", #Domain to append to the username to form an email address. Object Type: string
                "g_action_notify_account_expire_subject" : "", #Enter a subject for the notification email. Object Type: string
                "g_action_notify_account_expire_message" : 0, #The plain text or HTML print template to use when generating an email message. Object Type: integer
                "g_action_notify_account_expire_skin" : "", #The format in which to send email receipts. Object Type: string
                "g_action_notify_account_expire_copies" : "", #Specify when to send to the recipients in the Copies To list. Object Type: string
                "g_action_notify_account_expire_copies_to" : "", #An optional list of email addresses to which copies of expiry notifications will be sent. Object Type: string
                "g_action_notify_device_expire_email_unknown" : "", #Specify where to send emails if the user’s account doesn’t have an email or sponsor_email address recorded. Object Type: string
                "g_action_notify_device_expire_email_unknown_fixed" : "", #Address used when no email address is known for a device. Object Type: string
                "g_action_notify_device_expire_subject" : "", #Enter a subject for the notification email. Object Type: string
                "g_action_notify_device_expire_message" : 0, #The plain text or HTML print template to use when generating an email message. Object Type: integer
                "g_action_notify_device_expire_skin" : "", #The format in which to send email receipts. Object Type: string
                "g_action_notify_device_expire_copies" : "", #Specify when to send to the recipients in the Copies To list. Object Type: string
                "g_action_notify_device_expire_copies_to" : "", #An optional list of email addresses to which copies of expiry notifications will be sent. Object Type: string
                "site_ssid" : "", #The SSID of the wireless LAN, if applicable.  This will appear on guest account print receipts. Object Type: string
                "site_wpa_key" : "", #The WPA key for the wireless LAN, if applicable.  This will appear on guest account print receipts. Object Type: string
                "guest_receipt_print_button" : False, #Guest receipts can print simply by selecting the template in the dropdown, or by clicking a link. Object Type: boolean
                "guest_account_terms_of_use_url" : "", #The URL of a terms and conditions page.  The URL will appear in any terms checkbox with:{nwa_global name=guest_account_terms_of_use_url}It is recommended to upload your terms in Content Manager, where the files will be referenced with the "public/" prefix.Alternatively, you can edit Terms and Conditions under Configuration > Pages > Web Pages.If your site is hosted externally, be sure the proper access control lists (ACLs) are in place.If terms are not required, it is recommended to edit the terms field on your forms to a UI type "hidden" and an Initial Value of 1. Object Type: string
                "guest_active_sessions" : 0, #Enable limiting the number of active sessions a guest account may have.
        Enter 0 to allow an unlimited number of sessions. Object Type: integer
                "guest_about_guest_network_access" : "", #Template code to display on the Guest Manager start page, under the“About Guest Network Access” heading.  Leave blank to use the default text,or enter a hyphen (“-”) to remove the default text and the heading. Object Type: string
                }
        """
        url_path = "/guestmanager"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    # API Service: Manage print templates
    def get_template_print(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of print templates
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default -id)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric ID of the template. Object Type: integer
        "name" : "", #Name of the template. Object Type: string
        "enabled" : False, #Flag indicating if the template is enabled. Object Type: boolean
        "columns" : 0, #Columns in a template.. Object Type: integer
        "per_account" : "", #HTML template code used to generate a single account receipt. Object Type: string
        "header" : "", #HTML template code used at the beginning of the document. Object Type: string
        "footer" : "", #HTML template code used at the end of the document. Object Type: string
        "wizard_template" : "", #Style of print template to use. Object Type: string
        "wizard_logo" : "", #Image to use on the template. Object Type: string
        "wizard_title" : "", #Title which will be displayed on the template. Object Type: string
        "wizard_subtitle" : "", #Subtitle to display on the template. Object Type: string
        "wizard_field_header" : "", #Field header for the details displayed on the template. Object Type: string
        "wizard_fields" : "", #Visitor account fields. Object Type: string
        "wizard_notes" : "", #Notes to display on the template. Object Type: string
        "wizard_footer" : "", #Footer text to display on the template. Object Type: string
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/template/print/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_template_print_by_id(self, id="", body=({})):
        """
        Operation: Update some fields of a print template
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: URL parameter id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric ID of the template. Object Type: integer
        "name" : "", #Name of the template. Object Type: string
        "enabled" : False, #Flag indicating if the template is enabled. Object Type: boolean
        "columns" : 0, #Columns in a template.. Object Type: integer
        "per_account" : "", #HTML template code used to generate a single account receipt. Object Type: string
        "header" : "", #HTML template code used at the beginning of the document. Object Type: string
        "footer" : "", #HTML template code used at the end of the document. Object Type: string
        "wizard_template" : "", #Style of print template to use. Object Type: string
        "wizard_logo" : "", #Image to use on the template. Object Type: string
        "wizard_title" : "", #Title which will be displayed on the template. Object Type: string
        "wizard_subtitle" : "", #Subtitle to display on the template. Object Type: string
        "wizard_field_header" : "", #Field header for the details displayed on the template. Object Type: string
        "wizard_fields" : "", #Visitor account fields. Object Type: string
        "wizard_notes" : "", #Notes to display on the template. Object Type: string
        "wizard_footer" : "", #Footer text to display on the template. Object Type: string
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: URL parameter id
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric ID of the template. Object Type: integer
        "name" : "", #Name of the template. Object Type: string
        "enabled" : False, #Flag indicating if the template is enabled. Object Type: boolean
        "columns" : 0, #Columns in a template.. Object Type: integer
        "per_account" : "", #HTML template code used to generate a single account receipt. Object Type: string
        "header" : "", #HTML template code used at the beginning of the document. Object Type: string
        "footer" : "", #HTML template code used at the end of the document. Object Type: string
        "wizard_template" : "", #Style of print template to use. Object Type: string
        "wizard_logo" : "", #Image to use on the template. Object Type: string
        "wizard_title" : "", #Title which will be displayed on the template. Object Type: string
        "wizard_subtitle" : "", #Subtitle to display on the template. Object Type: string
        "wizard_field_header" : "", #Field header for the details displayed on the template. Object Type: string
        "wizard_fields" : "", #Visitor account fields. Object Type: string
        "wizard_notes" : "", #Notes to display on the template. Object Type: string
        "wizard_footer" : "", #Footer text to display on the template. Object Type: string
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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/template/print/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    # API Service: Manage web logins
    def get_weblogin(self, filter="", sort="", offset="", limit="", calculate_count=""):
        """
        Operation: Get a list of web login pages
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +name)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
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
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['name', 'vendor_preset', 'form_action', 'form_method', 'form_username', 'form_password', 'form_password_encryption', 'access_if_denied', 'login_delay', 'login_skin', 'login_pre_auth_check']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Unique ID of the web login. Object Type: integer
        "name" : "", #Enter a name for this web login page. Object Type: string
        "page_name" : "", #Enter a page name for this web login.The web login will be accessible from “/guest/page_name.php”. Object Type: string
        "description" : "", #Comments or descriptive text about the web login. Object Type: string
        "vendor_preset" : "", #Select a predefined group of settings suitable for standard network configurations. Object Type: string
        "vendor_ip" : "", #Enter the hostname (FQDN) of the vendor’s product here.When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device. Object Type: string
        "require_https" : "", #Select a security option to apply to the web login process. Object Type: string
        "webauth" : "", #Select how the user’s network login will be handled.Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process. Object Type: string
        "form_action" : "", #The URL of the NAS device’s login form. Object Type: string
        "form_method" : "", #Choose the method to use when submitting the login form to the NAS. Object Type: string
        "form_username_label" : "", #The form label for the username field.  Leave blank to use the default (Username:). Object Type: string
        "form_username" : "", #The name of the username field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_username_suffix" : "", #The suffix is automatically appended to the username before submitting the login form to the NAS. Object Type: string
        "form_password_label" : "", #The form label for the password field.  Leave blank to use the default (Password:). Object Type: string
        "form_password" : "", #The name of the password field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_extra" : "", #Specify any additional field names and values to send to the NAS device as name=value pairs, one per line. Object Type: string
        "submit_label" : "", #The form label for the log in button.  Leave blank to use the default (Log In). Object Type: string
        "form_password_encryption" : "", #Choose the type of password encryption to use when submitting the login form. Object Type: string
        "uam_secret" : "", #Enter the shared secret between the NAS device and the web login form. Object Type: string
        "url" : "", #The name of the destination field required by the NAS. Object Type: string
        "default_url" : "", #Enter the default URL to redirect clients.Please ensure you prepend "http://" for any external domain. Object Type: string
        "default_url_override" : False, #If selected, the client’s default destination will be overridden regardless of its value. Object Type: boolean
        "dynamic_address" : False, #In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.The address above will be used whenever the parameter is not available or fails the requirements below. Object Type: boolean
        "dynamic_allowlist" : "", #Enter the IP addresses and networks from which dynamic addresses are permitted. Object Type: string
        "dynamic_denylist" : "", #Enter the IP addresses and networks from which dynamic addresses are denied. Object Type: string
        "access_allowlist" : "", #Enter the IP addresses and networks from which logins are permitted. Object Type: string
        "access_denylist" : "", #Enter the IP addresses and networks that are denied login access. Object Type: string
        "access_if_denied" : "", #Select the response of the system to a request that is not permitted. Object Type: string
        "login_title" : "", #The title to display on the web login page.  Leave blank to use the default (Login). Object Type: string
        "login_header" : "", #HTML template code displayed before the login form. Object Type: string
        "login_footer" : "", #HTML template code displayed after the login form. Object Type: string
        "login_message" : "", #HTML template code displayed while the login attempt is in progress. Object Type: string
        "login_delay" : "" #variable unknown: , #The time in seconds to delay while displaying the login message. Object Type: number
        "login_skin" : "", #Choose the skin to use when this web login page is displayed. Object Type: string
        "login_terms_require" : False, #If checked, the user will be forced to accept a Terms and Conditions checkbox. Object Type: boolean
        "login_terms_label" : "", #The form label for the terms checkbox.  Leave blank to use the default (Terms:). Object Type: string
        "login_terms_text" : "", #HTML code containing your Terms and Conditions.  Leave blank to use the default (I accept the <a href="{nwa_global name=guest_account_terms_of_use_url}" target="_blank" title="Open the terms of use URL.">terms of use</a>). Object Type: string
        "login_terms_layout" : "", #Select the layout for the terms and conditions text. Object Type: string
        "login_terms_error" : "", #The text to display if the terms are not accepted.  Leave blank to use the default (In order to log in, you must accept the terms and conditions.). Object Type: string
        "login_captcha" : "", #Select a CAPTCHA mode. Object Type: string
        "username_auth" : "", #Select the authentication requirement.Access Code requires a single code (username) to be entered.Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.Auto is similar to anonymous but the page is automatically submitted.Access Code and Anonymous require the account to have the Username Authentication field set. Object Type: string
        "certificate_request" : "", #Choose whether the user should select a client certificate when authenticating. Object Type: string
        "username_auth_username" : "", #The account to use for anonymous authentication.The password will be visible within the HTML.It is recommended to increase the account Session Limit to the number of guests you wish to support. Object Type: string
        "certificate_auth" : "", #Choose whether other credentials must also be provided in addition to a certificate. Object Type: string
        "register_policy_manager" : False, #If selected, the endpoint’s attributes will also be updated with other details from the user account. Object Type: boolean
        "register_policy_manager_adv" : False, #Customize attributes stored with the endpoint. Object Type: boolean
        "register_policy_manager_attrs" : "", #List of name|value pairs to pass along.user_field | Endpoint Attribute. Object Type: string
        "hash_url" : "", #Select the level of checking to apply to URL parameters passed to the web login page.Use this option to detect when URL parameters have been modified by the user, for example their MAC address. Object Type: string
        "hash_secret" : "", #The redirection URL will be hashed using this shared secret. Object Type: string
        "bypass_cna" : False, #The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.Note that this option may not work with all vendors, depending on how the captive portal is implemented. Object Type: boolean
        "capport_venue_url" : "", #Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.https://www.rfc-editor.org/rfc/rfc8908.html. Object Type: string
        "onguard_healthcheck" : False, #If selected, the guest will be required to pass a health check prior to accessing the network. Object Type: boolean
        "onguard_agents" : "", #Select the agent options for client scanning.Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java. Object Type: string
        "onguard_header" : "", #HTML template code displayed before the health check text. Object Type: string
        "onguard_footer" : "", #HTML template code displayed after the health check text. Object Type: string
        "oauth_enabled" : False, #Enable logins with cloud identity / social network credentials. Object Type: boolean
        "oauth_debug" : False, #Log debugging data. Object Type: boolean
        "oauth_providers" : {}, #Configuration for cloud identity authentication providers. Object Type: object
        "login_custom_form" : False, #If selected, you must supply your own HTML login form in the Header or Footer HTML areas. Object Type: boolean
        "login_pre_auth_check" : "", #Select how the username and password should be checked before proceeding to the NAS authentication. Object Type: string
        "login_pre_auth_error" : "", #The text to display if the username and password lookup fails.  Leave blank to use the default (Invalid username or password). Object Type: string
        "mfa_enabled" : "", #No Desc. Object Type: string
        "mfa_first" : "", #All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device. Object Type: string
        "mfa_duo_ikey" : "", #No Desc. Object Type: string
        "mfa_duo_skey" : "", #No Desc. Object Type: string
        "mfa_duo_host" : "", #No Desc. Object Type: string
        "mfa_fn_client_id" : "", #No Desc. Object Type: string
        "mfa_fn_client_secret" : "", #No Desc. Object Type: string
        "mfa_fn_factors" : "", #Enter the number of factors to require. Object Type: string
        "mfa_fn_email" : False, #If disabled, the user must scan the QR code. Object Type: boolean
        "mfa_iws_tenant" : "", #No Desc. Object Type: string
        "mfa_iws_app" : "", #No Desc. Object Type: string
        "mfa_iws_hostname" : "", #Enter the hostname of the ImageWare server. Object Type: string
        "mfa_mc_scope" : "", #OAuth 2.0 scope value. Only mc_authn is supported for this release. Object Type: string
        "mfa_mc_context" : "", #Message which will be displayed on the authorization device. Object Type: string
        "mfa_mc_binding_message" : "", #Plain text reference to interlock the consumption device and authorization device. Object Type: string
        "mfa_mc_acr_values" : "", #Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6. Object Type: string
        "mfa_mc_display" : "", #User interface display for Authentication. Object Type: string
        "mfa_mc_prompt" : "", #Value to specify to the Authorisation server about type of prompt. Object Type: string
        "mfa_mc_max_age" : 0, #Maximum elapsed time in secs since last authenticaiton. Object Type: integer
        "mfa_mc_login_hint" : "", #An indication to IDP on what ID to use for login. Object Type: string
        "mfa_mc_version" : "", #No Desc. Object Type: string
        "mfa_mc_discovery_service_endpoint" : "", #Provide the endpoint URL provided by Mobile Connect during configuration. Object Type: string
        "mfa_mc_redirect_url" : "", #Mobile Connect Redirect URL provided during configuration. Object Type: string
        "mfa_mc_client_id" : "", #No Desc. Object Type: string
        "mfa_mc_client_secret" : "", #No Desc. Object Type: string
        "mfa_header_html" : "", #HTML template code displayed before the provider’s vendor-specific authentication area. Object Type: string
        "mfa_footer_html" : "", #HTML template code displayed after the provider’s vendor-specific authentication area. Object Type: string
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
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/weblogin/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_weblogin_by_id(self, id="", body=({})):
        """
        Operation: Update some fields of a web login page
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: URL parameter id
        Required Body Parameters:['name', 'vendor_preset', 'form_action', 'form_method', 'form_username', 'form_password', 'form_password_encryption', 'access_if_denied', 'login_delay', 'login_skin', 'login_pre_auth_check']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Unique ID of the web login. Object Type: integer
        "name" : "", #Enter a name for this web login page. Object Type: string
        "page_name" : "", #Enter a page name for this web login.The web login will be accessible from “/guest/page_name.php”. Object Type: string
        "description" : "", #Comments or descriptive text about the web login. Object Type: string
        "vendor_preset" : "", #Select a predefined group of settings suitable for standard network configurations. Object Type: string
        "vendor_ip" : "", #Enter the hostname (FQDN) of the vendor’s product here.When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device. Object Type: string
        "require_https" : "", #Select a security option to apply to the web login process. Object Type: string
        "webauth" : "", #Select how the user’s network login will be handled.Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process. Object Type: string
        "form_action" : "", #The URL of the NAS device’s login form. Object Type: string
        "form_method" : "", #Choose the method to use when submitting the login form to the NAS. Object Type: string
        "form_username_label" : "", #The form label for the username field.  Leave blank to use the default (Username:). Object Type: string
        "form_username" : "", #The name of the username field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_username_suffix" : "", #The suffix is automatically appended to the username before submitting the login form to the NAS. Object Type: string
        "form_password_label" : "", #The form label for the password field.  Leave blank to use the default (Password:). Object Type: string
        "form_password" : "", #The name of the password field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_extra" : "", #Specify any additional field names and values to send to the NAS device as name=value pairs, one per line. Object Type: string
        "submit_label" : "", #The form label for the log in button.  Leave blank to use the default (Log In). Object Type: string
        "form_password_encryption" : "", #Choose the type of password encryption to use when submitting the login form. Object Type: string
        "uam_secret" : "", #Enter the shared secret between the NAS device and the web login form. Object Type: string
        "url" : "", #The name of the destination field required by the NAS. Object Type: string
        "default_url" : "", #Enter the default URL to redirect clients.Please ensure you prepend "http://" for any external domain. Object Type: string
        "default_url_override" : False, #If selected, the client’s default destination will be overridden regardless of its value. Object Type: boolean
        "dynamic_address" : False, #In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.The address above will be used whenever the parameter is not available or fails the requirements below. Object Type: boolean
        "dynamic_allowlist" : "", #Enter the IP addresses and networks from which dynamic addresses are permitted. Object Type: string
        "dynamic_denylist" : "", #Enter the IP addresses and networks from which dynamic addresses are denied. Object Type: string
        "access_allowlist" : "", #Enter the IP addresses and networks from which logins are permitted. Object Type: string
        "access_denylist" : "", #Enter the IP addresses and networks that are denied login access. Object Type: string
        "access_if_denied" : "", #Select the response of the system to a request that is not permitted. Object Type: string
        "login_title" : "", #The title to display on the web login page.  Leave blank to use the default (Login). Object Type: string
        "login_header" : "", #HTML template code displayed before the login form. Object Type: string
        "login_footer" : "", #HTML template code displayed after the login form. Object Type: string
        "login_message" : "", #HTML template code displayed while the login attempt is in progress. Object Type: string
        "login_delay" : "" #variable unknown: , #The time in seconds to delay while displaying the login message. Object Type: number
        "login_skin" : "", #Choose the skin to use when this web login page is displayed. Object Type: string
        "login_terms_require" : False, #If checked, the user will be forced to accept a Terms and Conditions checkbox. Object Type: boolean
        "login_terms_label" : "", #The form label for the terms checkbox.  Leave blank to use the default (Terms:). Object Type: string
        "login_terms_text" : "", #HTML code containing your Terms and Conditions.  Leave blank to use the default (I accept the <a href="{nwa_global name=guest_account_terms_of_use_url}" target="_blank" title="Open the terms of use URL.">terms of use</a>). Object Type: string
        "login_terms_layout" : "", #Select the layout for the terms and conditions text. Object Type: string
        "login_terms_error" : "", #The text to display if the terms are not accepted.  Leave blank to use the default (In order to log in, you must accept the terms and conditions.). Object Type: string
        "login_captcha" : "", #Select a CAPTCHA mode. Object Type: string
        "username_auth" : "", #Select the authentication requirement.Access Code requires a single code (username) to be entered.Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.Auto is similar to anonymous but the page is automatically submitted.Access Code and Anonymous require the account to have the Username Authentication field set. Object Type: string
        "certificate_request" : "", #Choose whether the user should select a client certificate when authenticating. Object Type: string
        "username_auth_username" : "", #The account to use for anonymous authentication.The password will be visible within the HTML.It is recommended to increase the account Session Limit to the number of guests you wish to support. Object Type: string
        "certificate_auth" : "", #Choose whether other credentials must also be provided in addition to a certificate. Object Type: string
        "register_policy_manager" : False, #If selected, the endpoint’s attributes will also be updated with other details from the user account. Object Type: boolean
        "register_policy_manager_adv" : False, #Customize attributes stored with the endpoint. Object Type: boolean
        "register_policy_manager_attrs" : "", #List of name|value pairs to pass along.user_field | Endpoint Attribute. Object Type: string
        "hash_url" : "", #Select the level of checking to apply to URL parameters passed to the web login page.Use this option to detect when URL parameters have been modified by the user, for example their MAC address. Object Type: string
        "hash_secret" : "", #The redirection URL will be hashed using this shared secret. Object Type: string
        "bypass_cna" : False, #The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.Note that this option may not work with all vendors, depending on how the captive portal is implemented. Object Type: boolean
        "capport_venue_url" : "", #Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.https://www.rfc-editor.org/rfc/rfc8908.html. Object Type: string
        "onguard_healthcheck" : False, #If selected, the guest will be required to pass a health check prior to accessing the network. Object Type: boolean
        "onguard_agents" : "", #Select the agent options for client scanning.Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java. Object Type: string
        "onguard_header" : "", #HTML template code displayed before the health check text. Object Type: string
        "onguard_footer" : "", #HTML template code displayed after the health check text. Object Type: string
        "oauth_enabled" : False, #Enable logins with cloud identity / social network credentials. Object Type: boolean
        "oauth_debug" : False, #Log debugging data. Object Type: boolean
        "oauth_providers" : {}, #Configuration for cloud identity authentication providers. Object Type: object
        "login_custom_form" : False, #If selected, you must supply your own HTML login form in the Header or Footer HTML areas. Object Type: boolean
        "login_pre_auth_check" : "", #Select how the username and password should be checked before proceeding to the NAS authentication. Object Type: string
        "login_pre_auth_error" : "", #The text to display if the username and password lookup fails.  Leave blank to use the default (Invalid username or password). Object Type: string
        "mfa_enabled" : "", #No Desc. Object Type: string
        "mfa_first" : "", #All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device. Object Type: string
        "mfa_duo_ikey" : "", #No Desc. Object Type: string
        "mfa_duo_skey" : "", #No Desc. Object Type: string
        "mfa_duo_host" : "", #No Desc. Object Type: string
        "mfa_fn_client_id" : "", #No Desc. Object Type: string
        "mfa_fn_client_secret" : "", #No Desc. Object Type: string
        "mfa_fn_factors" : "", #Enter the number of factors to require. Object Type: string
        "mfa_fn_email" : False, #If disabled, the user must scan the QR code. Object Type: boolean
        "mfa_iws_tenant" : "", #No Desc. Object Type: string
        "mfa_iws_app" : "", #No Desc. Object Type: string
        "mfa_iws_hostname" : "", #Enter the hostname of the ImageWare server. Object Type: string
        "mfa_mc_scope" : "", #OAuth 2.0 scope value. Only mc_authn is supported for this release. Object Type: string
        "mfa_mc_context" : "", #Message which will be displayed on the authorization device. Object Type: string
        "mfa_mc_binding_message" : "", #Plain text reference to interlock the consumption device and authorization device. Object Type: string
        "mfa_mc_acr_values" : "", #Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6. Object Type: string
        "mfa_mc_display" : "", #User interface display for Authentication. Object Type: string
        "mfa_mc_prompt" : "", #Value to specify to the Authorisation server about type of prompt. Object Type: string
        "mfa_mc_max_age" : 0, #Maximum elapsed time in secs since last authenticaiton. Object Type: integer
        "mfa_mc_login_hint" : "", #An indication to IDP on what ID to use for login. Object Type: string
        "mfa_mc_version" : "", #No Desc. Object Type: string
        "mfa_mc_discovery_service_endpoint" : "", #Provide the endpoint URL provided by Mobile Connect during configuration. Object Type: string
        "mfa_mc_redirect_url" : "", #Mobile Connect Redirect URL provided during configuration. Object Type: string
        "mfa_mc_client_id" : "", #No Desc. Object Type: string
        "mfa_mc_client_secret" : "", #No Desc. Object Type: string
        "mfa_header_html" : "", #HTML template code displayed before the provider’s vendor-specific authentication area. Object Type: string
        "mfa_footer_html" : "", #HTML template code displayed after the provider’s vendor-specific authentication area. Object Type: string
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
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: id, Description: URL parameter id
        Required Body Parameters:['name', 'vendor_preset', 'form_action', 'form_method', 'form_username', 'form_password', 'form_password_encryption', 'access_if_denied', 'login_delay', 'login_skin', 'login_pre_auth_check']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Unique ID of the web login. Object Type: integer
        "name" : "", #Enter a name for this web login page. Object Type: string
        "page_name" : "", #Enter a page name for this web login.The web login will be accessible from “/guest/page_name.php”. Object Type: string
        "description" : "", #Comments or descriptive text about the web login. Object Type: string
        "vendor_preset" : "", #Select a predefined group of settings suitable for standard network configurations. Object Type: string
        "vendor_ip" : "", #Enter the hostname (FQDN) of the vendor’s product here.When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device. Object Type: string
        "require_https" : "", #Select a security option to apply to the web login process. Object Type: string
        "webauth" : "", #Select how the user’s network login will be handled.Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process. Object Type: string
        "form_action" : "", #The URL of the NAS device’s login form. Object Type: string
        "form_method" : "", #Choose the method to use when submitting the login form to the NAS. Object Type: string
        "form_username_label" : "", #The form label for the username field.  Leave blank to use the default (Username:). Object Type: string
        "form_username" : "", #The name of the username field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_username_suffix" : "", #The suffix is automatically appended to the username before submitting the login form to the NAS. Object Type: string
        "form_password_label" : "", #The form label for the password field.  Leave blank to use the default (Password:). Object Type: string
        "form_password" : "", #The name of the password field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_extra" : "", #Specify any additional field names and values to send to the NAS device as name=value pairs, one per line. Object Type: string
        "submit_label" : "", #The form label for the log in button.  Leave blank to use the default (Log In). Object Type: string
        "form_password_encryption" : "", #Choose the type of password encryption to use when submitting the login form. Object Type: string
        "uam_secret" : "", #Enter the shared secret between the NAS device and the web login form. Object Type: string
        "url" : "", #The name of the destination field required by the NAS. Object Type: string
        "default_url" : "", #Enter the default URL to redirect clients.Please ensure you prepend "http://" for any external domain. Object Type: string
        "default_url_override" : False, #If selected, the client’s default destination will be overridden regardless of its value. Object Type: boolean
        "dynamic_address" : False, #In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.The address above will be used whenever the parameter is not available or fails the requirements below. Object Type: boolean
        "dynamic_allowlist" : "", #Enter the IP addresses and networks from which dynamic addresses are permitted. Object Type: string
        "dynamic_denylist" : "", #Enter the IP addresses and networks from which dynamic addresses are denied. Object Type: string
        "access_allowlist" : "", #Enter the IP addresses and networks from which logins are permitted. Object Type: string
        "access_denylist" : "", #Enter the IP addresses and networks that are denied login access. Object Type: string
        "access_if_denied" : "", #Select the response of the system to a request that is not permitted. Object Type: string
        "login_title" : "", #The title to display on the web login page.  Leave blank to use the default (Login). Object Type: string
        "login_header" : "", #HTML template code displayed before the login form. Object Type: string
        "login_footer" : "", #HTML template code displayed after the login form. Object Type: string
        "login_message" : "", #HTML template code displayed while the login attempt is in progress. Object Type: string
        "login_delay" : "" #variable unknown: , #The time in seconds to delay while displaying the login message. Object Type: number
        "login_skin" : "", #Choose the skin to use when this web login page is displayed. Object Type: string
        "login_terms_require" : False, #If checked, the user will be forced to accept a Terms and Conditions checkbox. Object Type: boolean
        "login_terms_label" : "", #The form label for the terms checkbox.  Leave blank to use the default (Terms:). Object Type: string
        "login_terms_text" : "", #HTML code containing your Terms and Conditions.  Leave blank to use the default (I accept the <a href="{nwa_global name=guest_account_terms_of_use_url}" target="_blank" title="Open the terms of use URL.">terms of use</a>). Object Type: string
        "login_terms_layout" : "", #Select the layout for the terms and conditions text. Object Type: string
        "login_terms_error" : "", #The text to display if the terms are not accepted.  Leave blank to use the default (In order to log in, you must accept the terms and conditions.). Object Type: string
        "login_captcha" : "", #Select a CAPTCHA mode. Object Type: string
        "username_auth" : "", #Select the authentication requirement.Access Code requires a single code (username) to be entered.Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.Auto is similar to anonymous but the page is automatically submitted.Access Code and Anonymous require the account to have the Username Authentication field set. Object Type: string
        "certificate_request" : "", #Choose whether the user should select a client certificate when authenticating. Object Type: string
        "username_auth_username" : "", #The account to use for anonymous authentication.The password will be visible within the HTML.It is recommended to increase the account Session Limit to the number of guests you wish to support. Object Type: string
        "certificate_auth" : "", #Choose whether other credentials must also be provided in addition to a certificate. Object Type: string
        "register_policy_manager" : False, #If selected, the endpoint’s attributes will also be updated with other details from the user account. Object Type: boolean
        "register_policy_manager_adv" : False, #Customize attributes stored with the endpoint. Object Type: boolean
        "register_policy_manager_attrs" : "", #List of name|value pairs to pass along.user_field | Endpoint Attribute. Object Type: string
        "hash_url" : "", #Select the level of checking to apply to URL parameters passed to the web login page.Use this option to detect when URL parameters have been modified by the user, for example their MAC address. Object Type: string
        "hash_secret" : "", #The redirection URL will be hashed using this shared secret. Object Type: string
        "bypass_cna" : False, #The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.Note that this option may not work with all vendors, depending on how the captive portal is implemented. Object Type: boolean
        "capport_venue_url" : "", #Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.https://www.rfc-editor.org/rfc/rfc8908.html. Object Type: string
        "onguard_healthcheck" : False, #If selected, the guest will be required to pass a health check prior to accessing the network. Object Type: boolean
        "onguard_agents" : "", #Select the agent options for client scanning.Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java. Object Type: string
        "onguard_header" : "", #HTML template code displayed before the health check text. Object Type: string
        "onguard_footer" : "", #HTML template code displayed after the health check text. Object Type: string
        "oauth_enabled" : False, #Enable logins with cloud identity / social network credentials. Object Type: boolean
        "oauth_debug" : False, #Log debugging data. Object Type: boolean
        "oauth_providers" : {}, #Configuration for cloud identity authentication providers. Object Type: object
        "login_custom_form" : False, #If selected, you must supply your own HTML login form in the Header or Footer HTML areas. Object Type: boolean
        "login_pre_auth_check" : "", #Select how the username and password should be checked before proceeding to the NAS authentication. Object Type: string
        "login_pre_auth_error" : "", #The text to display if the username and password lookup fails.  Leave blank to use the default (Invalid username or password). Object Type: string
        "mfa_enabled" : "", #No Desc. Object Type: string
        "mfa_first" : "", #All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device. Object Type: string
        "mfa_duo_ikey" : "", #No Desc. Object Type: string
        "mfa_duo_skey" : "", #No Desc. Object Type: string
        "mfa_duo_host" : "", #No Desc. Object Type: string
        "mfa_fn_client_id" : "", #No Desc. Object Type: string
        "mfa_fn_client_secret" : "", #No Desc. Object Type: string
        "mfa_fn_factors" : "", #Enter the number of factors to require. Object Type: string
        "mfa_fn_email" : False, #If disabled, the user must scan the QR code. Object Type: boolean
        "mfa_iws_tenant" : "", #No Desc. Object Type: string
        "mfa_iws_app" : "", #No Desc. Object Type: string
        "mfa_iws_hostname" : "", #Enter the hostname of the ImageWare server. Object Type: string
        "mfa_mc_scope" : "", #OAuth 2.0 scope value. Only mc_authn is supported for this release. Object Type: string
        "mfa_mc_context" : "", #Message which will be displayed on the authorization device. Object Type: string
        "mfa_mc_binding_message" : "", #Plain text reference to interlock the consumption device and authorization device. Object Type: string
        "mfa_mc_acr_values" : "", #Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6. Object Type: string
        "mfa_mc_display" : "", #User interface display for Authentication. Object Type: string
        "mfa_mc_prompt" : "", #Value to specify to the Authorisation server about type of prompt. Object Type: string
        "mfa_mc_max_age" : 0, #Maximum elapsed time in secs since last authenticaiton. Object Type: integer
        "mfa_mc_login_hint" : "", #An indication to IDP on what ID to use for login. Object Type: string
        "mfa_mc_version" : "", #No Desc. Object Type: string
        "mfa_mc_discovery_service_endpoint" : "", #Provide the endpoint URL provided by Mobile Connect during configuration. Object Type: string
        "mfa_mc_redirect_url" : "", #Mobile Connect Redirect URL provided during configuration. Object Type: string
        "mfa_mc_client_id" : "", #No Desc. Object Type: string
        "mfa_mc_client_secret" : "", #No Desc. Object Type: string
        "mfa_header_html" : "", #HTML template code displayed before the provider’s vendor-specific authentication area. Object Type: string
        "mfa_footer_html" : "", #HTML template code displayed after the provider’s vendor-specific authentication area. Object Type: string
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
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: URL parameter id
        """
        url_path = "/weblogin/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_weblogin_page_name_by_page_name(self, page_name=""):
        """
        Operation: Get a web login page by page-name
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: page-name, Description: Unique page name of the web login
        """
        url_path = "/weblogin/page-name/{page_name}"
        dict_path = {"page_name": page_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_weblogin_page_name_by_page_name(self, page_name="", body=({})):
        """
        Operation: Update some fields of a web login page by page-name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: page-name, Description: Unique page name of the web login
        Required Body Parameters:['name', 'vendor_preset', 'form_action', 'form_method', 'form_username', 'form_password', 'form_password_encryption', 'access_if_denied', 'login_delay', 'login_skin', 'login_pre_auth_check']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Unique ID of the web login. Object Type: integer
        "name" : "", #Enter a name for this web login page. Object Type: string
        "page_name" : "", #Enter a page name for this web login.The web login will be accessible from “/guest/page_name.php”. Object Type: string
        "description" : "", #Comments or descriptive text about the web login. Object Type: string
        "vendor_preset" : "", #Select a predefined group of settings suitable for standard network configurations. Object Type: string
        "vendor_ip" : "", #Enter the hostname (FQDN) of the vendor’s product here.When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device. Object Type: string
        "require_https" : "", #Select a security option to apply to the web login process. Object Type: string
        "webauth" : "", #Select how the user’s network login will be handled.Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process. Object Type: string
        "form_action" : "", #The URL of the NAS device’s login form. Object Type: string
        "form_method" : "", #Choose the method to use when submitting the login form to the NAS. Object Type: string
        "form_username_label" : "", #The form label for the username field.  Leave blank to use the default (Username:). Object Type: string
        "form_username" : "", #The name of the username field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_username_suffix" : "", #The suffix is automatically appended to the username before submitting the login form to the NAS. Object Type: string
        "form_password_label" : "", #The form label for the password field.  Leave blank to use the default (Password:). Object Type: string
        "form_password" : "", #The name of the password field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_extra" : "", #Specify any additional field names and values to send to the NAS device as name=value pairs, one per line. Object Type: string
        "submit_label" : "", #The form label for the log in button.  Leave blank to use the default (Log In). Object Type: string
        "form_password_encryption" : "", #Choose the type of password encryption to use when submitting the login form. Object Type: string
        "uam_secret" : "", #Enter the shared secret between the NAS device and the web login form. Object Type: string
        "url" : "", #The name of the destination field required by the NAS. Object Type: string
        "default_url" : "", #Enter the default URL to redirect clients.Please ensure you prepend "http://" for any external domain. Object Type: string
        "default_url_override" : False, #If selected, the client’s default destination will be overridden regardless of its value. Object Type: boolean
        "dynamic_address" : False, #In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.The address above will be used whenever the parameter is not available or fails the requirements below. Object Type: boolean
        "dynamic_allowlist" : "", #Enter the IP addresses and networks from which dynamic addresses are permitted. Object Type: string
        "dynamic_denylist" : "", #Enter the IP addresses and networks from which dynamic addresses are denied. Object Type: string
        "access_allowlist" : "", #Enter the IP addresses and networks from which logins are permitted. Object Type: string
        "access_denylist" : "", #Enter the IP addresses and networks that are denied login access. Object Type: string
        "access_if_denied" : "", #Select the response of the system to a request that is not permitted. Object Type: string
        "login_title" : "", #The title to display on the web login page.  Leave blank to use the default (Login). Object Type: string
        "login_header" : "", #HTML template code displayed before the login form. Object Type: string
        "login_footer" : "", #HTML template code displayed after the login form. Object Type: string
        "login_message" : "", #HTML template code displayed while the login attempt is in progress. Object Type: string
        "login_delay" : "" #variable unknown: , #The time in seconds to delay while displaying the login message. Object Type: number
        "login_skin" : "", #Choose the skin to use when this web login page is displayed. Object Type: string
        "login_terms_require" : False, #If checked, the user will be forced to accept a Terms and Conditions checkbox. Object Type: boolean
        "login_terms_label" : "", #The form label for the terms checkbox.  Leave blank to use the default (Terms:). Object Type: string
        "login_terms_text" : "", #HTML code containing your Terms and Conditions.  Leave blank to use the default (I accept the <a href="{nwa_global name=guest_account_terms_of_use_url}" target="_blank" title="Open the terms of use URL.">terms of use</a>). Object Type: string
        "login_terms_layout" : "", #Select the layout for the terms and conditions text. Object Type: string
        "login_terms_error" : "", #The text to display if the terms are not accepted.  Leave blank to use the default (In order to log in, you must accept the terms and conditions.). Object Type: string
        "login_captcha" : "", #Select a CAPTCHA mode. Object Type: string
        "username_auth" : "", #Select the authentication requirement.Access Code requires a single code (username) to be entered.Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.Auto is similar to anonymous but the page is automatically submitted.Access Code and Anonymous require the account to have the Username Authentication field set. Object Type: string
        "certificate_request" : "", #Choose whether the user should select a client certificate when authenticating. Object Type: string
        "username_auth_username" : "", #The account to use for anonymous authentication.The password will be visible within the HTML.It is recommended to increase the account Session Limit to the number of guests you wish to support. Object Type: string
        "certificate_auth" : "", #Choose whether other credentials must also be provided in addition to a certificate. Object Type: string
        "register_policy_manager" : False, #If selected, the endpoint’s attributes will also be updated with other details from the user account. Object Type: boolean
        "register_policy_manager_adv" : False, #Customize attributes stored with the endpoint. Object Type: boolean
        "register_policy_manager_attrs" : "", #List of name|value pairs to pass along.user_field | Endpoint Attribute. Object Type: string
        "hash_url" : "", #Select the level of checking to apply to URL parameters passed to the web login page.Use this option to detect when URL parameters have been modified by the user, for example their MAC address. Object Type: string
        "hash_secret" : "", #The redirection URL will be hashed using this shared secret. Object Type: string
        "bypass_cna" : False, #The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.Note that this option may not work with all vendors, depending on how the captive portal is implemented. Object Type: boolean
        "capport_venue_url" : "", #Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.https://www.rfc-editor.org/rfc/rfc8908.html. Object Type: string
        "onguard_healthcheck" : False, #If selected, the guest will be required to pass a health check prior to accessing the network. Object Type: boolean
        "onguard_agents" : "", #Select the agent options for client scanning.Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java. Object Type: string
        "onguard_header" : "", #HTML template code displayed before the health check text. Object Type: string
        "onguard_footer" : "", #HTML template code displayed after the health check text. Object Type: string
        "oauth_enabled" : False, #Enable logins with cloud identity / social network credentials. Object Type: boolean
        "oauth_debug" : False, #Log debugging data. Object Type: boolean
        "oauth_providers" : {}, #Configuration for cloud identity authentication providers. Object Type: object
        "login_custom_form" : False, #If selected, you must supply your own HTML login form in the Header or Footer HTML areas. Object Type: boolean
        "login_pre_auth_check" : "", #Select how the username and password should be checked before proceeding to the NAS authentication. Object Type: string
        "login_pre_auth_error" : "", #The text to display if the username and password lookup fails.  Leave blank to use the default (Invalid username or password). Object Type: string
        "mfa_enabled" : "", #No Desc. Object Type: string
        "mfa_first" : "", #All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device. Object Type: string
        "mfa_duo_ikey" : "", #No Desc. Object Type: string
        "mfa_duo_skey" : "", #No Desc. Object Type: string
        "mfa_duo_host" : "", #No Desc. Object Type: string
        "mfa_fn_client_id" : "", #No Desc. Object Type: string
        "mfa_fn_client_secret" : "", #No Desc. Object Type: string
        "mfa_fn_factors" : "", #Enter the number of factors to require. Object Type: string
        "mfa_fn_email" : False, #If disabled, the user must scan the QR code. Object Type: boolean
        "mfa_iws_tenant" : "", #No Desc. Object Type: string
        "mfa_iws_app" : "", #No Desc. Object Type: string
        "mfa_iws_hostname" : "", #Enter the hostname of the ImageWare server. Object Type: string
        "mfa_mc_scope" : "", #OAuth 2.0 scope value. Only mc_authn is supported for this release. Object Type: string
        "mfa_mc_context" : "", #Message which will be displayed on the authorization device. Object Type: string
        "mfa_mc_binding_message" : "", #Plain text reference to interlock the consumption device and authorization device. Object Type: string
        "mfa_mc_acr_values" : "", #Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6. Object Type: string
        "mfa_mc_display" : "", #User interface display for Authentication. Object Type: string
        "mfa_mc_prompt" : "", #Value to specify to the Authorisation server about type of prompt. Object Type: string
        "mfa_mc_max_age" : 0, #Maximum elapsed time in secs since last authenticaiton. Object Type: integer
        "mfa_mc_login_hint" : "", #An indication to IDP on what ID to use for login. Object Type: string
        "mfa_mc_version" : "", #No Desc. Object Type: string
        "mfa_mc_discovery_service_endpoint" : "", #Provide the endpoint URL provided by Mobile Connect during configuration. Object Type: string
        "mfa_mc_redirect_url" : "", #Mobile Connect Redirect URL provided during configuration. Object Type: string
        "mfa_mc_client_id" : "", #No Desc. Object Type: string
        "mfa_mc_client_secret" : "", #No Desc. Object Type: string
        "mfa_header_html" : "", #HTML template code displayed before the provider’s vendor-specific authentication area. Object Type: string
        "mfa_footer_html" : "", #HTML template code displayed after the provider’s vendor-specific authentication area. Object Type: string
        }
        """
        url_path = "/weblogin/page-name/{page_name}"
        dict_path = {"page_name": page_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_weblogin_page_name_by_page_name(self, page_name="", body=({})):
        """
        Operation: Replace a web login page by page-name
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: page-name, Description: Unique page name of the web login
        Required Body Parameters:['name', 'vendor_preset', 'form_action', 'form_method', 'form_username', 'form_password', 'form_password_encryption', 'access_if_denied', 'login_delay', 'login_skin', 'login_pre_auth_check']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Unique ID of the web login. Object Type: integer
        "name" : "", #Enter a name for this web login page. Object Type: string
        "page_name" : "", #Enter a page name for this web login.The web login will be accessible from “/guest/page_name.php”. Object Type: string
        "description" : "", #Comments or descriptive text about the web login. Object Type: string
        "vendor_preset" : "", #Select a predefined group of settings suitable for standard network configurations. Object Type: string
        "vendor_ip" : "", #Enter the hostname (FQDN) of the vendor’s product here.When using Secure Login over HTTPS, this name should match the name of the HTTPS certificate installed on your device. Object Type: string
        "require_https" : "", #Select a security option to apply to the web login process. Object Type: string
        "webauth" : "", #Select how the user’s network login will be handled.Server-initiated logins require the user’s MAC address to be available, usually from the captive portal redirection process. Object Type: string
        "form_action" : "", #The URL of the NAS device’s login form. Object Type: string
        "form_method" : "", #Choose the method to use when submitting the login form to the NAS. Object Type: string
        "form_username_label" : "", #The form label for the username field.  Leave blank to use the default (Username:). Object Type: string
        "form_username" : "", #The name of the username field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_username_suffix" : "", #The suffix is automatically appended to the username before submitting the login form to the NAS. Object Type: string
        "form_password_label" : "", #The form label for the password field.  Leave blank to use the default (Password:). Object Type: string
        "form_password" : "", #The name of the password field for the login form. This will be passed to the NAS device when the form is submitted. Object Type: string
        "form_extra" : "", #Specify any additional field names and values to send to the NAS device as name=value pairs, one per line. Object Type: string
        "submit_label" : "", #The form label for the log in button.  Leave blank to use the default (Log In). Object Type: string
        "form_password_encryption" : "", #Choose the type of password encryption to use when submitting the login form. Object Type: string
        "uam_secret" : "", #Enter the shared secret between the NAS device and the web login form. Object Type: string
        "url" : "", #The name of the destination field required by the NAS. Object Type: string
        "default_url" : "", #Enter the default URL to redirect clients.Please ensure you prepend "http://" for any external domain. Object Type: string
        "default_url_override" : False, #If selected, the client’s default destination will be overridden regardless of its value. Object Type: boolean
        "dynamic_address" : False, #In multi-controller deployments, it is often required to post credentials to different addresses made available as part of the original redirection.The address above will be used whenever the parameter is not available or fails the requirements below. Object Type: boolean
        "dynamic_allowlist" : "", #Enter the IP addresses and networks from which dynamic addresses are permitted. Object Type: string
        "dynamic_denylist" : "", #Enter the IP addresses and networks from which dynamic addresses are denied. Object Type: string
        "access_allowlist" : "", #Enter the IP addresses and networks from which logins are permitted. Object Type: string
        "access_denylist" : "", #Enter the IP addresses and networks that are denied login access. Object Type: string
        "access_if_denied" : "", #Select the response of the system to a request that is not permitted. Object Type: string
        "login_title" : "", #The title to display on the web login page.  Leave blank to use the default (Login). Object Type: string
        "login_header" : "", #HTML template code displayed before the login form. Object Type: string
        "login_footer" : "", #HTML template code displayed after the login form. Object Type: string
        "login_message" : "", #HTML template code displayed while the login attempt is in progress. Object Type: string
        "login_delay" : "" #variable unknown: , #The time in seconds to delay while displaying the login message. Object Type: number
        "login_skin" : "", #Choose the skin to use when this web login page is displayed. Object Type: string
        "login_terms_require" : False, #If checked, the user will be forced to accept a Terms and Conditions checkbox. Object Type: boolean
        "login_terms_label" : "", #The form label for the terms checkbox.  Leave blank to use the default (Terms:). Object Type: string
        "login_terms_text" : "", #HTML code containing your Terms and Conditions.  Leave blank to use the default (I accept the <a href="{nwa_global name=guest_account_terms_of_use_url}" target="_blank" title="Open the terms of use URL.">terms of use</a>). Object Type: string
        "login_terms_layout" : "", #Select the layout for the terms and conditions text. Object Type: string
        "login_terms_error" : "", #The text to display if the terms are not accepted.  Leave blank to use the default (In order to log in, you must accept the terms and conditions.). Object Type: string
        "login_captcha" : "", #Select a CAPTCHA mode. Object Type: string
        "username_auth" : "", #Select the authentication requirement.Access Code requires a single code (username) to be entered.Anonymous allows a blank form requiring just the terms or a Log In button.  A pre-existing account is required.Auto is similar to anonymous but the page is automatically submitted.Access Code and Anonymous require the account to have the Username Authentication field set. Object Type: string
        "certificate_request" : "", #Choose whether the user should select a client certificate when authenticating. Object Type: string
        "username_auth_username" : "", #The account to use for anonymous authentication.The password will be visible within the HTML.It is recommended to increase the account Session Limit to the number of guests you wish to support. Object Type: string
        "certificate_auth" : "", #Choose whether other credentials must also be provided in addition to a certificate. Object Type: string
        "register_policy_manager" : False, #If selected, the endpoint’s attributes will also be updated with other details from the user account. Object Type: boolean
        "register_policy_manager_adv" : False, #Customize attributes stored with the endpoint. Object Type: boolean
        "register_policy_manager_attrs" : "", #List of name|value pairs to pass along.user_field | Endpoint Attribute. Object Type: string
        "hash_url" : "", #Select the level of checking to apply to URL parameters passed to the web login page.Use this option to detect when URL parameters have been modified by the user, for example their MAC address. Object Type: string
        "hash_secret" : "", #The redirection URL will be hashed using this shared secret. Object Type: string
        "bypass_cna" : False, #The Apple Captive Network Assistant (CNA) is the pop-up browser shown when joining a network that has a captive portal.Note that this option may not work with all vendors, depending on how the captive portal is implemented. Object Type: boolean
        "capport_venue_url" : "", #Enter an optional URL to send as the Venue Info URL for CAPPORT RFC-8908.https://www.rfc-editor.org/rfc/rfc8908.html. Object Type: string
        "onguard_healthcheck" : False, #If selected, the guest will be required to pass a health check prior to accessing the network. Object Type: boolean
        "onguard_agents" : "", #Select the agent options for client scanning.Native agents are available for Microsoft Windows and Apple OS X.  All other OS will fall back to Java. Object Type: string
        "onguard_header" : "", #HTML template code displayed before the health check text. Object Type: string
        "onguard_footer" : "", #HTML template code displayed after the health check text. Object Type: string
        "oauth_enabled" : False, #Enable logins with cloud identity / social network credentials. Object Type: boolean
        "oauth_debug" : False, #Log debugging data. Object Type: boolean
        "oauth_providers" : {}, #Configuration for cloud identity authentication providers. Object Type: object
        "login_custom_form" : False, #If selected, you must supply your own HTML login form in the Header or Footer HTML areas. Object Type: boolean
        "login_pre_auth_check" : "", #Select how the username and password should be checked before proceeding to the NAS authentication. Object Type: string
        "login_pre_auth_error" : "", #The text to display if the username and password lookup fails.  Leave blank to use the default (Invalid username or password). Object Type: string
        "mfa_enabled" : "", #No Desc. Object Type: string
        "mfa_first" : "", #All options with credentials must pass the Pre-Auth Check whenever a new user authenticates a device. Object Type: string
        "mfa_duo_ikey" : "", #No Desc. Object Type: string
        "mfa_duo_skey" : "", #No Desc. Object Type: string
        "mfa_duo_host" : "", #No Desc. Object Type: string
        "mfa_fn_client_id" : "", #No Desc. Object Type: string
        "mfa_fn_client_secret" : "", #No Desc. Object Type: string
        "mfa_fn_factors" : "", #Enter the number of factors to require. Object Type: string
        "mfa_fn_email" : False, #If disabled, the user must scan the QR code. Object Type: boolean
        "mfa_iws_tenant" : "", #No Desc. Object Type: string
        "mfa_iws_app" : "", #No Desc. Object Type: string
        "mfa_iws_hostname" : "", #Enter the hostname of the ImageWare server. Object Type: string
        "mfa_mc_scope" : "", #OAuth 2.0 scope value. Only mc_authn is supported for this release. Object Type: string
        "mfa_mc_context" : "", #Message which will be displayed on the authorization device. Object Type: string
        "mfa_mc_binding_message" : "", #Plain text reference to interlock the consumption device and authorization device. Object Type: string
        "mfa_mc_acr_values" : "", #Authentication Context class reference. Values as specified by ISO/IEC 29115 Clause 6. Object Type: string
        "mfa_mc_display" : "", #User interface display for Authentication. Object Type: string
        "mfa_mc_prompt" : "", #Value to specify to the Authorisation server about type of prompt. Object Type: string
        "mfa_mc_max_age" : 0, #Maximum elapsed time in secs since last authenticaiton. Object Type: integer
        "mfa_mc_login_hint" : "", #An indication to IDP on what ID to use for login. Object Type: string
        "mfa_mc_version" : "", #No Desc. Object Type: string
        "mfa_mc_discovery_service_endpoint" : "", #Provide the endpoint URL provided by Mobile Connect during configuration. Object Type: string
        "mfa_mc_redirect_url" : "", #Mobile Connect Redirect URL provided during configuration. Object Type: string
        "mfa_mc_client_id" : "", #No Desc. Object Type: string
        "mfa_mc_client_secret" : "", #No Desc. Object Type: string
        "mfa_header_html" : "", #HTML template code displayed before the provider’s vendor-specific authentication area. Object Type: string
        "mfa_footer_html" : "", #HTML template code displayed after the provider’s vendor-specific authentication area. Object Type: string
        }
        """
        url_path = "/weblogin/page-name/{page_name}"
        dict_path = {"page_name": page_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_weblogin_page_name_by_page_name(self, page_name=""):
        """
        Operation: Delete a web login page by page-name
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: page-name, Description: Unique page name of the web login
        """
        url_path = "/weblogin/page-name/{page_name}"
        dict_path = {"page_name": page_name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")
