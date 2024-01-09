# LangChain
above project is simple LangChain based project which is using Langchain Libray. Where i'm using flask(Python framework) and simple html,css, javascript(js). simple description based project of LangChain. Also you have to add your openAi api key using 

import os

# Set your OpenAI API key here
openai_api_key = "your_api_key_here"

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = openai_api_key

or 

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(openai_api_key="...") 

or you can use this way. 

