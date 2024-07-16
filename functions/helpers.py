import os
from agency_swarm.tools import ToolFactory

def parse_all_tools():
    tools_folder = './tools'
    tools = []
    for filename in os.listdir(tools_folder):
        if filename.endswith('.py'):
            tool_path = os.path.join(tools_folder, filename)
            tool_class = ToolFactory.from_file(tool_path)
            tools.append(tool_class)
    return tools