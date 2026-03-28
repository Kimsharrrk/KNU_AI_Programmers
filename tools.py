from langchain_core.tools import tool
from models import UserFridge, MealGoal, RecipePlan
from mock_db import get_store


@tool
def save_fridge_info(ingredients: str, skill_level: str, allergies: str = "없음") -> UserFridge:
    """사용자가 가진 재료와 요리 실력을 저장합니다."""
    info = UserFridge(ingredients=ingredients, skill_level=skill_level, allergies=allergies)
    store = get_store()
    if "fridge" not in store: store["fridge"] = []
    store["fridge"].append(info)
    return info


@tool
def save_meal_goal(meal_type: str, max_time: int) -> MealGoal:
    """어떤 식사를 원하는지, 조리 시간은 얼마나 있는지 저장합니다."""
    goal = MealGoal(meal_type=meal_type, max_time=max_time)
    store = get_store()
    if "meal_goals" not in store: store["meal_goals"] = []
    store["meal_goals"].append(goal)
    return goal


@tool
def save_recipe(recipe_name: str, content: str) -> RecipePlan:
    """에이전트가 만든 최종 레시피를 저장합니다."""
    recipe = RecipePlan(recipe_name=recipe_name, content=content)
    store = get_store()
    if "recipes" not in store: store["recipes"] = []
    store["recipes"].append(recipe)
    return recipe


@tool
def get_user_info() -> str:
    """저장된 사용자의 냉장고 재료와 식사 목표를 조회합니다."""
    store = get_store()
    fridge = store.get("fridge", [])
    goals = store.get("meal_goals", [])

    if not fridge:
        return "등록된 냉장고 정보가 없습니다."

    result = f"""
    [냉장고 상태]
    - 보유 재료: {fridge[-1].ingredients}
    - 요리 실력: {fridge[-1].skill_level}
    - 알레르기/기피: {fridge[-1].allergies}
    """
    if goals:
        result += f"\n[식사 목표]\n- 식사 유형: {goals[-1].meal_type}\n- 최대 조리 시간: {goals[-1].max_time}분"

    return result