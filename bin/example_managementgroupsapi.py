'''
Example of using the ManagementGroupsAPI class to list management
groups in a tenant
'''
from common import DEFAULT_CLOUD, get_default_az_credential, ManagementGroups

cred = get_default_az_credential(DEFAULT_CLOUD)

client = ManagementGroups(cred, DEFAULT_CLOUD).client

mgs = [page.as_dict() for page in client.management_groups.list()]
print(mgs)
