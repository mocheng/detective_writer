# Detective Novel Generator - Design Principles

- Don't use database. Use file as outline or other intermediate content storage.
- Favor markdown over json file.
- Output of the program are in './outputs' folder.
- Use DSPy with `dspy.LM(f'gemini/{model_name}', api_key=api_key)` pattern, not `dspy.Google()`.
