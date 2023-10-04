import requests
import uuid


def stk_push():
    token = get_token()
    url = "https://openapi.airtel.africa/merchant/v1/payments/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "X-Country": "KE",
        "X-Currency": "KES",
        "Authorization": f"Bearer {token}",
    }
    body = {
        "reference": "Insuarance payment",
        "subscriber": {"country": "KE", "currency": "KES", "msisdn": 101636327},
        "transaction": {
            "amount": 10,
            "country": "KE",
            "currency": "KES",
            "id": str(uuid.uuid4())[0:16],
        },
    }
    params = {}
    response = requests.post(url=url, headers=headers, json=body, params=params)
    return response


def get_token():
    url = "https://openapi.airtel.africa/auth/oauth2/token"
    payload = {
        "client_id": "5394abba-dbe1-4cb6-9683-37a83bb8028e",
        "client_secret": "381fa952-4348-4e88-bf5b-8d9839e78de2",
        "grant_type": "client_credentials",
    }
    headers = {"Content-Type": "application/json", "Accept": "*/*"}
    response = requests.request("POST", url, headers=headers, json=payload)
    payload = response.json()
    access_token = payload.get("access_token")
    return access_token

def process_stk_push_response(response):
    if response.status_code == 200:
        data = response.json()
        transaction_id = data.get("transactions", {}).get("id")
        response_code = data.get('status', {}).get('response_code')
        if response_code == 'DP00800001006':
            return get_status_of_previous_transaction(transaction_id)
    return {}

def get_status_of_previous_transaction(transaction_id):
    print(transaction_id)
    token = get_token()
    url = f"https://openapi.airtel.africa/standard/v1/payments/{transaction_id}"
    headers ={
        "Accept": "*/*",
        "X-Country": "KE",
        "X-Currency": "KES",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(url=url, headers=headers)
    return response

    