"""
Agent  = LLM  + Prompt + Tools 
"""
import os

from dotenv import load_dotenv
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

load_dotenv()

# print(os.getenv("DATABASE_URL"))
db = SQLDatabase.from_uri(os.getenv("DATABASE_URL"))


# print(db.dialect)
# print(db.get_usable_table_names())
# print(db.run("SELECT * FROM emp LIMIT 10;"))


class SQLAgent:
    def __init__(self, openai_model_name="gpt-3.5-turbo-0125"):
        self.db = db
        self.llm = ChatOpenAI(model=openai_model_name, temperature=0.5)
        self.agent = self._agent()

    def _agent(self):
        agent_executor = create_sql_agent(
            self.llm, db=db, agent_type="openai-tools", verbose=True)
        return agent_executor

    def run(self, query):
        return self.agent.run(query)
