from dotenv import load_dotenv
import os
import pynetbox

# Clearing the Screen
os.system('clear')

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

# Read devices from file devices.txt. One device name per line
devices2update=[]
with open('./devices.txt') as f:
    devices2update = f.read().splitlines()
f.close()


# Function to assign support contact to device list in devices2update
def assign_support_contact(device_id,contact_id):            
    try:
        assign_contact = netbox.tenancy.contact_assignments.create(
        content_type = 'dcim.device',
        object_id = device_id,
        contact = contact_id,
        role =  '5' # Support Contract
        )
    except:
        print("Contact already assigned")

     
# Get Netbox Objects
devices = list(netbox.dcim.devices.filter(name=devices2update))
assigned_contacts = list(netbox.tenancy.contact_assignments.filter(object_id=map(lambda d: d.id,devices)))
contacts = list(netbox.tenancy.contacts.all())

# ========= MAIN =========

print("-------------------------------------------------------------------")
print('{0:12} {1:5} {2:}'.format('Contact','id','Group'))
print("-------------------------------------------------------------------")
for c in contacts:      
    if c.group.name == 'Support Contacts':
            print('{0:20} {1:5} {2:}'.format(c.name,c.id,c.group.name))
print("-------------------------------------------------------------------")


# Ask used to input contact ID to add to server list
user_input = input("Contact ID to add : ")

# Assign Contact. To find contact ID, check contacts in Netbox, and display column 'ID'
for d in devices:
    assign_support_contact(d.id,user_input)


print("-------------------------------------------------------------------")
print('{0:12} {1:5} {2:18} {3:5} {4:16} {5:5}'.format('Device','id','Contact','id','Role','id'))
print("-------------------------------------------------------------------")
assigned_contacts = list(netbox.tenancy.contact_assignments.filter(object_id=map(lambda d: d.id,devices)))
for c in assigned_contacts:      
    for d in devices:         
        if d.name == c.object.name:
            print('{0:12} {1:5} {2:18} {3:5} {4:16} {5:5}'.format(c.object.name,c.object.id,c.contact.name,c.contact.id,c.role.name,c.role.id))
print("-------------------------------------------------------------------")
