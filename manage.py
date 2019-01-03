from project import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from project import db
from project.modules.models import *


app = create_app("dev")

manage = Manager(app)

Migrate(app, db)

manage.add_command("mysql", MigrateCommand)

if __name__ == '__main__':

    print(app.url_map)

    manage.run()
