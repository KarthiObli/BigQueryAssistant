import google.auth
from google.auth.transport.requests import Request
from langchain_mcp_adapters.client import MultiServerMCPClient


async def get_mcp_tools():

    credentials, project_id = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/bigquery"
        ]
    )

    credentials.refresh(Request())

    access_token = credentials.token

    client = MultiServerMCPClient(
        {
            "bigquery": {
                "transport": "streamable_http",
                "url": "https://bigquery.googleapis.com/mcp",
                "headers": {
                    "Authorization": f"Bearer {access_token}",
                    "x-goog-user-project": project_id,
                },
            }
        }
    )

    tools = await client.get_tools()

    return tools