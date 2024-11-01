from modules.database.db_class import db
def create_users():
    db.execute_query('''
        create table users(
          id int primary key identity(1, 1),
          login nvarchar(100),
          password nvarchar(100),
          name nvarchar(50),
          surname nvarchar(50),
          phone nvarchar(50),
          email nvarchar(100),
          balance int default 0,
          photo_url nvarchar(200),
          create_at datetime default dateadd(hour, 3, getutcdate()),
          update_at datetime default dateadd(hour, 3, getutcdate())
        );
    ''')

    db.execute_query('''
        insert into users (login, password, name, surname, phone, email, balance, photo_url)  values ('admin', 'admin', 'admin', 'admin', '79000000000', 'admin@gmail.com', 1000, 'default.png')
    ''')

    db.execute_query('''
        create table reviews(
          id int primary key identity(1, 1),
          title nvarchar(100) not null,
          description nvarchar(1000) not null,
          user_id int foreign key references users,
          create_at datetime default dateadd(hour, 3, getutcdate())
        );
    ''')

    db.execute_query('''
        insert into reviews (title, description, user_id) values ('TEST', 'testtttttttttttttt', 1)
    ''')

    db.execute_query('''
        create table verification_code(
        id int primary key identity(1, 1),
        user_id int foreign key references users,
        code nvarchar(10) not null,
        create_at datetime default dateadd(hour, 3, getutcdate())
    );
    ''')

    print('users, reviews and verification_code created')

