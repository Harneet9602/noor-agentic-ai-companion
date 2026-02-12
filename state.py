import operator
from typing import Annotated,List, TypedDict
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    #'messages' tracks the conversation history.
    #operator.add tells Langgraph to append new msgs. not overwrite them.
    messages: Annotated[list[BaseMessage],operator.add]
    # 'next' tells the graph which agent acts next
    next: str
    #dynamic name field
    user_name: str
