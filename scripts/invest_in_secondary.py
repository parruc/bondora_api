#!/usr/bin/env python
import argparse
import datetime
import json
import logging
from pprint import pprint

import bondora_api
from utils import load_config_file
from utils import oauth2_get_token
from utils import save_config_file

# from bondora_api.rest import ApiException
CONFIG_FILE_PATH = "config/secondary.json"


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


def get_params():
    """Gets the scripts params.
       Resolution order is cli -> .config file -> parser defaults
    """
    try:
        defaults = load_config_file(CONFIG_FILE_PATH)
    except Exception:
        defaults = {}
    parser = get_cli_parser(defaults)
    args = parser.parse_args()
    return vars(args)


def main():
    params = get_params()
    # Get only those that has next payment at least one month from now
    next_30_days = datetime.datetime.today() + datetime.timedelta(30)
    params["request_next_payment_date_from"] = next_30_days.isoformat()
    # Configure OAuth2 access token for authorization: oauth2
    # bondora_api.configuration.debug = True
    auth_token = oauth2_get_token()
    bondora_api.configuration.access_token = auth_token
    bondora_api.configuration.host = "https://api.bondora.com"
    # create an instance of the API class
    secondary_api = bondora_api.SecondMarketApi()
    results = secondary_api.second_market_get_active(**params)
    pprint(results)
    save_config_file(params, CONFIG_FILE_PATH)


if __name__ == "__main__":
    # execute only if run as a script
    main()
