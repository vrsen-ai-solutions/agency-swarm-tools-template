from helpers import parse_all_tools
from agency_swarm.tools import ToolFactory


if __name__ == '__main__':
    tools = parse_all_tools()

    print(ToolFactory.get_openapi_schema(tools, 'your_function_url'))