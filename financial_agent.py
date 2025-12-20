from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
import os

load_dotenv()

print("GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))

web_search_agent = Agent(
    name = "Web_Search_Agent",
    role = "Search the web for the information",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    information = ["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)

## Finance agent
Finance_agent = Agent(
    name="Finance AI Agent",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news= True),
    ],
    instructions=["use tables to display the data"],
    show_tools_calls= True,
    markdown = True,

)

multi_ai_agent = Agent(
    team=[web_search_agent,Finance_agent],
    instructions=['Always include sources',"use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("summarize analyst recommendation and share the latest news for 'NVDA",stream=True)

