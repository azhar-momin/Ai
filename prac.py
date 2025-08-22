import getpass
import os

from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv()



# if not os.environ.get("GROQ_API_KEY"):
#   os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")/
api_key=os.getenv("GROQ_API_KEY")


model = init_chat_model("llama3-8b-8192", model_provider="groq")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("you give Ai related advice"),
    HumanMessage("give information about latest trends in Ai in one line"),
]

response = model.invoke(messages)

print(response.content)