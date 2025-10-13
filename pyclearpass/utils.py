# (C) Copyright 2019-2025 Hewlett Packard Enterprise Development LP.
# Apache License 2.0

import json
import csv
import os

 
class Utils:
    def get_token_from_file(fileName):
        """
        Use this function to retrieve the access_token from a file which is located in the working directory of the script.
        The file must use the following structure:
        {"access_token":"your_secret_token"}
        """
        try:
            f = open(fileName, "r")
            content = f.read()
            jsonContent = json.loads(content)
            if jsonContent["access_token"]:
                return jsonContent["access_token"]
            else:
                raise ValueError(
                    {"status": "Error", "message": "Missing Access Token."}
                )

        except KeyError as e:
            raise Exception(
                {
                    "status": "Error",
                    "Message": "Missing 'access_token' key name. Ensure key name exists as per the function usage details.",
                }
            )
        except json.JSONDecodeError as e:
            raise Exception(
                {
                    "status": "Error",
                    "Message": "Ensure a valid json file as described in the function usage details.",
                }
            )
        except FileNotFoundError as e:
            raise Exception(
                {
                    "status": "Error",
                    "Message": "Ensure the token file '"
                    + fileName
                    + "' exists. "
                    + e.strerror,
                }
            )

        except Exception as e:
            raise Exception({"status": "Error", "Message": e})
