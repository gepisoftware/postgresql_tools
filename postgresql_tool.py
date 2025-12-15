from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List
import psycopg2
import psycopg2.extras

class PostgresQueryInput(BaseModel):
    query: str = Field(..., description="SQL query to run on PostgreSQL")

class PostgreSQLTool(BaseTool):
    name: str = "PostgreSQL Tool"
    description: str = "Tool to run SQL queries on PostgreSQL"
    args_schema: Type[BaseModel] = PostgresQueryInput

    def _execute(self, query: str):
        # Obtener la conexión desde variables de entorno o config
        conn_str = self.get_tool_config("POSTGRES_CONNECTION")
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
