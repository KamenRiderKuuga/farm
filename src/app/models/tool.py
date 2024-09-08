class Tool:
    def __init__(self, id=None, name=None):
        """
        初始化 Tool 对象。

        参数:
        id (int): 工具的唯一标识符。
        name (str): 工具的名称。
        """
        self._id = id
        self._name = name

    @property
    def id(self):
        """
        获取工具的唯一标识符。

        返回:
        int: 工具的唯一标识符。
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        设置工具的唯一标识符。

        参数:
        value (int): 新的工具唯一标识符。
        """
        self._id = value

    @property
    def name(self):
        """
        获取工具的名称。

        返回:
        str: 工具的名称。
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        设置工具的名称。

        参数:
        value (str): 新的工具名称。
        """
        self._name = value
