from modules.database.db_class import db

def create_services():

    db.execute_query('''
        create table services(
          id int primary key identity(1, 1),
          name nvarchar(100) not null,
          description nvarchar(1000) not null,
          photo_url nvarchar(100) not null
        );
    ''')

    db.execute_query('''
    insert into services (name, description, photo_url) values
    ('Football', 'описание', 'football-pole.png'),
    ('Voleyball', 'описание', 'Volleyball.png'),
    ('Diving', 'описание', 'pool.png'),
    ('hokkey', 'описание', 'hokkey.png'),
    ('gym', 'описание', 'gym.png'),
    ('Shooting', 'описание', 'shooting.png'),
    ('gymnastic', 'описание', 'gymnastic.jpg'),
    ('judo', 'описание', 'judo.jpg'),
    ('basketball', 'описание', 'basketball.jpg')
    ''')

    db.execute_query('''
        create table rooms(
          id int primary key identity(1, 1),
          name nvarchar(100) not null,
          description nvarchar(1000) not null,
          length int default 0,
          width int default 0,
          height int default 0,
          photo_url nvarchar(100),
          service_id int foreign key references services
        );
    ''')

    db.execute_query('''
    insert into rooms (name, description, length, width, height, photo_url,  service_id) values
    ('Football-large', 'описание', '105', '68', '0', 'football-pole.png', 1),
    ('Voleyball-large', 'описание', '15', '7', '0', 'Volleyball.png', 2),
    ('Diving', 'описание', ' 12', '7', '5', 'pool.png', 3),
    ('hokkey', 'описание', '61', '37', '0', 'hokkey.png', 4),
    ('gym', 'описание', '30', '20', '0', 'gym.png', 5),
    ('Shooting', 'описание', '200', '50', '0', 'shooting.png', 6),
    ('gymnastic', 'описание', '36', '18', '0', 'gymnastic.jpg', 7),
    ('judo', 'описание', '36', '18', '0', 'judo.jpg', 8),
    ('basketball', 'описание', '28', '15', '0', 'basketball.jpg', 9)
    ''')

    db.execute_query('''
    create table coaches(
      id int primary key identity(1, 1),
      name nvarchar(100) not null,
      surname nvarchar(100),
      date_of_employment date,
      birthday date,
      photo_url nvarchar(100),
      service_id int foreign key references services,
      room_id int foreign key references rooms
    );
    ''')

    db.execute_query('''
    insert into coaches (name, surname, date_of_employment, birthday, photo_url, service_id, room_id) values 
    ('Луис', 'Фуэнте', '2020-04-20', '1961-06-21', 'coach-football.jpg', 1, 1),
    ('Владимир', 'Алекно', '2022-07-11', '1966-12-04', 'coach-voleyball.jpg', 2, 2),
    ('Александр', 'Попов', '2022-11-07', '1971-11-16', 'coach-diving.jpg', 3, 3),
    ('Алексей', 'Кудашов', '2019-04-09', '1971-07-21', 'coach-hokkey.jpg', 4, 4),
    ('Кирилл', 'Сарычев', '2023-12-22', '1989-01-01', 'coach-gym.jpg', 5, 5),
    ('Алексей', 'Бобков', '2021-11-20', '1994-02-14', 'coach-shooting.jpg', 6, 6),
    ('Юлия', 'Барсукова', '2018-10-24', '1978-10-20', 'coach-gymnastic.jpg', 7, 7),
    ('Эцио', 'Гамба', '2019-09-23', '1952-12-02', 'coach-judo.jpg', 8, 8),
    ('Кирилл', 'Чернов', '2017-09-18', '1966-07-08', 'coach-basketball.jpg', 9, 9)
    ''')
    print('services, rooms and coaches created')
