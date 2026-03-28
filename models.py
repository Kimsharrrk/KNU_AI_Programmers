from pydantic import BaseModel, Field

class UserFridge(BaseModel):
    ingredients: str = Field(description="현재 냉장고에 있는 재료들 (쉼표로 구분)")
    skill_level: str = Field(description="요리 실력 (초보, 중급, 고수)")
    allergies: str = Field(description="알레르기나 못 먹는 음식", default="없음")

class MealGoal(BaseModel):
    meal_type: str = Field(description="식사 유형 (아침, 점심, 저녁, 야식, 간식)")
    max_time: int = Field(description="최대 조리 가능 시간 (분)")

class RecipePlan(BaseModel):
    recipe_name: str = Field(description="요리 이름")
    content: str = Field(description="필요한 추가 조미료 및 구체적인 조리 순서")