from modules.database.db_class import db

def create_other_services():

    db.execute_query('''
       create table subscriptions_types(
          id int primary key identity(1, 1),
          name nvarchar(100) not null,
          description nvarchar(1000) not null,
          time_duration int not null,
          duration nvarchar(30) not null
        );
    ''')

    db.execute_query('''
        create table subscriptions(
          id int primary key identity(1, 1),
          user_id int foreign key references users,
          service_id int foreign key references services,
          subscription_type_id int foreign key references subscriptions_types,
          date_start date default dateadd(hour, 3, getutcdate()),
          date_end date default dateadd(hour, 3, getutcdate())
        );
    ''')

    db.execute_query('''
        create table sports_activities(
          id int primary key identity(1, 1),
          user_id int foreign key references users,
          service_id int foreign key references services,
          coach_id int foreign key references coaches,
          rooms_id int foreign key references rooms,
          time_start datetime,
          time_end datetime,
          price int
        );
    ''')

    print('other services created')
