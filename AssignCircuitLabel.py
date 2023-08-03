import requests
import json


tenant_ID='ENTER TENANT ID'
Site_ID='Site ID'
Element_id='ION Element ID'
Physical_int_ID='Physical WAN Interface'
AUTHToken='Paste Auth Token'
NewSiteWanInterface='enternew Sitewan inteface ID'

url = "https://api.elcapitan.cloudgenix.com/v4.15/api/tenants/{}/sites/{}/elements/{}/interfaces/{}".format(tenant_ID, Site_ID, Element_id, Physical_int_ID)



headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': AUTHToken
}
####Get the Interface Config
GET_INT_CONFIG = requests.request("GET", url, headers=headers)

###Convert to DICTIONARY
Jsonformatted = GET_INT_CONFIG.json()

###Add changed value
InterfaceUpdate = {'site_wan_interface_ids': [NewSiteWanInterface]}
Jsonformatted.update(InterfaceUpdate)

##Format back to type to import back in
Serialized_JSON_DATA = json.dumps(Jsonformatted)


##PUTTING DATA BACK
response = requests.request("PUT", url, headers=headers, data=Serialized_JSON_DATA)
print(response.text)
