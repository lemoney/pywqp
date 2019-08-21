from pywqp import pywqp_client
client_instance = pywqp_client.RESTClient()
from pprint import pprint


verb = 'get'
host_url = 'http://waterqualitydata.us'
resource_label = 'station'
params = {'countrycode': 'US', 'statecode': 'US:19', 'countycode': 'US:19:015', 'characteristicName': 'pH'}
result = client_instance.request_wqp_data(verb, host_url, resource_label, params, mime_type='text/csv')

pprint(result.text)
