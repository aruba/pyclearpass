# Release Notes
This document contains high level documented changes to the pyclearpass module releases
## Version 1.0.0
Initial Release
## Version 1.0.1
1. Code updated to PEP8 standards (formatting of code along with renaming of variables, packages, classes and modules)
2. Additional examples provided
## Version 1.0.2
1. Fixed an issue with the parameter name as not injected correctly into dictionary (page-name)
2. Added descriptions to body parameters across all methods 
3. Used new method to generate modules file 
4. Python package generated  based on latest API available within ClearPass v6.11.4
5. Newly created code updated to PEP8 standards
6. Updated ClearPassAPILogin class init method to include 'api_token' to allow an api token to be used rather than client_credentials
7. Updated ClearPassAPILogin class method name from _get_api_key to _new_api_token and updated local references
8. Updated ClearPassAPILogin class method _send_request to include a except for KeyError
9. All file names updated
10. Updated __init__.py to reflect new filenames
11. Updated README.md
## Version 1.0.3
1. Missing '_new_api_token' rename from ClearPassAPILogin (common.py)