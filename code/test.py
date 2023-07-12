# 导入 langchain 模块
import langchain

# 初始化 langchain 对象
lc = langchain.LLMChain()

# 定义问题
question = "Who is the president of the United States?"

# 调用函数，使用 "map_rerank" 类型的函数链，打印出更多的信息，使用 "Answer:" 作为提示语
answer, sources = lc.load_qa_with_sources_chain(question, chain_type="map_rerank", verbose=True, prompt="Answer:")

# 打印答案和信息来源
print(answer)
print(sources)