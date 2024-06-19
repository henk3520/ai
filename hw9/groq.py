#參考chatgpt
import os
import sys
from groq import Groq

# 獲取命令行參數作為問題
question = " ".join(sys.argv[1:])
print("問題：", question)

# 初始化 Groq 客戶端
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# 創建聊天補全
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama3-8b-8192",
)

# 輸出結果
print(chat_completion.choices[0].message.content)

