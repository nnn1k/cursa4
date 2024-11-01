from modules.database.db_class import db

def create_other_services():

    db.execute_query('''
       create table subscriptions_types(
          id int primary key identity(1, 1),
          name nvarchar(100),
          description nvarchar(1000),
          time_duration int,
          duration nvarchar(30), 
          price int
        );
    ''')

    db.execute_query('''
        insert into subscriptions_types (name, description, time_duration, duration, price) values 
        ('1 month', '1 month', 1, 'month', 1000),
        ('1 year', '1 year', 1, 'year', 10000),
        ('1 week', '1 week', 1, 'week', 500)   
    ''')

    db.execute_query('''
        create table subscriptions(
          id int primary key identity(1, 1),
          user_id int foreign key references users,
          service_id int foreign key references services,
          subscription_type_id int foreign key references subscriptions_types,
          date_start date,
          date_end date
        );
    ''')

    db.execute_query('''
        create table sports_activities(
          id int primary key identity(1, 1),
          user_id int foreign key references users,
          service_id int foreign key references services,
          coach_id int foreign key references coaches,
          room_id int foreign key references rooms,
          date date,
          time time,
          price int
        );
    ''')

    print('other services created')
