from dotenv import load_dotenv

from villa.npc_generator import generate_npc

load_dotenv()


def main():
    language = input("Language to practice: ")
    scenario = input("Scenario: ")
    template = generate_npc(language, scenario)
    print(template.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
