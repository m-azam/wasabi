import msal
import requests

msalCca = msal.ConfidentialClientApplication( "4b99bffa-0a45-4f7e-bcd6-d3712ec471fb", 
    authority="https://login.microsoftonline.com/" + "1c5ffd4f-6cec-4ad2-954f-5e7eedb10095",
    client_credential="wuD7Q~O7X-S2M7TJQHdKfrcUGjQV84_OWveC0",
    )

accessToken = ""
result = msalCca.acquire_token_for_client( scopes="bbb94529-53a3-4be5-a069-7eaf2712b826/.default" )
if "access_token" in result:
    accessToken = result['access_token']

