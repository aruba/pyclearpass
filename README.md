# pyclearpass
## Aruba ClearPass V6.11 SDK
Aruba ClearPass SDK has been developed in Python v3.9 to utilise the full functionality of the Aruba ClearPass REST API environment. Each available REST API command is available for use in this module. All responses from the ClearPass API are in JSON format and any interactions with the API are logged within the Audit Viewer.

This package has been uploaded to https://pypi.org/ (outstanding) and is also available to install via https://github.com/aruba/pyclearpass. Installation instructions are provided below. 
## Available API Categories 
The following describes the available top level functionality of the ClearPass API available within this Python Package. 
- Operations
- Certificate Authority
- Endpoint Visibility 
- Enforcement Profile
- Global Server Configuration
- Guest Actions
- Guest Configuration
- Identities
- Insights
- Integrations
- Local Server Configuration 
- Logs
- Platform Certificates
- Policy Elements
- Session Controls
- Tools and Utilities

_This package comes without any warranties and should be used at your own risk._

## ClearPass Server Readiness
These steps list what is required on the ClearPass server:
1. Make sure you have the API Service enabled within Services. You may use the template to help you do this. 
2. Create a new API Client within the ClearPass Guest Portal 
    - a. client id = demo, 
    - b. enabled, Operating Mode = Rest API, 
    - c. Operator Profile = Pick one with apporpiate permission level or make a new one,  
    - d. Grant Type = client credentials
    - e. Access Token Lifetime: 8 Hours
3. Optional but preferred, a valid SSL cerfificate

If you need information, refer to the ClearPass configuration documentation for the API account -
https://developer.arubanetworks.com/aruba-cppm/docs/clearpass-configuration  

# Python Requirements  
Ensure Python v3.9 or greater is installed on your operating system
# Package Installation  
#### Method 1 - Installing Package from PyPi (not yet published!)
Run the following in a command line terminal to install the pip package - ```pip3 install pyclearpass``` or ```pip install pyclearpass```. This may vary between Operating Systems. 

#### Method 2 - Installing Package from Github (not using Git.exe)
1. Click into the Aruba Github Repository where the latest version of pyclearpass is located 
2. Click Code (in green) and Download to Zip
3. Extract the zip file into a directory
4. Go into a command line terminal and change directory (cd) into the folder where you extracted the zipped file and then down one child folder. The folder contents should pyclearpass (FOLDER), LICENCE, pyproject.toml and README.md   
5. In your command line terminal type ```python3 -m build``` or ```python -m build```. This will create a folder called dist with a file containing a .gz extension. 
6. Run the following in a command line terminal to install the pip package - ```pip3 install pathtozip.gz``` or ```pip install pathtozip.gz```. This may vary between Operating Systems.

#### Method 3 - Installing Package from Github (using Git.exe)
1. Install Git for your Operating System from https://git-scm.com/download
2. Run the following in a command line terminal to install the pip package - ```pip3 install git+https://github.com/aruba/pyclearpass``` or ```pip install git+https://github.com/aruba/pyclearpass```. This may vary between Operating Systems. 


# Inital Usage Instructions
Within your Python favourite IDE environment, create an import reference
```
from pyclearpass import *
```
Create a object to login into ClearPass. The login object needs to be passed to use any function within the ClearPass API.
An example below shows how to create the login object.
```
login = ClearPassAPILogin(server="https://yourserver.network.local:443/api",granttype="client_credentials",
clientsecret="myclientsecretexample", clientid="myclientidexample", verify_ssl=False)
```
>Note - The login object will contain the APIToken once any function has been used. 
It grabs it once for the session and uses the same token through the execution of the rest of the script. 

Find an API you want to use, by prefixing  ```Api```  in your IDE and intellisense will show the available APIs available. Each of the top level API category names are available as a module. Once you have chosen a specifc API to use, for example ApiPolicyElements, it will show you the available methods if you suffix a . to the command - ```ApiPolicyElements.```

The example below prints the roles available within the clearpass server.
```	
print(ApiPolicyElements.get_role(login)) 
```
By default, the example above to return the roles available within the clearpass server will only show the first 25 roles. If you want to view more, you have to adjust the limit. Placing your cursor over the .getRole will usually show you help about the method. 
```
print(ApiPolicyElements.get_role(login, limit=100))
```
# Help 
Once you have written a specific API  ```ApiName.FunctionName(```, placing your cursor over the command will show you help for the function and what the required parameters are (example is Visual Studio Code). The first parameter is always login. 
You may also read the help for the function by calling ```help(ApiName.FunctionName)```. Each function contains a help section on how to use it. 
# Python Package Upgrade Instructions
Once an update is available on the Python PyPi repository, you may upgrade your release by completing the following in a command line terminal - ```pip3 install pyclearpass --upgrade```
# Uninstall Package Package
To remove the Python pyclearpass package, type the following command into a command line terminal - ```pip3 uninstall pyclearpass ``` or ```pip uninstall pyclearpass ```

# Release Notes
Release notes for this version are availble in the [RELEASE-NOTES.md](RELEASE-NOTES.md) file.

# Further Usage Examples
The examples below all exclude importing the module and creating the login variable. An example is shown below
```
from pyclearpass import *
login = ClearPassAPILogin(server="https://yourserver.network.local:443/api",granttype="client_credentials",
clientsecret="myclientsecretexample", clientid="myclientidexample", verify_ssl=False)
```

## Get Local Server Configuration 
```
LSCGCS = ApiLocalServerConfiguration.get_cluster_server(login)
print(json.dumps(LSCGCS['_embedded']['items'],indent=1))
```

## Get Total End Point Count 
```
IGEP = ApiIdentities.get_endpoint(login, calculate_count='true')
print("Total MACs in Table: "+str(IGEP['count']))
```

## Get Insight Device Details
```
print(ApiLogs.get_insight_endpoint_ip_by_ip(login,ip="192.168.0.99"))
```

## Get list of Admin Users
```
AU = ApiGlobalServerConfiguration.get_admin_user(login)
for users in AU['_embedded']['items']:
  print(users)
```

## Add New Endpoint
```
newEndPoint = {
  "mac_address": "11:22:33:44:55:66",
  "description": "Demo EndPoint 1",
  "status": "Known"
}
print(ApiIdentities.new_endpoint(login,body=newEndPoint))
```

## Add New Role
```
role={"name": "Test1","description": "Test role made using the API Package in Python"}
print(ApiPolicyElements.new_role(login,body=role))
```

## Delete Role
```
print(ApiPolicyElements.delete_role_name_by_name(login,name='Demo'))
```

## Add New Guest Device 
This example adds a Guest Device including 
1. An expiry date within 24 hours in seconds 
2. Associated to the role ID of 3 (Guest in test environment)
3. Statically assigned MPSK password
```
import time
new_guest_device = {
  "enabled": True,
  "expire_time": int(time.time()) + 86400,
  "mac": "11:22:22:33:33:11",
  "notes": "Created by API Test Script",
  "role_id": 3,
  "sponsor_profile_name": "Super Administrator",
  "visitor_name": "API Test Device",
  "mpsk":"SecretPassword",
  "mpsk_enable":"1"
}
new_device= ApiIdentities.new_device(login,body=new_guest_device)
print(new_device)
```

## Get Guest Device by MAC
```
import json
get_mac_address = "11-22-33-33-22-11"
view_guest_device = ApiIdentities.get_device_mac_by_macaddr(login,get_mac_address)
print(json.dumps(view_guest_device,indent=2))
```

## Delete an Enforcement Policy
```
print(ApiPolicyElements.delete_enforcement_policy_by_enforcement_policy_id(login,enforcement_policy_id='3058'))
```

## Create a new Enforcement Policy with staged initial rules and then a loop to create additional rules. 
```
newEnforcementPolicy= {
  "name": "MPSK Demo",
  "description": "MPSK Enforcement",
  "enforcement_type": "RADIUS",
  "default_enforcement_profile": "Deny Device",
  "rule_eval_algo": "first-applicable",
  "rules": ''}

newEnforcementPolicyRules =({"rules":[]})

initialrule = {
            "enforcement_profile_names": [
                "Sample Enforcement Policy"
            ],
            "condition": [
                {
                    "type": "Connection",
                    "name": "AP-Name",
                    "oper": "BEGINS_WITH",
                    "value": "APDemo"
                }
            ]
        }
newEnforcementPolicyRules["rules"].append(initialrule)

for id in range(9,11):
    randompsk = random.randint(8000000,9000000)
    epf ={
            "enforcement_profile_names": [
                "Sample Enforcement Policy"

            ],
            "condition": [
                {
                    "type": "Connection",
                    "name": "AP-Name",
                    "oper": "BEGINS_WITH",
                    "value": "APNo"+str(id)
                }
            ]
        }
    
    newEnforcementPolicyRules["rules"].append(epf) 
 
newEnforcementPolicy["rules"] = newEnforcementPolicyRules["rules"]
print(ApiPolicyElements.new_enforcement_policy(login,body=newEnforcementPolicy))
```

>Note - you may find it easier to initially pull a working Enforcement Policy with minimal rules before trying to create a new one from scratch. For example, the rule evaluation in the GUI shows as 'First applicable', however in the backend it is shown as 'first-applicable'. This example is a working policy. It is demonstrated with a loop which could read an entry in a CSV file if adapted. 

## Update an existing Enforcement Policy, retaining the original items and using a loop to add additional items 
```
epol = ApiPolicyElements.get_enforcement_policy_name_by_name(login, name="MPSK Enforcement")
OriginalRules = epol["rules"]
CombinedRules =({"rules":[]})
for item in range(len(OriginalRules)):
    CombinedRules["rules"].append(OriginalRules[item])

for no in range(9,11):
    rule ={
            "enforcement_profile_names": [
                "Sample Enforcement Policy"

            ],
            "condition": [
                {
                    "type": "Connection",
                    "name": "AP-Name",
                    "oper": "BEGINS_WITH",
                    "value": "APNo"+str(no)
                }
            ]
        }
    
    CombinedRules["rules"].append(rule)  

ApiPolicyElements.update_enforcement_policy_name_by_name(login,name="MPSK Enforcement",body=CombinedRules)
```
