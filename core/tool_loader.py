import os
import importlib


def load_tools():

    tools = {}

    tool_folder = "tools"


    for file in os.listdir(tool_folder):

        if file.endswith(".py") and file != "__init__.py":

            module_name = file[:-3]

            module = importlib.import_module(
                f"tools.{module_name}"
            )


            if hasattr(module, "tool_name") and hasattr(module, "run"):

                tools[module.tool_name] = module.run


    return tools