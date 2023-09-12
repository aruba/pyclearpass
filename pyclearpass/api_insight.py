from pyclearpass.common import (
    _generate_parameterised_url,
    _remove_empty_keys,
    ClearPassAPILogin,
)

# API Category Name: Insight
# FileName: api_insight.py


class ApiInsight(ClearPassAPILogin):
    # API Service: Operations for Alert
    def get_alert(self, offset="", limit="", calculate_count=""):
        """
        Operation: Get all Insight alert configurations.
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type (Optional): query, Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Parameter Type (Optional): query, Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/alert"
        dict_query = {
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_alert(self, body=({})):
        """
        Operation: Create an Insight alert configuration.
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters:['id', 'name', 'category', 'subcategory', 'email_targets', 'severity', 'threshold', 'interval', 'interval_unit']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the alert. Object Type: integer
        "name" : "", #Name of the alert. Object Type: string
        "description" : "", #Description of the alert. Object Type: string
        "category" : "", #Category of the alert. Object Type: string
        "subcategory" : "", #Sub category is the template name of the alert. Object Type: string
        "email_targets" : {}, #Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "config" : {},      Setting the alert filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     }     #}. Object Type: object
        "severity" : "", #Severity of the alert, either "critical" or "warning". Object Type: string
        "threshold" : 0, #Triggering the alert when reaching the specified numeric threshold value. Object Type: integer
        "interval" : 0, #Triggering the alert at the numeric interval. Object Type: integer
        "interval_unit" : "", #Interval units either "minute" or "hour". Object Type: string
        "is_enabled" : False, #Enable/Disable the alert. Object Type: boolean
        "is_muted" : False, #Mute/Unmute the alert. Object Type: boolean
        }
        """
        url_path = "/alert"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_alert_by_id(self, id=""):
        """
        Operation: Get an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        """
        url_path = "/alert/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_alert_by_id(self, id="", body=({})):
        """
        Operation: Partial update of an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        Required Body Parameters:['id', 'name', 'category', 'subcategory', 'email_targets', 'severity', 'threshold', 'interval', 'interval_unit']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the alert. Object Type: integer
        "name" : "", #Name of the alert. Object Type: string
        "description" : "", #Description of the alert. Object Type: string
        "category" : "", #Category of the alert. Object Type: string
        "subcategory" : "", #Sub category is the template name of the alert. Object Type: string
        "email_targets" : {}, #Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "config" : {},      Setting the alert filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     }     #}. Object Type: object
        "severity" : "", #Severity of the alert, either "critical" or "warning". Object Type: string
        "threshold" : 0, #Triggering the alert when reaching the specified numeric threshold value. Object Type: integer
        "interval" : 0, #Triggering the alert at the numeric interval. Object Type: integer
        "interval_unit" : "", #Interval units either "minute" or "hour". Object Type: string
        "is_enabled" : False, #Enable/Disable the alert. Object Type: boolean
        "is_muted" : False, #Mute/Unmute the alert. Object Type: boolean
        }
        """
        url_path = "/alert/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_alert_by_id(self, id="", body=({})):
        """
        Operation: Complete update of an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        Required Body Parameters:['id', 'name', 'category', 'subcategory', 'email_targets', 'severity', 'threshold', 'interval', 'interval_unit']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the alert. Object Type: integer
        "name" : "", #Name of the alert. Object Type: string
        "description" : "", #Description of the alert. Object Type: string
        "category" : "", #Category of the alert. Object Type: string
        "subcategory" : "", #Sub category is the template name of the alert. Object Type: string
        "email_targets" : {}, #Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "config" : {},      Setting the alert filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     }     #}. Object Type: object
        "severity" : "", #Severity of the alert, either "critical" or "warning". Object Type: string
        "threshold" : 0, #Triggering the alert when reaching the specified numeric threshold value. Object Type: integer
        "interval" : 0, #Triggering the alert at the numeric interval. Object Type: integer
        "interval_unit" : "", #Interval units either "minute" or "hour". Object Type: string
        "is_enabled" : False, #Enable/Disable the alert. Object Type: boolean
        "is_muted" : False, #Mute/Unmute the alert. Object Type: boolean
        }
        """
        url_path = "/alert/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_alert_by_id(self, id=""):
        """
        Operation: Delete an Insight alert configuration by id.
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        """
        url_path = "/alert/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_alert_by_name(self, name=""):
        """
        Operation: Get an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        """
        url_path = "/alert/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_alert_by_name(self, name="", body=({})):
        """
        Operation: Partial update of an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        Required Body Parameters:['id', 'name', 'category', 'subcategory', 'email_targets', 'severity', 'threshold', 'interval', 'interval_unit']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the alert. Object Type: integer
        "name" : "", #Name of the alert. Object Type: string
        "description" : "", #Description of the alert. Object Type: string
        "category" : "", #Category of the alert. Object Type: string
        "subcategory" : "", #Sub category is the template name of the alert. Object Type: string
        "email_targets" : {}, #Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "config" : {},      Setting the alert filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     }     #}. Object Type: object
        "severity" : "", #Severity of the alert, either "critical" or "warning". Object Type: string
        "threshold" : 0, #Triggering the alert when reaching the specified numeric threshold value. Object Type: integer
        "interval" : 0, #Triggering the alert at the numeric interval. Object Type: integer
        "interval_unit" : "", #Interval units either "minute" or "hour". Object Type: string
        "is_enabled" : False, #Enable/Disable the alert. Object Type: boolean
        "is_muted" : False, #Mute/Unmute the alert. Object Type: boolean
        }
        """
        url_path = "/alert/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_alert_by_name(self, name="", body=({})):
        """
        Operation: Complete update of an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        Required Body Parameters:['id', 'name', 'category', 'subcategory', 'email_targets', 'severity', 'threshold', 'interval', 'interval_unit']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the alert. Object Type: integer
        "name" : "", #Name of the alert. Object Type: string
        "description" : "", #Description of the alert. Object Type: string
        "category" : "", #Category of the alert. Object Type: string
        "subcategory" : "", #Sub category is the template name of the alert. Object Type: string
        "email_targets" : {}, #Send alert notification to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send alert notification to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "config" : {},      Setting the alert filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     }     #}. Object Type: object
        "severity" : "", #Severity of the alert, either "critical" or "warning". Object Type: string
        "threshold" : 0, #Triggering the alert when reaching the specified numeric threshold value. Object Type: integer
        "interval" : 0, #Triggering the alert at the numeric interval. Object Type: integer
        "interval_unit" : "", #Interval units either "minute" or "hour". Object Type: string
        "is_enabled" : False, #Enable/Disable the alert. Object Type: boolean
        "is_muted" : False, #Mute/Unmute the alert. Object Type: boolean
        }
        """
        url_path = "/alert/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_alert_by_name(self, name=""):
        """
        Operation: Delete an Insight alert configuration by name.
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        """
        url_path = "/alert/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_alert_by_id_enable(self, id=""):
        """
        Operation: Enable an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        """
        url_path = "/alert/{id}/enable"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_id_disable(self, id=""):
        """
        Operation: Disable an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        """
        url_path = "/alert/{id}/disable"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_id_mute(self, id=""):
        """
        Operation: Mute an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        """
        url_path = "/alert/{id}/mute"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_id_unmute(self, id=""):
        """
        Operation: Unmute an Insight alert configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the alert
        """
        url_path = "/alert/{id}/unmute"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_name_enable(self, name=""):
        """
        Operation: Enable an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        """
        url_path = "/alert/{name}/enable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_name_disable(self, name=""):
        """
        Operation: Disable an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        """
        url_path = "/alert/{name}/disable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_name_mute(self, name=""):
        """
        Operation: Mute an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        """
        url_path = "/alert/{name}/mute"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_alert_by_name_unmute(self, name=""):
        """
        Operation: Unmute an Insight alert configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the alert
        """
        url_path = "/alert/{name}/unmute"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    # API Service: Operations for Report
    def get_report(self, offset="", limit="", calculate_count=""):
        """
        Operation: Get all Insight report configurations.
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type (Optional): query, Name: offset, Description: Starting point to return rows from a result set. i.e Default: 0
        Parameter Type (Optional): query, Name: limit, Description: Limit the number of rows returned from a result set. i.e Default: 25
        Parameter Type (Optional): query, Name: calculate_count, Description: Whether to calculate the total item count
        """
        url_path = "/report"
        dict_query = {
            "offset": offset,
            "limit": limit,
            "calculate_count": calculate_count,
        }
        url_path = _generate_parameterised_url(parameters=dict_query, url=url_path)
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def new_report(self, body=({})):
        """
        Operation: Create an Insight report configuration.
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 406 Not Acceptable, 415 Unsupported Media Type
        Required Body Parameters:['id', 'name', 'category', 'subcategory']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the report. Object Type: integer
        "name" : "", #Name of the report. Object Type: string
        "description" : "", #Description of the report. Object Type: string
        "category" : "", #Category of the report. Object Type: string
        "subcategory" : "", #Sub category is the template name of the report. Object Type: string
        "email_targets" : {}, #Send report to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "copy_remote" : False, #Enable to copy the report to the configured SCP/SFTP server. Object Type: boolean
        "config" : {},      Setting the report filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     },     csv_cols": ["...", "...", "..."]     #}. Object Type: object
        "schedule" : {},      Scheduling the report. Options are [noRepeat, daily, weekly, monthly],     e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,     when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}     when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}     when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}     #. Object Type: object
        "begin_dt" : 0, #Collect the data for the report from this "begin_dt". Object Type: integer
        "end_dt" : "", #Collect the data for the report till this "end_dt". Object Type: string
        "is_enabled" : False, #Enable/Disable the report. Object Type: boolean
        }
        """
        url_path = "/report"
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="post", query=body
        )

    def get_report_by_id(self, id=""):
        """
        Operation: Get an Insight report configuration by id.
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        """
        url_path = "/report/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_report_by_id(self, id="", body=({})):
        """
        Operation: Partial update of an Insight report configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        Required Body Parameters:['id', 'name', 'category', 'subcategory']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the report. Object Type: integer
        "name" : "", #Name of the report. Object Type: string
        "description" : "", #Description of the report. Object Type: string
        "category" : "", #Category of the report. Object Type: string
        "subcategory" : "", #Sub category is the template name of the report. Object Type: string
        "email_targets" : {}, #Send report to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "copy_remote" : False, #Enable to copy the report to the configured SCP/SFTP server. Object Type: boolean
        "config" : {},      Setting the report filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     },     csv_cols": ["...", "...", "..."]     #}. Object Type: object
        "schedule" : {},      Scheduling the report. Options are [noRepeat, daily, weekly, monthly],     e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,     when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}     when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}     when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}     #. Object Type: object
        "begin_dt" : 0, #Collect the data for the report from this "begin_dt". Object Type: integer
        "end_dt" : "", #Collect the data for the report till this "end_dt". Object Type: string
        "is_enabled" : False, #Enable/Disable the report. Object Type: boolean
        }
        """
        url_path = "/report/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_report_by_id(self, id="", body=({})):
        """
        Operation: Complete update of an Insight report configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        Required Body Parameters:['id', 'name', 'category', 'subcategory']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the report. Object Type: integer
        "name" : "", #Name of the report. Object Type: string
        "description" : "", #Description of the report. Object Type: string
        "category" : "", #Category of the report. Object Type: string
        "subcategory" : "", #Sub category is the template name of the report. Object Type: string
        "email_targets" : {}, #Send report to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "copy_remote" : False, #Enable to copy the report to the configured SCP/SFTP server. Object Type: boolean
        "config" : {},      Setting the report filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     },     csv_cols": ["...", "...", "..."]     #}. Object Type: object
        "schedule" : {},      Scheduling the report. Options are [noRepeat, daily, weekly, monthly],     e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,     when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}     when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}     when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}     #. Object Type: object
        "begin_dt" : 0, #Collect the data for the report from this "begin_dt". Object Type: integer
        "end_dt" : "", #Collect the data for the report till this "end_dt". Object Type: string
        "is_enabled" : False, #Enable/Disable the report. Object Type: boolean
        }
        """
        url_path = "/report/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_report_by_id(self, id=""):
        """
        Operation: Delete an Insight report configuration by id.
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        """
        url_path = "/report/{id}"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def get_report_by_name(self, name=""):
        """
        Operation: Get an Insight report configuration by name.
        HTTP Response Codes: 200 OK, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        """
        url_path = "/report/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="get")

    def update_report_by_name(self, name="", body=({})):
        """
        Operation: Partial update of an Insight report configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        Required Body Parameters:['id', 'name', 'category', 'subcategory']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the report. Object Type: integer
        "name" : "", #Name of the report. Object Type: string
        "description" : "", #Description of the report. Object Type: string
        "category" : "", #Category of the report. Object Type: string
        "subcategory" : "", #Sub category is the template name of the report. Object Type: string
        "email_targets" : {}, #Send report to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "copy_remote" : False, #Enable to copy the report to the configured SCP/SFTP server. Object Type: boolean
        "config" : {},      Setting the report filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     },     csv_cols": ["...", "...", "..."]     #}. Object Type: object
        "schedule" : {},      Scheduling the report. Options are [noRepeat, daily, weekly, monthly],     e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,     when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}     when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}     when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}     #. Object Type: object
        "begin_dt" : 0, #Collect the data for the report from this "begin_dt". Object Type: integer
        "end_dt" : "", #Collect the data for the report till this "end_dt". Object Type: string
        "is_enabled" : False, #Enable/Disable the report. Object Type: boolean
        }
        """
        url_path = "/report/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="patch", query=body
        )

    def replace_report_by_name(self, name="", body=({})):
        """
        Operation: Complete update of an Insight report configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        Required Body Parameters:['id', 'name', 'category', 'subcategory']
        Parameter Type: body, Name: body
        Body example with descriptions and object types below (type(dict):
        body={
        "id" : 0, #Numeric id of the report. Object Type: integer
        "name" : "", #Name of the report. Object Type: string
        "description" : "", #Description of the report. Object Type: string
        "category" : "", #Category of the report. Object Type: string
        "subcategory" : "", #Sub category is the template name of the report. Object Type: string
        "email_targets" : {}, #Send report to the configured email targets, e.g. "email_targets":["...", "..."]. Object Type: object
        "sms_targets" : {}, #Send report to the configured SMS targets, e.g. "sms_targets":["...", "..."]. Object Type: object
        "copy_remote" : False, #Enable to copy the report to the configured SCP/SFTP server. Object Type: boolean
        "config" : {},      Setting the report filter configurations & adding CSV columns for the CSV report,     e.g. "config": {     "filter": {     "auth.ap_name": {     "operator": "EQUALS",     "value": ["..."]     },     "cppm_cluster.hostname": {     "operator":"CONTAINS",     "value":["...", "..."]     }     },     csv_cols": ["...", "...", "..."]     #}. Object Type: object
        "schedule" : {},      Scheduling the report. Options are [noRepeat, daily, weekly, monthly],     e.g. when running the report "now" itself => "schedule": {} - then "begin_dt" & "end_dt" are mandatory,     when scheduling the report at "daily" => "schedule": {"freq": "daily", "hour": 12}     when scheduling the report at "weekly" => "schedule": {"freq": "weekly", "day": 0, "hour": 12}     when scheduling the report at "monthly" => "schedule": {"freq": "monthly", "date": 1, "hour": 12}     #. Object Type: object
        "begin_dt" : 0, #Collect the data for the report from this "begin_dt". Object Type: integer
        "end_dt" : "", #Collect the data for the report till this "end_dt". Object Type: string
        "is_enabled" : False, #Enable/Disable the report. Object Type: boolean
        }
        """
        url_path = "/report/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        body = _remove_empty_keys(keys=body)
        return ClearPassAPILogin._send_request(
            self, url=url_path, method="put", query=body
        )

    def delete_report_by_name(self, name=""):
        """
        Operation: Delete an Insight report configuration by name.
        HTTP Response Codes: 204 No Content, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        """
        url_path = "/report/{name}"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="delete")

    def update_report_by_id_enable(self, id=""):
        """
        Operation: Enable an Insight report configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        """
        url_path = "/report/{id}/enable"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_report_by_id_disable(self, id=""):
        """
        Operation: Disable an Insight report configuration by id.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        """
        url_path = "/report/{id}/disable"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_report_by_name_enable(self, name=""):
        """
        Operation: Enable an Insight report configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        """
        url_path = "/report/{name}/enable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def update_report_by_name_disable(self, name=""):
        """
        Operation: Disable an Insight report configuration by name.
        HTTP Response Codes: 200 OK, 204 No Content, 304 Not Modified, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        """
        url_path = "/report/{name}/disable"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="patch")

    def new_report_by_id_run(self, id=""):
        """
        Operation: Run an Insight report by id.
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: id, Description: Numeric id of the report
        """
        url_path = "/report/{id}/run"
        dict_path = {"id": id}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="post")

    def new_report_by_name_run(self, name=""):
        """
        Operation: Run an Insight report by name.
        HTTP Response Codes: 201 Created, 401 Unauthorized, 403 Forbidden, 404 Not Found, 406 Not Acceptable, 415 Unsupported Media Type
        Parameter Type: path, Name: name, Description: Name of the report
        """
        url_path = "/report/{name}/run"
        dict_path = {"name": name}
        for item in dict_path:
            url_path = url_path.replace("{" + item + "}", dict_path[item])
        return ClearPassAPILogin._send_request(self, url=url_path, method="post")
