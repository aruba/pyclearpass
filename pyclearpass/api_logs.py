from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: Logs
# FileName: api_logs.py


class ApiLogs(ClearPassAPILogin):

    # API Service: Collection of endpoints
    def get_insight_endpoint_mac_by_mac(self, mac=""):
        """
        Operation: Get a single endpoint by MAC address
        HTTP Response Codes: 200 OK, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: mac, Description: URL parameter mac
        """
        url_path = "/insight/endpoint/mac/{mac}"
        dict_path = {"mac": mac}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_insight_endpoint_ip_by_ip(self, ip=""):
        """
        Operation: Look up endpoints by IP address
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: ip, Description: IPv4/IPv6 address to match with endpoints
        """
        url_path = "/insight/endpoint/ip/{ip}"
        dict_path = {"ip": ip}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_insight_endpoint_ip_range_by_ip_range(self, ip_range=""):
        """
        Operation: Look up endpoints by IP address range
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: ip_range, Description: IPv4/IPv6 address range, e.g. 192.168.1.1-255 or 2001:db8:a0b:12cd::a-f
        """
        url_path = "/insight/endpoint/ip-range/{ip_range}"
        dict_path = {"ip_range": ip_range}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def get_insight_endpoint_time_range_by_from_time_to_time(
        self, from_time="", to_time=""
    ):
        """
        Operation: Look up endpoints by time range
        HTTP Response Codes: 200 OK, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type: path, Name: from_time, Description: Start time for search, as UNIX timestamp
        Parameter Type: path, Name: to_time, Description: End time for search, as UNIX timestamp
        """
        url_path = "/insight/endpoint/time-range/{from_time}/{to_time}"
        dict_path = {"from_time": from_time, "to_time": to_time}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Get previous login details for an admin user
    def get_login_audit_by_name(self, name=""):
        """
        Operation: Get previous login details for an admin user
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: User name of admin
        """
        url_path = "/login-audit/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    # API Service: Collection of system events
    def get_system_event(
        self, filter="", sort="", offset="", limit="", calculate_count=""
    ):
        """
        Operation: Get a list of system events
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Parameter Type (Optional): query, Name: filter, Description: JSON filter expression specifying the items to return
        Parameter Type (Optional): query, Name: sort, Description: Sort ordering for returned items (default +source)
        Parameter Type (Optional): query, Name: offset, Description: Zero based offset to start from
        Parameter Type (Optional): query, Name: limit, Description: Maximum number of items to return (1 – 1000)
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/system-event"
        dict_query = {
            "filter": filter,
            "sort": sort,
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_system_event(self, body=({})):
        """
        Operation: Create a new system event
        HTTP Response Codes: 201 Created, 406 Not Acceptable, 415 Unsupported Media Type, 422 Unprocessable Entity
        Required Body Parameters:['source', 'level', 'category', 'action', 'description', 'timestamp']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):

        body={
        "source" : "", #Source. Object Type: string
        "level" : "", #Level. Object Type: string
        "category" : "", #Category. Object Type: string
        "action" : "", #Action. Object Type: string
        "description" : "", #Description. Object Type: string
        "timestamp" : "", #Timestamp. Object Type: string

        }
        """
        url_path = "/system-event"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )
