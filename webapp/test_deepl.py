from pkgutil import ImpImporter
import deepl
from webapp import botanical_org_news
 
auth_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="RU")
print(result.text)