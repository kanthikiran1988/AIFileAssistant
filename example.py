from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from file_assistant import FileAssistant
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    # Initialize the FileAssistant
    file_assistant = FileAssistant()
    
    # Get the tools using the new method
    tools = file_assistant.get_tools()
    
    # Initialize the language model
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # Create a prompt template with agent_scratchpad
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant that can help with file operations. "
                  "Use the available tools to help users manage their files and directories. "
                  "Be concise in your responses and focus on executing the requested file operations."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # Create the agent
    agent = create_openai_functions_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    print("\nWelcome to FileAssistant! Type 'exit' to quit.")
    print("Example commands:")
    print("- List all files in the current directory")
    print("- Create a new file called example.txt with content 'Hello!'")
    print("- Read the contents of requirements.txt")
    print("- Create a directory named 'data' and add a file in it\n")

    while True:
        user_input = input("\nWhat would you like me to do? > ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
            
        if user_input.strip():
            try:
                result = agent_executor.invoke({"input": user_input})
                print("\nResult:", result["output"])
            except Exception as e:
                print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main() 