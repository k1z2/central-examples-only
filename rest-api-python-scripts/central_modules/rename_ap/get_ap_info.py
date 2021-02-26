#get ap original information which will be exported to apinfo.csv
#get name and serial infomation, add nessisary columns which renaming workflow needs, also change the ap_name as site+"AP"+model+number, the info will be exported to csv_file.csv.

import http.client
import pandas as pd
import json
import pprint as pp

conn = http.client.HTTPSConnection("internal-apigw.central.arubanetworks.com")
payload = ''
headers = {
  'Authorization': 'Bearer rWp0OLrJAvR07EJkoy2wxDcxNTPjUGar'
}
conn.request("GET", "/monitoring/v1/aps", payload, headers)
res = conn.getresponse()
data = res.read()
data_json=json.loads(data)
df = pd.DataFrame(data_json["aps"])
df[['name','serial']].to_csv("apinfo.csv")
df['achannel']=""
df['atxpower']=""
df['gtxpower']=""
df['gchannel']=""
df['dot11a_radio_disable']=""
df['dot11g_radio_disable']=""
df['usb_port_disable']=""
df['zonename']=""
ap_count=int(pd.DataFrame(data_json)["count"][0])
print(type(ap_count))
for i in df.index:
 df.at[i,'name']=df.at[i,'site']+'-AP'+df.at[i,'model']+"-"+str(i)
df=df.rename(columns={"serial": "serial_number", "name": "hostname"})
df.loc[:,['serial_number','hostname','ip_address','zonename','achannel','atxpower','gtxpower','gchannel','dot11a_radio_disable','dot11g_radio_disable','usb_port_disable']].to_csv("csv_file.csv",index=False)



