import msal
import requests
import json


def issue_token_api(student_id):
    msalCca = msal.ConfidentialClientApplication( "4b99bffa-0a45-4f7e-bcd6-d3712ec471fb", 
        authority="https://login.microsoftonline.com/" + "1c5ffd4f-6cec-4ad2-954f-5e7eedb10095",
        client_credential="wuD7Q~O7X-S2M7TJQHdKfrcUGjQV84_OWveC0",
        )

    accessToken = ""
    result = msalCca.acquire_token_for_client( scopes="bbb94529-53a3-4be5-a069-7eaf2712b826/.default" )
    if "access_token" in result:
        accessToken = result['access_token']

    request_file = open("/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/issuance_request_config.json")

    issuance_request = json.load(request_file)

    issuance_request["issuance"]["claims"]["studentId"] = student_id

    post_headers = { "content-type": "application/json", "Authorization": "Bearer " + accessToken }

    client_api_request_endpoint = "https://beta.did.msidentity.com/v1.0/" + "1c5ffd4f-6cec-4ad2-954f-5e7eedb10095" + "/verifiablecredentials/request"

    response = requests.post( client_api_request_endpoint, headers=post_headers, data=json.dumps(issuance_request))

    return response.json()
