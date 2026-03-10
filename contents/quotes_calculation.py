from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from datetime import datetime
import requests

# Date: 202509009
# Modified: 20260310

# This script will generate a PowerPoint (pptx) presentation for Energia Insurance.
# The goal is to generate a PowerPoint presentation with insurance quote information from the insurance company.
# The insurance company quote information is to be accessed with the insurance company API.

keyfile = "keys.txt"

with open(keyfile, 'r') as file:
    lines = file.readlines()

# Access the two lines from the list
try:
    if len(lines) >= 2:
        line1 = lines[0].strip() # Use strip() to remove leading/trailing whitespace, including \n
        line2 = lines[1].strip()
        CLIENT_ID = line1
        CLIENT_SECRET = line2
    else:
        print("One or more keys are missing.")
except:
    print(f"The '{keyfile}' is missing the keys.")


AP_URL = 'https://uat-api.tugo.com'

def get_access_token():
    # API endpoint url for access token
    token_endpoint_url = AP_URL + '/v1/venture/accessToken'

    # API parameters
    access_token_params = {
        'grant_type' : 'password',
        'user_name' : 'ENE000',
        'password' : 'Test1234!',
        'client_id' : CLIENT_ID,
        'client_secret' : CLIENT_SECRET
    }

    headers = {
        'content-type' : 'application/x-www-form-urlencoded',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0'
    }

    session = requests.Session()
    token_response = session.post(token_endpoint_url, data=access_token_params, headers=headers)

    if token_response.status_code == 200:
        return token_response.json()['accessToken']
    else:
        raise Exception(f'{token_response.status_code} Could not get access token\n{token_response.reason}\n{token_response.content}')

def get_quote(coverage_level, access_token, client=None):
    """
    Returns quotes price for the following plan paramteres:
    - VISITOR
    - PR-VIS-1 (Product Line Code)
    - PL-SMED-21 (Plan Code for 'Visitors to Canada Medical' Plan)
    - Assumes 'YES' answer for QU-VEQ-4 questionnaire (need to find out what is answering)
    """
    # endpoint url of travel insurance API
    quotes_endpoint_url = AP_URL + '/v1/venture/quotes/price'

    # get all insured people on trip
    insured_persons = []
    for person_num in range(1,client["num_travellers"]+1):
        person_obj = {
            'insuredType' : 'VISITOR',
            'birthDate' : client[f"dob_{person_num}"],
            'questionnaires':[
                {
                    'code':'QU-VEQ-4',
                    'questions':[
                        {
                            'code':'QT-VIS-2', # Question for visitors (not sure what is, need to find out)
                            # answers are likely 2 options (YES/NO), a1 is YES, a2 is NO (if set -> ineligible)
                            'answers':[
                                {
                                    'code':'q1a1', # YES (just know must be set to YES / 1 to be eligible for plan)
                                    'value':1
                                }
                            ]
                        }
                    ]
                }
            ],
            'plansToPrice' : [
                {
                'planCode' : 'PL-SMED-21', # code for 'Visitors to Canada Medical' plan
                'priceInputParameters' : [
                        {
                            'code' : 'SUMM', # code to set coverage level
                            'value' : coverage_level # coverage value (e.g., 10k, 25k, 50k, 100k, 200k, 300k, 500k)
                        }
                    ]
                }
            ]
        }
        # append to list
        insured_persons.append(person_obj)

    # quotes request parameters dictionary
    # reformatting dates

    quotes_params = {
        'partnerCode' : 'ENE000',
        'productLineCode' : 'PR-VIS-1', # visitor product line (visitors to Canada)
        'insuredType' : 'VISITOR',
        'trip' : {
            'startDate' : client["trip_start"], #when trip starts (note: insurance only starts at destination)
            'endDate' : client["end"], #trip end date (i think is when come back to home)
            'bookingDate': client["submit"], #assuming request submission date is booking date of trip
            'arrivalDate': client["dest_arrival"], #expected date of arrival at destination, is when insurance starts
            'destination': client["dest_region"]
            # 'departureProvince' : '' not mandatory for visitor type
        },
        'insuredPersons' : insured_persons
    }

    # API request header
    quotes_headers = {
        'content-type' : 'application/json',
        'X-Auth-API-Key' : CLIENT_ID,
        'Authorization' : f'Bearer {access_token}',
    }

    # API post request call to retrieve information
    quotes_response = requests.post(quotes_endpoint_url, json=quotes_params, headers=quotes_headers)
    
    # Checking response status and returning retrieved information
    if quotes_response.status_code == 200:
        response_json = quotes_response.json()
        if 'messages' in response_json:
            messages = response_json['messages']
            error_string = ""
            for message in messages:
                if message['key'] == 'sales.drl.error.rule.policy.ineligible.medical.questionnaire.require':
                    error_string += f"Client 60 or over. {message['detailMessage']}"
                if message['key'] == 'sales.drl.trip.arrivalDate.after.effectiveDate.2days':
                    error_string += f"Trip start date must be at most 2 days before the arrival date."
            raise Exception(f'{error_string, response_json}')
        else:
            return response_json
    else:
        raise Exception(f'{quotes_response} {quotes_response.reason}\n{quotes_response.content}')
    