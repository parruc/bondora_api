import os
import json
import datetime

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

OAUTH_CONFIG_FILE = "oauth2.json"
PARAMS_TO_CLEAN = ["request_next_payment_date_from",
                   "request_next_payment_date_to"]

def get_config_file_path(file_name):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, "config", file_name)


def load_config_file(file_name):
    """Reads configuration from 'file_path' file
    """
    file_path = get_config_file_path(file_name)
    with open(file_path) as config_file:
        return json.load(config_file)


def clean_params(params):
    for param in PARAMS_TO_CLEAN:
        if param in params:
            del(params[param])


def save_config_file(params, file_name):
    """Save last working params to 'file_path' file
    """
    clean_params(params)
    file_path = get_config_file_path(file_name)
    with open(file_path, "w") as out_file:
        json.dump(params, out_file, sort_keys=True, indent=4)


def add_next_payment_day_filters(params):
    if "min_days_till_next_payment" in params:
        min_days = datetime.timedelta(params["min_days_till_next_payment"])
        future_date = datetime.datetime.today() + min_days
        params["request_next_payment_date_from"] = future_date.isoformat()
    if "max_days_till_next_payment" in params:
        max_days = datetime.timedelta(params["max_days_till_next_payment"])
        future_date = datetime.datetime.today() + max_days
        params["request_next_payment_date_to"] = future_date.isoformat()
    return params


def oauth2_get_token():
    """Get an oauth2 auth_token for the app to work. May need app approval
    """
    params = load_config_file(OAUTH_CONFIG_FILE)
    oauth = OAuth2Session(params["client_id"], scope=params["scope"])
    if "access_token" not in params:
        authorization_url, state = oauth.authorization_url(params["auth_url"])
        print('Please go to %s and authorize access.' % authorization_url)
        authorization_response = input('Paste the full redirect URL here:')
        token = oauth.fetch_token(
            params["token_url"],
            authorization_response=authorization_response,
            client_secret=params["client_secret"])
        params.update(token)
        save_config_file(params, OAUTH_CONFIG_FILE)

    return params["access_token"]
