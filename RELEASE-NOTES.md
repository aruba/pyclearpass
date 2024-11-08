# Release Notes
This document contains high level documented changes to the pyclearpass package.

## Version 1.0.0 (Not listed) 
1. Initial Release

## Version 1.0.1 (04/07/2023)
1. Code updated to PEP8 standards (formatting of code along with renaming of variables, packages, classes and modules)
2. Additional examples provided

## Version 1.0.2 (12/09/2023)
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

## Version 1.0.3 (12/09/2023)
1. Missing '_new_api_token' rename from ClearPassAPILogin (common.py)

## Version 1.0.4 (06/11/2023)
1. Fixed incorrect positioning of characters in 'body dictionary object' across all api files (to allow copy and paste of body for easy use of script).
2. Fixed missed # 'body dictionary object' across all api files for 'object' type.  
3. API code includes new, modified or deleted API that is implemented in Aruba ClearPass v6.11.5.

## Version 1.0.5 (30/05/2024)
1. Updated references of 'Aruba ClearPass' to 'HPE Aruba Networking ClearPass'
2. API code includes new, modified or deleted API that is implemented in HPE Aruba Networking ClearPass v6.12.2. To use older version built on v6.11.5, execute 'pip install pyclearpass==1.0.4'
3. Updated README.md
4. Updated year in license.md

## Version 1.0.6 (05/07/2024)
1. Updated common.py to include accept in the header for non JSON response content types. 
2. Added response content-type to methods in other api files where required. 

## Version 1.0.7 (08/11/2024)
1. Updated common.py to convert dict to json when creating parameterised urls within the _generate_parameterised_url method. 