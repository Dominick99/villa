from pydantic import BaseModel

LEVEL_END_TOKEN = "<LEVEL_END>"


class NpcTemplate(BaseModel):
    name: str
    age: int
    background: str
    context: str
    end_conditions: list[str]
