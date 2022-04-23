'''
Example of using the ManagementGroupsAPI class to list management
groups in a tenant
'''
from common import get_default_az_credential, ManagementGroups

cred = get_default_az_credential()

client = ManagementGroups(cred).client

mgs = [page.as_dict() for page in client.management_groups.list()]
print(mgs)
