import requests

apikey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJFLUVFaEtfSkxGckdtcDdDUmlCcE03LWY3bldDakZxSVV3YXdEM1FCbS1ZIiwiaWF0IjoxNzU2NTI3OTQ4fQ.JSlweOlbpsW9fmVEZ3iqIMMlUFo76S_iGDrRVnX7HrY"

trains_url = 'https://api.transport.nsw.gov.au/v2/gtfs/vehiclepos/sydneytrains'
buses_url = 'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/buses'
headers = {
    'accept': 'application/x-google-protobuf',
    'Authorization': 'apikey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJFLUVFaEtfSkxGckdtcDdDUmlCcE03LWY3bldDakZxSVV3YXdEM1FCbS1ZIiwiaWF0IjoxNzU2NTI3OTQ4fQ.JSlweOlbpsW9fmVEZ3iqIMMlUFo76S_iGDrRVnX7HrY',
}

params = {
    'debug': 'true',
}

trains_response = requests.get(trains_url, params=params, headers=headers)
buses_response = requests.get(buses_url, params=params, headers=headers)
trains_file = open("trains_response.txt", "w")
trains_file.write(trains_response.text)
trains_file.close()
buses_file = open("buses_response.txt", "w")
buses_file.write(buses_response.text)
buses_file.close()
