from superagi.tools.base_tool import BaseToolkit
from typing import List

from .postgresql_tool import PostgreSQLTool

class PostgresToolkit(BaseToolkit):
    name: str = "postgresql_toolkit"
    description: str = "Toolkit para consultar PostgreSQL"

    def get_tools(self) -> List[PostgreSQLTool]:
        return [PostgreSQLTool()]

    def get_env_keys(self) -> List[str]:
        return ["POSTGRES_CONNECTION"]
