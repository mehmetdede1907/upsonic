import os
from dotenv import load_dotenv

load_dotenv()

class GoogleSearchMCP:
    command = "node"
    args = [os.path.join(os.getcwd(), "google-search-mcp", "dist", "index.js")]
    env = {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY", ""),
        "GOOGLE_CSE_ID": os.getenv("GOOGLE_CSE_ID", "")
    }