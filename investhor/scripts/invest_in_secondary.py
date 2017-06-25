#!/usr/bin/env python
import argparse
import json
import logging
from pprint import pprint

import bondora_api
from investhor.utils import load_config_file
from investhor.utils import oauth2_get_token
from investhor.utils import save_config_file
from investhor.utils import add_next_payment_day_filters
from investhor.utils import clean_params

# from bondora_api.rest import ApiException
CONFIG_FILE = "secondary.json"


def get_cli_parser(defaults):
    """Creates a cli parser using argparse
    """
    parser = argparse.ArgumentParser(description='Bondora investing script')

    parser.add_argument('--request_has_debt', action='store_true',
                        help='Select users with overdue debts',
                        default=defaults.get("request_has_debt", False),)
    parser.add_argument('--request_interest_min',
                        help='Minimum interest required',
                        default=defaults.get("request_interest_min", 190),
                        required=False)
    parser.add_argument('--request_desired_discount_rate_max',
                        help='Maximum discount rate',
                        default=defaults.get("request_desired_discount_rate_max", 21),
                        required=False)
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
    secondary_api = bondora_api.SecondMarketApi()
    request_params = {k: params[k] for k in params if k.startswith("request_")}
    results = secondary_api.second_market_get_active(**request_params)
    pprint(results)
    clean_params(params)
    save_config_file(params, CONFIG_FILE)


if __name__ == "__main__":
    # execute only if run as a script
    main()
