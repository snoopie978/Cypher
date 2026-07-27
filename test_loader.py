from core.tool_loader import load_tools


tools = load_tools()


print(tools)


tools["test"]()