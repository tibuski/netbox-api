from dotenv import load_dotenv
import pynetbox
import os

# Get API connection URL and TOKEN from .env file
# Exemple :
# NETBOX_URL=http://nuc.lan:9000/
# NETBOX_TOKEN=0123456789abcdef0123456789abcdef01234567
load_dotenv()
netbox_url = os.getenv("NETBOX_URL")
netbox_token = os.getenv("NETBOX_TOKEN")

# Initiate API connection settings
netbox = pynetbox.api(
    netbox_url,
    token=netbox_token
)

devices = list(netbox.dcim.devices.all())
assignments = list(netbox.tenancy.contact_assignments.all())
assigned_contacts = 0
support_contacts = 0

print('{0:18},{1:20},{2:8},{3}'.format("Device","Contact Role","TAG","Device Role"))

for d in devices:
    for a in assignments:
        if a.object.display == d.display:
            assigned_contacts += 1
            if a.role.display == 'Support Contract':
                support_contacts += 1
    
    if assigned_contacts == 0:
        if len(d.tags) == 0:
            print('{0:18},{1:20},{2:8},{3}'.format(str(d),"No Contact","NO TAG",str(d.device_role.display)))
        else:
            print('{0:18},{1:20},{2:8},{3}'.format(str(d),"No Contact",str(d.tags[0]),str(d.device_role.display)))
   
    if support_contacts ==0:
        if len(d.tags) == 0:
            print('{0:18},{1:20},{2:8},{3}'.format(str(d),"No Support-Contract","NO TAG",str(d.device_role.display)))
        else:
            print('{0:18},{1:20},{2:8},{3}'.format(str(d),"No Support-Contract",str(d.tags[0]),str(d.device_role.display)))

    assigned_contacts = 0
    support_contacts = 0
        
