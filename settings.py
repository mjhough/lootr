from pathlib import Path
from dotenv import load_dotenv

# Load env vars from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
