from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

version = "1.0.1"
input_data = {
    "role": input("Who are you? \n"),
    "setting": input("Where does the story take place? \n"),
    "objective": input("What do you wish to  achieve? \n"),
    "ally": input("Who is your ally? \n")
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@sambhav/ridonkulous-realms/{version}"
else:
    flow_name = "@sambhav/ridonkulous-realms"

result = client.flow.execute(flow_name, input_data)
print("\n\n")
print(result["result"])