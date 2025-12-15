from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from postgresql_tool import PostgreSQLTool


class PostgreSQLToolkit(BaseToolkit, ABC):
    name: str = "PostgreSQL Toolkit"
    description: str = "Toolkit to interact with an external PostgreSQL database"

    def get_tools(self) -> List[BaseTool]:
        return [PostgreSQLTool(connection_string="postgresql://user:password@host:port/dbname")]

    def get_env_keys(self) -> List[str]:
        # Si tu herramienta necesita variables de entorno, aquí se listan
        return []
