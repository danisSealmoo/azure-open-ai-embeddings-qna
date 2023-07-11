# flake8: noqa
from langchain.prompts import PromptTemplate

template = """{summaries}
请只使用summaries提供的信息回答问题。如果适用，包括对用于创建答案的来源的引用（"来源"）。如果在summaries中找不到信息，请礼貌地回复该信息不在知识库中。使用用户提问的语言回复。
Question: {question}
Answer:
Tags:[]"""

# template = """{summaries}
# Please reply to the question using only the information present in the text above. 
# Include references to the sources you used to create the answer if those are relevant ("SOURCES"). 
# If you can't find it, reply politely that the information is not in the knowledge base.
# Question: {question}
# Answer:"""

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)


