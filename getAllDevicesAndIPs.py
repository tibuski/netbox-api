from netbox_python import NetBoxClient, Result
nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="0123456789abcdef0123456789abcdef01234567"
)

ret = nb.dcim.sites.all()
print(f"status code: {ret.response.status_code}")
print(ret.data)