from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

#web search agent
web_search_agent=Agent(
    name="web search agent",
    role="search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["always include source"],
    show_tools_calls=True,
    markdown=True,
    
)

#financial agent

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True, 
    
)

multi_ai_agent= Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include source","Use table to dispaly the data"],
    show_tool_calls=True,
    markdown=True,
    
)

multi_ai_agent.print_response("summarize analyst recommendation and share the latest news on HDFC Bank ltd", stream=True)