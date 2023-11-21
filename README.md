## ClarifyDocs

# Quick Start

NOTE: The project uses Python 3.11, so need it installed first. It is recommended to use pyenv for installation.
NOTE: Create your OpenAI token: https://platform.openai.com/api-keys

1. install poetry
2. cd clarify_docs/clarify_docs
3. create .env (OPENAI_API_KEY = "Your OpenAI token")
3. poetry install
4. poetry shell
5. Make Migrations python manage.py migrate
6. Create a superuser python manage.py createsuperuser
7. Run the program python manage.py runserver
Follow the link http://127.0.0.1:8000/.

## Use with Docker
1. install docker
2. docker run -p 8000:8000 -e OPENAI_API_KEY="Your OpenAI token" 2aaecf268a84
3. Follow the link http://0.0.0.0:8000/.
