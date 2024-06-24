from flask import Flask, request, jsonify

app = Flask(__name__)

# 词性标注示例函数
def pos_tagging(text):
    # 这里你可以调用实际的词性标注模型或API
    # 这是一个简单的示例返回
    return [{"word": word, "pos": "NOUN"} for word in text.split()]

@app.route('/api/pos_tag', methods=['POST'])
def pos_tag():
    data = request.get_json()
    text = data.get('text', '')
    result = pos_tagging(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
