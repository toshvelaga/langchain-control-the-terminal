from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI
from langchain.agents import load_tools
from langchain.utilities import BashProcess

bash = BashProcess()

agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000),
    tool=PythonREPLTool(),
    verbose=True
)

agent_executor.run("""You have access to the terminal through the bash variable. Open the browser, go to youtube and search for Lex Fridman. Then write the text contents from the page into a file called page.txt""")