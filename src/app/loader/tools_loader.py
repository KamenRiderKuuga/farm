import os
import json
from app.models.category import Category
from app.models.tool import Tool
from typing import List


def load_tools(tools_directory="src/app/templates/tools") -> List[Category]:
    tools = []
    all_categories = os.listdir(tools_directory)
    all_categories.sort()
    start_category_number = 1
    for category in all_categories:
        category_info = Category()
        category_path = os.path.join(tools_directory, category)
        category_meta_path = os.path.join(category_path, "meta.json")
        if not os.path.exists(category_meta_path):
            # print error and exit the program
            print(f"Category {category} does not have meta.json file.")
            exit(1)
        category_prefix = str(start_category_number).zfill(3) + "_"
        category_info.id = category.removeprefix(category_prefix)
        category_info.path = category
        if not category.startswith(category_prefix):
            # print error and exit the program
            print(f"Category {category} is not in the correct format.")
            exit(1)
        with open(category_meta_path, "r", encoding="utf-8") as f:
            category_meta = json.load(f)
            category_name = category_meta["name"]
            category_info.name = category_name
            tool_map = category_meta["tools"]
            for tool in tool_map:
                name = tool_map[tool]
                tool_info = Tool(tool, name)
                category_info.tools.append(tool_info)

        tools.append(category_info)
        start_category_number += 1

    for category in tools:
        print(f"Category: {category.name}")
        print(f"Category ID: {category.id}")
        print(f"Category Path: {category.path}")
        for tool in category.tools:
            print(f"  Tool: {tool.name}")
            print(f"  Tool ID: {tool.id}")
    return tools
