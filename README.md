# ClarifyDocs

1. Install the dependencies: poetry install
2. poetry shell
3. Make Migrations python manage.py migrate
4. Create a superuser python manage.py createsuperuser
5. Run the program python manage.py runserver
Follow the link http://127.0.0.1:8000/.
6. Start Docker: 
docker run -p 8000:8000 -e OPENAI_API_KEY=Your OpenAI token 2aaecf268a84
7. Stop Docker:  
sudo docker stop 2aaecf268a84
