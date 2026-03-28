_store: dict = {
    "fridge": [],       # 사용자의 냉장고 재료와 요리 실력
    "meal_goals": [],   # 식사 유형과 최대 조리 시간
    "recipes": [],      # 에이전트가 생성한 최종 레시피
}

def get_store():
    return _store