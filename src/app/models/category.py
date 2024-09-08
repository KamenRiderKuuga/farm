from .tool import Tool
from typing import List


class Category:
    def __init__(self, id=None, name=None, path=None):
        """
        初始化 Category 对象。

        参数:
        id (int): 类别的唯一标识符。
        name (str): 类别的名称。
        """
        self._id = id
        self._name = name
        self._path = path
        self._tools: List[Tool] = []

    @property
    def id(self):
        """
        获取类别的唯一标识符。

        返回:
        int: 类别的唯一标识符。
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        设置类别的唯一标识符。

        参数:
        value (int): 新的类别唯一标识符。
        """
        self._id = value

    @property
    def name(self):
        """
        获取类别的名称。

        返回:
        str: 类别的名称。
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        设置类别的名称。

        参数:
        value (str): 新的类别名称。
        """
        self._name = value

    @property
    def path(self):
        """
        获取类别的真实路径。

        返回:
        str: 类别的真实路径。
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        设置类别的真实路径。

        参数:
        value (str): 新的类别真实路径。
        """
        self._path = value
        
    @property
    def tools(self) -> List[Tool]:
        """
        获取类别中的工具列表。

        返回:
        list: 工具对象的列表。
        """
        return self._tools
