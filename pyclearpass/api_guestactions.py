from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: GuestActions
# FileName: api_guestactions.py


class ApiGuestActions(ClearPassAPILogin):

    # API Service: Operations for GenerateGuestDigitalPass
    def get_guest_by_guest_id_pass_id(self, guest_id="", id=""):
        """
        Operation: Generate digital pass for guest account based on template specified by ID
        HTTP Response Codes: 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        Parameter Type: path, Name: id, Description: Numeric ID of the digital pass template
        """
        url_path = "/guest/{guest_id}/pass/{id}"
        dict_path = {"guest_id": guest_id, "id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Generate a guest account receipt
    def get_guest_by_guest_id_receipt_id(self, guest_id="", id=""):
        """
        Operation: Generate print template for guest account, using specified template ID
        HTTP Response Codes: 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        Parameter Type: path, Name: id, Description: Numeric ID of the print template
        """
        url_path = "/guest/{guest_id}/receipt/{id}"
        dict_path = {"guest_id": guest_id, "id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Operations for SendSmsReceipt
    def new_guest_by_guest_id_sendreceipt_sms(self, guest_id="", body=({})):
        """
        Operation: Resend guest receipt for guest account, via SMS
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters:['confirm']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "confirm" : False, #Flag to confirm sending guest receipt via SMS. Object Type: boolean

        }
        """
        url_path = "/guest/{guest_id}/sendreceipt/sms"
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Operations for SendSmtpReceipt
    def new_guest_by_guest_id_sendreceipt_smtp(self, guest_id="", body=({})):
        """
        Operation: Resend guest receipt for guest account,  via SMTP
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: guest_id, Description: URL parameter guest_id
        Required Body Parameters:['confirm']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "confirm" : False, #Flag to confirm sending guest receipt via SMTP. Object Type: boolean

        }
        """
        url_path = "/guest/{guest_id}/sendreceipt/smtp"
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Sponsor confirmation for guest accounts
    def new_guest_by_guest_id_sponsor(self, gsr_id="", guest_id="", body=({})):
        """
        Operation: Accept or reject a guest sponsorship request
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: gsr_id, Description: Optional name of the self-registration with the sponsor confirmation configuration.
        Parameter Type: path, Name: guest_id, Description: Numeric ID of the guest account
        Required Body Parameters:['token', 'register_token']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "token" : "", #Registration token. Object Type: string
        "register_token" : "", #Registration token. Object Type: string
        "register_reject" : False, #Set to true to reject the sponsorship request. Object Type: boolean
        "role_id" : 0, #Override the guest role. Object Type: integer
        "modify_expire_time" : "", #Override the guest expiration time. Object Type: string
        "confirm_expire_time" : "", #Timestamp for new expiration time; used if modify_expire_time is "expire_time". Object Type: string

        }
        """
        url_path = "/guest/{guest_id}/sponsor"
        dict_query = {"gsr_id": gsr_id}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )
