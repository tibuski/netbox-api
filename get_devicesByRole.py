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

d_role = 's4b'

devices = netbox.dcim.devices.filter(role = d_role)

for d in devices:
    print(d.name,'\t',d.device_role)