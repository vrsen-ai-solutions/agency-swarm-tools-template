from agency_swarm.tools import BaseTool
from pydantic import Field

class MyCustomTool(BaseTool):
    """
    A brief description of what the custom tool does.
    The docstring should clearly explain the tool's purpose and functionality.
    """
    # Define the fields with descriptions using Pydantic Field
    example_field: str = Field(
        ..., description="Description of the example field, explaining its purpose and usage."
    )

    # Additional fields as required
    # ...

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform its task.
        Doc string description is not required for this method.
        """

        # Your custom tool logic goes here
        # do_something(self.example_field)

        # Return the result of the tool's operation
        return "Result of MyCustomTool operation"


if __name__ == "__main__":
    # Create an instance of the custom tool
    my_tool = MyCustomTool(example_field="example_value")

    # Test the tool
    result = my_tool.run()
    print(result)