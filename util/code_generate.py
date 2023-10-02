import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("Typing Extensions")

# Initialize state variables
problem_description = ""
solution_code = ""

# Function to generate solution python code based on the problem description
def pythonCodeGenerator(problem_description):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
        openai_api_key = "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"
        # put your api here
    )
    system_template = """You are an AI assistant tasked with generating a solution code in Python based on the given problem description."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please write a Python code to solve the following problem:

{problem_description}"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(problem_description=problem_description)
    return result # returns string

# Function to display the generated solution python code to the user
def display_solution_code(solution_code):
    st.markdown("## Generated Solution Code")
    st.code(solution_code)

# Get the problem description from the user
problem_description = st.text_area("Problem Description")

# Put a submit button with an appropriate title
if st.button("Generate Solution"):
    # Call the function to generate solution code if problem description is provided
    if problem_description:
        solution_code = pythonCodeGenerator(problem_description)
        # Call the function to display the solution code if solution code is generated
        if solution_code:
            display_solution_code(solution_code)