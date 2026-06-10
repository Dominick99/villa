from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from villa.models import LEVEL_END_TOKEN, NpcTemplate

_SYSTEM_PROMPT = """You are an expert NPC creator for a language-learning immersion game. You create rich, culturally authentic characters that make the player feel immersed in a foreign country.

Rules:
- All fields (name, background, context, end_conditions) must be written in English. The character itself may speak a foreign language in-game, but the template is metadata for the actor LLM.
- The character's name, age, background, and context must be consistent with the given language, culture, and scenario.
- Be maximally creative and vivid — use specific cultural details, local references, and unique personality traits that make the character feel real.
- Each end_condition must be a complete sentence describing a concrete player action that triggers the end of the scene.
- In EVERY end_condition, include the token {level_end_token} at the end exactly as shown, so the actor LLM knows to signal level completion.
- Aim for 2-5 end_conditions. Make them varied — some easy, some hard, some unexpected.
- Output valid JSON matching the required schema exactly."""


def generate_npc(language: str, scenario: str) -> NpcTemplate:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", _SYSTEM_PROMPT),
            ("human", "Language: {language}\nScenario: {scenario}"),
        ]
    )

    model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)
    structured_model = model.with_structured_output(NpcTemplate)

    chain = prompt | structured_model
    return chain.invoke(
        {
            "language": language,
            "scenario": scenario,
            "level_end_token": LEVEL_END_TOKEN,
        }
    )
