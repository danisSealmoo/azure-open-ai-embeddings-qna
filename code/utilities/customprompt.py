# flake8: noqa
from langchain.prompts import PromptTemplate

# template = """{summaries}
# Please reply to the question using only the information present in the text above. 
# Include references to the sources you used to create the answer if those are relevant ("SOURCES"). 
# If you can't find it, reply politely that the information is not in the knowledge base.
# Question: {question}
# Answer:"""

template = """
只使用下面Summarie的内容回答问题，不能发散。如果Summaries没有内容或者内容不适用，则礼貌的回答该信息不在知识库中。如果内容适用，包括对用于创建答案的来源的引用（"来源"）。使用用户提问的语言回复。
Summaries: "{summaries}"........
Question: "{question}"........
Answer:
Tags:[]"""

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)


