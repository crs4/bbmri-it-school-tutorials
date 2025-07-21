import requests
import pprint
PDQ_SUPPLIER_BASE_URL = "https://gazelle.ihe.net/PatientManager/fhir"

def check_next_link(bundle_json):
    """
    Check if the bundle has a 'next' link and return it.
    """
    for link in bundle_json.get('link', []):
        if link.get('relation') == 'next':
            return link.get('url')
    return None


response = requests.get(f"{PDQ_SUPPLIER_BASE_URL}/Patient?family=Smith&_count=1",
          headers={"Accept": "application/fhir+json"})

if response.status_code == 200:
  bundle_json = response.json()
  pprint.pprint(f'Found {bundle_json}' )
  while check_next_link(bundle_json):
        next_link = check_next_link(bundle_json)
        if not next_link:
            break
        response = requests.get(next_link, headers={"Accept": "application/fhir+json"})
        if response.status_code != 200:
            print(f"Error fetching next page: {response.status_code}")
            break
        bundle_json = response.json()
        pprint.pprint(f'Found {bundle_json}')
