# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_admin import initialize_app
from firebase_functions import https_fn

from tools import MyCustomTool

initialize_app()

db_token = ""


@https_fn.on_request()
def my_custom_tool(req: https_fn.Request):
    token = req.headers.get("Authorization").split("Bearer ")[1]
    if token != db_token:
        return https_fn.Response("Unauthorized", status=401)

    try:
        tool = MyCustomTool(**req.get_json())

        return {
            "response": tool.run(),
        }
    except Exception as e:
        return {
            "Error": str(e)
        }
