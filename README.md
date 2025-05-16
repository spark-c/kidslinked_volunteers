# kidslinked_volunteers

To start the development server:
```bash
python3 manage.py runserver
```

---
To start the database server (MacOS):
```bash
brew services run postgresql
```

You can hop into the postgres shell with user `postgres`:
```bash
psql postgres

# \q to quit
```

(This project database is `volunteers` with admin user `volunteer_admin`).