from openai import OpenAI

# 1. 填入你的 API Key
client = OpenAI(
    api_key="YOUR_API_KEY_HERE", 
    base_url="https://api.deepseek.com"
)

def cognitive_diagnostic_tool():
    print("--- 🤖 认知诊断助手已就绪 ---")
    print("请输入学生的观点，我将为您分析其逻辑前提与潜在盲点。")
    
    user_input = input("\n学生观点：")

    # 2. 纯学术化的引导逻辑
    system_prompt = """
    你是一位严谨的认知诊断专家。
    针对用户的论述，请提供3个深度的逻辑追问：
    1. 挖掘其论述中跳过的逻辑前提。
    2. 要求其对核心概念进行界定。
    3. 指出其观点可能存在的逻辑不一致性。
    请保持语气专业、中立，不直接提供答案，只提供启发性问题。
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ]
        )
        print("\n--- 💡 诊断性追问 ---")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\n❌ 连接失败: {e}")

if __name__ == "__main__":
    cognitive_diagnostic_tool()