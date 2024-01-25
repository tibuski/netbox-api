import pynetbox

nb = pynetbox.api(
    'https://demo.netbox.dev',
    token='dd22fbf1157f54c7a67374393ba098ab9247e430'
)
devices = nb.dcim.devices.all()

for device in devices:
    print(device.name)