from modules.database.migration.drop_tables import drop_tables
from modules.database.migration.create_users import create_users
from modules.database.migration.create_services import create_services
from modules.database.migration.other_services import create_other_services

drop_tables()
create_users()
create_services()
create_other_services()


