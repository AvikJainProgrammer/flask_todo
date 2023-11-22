### Option 1: Using Flask-Migrate for Database Migrations

Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. It's a preferable way to handle database schema changes in a Flask application.

1. **Install Flask-Migrate**:
   If you haven't already, you need to install Flask-Migrate. You can do this using pip:
   ```bash
   pip install Flask-Migrate
   ```

2. **Integrate Flask-Migrate in Your Application**:
   Modify your `__init__.py` file to include Flask-Migrate.
   ```python
   from flask_migrate import Migrate

   # existing code ...
   db = SQLAlchemy(app)
   migrate = Migrate(app, db)
   ```

3. **Initialize the Migration Repository**:
   In your terminal, navigate to your project directory and run:
   ```bash
   flask db init
   ```

4. **Generate the Initial Migration**:
   Run:
   ```bash
   flask db migrate -m "Initial migration."
   ```

5. **Apply the Migration to the Database**:
   Finally, apply the migration with:
   ```bash
   flask db upgrade
   ```

   This will create the `User` table in your database.

### Option 2: Creating Tables Manually

If you prefer not to use Flask-Migrate, you can create the tables manually.

1. **Add Code to Create Tables**:
   In your `run.py` file, right before you run the app, add the following lines:
   ```python
   from app import db
   db.create_all()
   ```

2. **Run Your Application**:
   Now, when you start your Flask application by running `run.py`, it will create the necessary tables.

   Make sure you do this only once or when you are sure that you need to recreate the tables, as it could lead to data loss in a production environment.

### Note:
- We have opted for option 1