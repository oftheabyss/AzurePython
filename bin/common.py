'''
Contains example classes and functions for use with Microsoft Azure.
'''
from azure.identity import DefaultAzureCredential
from azure.mgmt.managementgroups import ManagementGroupsAPI
from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD, AZURE_US_GOV_CLOUD

CLOUDS = {
    'AzureCloud': {
        'cloud': AZURE_PUBLIC_CLOUD
    },
    'AzureUSGovernment': {
        'cloud': AZURE_US_GOV_CLOUD
    }
}

DEFAULT_CLOUD = 'AzureCloud'


class AzureClient():  # pylint: disable=too-few-public-methods
    '''
    Base class that sets the base_url and credential_scopes that are
    different between Azure Clouds, e.g. AzureCloud vs AzureUSGovernment

    Parameters
    ----------
    credential : azure.identity.DefaultAzureCredential (Default: None)
        A credential used for authentication

    authority : str (Default: AzureCloud)
        The Azure Cloud to use when authenticating and making requests

    NOTE:
        The base_url and credential_scopes in this class are what gets
        the Azure Python classes to work for non-standard Azure Clouds,
        e.g. AzureUSGovernment
    '''
    def __init__(self, credential: DefaultAzureCredential = None,
                 authority: str = DEFAULT_CLOUD):
        if credential is None:
            raise ValueError('A valid credential was not passed to the class')

        self.credential = credential
        self.authority = authority
        self.base_url = get_cloud_endpoints(self.authority).resource_manager
        self.credential_scopes = [f'{self.base_url}/.default']


class ManagementGroups(AzureClient):  # pylint: disable=too-few-public-methods
    '''
    Returns a client class for ManagementGroupsAPI

    Parameters
    ----------
    credential : azure.identity.DefaultAzureCredential (Default: None)
        A credential used for authentication

    authority : str (Default: AzureCloud)
        The Azure Cloud to use when authenticating and making requests
    '''
    def __init__(self, credential: DefaultAzureCredential = None,
                 authority: str = DEFAULT_CLOUD):
        super().__init__(credential, authority)
        self.client = ManagementGroupsAPI(
            self.credential, self.base_url,
            credential_scopes=self.credential_scopes
        )


def get_cloud_endpoints(cloud: str = DEFAULT_CLOUD):
    '''
    Returns a CloudEndpoints object for the specified Azure Cloud

    Parameters
    ----------
    cloud : str (Default: AzureCloud)
        The Azure Cloud to return endpoints for
    '''
    return CLOUDS[cloud]['cloud'].endpoints


def get_default_az_credential(cloud: str = DEFAULT_CLOUD):
    '''
    Returns a DefaultAzureCredential for use with most Azure SDK classes

    Parameters
    ----------
    cloud : str (Default: AzureCloud)
        The Azure Cloud to use for authentication
    '''
    return DefaultAzureCredential(
        authority=get_cloud_endpoints(cloud).active_directory
    )
