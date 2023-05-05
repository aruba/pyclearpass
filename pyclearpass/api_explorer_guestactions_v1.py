from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# File Name: api_explorer_guestactions_v1.py


class ApiGuestActions(ClearPassAPILogin):
    # Function Section Name:GenerateGuestDigitalPass
    # Function Section Description: Operations for GenerateGuestDigitalPass

    def get_guest_by_guest_id_pass_id(self, guest_id="", id=""):
        """
        Operation: Generate digital pass for guest account based on template specified by ID
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Path Parameter Name: id, Description: Numeric ID of the digital pass template
        """
        url_path = "/guest/{guest_id}/pass/{id}"
        dict_path = {"guest_id": guest_id, "id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:GenerateGuestReceipt
    # Function Section Description: Generate a guest account receipt

    def get_guest_by_guest_id_receipt_id(self, guest_id="", id=""):
        """
        Operation: Generate print template for guest account, using specified template ID
        HTTP Status Response Codes: 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
        Required Path Parameter Name: id, Description: Numeric ID of the print template
        """
        url_path = "/guest/{guest_id}/receipt/{id}"
        dict_path = {"guest_id": guest_id, "id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # Function Section Name:SendSmsReceipt
    # Function Section Description: Operations for SendSmsReceipt

    def new_guest_by_guest_id_sendreceipt_sms(self, guest_id="", body=({})):
        """
                Operation: Resend guest receipt for guest account, via SMS
                HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
                Required Body Parameters (body description)- SendSmsReceipt {confirm (boolean): Flag to confirm sending guest receipt via SMS}
                Required Body Parameters (type(dict) body example)- {
          "confirm": false
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

    # Function Section Name:SendSmtpReceipt
    # Function Section Description: Operations for SendSmtpReceipt

    def new_guest_by_guest_id_sendreceipt_smtp(self, guest_id="", body=({})):
        """
                Operation: Resend guest receipt for guest account,  via SMTP
                HTTP Status Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: guest_id, Description: URL parameter guest_id
                Required Body Parameters (body description)- SendSmtpReceipt {confirm (boolean): Flag to confirm sending guest receipt via SMTP}
                Required Body Parameters (type(dict) body example)- {
          "confirm": false
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

    # Function Section Name:SponsorshipApproval
    # Function Section Description: Sponsor confirmation for guest accounts

    def new_guest_by_guest_id_sponsor(self, guest_id="", body=({}), gsr_id=""):
        """
                Operation: Accept or reject a guest sponsorship request
                HTTP Status Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity, 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
                Required Path Parameter Name: guest_id, Description: Numeric ID of the guest account
                Required Body Parameters (body description)- SponsorshipApproval {token (string): Registration token,register_token (string): Registration token,register_reject (boolean, optional): Set to true to reject the sponsorship request,role_id (integer, optional): Override the guest role,modify_expire_time (string, optional): Override the guest expiration time,confirm_expire_time (string, optional): Timestamp for new expiration time; used if modify_expire_time is "expire_time"}
                Required Body Parameters (type(dict) body example)- {
          "token": "",
          "register_token": "",
          "register_reject": false,
          "role_id": 0,
          "modify_expire_time": "",
          "confirm_expire_time": ""
        }
                Optional Query Parameter Name: gsr_id, Description: Optional name of the self-registration with the sponsor confirmation configuration.
        """
        url_path = "/guest/{guest_id}/sponsor"
        dict_path = {"guest_id": guest_id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        dict_query = {"gsr_id": gsr_id}
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )
