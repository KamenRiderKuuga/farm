from flask import Blueprint, render_template, request

bp = Blueprint('toolbox', __name__)


# 示例数据
categories = [
    {"id": 1, "name": "开发工具"},
    {"id": 2, "name": "编解码"},
    {"id": 3, "name": "业务工具"}
]

tools = {
    1: [
        {"id": "dev_tool_1", "name": "工具1", "subtools": [{"id": "subtool_1", "name": "子工具1"}]},
        {"id": "dev_tool_2", "name": "工具2", "subtools": [{"id": "subtool_2", "name": "子工具1"}]}
    ],
    2: [
        {"id": "codec_tool_1", "name": "工具1", "subtools": [{"id": "subtool_3", "name": "子工具3"}]},
        {"id": "codec_tool_2", "name": "工具2", "subtools": [{"id": "subtool_4", "name": "子工具4"}]}
    ],
    3: [
        {"id": "biz_tool_1", "name": "工具1", "subtools": [{"id": "subtool_5", "name": "子工具5"}]},
        {"id": "biz_tool_2", "name": "工具2", "subtools": [{"id": "subtool_6", "name": "子工具6"}]}
    ]
}

@bp.route('/toolbox')
@bp.route('/')
def index():
    return render_template("toolbox.html")

@bp.route('/toolbox/<int:category_id>')
def tool_page(category_id):
    category = next((cat for cat in categories if cat["id"] == category_id), None)
    if category:
        category_tools = tools.get(category_id, [])
        print(category_tools)
        return render_template("tool_page.html", category=category, tools=category_tools, categories=categories)
    else:
        return "Category not found", 404