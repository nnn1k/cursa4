from modules.database.db_class import db

def create_services():

    db.execute_query('''
        create table services(
          id int primary key identity(1, 1),
          name nvarchar(100) not null,
          description nvarchar(1000) not null,
        );
    ''')

    db.execute_query('''
        create table rooms(
          id int primary key identity(1, 1),
          name nvarchar(100) not null,
          description nvarchar(1000) not null,
          length int,
          width int,
          height int,
          service_id int foreign key references services
        );
    ''')

    db.execute_query('''
    create table coaches(
      id int primary key identity(1, 1),
      name nvarchar(100) not null,
      surname nvarchar(100),
      birthday date,
      service_id int foreign key references services,
      rooms_id int foreign key references rooms
    );
    ''')
    print('services, rooms and coaches created')
