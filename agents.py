from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv
load_dotenv()
 
 
GROK_API_KEY = os.getenv("GROK_API_KEY")
 
llm = ChatGroq(
    api_key=GROK_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)
 
 
def build_search_agent():
     return create_agent(
         model=llm,
         tools=[web_search]
     )
     
def build_scrape_agent():
     return create_agent(
         model=llm,
         tools=[scrape_url]
     )
     
writer_prompt = ChatPromptTemplate.from_messages([
    ('system','You are an expert research writer. write clear, structured and insightful reports'),
    ('human',"""write a detailed research report on the topic below.
    
Topic: {topic}

Research Gathered: {research}

Structure the report as:
    -Intoduction
    -Key Findings (minimum 3 well-explained points)
    -Conclusion
    -Sources (list of all URLs found in the research)
    
    Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
    ('system','you are a sharp and constructive research critic. be honest and specific'),
    ('human',"""review the research report below and evaluate it strictly.
     
     Report: {report}
     
     Respond in this exact format:
     
     Score: X/10
     
     Strengths:
     - ...
     - ...
    
    
    Areas for Improvement:
    - ...
    - ...
    
    One line Verdict: ...
""")
])

critic_chain = critic_prompt | llm | StrOutputParser()
