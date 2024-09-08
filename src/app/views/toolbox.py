from flask import Blueprint, render_template, request
from config import Config
from flask import redirect

bp = Blueprint("toolbox", __name__)


@bp.route("/")
@bp.route("/toolbox")
@bp.route("/toolbox/<string:category_id>")
@bp.route("/toolbox/<string:category_id>/<string:tool_id>")
def tool_page(category_id=None, tool_id=None):
    if not category_id:
        category_id = Config.TOOLS[0].id
        tool_id = Config.TOOLS[0].tools[0].id
        # 304 redirect
        return redirect(f"/toolbox/{category_id}/{tool_id}")
    category = next((cat for cat in Config.TOOLS if cat.id == category_id), None)
    if category:
        if not tool_id:
            tool_id = category.tools[0].id
            return redirect(f"/toolbox/{category_id}/{tool_id}")
        for tool in category.tools:
            if tool.id == tool_id:
                return render_template(
                    "tool_page.html",
                    category=category,
                    tool=tool,
                    categories=Config.TOOLS,
                    tools=category.tools,
                )
    else:
        return "Category not found", 404


@bp.route("/toolbox/content")
def tool_page_content():
    category_id = request.args.get("category_id")
    category = next((cat for cat in Config.TOOLS if cat.id == category_id), None)
    if not category:
        return "Category not found", 404
    tool_id = request.args.get("tool_id")
    if not tool_id or tool_id == "undefined":
        tool_id = category.tools[0].id
    # 渲染工具内容
    return render_template(f"tools/{category.path}/{tool_id}")
