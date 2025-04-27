from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import BaseOutputParser


# --------- 自定义格式化输出类
class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        print(text)
        return text.strip().split(",")


# --------- 调用 LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)

prompt = PromptTemplate.from_template(
    "你是一个起名大师，请模仿示例起3个{county}名字，比如男孩经常被叫做{boy}，女孩经常被叫做{girl}"
)

message = prompt.format(county="中国特色的", boy="狗蛋", girl="翠花")
print(message)

llm.invoke(message)
