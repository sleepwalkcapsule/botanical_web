import deepl

auth_key = "d601ad14-1297-2ba8-ee31-9df3be7b5153:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="UA")
print(result.text)