# Flask ToDo
Flask python todo app project and tailwind css.

```bash
   # virtualenv
   python -m venv venv
   source venv/bin/activate (Linux)
   venv\Scripts\activate    (Windows)

   # copy .env.example to .env
   cp .env.example .env

   # secret key
   python -c "import secrets;print(secrets.token_urlsafe(your_number))"

   # install packages
   pip install -r requirements.txt

   # install packages
   rav run tailwind_install

   # rav list command
   rav list

   # rav run tailwind
   rav run tailwind_server

   # flask migrate
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

   # rav server
   rav run server
```
