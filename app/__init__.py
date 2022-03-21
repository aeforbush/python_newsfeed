from fcntl import F_SEAL_SEAL
# use from..import statement to import Flask()
from flask import Flask 

# def defines create_app() || code block defined by indenting by 2 spaces
def create_app(test_config=None):
    # set up app config
    # The app should serve any static resources from the root directory and not from the default /static directory
    app = Flask(__name__, static_url_path='/')
    # Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route)
    app.url_map.strict_slashes = False
    # The app should use the key called 'super_secret_key' when creating server-side sessions.
    app.config.from_mapping(
        SECRET_KEY ='super_secret_key'
    )

    return app