#!/usr/bin/env python
import argparse
import json
import logging
import math
from pprint import pprint

import bondora_api

from investhor.utils import load_config_file
from investhor.utils import oauth2_get_token
from investhor.utils import save_config_file
from investhor.utils import add_next_payment_day_filters
from investhor.utils import clean_params

# from bondora_api.rest import ApiException
CONFIG_FILE = "sell.json"


def get_cli_parser(defaults):
    """Creates a cli parser using argparse
    """
    parser = argparse.ArgumentParser(description='Bondora investing script')

    return parser


def get_params(config_file):
    """Gets the scripts params.
       Resolution order is cli -> .config file -> parser defaults
    """
    try:
        defaults = load_config_file(config_file)
    except Exception:
        defaults = {}
    parser = get_cli_parser(defaults)
    args = vars(parser.parse_args())
    defaults.update(args)
    return defaults


def calculate_selling_discount(interest, verification):
    """ Calculates the discount based on investment interest and risk
    """

    if interest > 100:
        discount = math.floor(interest/20)
    elif interest > 50:
        discount = math.floor(interest/15)
    else:
        discount = math.floor(interest/10)
    if verification:
        discount += 1
    return discount


def main():
    params = get_params(CONFIG_FILE)
    # Get only those that has next payment at least one month from now
    params = add_next_payment_day_filters(params)
    # Configure OAuth2 access token for authorization: oauth2
    # bondora_api.configuration.debug = True
    auth_token = oauth2_get_token()
    bondora_api.configuration.access_token = auth_token
    bondora_api.configuration.host = "https://api.bondora.com"
    # create an instance of the API class
    account_api = bondora_api.AccountApi()
    request_params = {k: params[k] for k in params if k.startswith("request_")}
    import pdb; pdb.set_trace()
    results = account_api.account_get_active(**request_params)
    pprint(results)
    clean_params(params)
    save_config_file(params, CONFIG_FILE)


if __name__ == "__main__":
    # execute only if run as a script
    main()
