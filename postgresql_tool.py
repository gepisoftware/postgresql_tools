from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, List
import psycopg2

class PostgresQueryInput(BaseModel):
    query: str = Field(..., description="SQL query to run on PostgreSQL")

class PostgreSQLTool(BaseTool):
    name: str = "PostgreSQLTool"
    description: str = "Tool to run SQL queries on PostgreSQL"
    args_schema: PostgresQueryInput

    def _execute(self, query: str = None) -> List[dict]:
        # Conexión desde variables de env o config
        conn_str = self.get_tool_config("POSTGRES_CONNECTION")
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        cur.execute(query)
        rows = [dict(r) for r in cur.fetchall()]
        cur.close()
        conn.close()
        return rows
