from firebase_functions import https_fn
from firebase_admin import initialize_app
from flask import Flask, request, jsonify
from helpers import parse_all_tools

initialize_app()

app = Flask(__name__)

db_token = ""

def create_endpoint(route, tool_class):
    @app.route(route, methods=['POST'], endpoint=tool_class.__name__)
    def endpoint():
        print(f"Endpoint {route} called")  # Debug print
        token = request.headers.get("Authorization").split("Bearer ")[1]
        if token != db_token:
            return jsonify({"message": "Unauthorized"}), 401

        try:
            tool = tool_class(**request.get_json())
            return jsonify({"response": tool.run()})
        except Exception as e:
            return jsonify({"Error": str(e)})

# create endpoints for each file in ./tools
tools = parse_all_tools()
print(f"Tools found: {tools}")  # Debug print

for tool in tools:
    route = f"/{tool.__name__}"
    print(f"Creating endpoint for {route}")  # Debug print
    create_endpoint(route, tool)

@https_fn.on_request(max_instances=1)
def tools_handler(req: https_fn.Request) -> https_fn.Response:
    print("tools_handler called")  # Debug print
    print(req.headers)  # Debug print
    try:
        token = req.headers.get("Authorization").split("Bearer ")[1]
    except Exception:
        return https_fn.Response("Unauthorized", status=401)
        
    if token != db_token:
        return https_fn.Response("Unauthorized", status=401)

    with app.request_context(req.environ):
        return app.full_dispatch_request()
