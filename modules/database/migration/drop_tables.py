from modules.database.db_class import db

def drop_tables():
    db.execute_query('DROP TABLE IF EXISTS sports_activities')
    db.execute_query('DROP TABLE IF EXISTS subscriptions')
    db.execute_query('DROP TABLE IF EXISTS subscriptions_types')
    db.execute_query('DROP TABLE IF EXISTS coaches')
    db.execute_query('DROP TABLE IF EXISTS rooms')
    db.execute_query('DROP TABLE IF EXISTS services')
    db.execute_query('DROP TABLE IF EXISTS verification_code')
    db.execute_query('DROP TABLE IF EXISTS reviews')
    db.execute_query('DROP TABLE IF EXISTS users')

    print('Dropped all tables')

