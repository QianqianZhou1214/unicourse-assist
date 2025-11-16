import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

class LLMClient:
  """
  encapsulates interactions with the OpenAI API. It
  manages:
  - Function calling
  - System and user messages
  - temperature settings
  - model selection
  """

  def __init__(self, model="gpt-4-0613", temperature=0.2):
    self.model = model
    self.temperature = temperature
  
  def chat(self, messages, functions=None):
    """
    messages: list of dicts with role and content
    functions: list of function definitions for function calling
    """
    