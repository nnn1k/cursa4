from modules.database.db_class import db
from modules.models.Subscriptions import Subscriptions
def get_subscriptions(user_id) -> Subscriptions:
    res = db.execute_query('select * from subscriptions where user_id = ?', user_id)


