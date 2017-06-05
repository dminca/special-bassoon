#!/usr/bin/env python3
import requests

API_URL = 'http://localhost:8080/v2-beta'
payload = requests.get(API_URL)
apikeys_url = payload.json()['links']['apiKeys']

# print apikeys commands
requests.get(apikeys_url).json()

# create admin account with API Key
def create_account(role, description, acc_id, public_key, private_key):
    """Create an account with API Keys

    Create an admin account and generate API Keys for it.
    Returns a dict() of account data
    """
    data = {
            'accountId': role,
            'description': description,
            'name': acc_id,
            'publicValue': public_key,
            'secretValue': private_key }


    req = requests.post(apikeys_url, data)

    if req.status_code == 201:
        print(req.json())
    else:
        print("{} {}".format(req.status_code, 'ERROR'))


def main():
    pass

if __name__ == '__main__':
    main()

# vim: fdm=indent: tw=79
