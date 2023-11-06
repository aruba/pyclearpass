from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: ToolsAndUtilities
# FileName: api_toolsandutilities.py


class ApiToolsAndUtilities(ClearPassAPILogin):
    # API Service: Operations for Email Send
    def new_email_send(self, body=({})):
        """
        Operation: Send an Email
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['to', 'message']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "to" : {}, #List of Recipients Email Address (e.g., ["a@example.com", "b@example.com"]). Object Type: object
        "subject" : "", #Email Subject. Object Type: string
        "message" : "", #Email Body. Object Type: string
        "cc_recipients" : {}, #List of CC recipients Email Address (e.g., ["a@example.com", "b@example.com"]). Object Type: object
        "bcc_recipients" : {}, #List of BCC recipients Email Address (e.g., ["a@example.com", "b@example.com"]). Object Type: object
        "headers" : {}, #Email headers (e.g., {"Content-Type":"text/plain; charset=UTF-8","Content-Transfer-Encoding": "8bit"}). Object Type: object

        }
        """
        url_path = "/email/send"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Generate a random MPSK
    def get_random_mpsk(self):
        """
        Operation:
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        """
        url_path = "/random-mpsk"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_random_mpsk(self, body=({})):
        """
        Operation:
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "random_mpsk_method" : "", #The random MPSK method.  See the documentation for the allowed values.. Object Type: string
        "random_mpsk_length" : 0, #The desired length of the MPSK.. Object Type: integer
        "random_mpsk_picture" : "", #The picture to be used for the ‘nwa_picture_password’ method.  See the documentation for the valid syntax.. Object Type: string

        }
        """
        url_path = "/random-mpsk"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Generate a random password
    def get_random_password(self):
        """
        Operation:
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        """
        url_path = "/random-password"
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_random_password(self, body=({})):
        """
        Operation:
        HTTP Response Codes: 200 OK, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters: None listed
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "random_password_method" : "", #The random password method.  See the documentation for the allowed values.. Object Type: string
        "random_password_length" : 0, #The desired length of the password.. Object Type: integer
        "random_password_picture" : "", #The picture to be used for the ‘nwa_picture_password’ method.  See the documentation for the valid syntax.. Object Type: string

        }
        """
        url_path = "/random-password"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    # API Service: Send SMS using Configuration -> SMS Services -> Send SMS
    def new_sms_send(self, body=({})):
        """
        Operation: Send an SMS message
        HTTP Response Codes: 200 OK, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['recipient', 'message']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "handler" : 0, #Select the service to use when sending the message. Object Type: integer
        "recipient" : "", #Enter the mobile telephone number of the recipient in international format. Object Type: string
        "carrier" : "", #The visitor’s mobile carrier. Object Type: string
        "message" : "", #Enter the message to send (maximum 160 characters). Object Type: string

        }
        """
        url_path = "/sms/send"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )
