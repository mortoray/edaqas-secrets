from yaml import safe_load
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

with open('templates/messages.yaml', 'r', encoding='utf-8') as input:
	context = safe_load(input)

with open('edaqas-secrets.html', 'w', encoding='utf-8') as output:
	output.write(env.get_template("encode.html").render(context=context))

with open('edaqas-secrets-decoder.html', 'w', encoding='utf-8') as output:
	output.write(env.get_template("decode.html").render(context=context))
