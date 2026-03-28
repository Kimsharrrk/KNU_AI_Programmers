from agent import get_chef_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

chef_agent = get_chef_agent(model)

print("  셰프가 냉장고를 스캔 중입니다... (잠시만 대기해주세요!)\n")

result = chef_agent.invoke({
    "input": "나 지금 냉장고에 계란 2개, 대파 조금, 먹다 남은 스팸 반 통 있어. 요리는 완전 쌩초보이고, 오늘 저녁으로 15분 안에 후딱 해먹을 수 있는 맛있는 거 하나만 추천해줘!"
})

print("====================================")
print(" 자취생 전용 셰프 에이전트의 답변")
print("====================================")
print(result['output'])