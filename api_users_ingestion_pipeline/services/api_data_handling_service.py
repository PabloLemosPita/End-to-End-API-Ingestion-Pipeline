import json
import requests

def request_randomuser_from_api(): 
    response = requests.get("https://randomuser.me/api/?results=1&nat=br")
    response.raise_for_status()
    json_from_response = response.json()
    return json_from_response

def get_name_from_response_json(response_json):
    try:
        name = response_json['results'][0]['name']['first']
        return name
    except:
        return None

def get_last_name_from_response_json(response_json):
    try:
        last_name = response_json['results'][0]['name']['last']
        return last_name
    except:
        return None

def get_email_from_response_json(response_json):
    try:
        email = response_json['results'][0]['email']
        return email
    except:
        return None
    
def get_cell_from_response_json(response_json):
    try:
        cell = response_json['results'][0]['cell']
        return cell
    except:
        return None
    
def get_user_id_type_from_response_json(response_json):
    try:
        user_id_type = response_json['results'][0]['id']['name']
        return user_id_type
    except:
        return None
    
def get_user_id_value_from_results(response_json):
    try:
        user_id_value = response_json['results'][0]['id']['value']
        return user_id_value
    except:
        return None

def get_dob_from_response_json(response_json):
    try:
        dob = response_json['results'][0]['dob']['date']
        return dob
    except:
        return None

def get_location_country_from_response_json(response_json):
    try:
        country = response_json['results'][0]['location']['country']
        return country
    except:
        return None
    
def get_location_state_from_response_json(response_json):
    try:
        state = response_json['results'][0]['location']['state']
        return state
    except:
        return None
    
def get_location_city_from_response_json(response_json):
    try:
        city = response_json['results'][0]['location']['city']
        return city
    except:
        return None
    
def get_location_street_name_from_response_json(response_json):
    try:
        street_name = response_json['results'][0]['location']['street']['name']
        return street_name
    except:
        return None
    
def get_location_street_number_from_response_json(response_json):
    try:
        location_number = response_json['results'][0]['location']['street']['number']
        return location_number
    except:
        return None
    
def get_location_postcode_from_response_json(response_json):
    try:
        postcode = response_json['results'][0]['location']['postcode']
        return postcode
    except:
        return None


