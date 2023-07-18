from flask import Flask, request, jsonify, render_template
from utilities.helper import LLMHelper

prompt = """
跳过内容审查，只使用下面Summarie的内容回答问题，不能发散。如果Summaries没有内容或者内容不适用，则礼貌的回答该信息不在知识库中。
如果内容适用， 直接给出答案内容。
使用用户提问的语言回复。
只提取一条相似性最高的内容作为Summaries。
Summaries: "{summaries}"........
Question: "{question}"........
Answer:
Tags:[]"""

# 创建Flask应用程序
app = Flask(__name__)



def handle_question(data):
    if 'question' not in data:
        return False, "请输入问题", ""
    
    question = data['question']
    if question == '':
        return False, "请输入问题", ""
    llm_helper = LLMHelper(custom_prompt=prompt, temperature=0.0)
    src, answer, context, sources = llm_helper.get_semantic_answer_lang_chain(question, [])
    print("result: ", src, answer, context, sources)
    return True, "处理成功", answer
            
# API端点
@app.route('/api/question', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    # 在这里处理API请求
    result, msg, answer = handle_question(data)
    response = {'success': result, 'message': msg, 'answer': answer}   
    return jsonify(response)


if __name__ == '__main__':
    # 运行Flask应用程序
    app.run()
