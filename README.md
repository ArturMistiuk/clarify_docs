# ClarifyDocs

## Quick Start

NOTE: The project uses Python 3.11, so need it installed first. It is recommended to use pyenv for installation.

NOTE: Create your OpenAI token: https://platform.openai.com/api-keys

1. install poetry
2. git clone https://github.com/ArturMistiuk/clarify_docs
3. cd clarify_docs/clarify_docs
4. create .env (OPENAI_API_KEY = "Your OpenAI token")
5. poetry install
6. poetry shell
7. Make Migrations python manage.py migrate
8. Create a superuser python manage.py createsuperuser
9. Run the program python manage.py runserver
10. Follow the link http://127.0.0.1:8000/.

## Use with Docker
1. install docker
2. docker build .
3. docker run -p 8000:8000 -e OPENAI_API_KEY="Your OpenAI token" "IMAGE ID"  
4. Follow the link http://0.0.0.0:8000/.
