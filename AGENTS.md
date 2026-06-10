# villa

**Python 3.14+** — enforced by `.python-version` and `pyproject.toml`. Use `pyenv` or `uv` for the right interpreter.

## Commands

```bash
uv sync                          # install deps + local package
uv run python main.py            # run the app (requires OPENAI_API_KEY)
uv run python -c "..."           # run any script in the venv
```

## Architecture

- Entrypoint: `main.py` → `main()` — prompts for language + scenario, calls NPC generator, prints template.
- `src/villa/` is the `villa` package, auto-discovered by hatchling.
  - `models.py` — `NpcTemplate` Pydantic model + `LEVEL_END_TOKEN` constant (`"<LEVEL_END>"`).
  - `npc_generator.py` — `generate_npc(language, scenario)` → `NpcTemplate`. Uses LangChain with `gpt-5-nano` and structured output.
- Deps managed by `uv`; lockfile is `uv.lock`.

## State

- No tests, no linting/formatting/typechecking configured.
- No commits on `master` — this is a scaffold.
- Empty `README.md` — do not edit unless asked.
