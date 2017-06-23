import json

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

CONFIG_FILE_PATH = "config/oauth2.json"


def load_config_file(file_path):
    """Reads configuration from 'file_path' file
    """
    with open(file_path) as config_file:
        return json.load(config_file)


def save_config_file(params, file_path):
    """Save last working params to 'file_path' file
    """
    with open(file_path, "w") as out_file:
        json.dump(params, out_file, sort_keys=True, indent=4)


def oauth2_get_token():
    """Get an oauth2 auth_token for the app to work. May need app approval
    """
    params = load_config_file(CONFIG_FILE_PATH)
    oauth = OAuth2Session(params["client_id"], scope=params["scope"])
    if "access_token" not in params:
        authorization_url, state = oauth.authorization_url(params["auth_url"])
        print 'Please go to %s and authorize access.' % authorization_url
        authorization_response = raw_input('Paste the full redirect URL here:')
        token = oauth.fetch_token(
            params["token_url"],
            authorization_response=authorization_response,
            client_secret=params["client_secret"])
        params.update(token)
        save_config_file(params, CONFIG_FILE_PATH)

    return params["access_token"]
