import pyodbc

class DB:
    data = {
        'Driver': 'SQL Server',
        'Server': 'Lazurniy.mssql.somee.com',
        'Database': 'Lazurniy',
        'UID': 'nnn1k_SQLLogin_1',
        'PWD': '2r7qxnhtxe'
    }
    connect = None

    def __init__(self):
        self.create_connection()
        self.connect.autocommit = True

    def create_connection(self):
        self.connect = pyodbc.connect(
            f'''Driver={self.data['Driver']};
                    Server={self.data['Server']};
                    Database={self.data['Database']};
                    UID={self.data['UID']};
                    PWD={self.data['PWD']}''')

    def close_connection(self):
        self.connect.close()

    def execute_query(self, query, *args, is_select=False):
        cursor = self.connect.cursor()
        result = {'error': False, 'result': None}
        print('------')
        try:
            if args:
                cursor.execute(query, args)
            else:
                cursor.execute(query)

            if is_select:
                result['result'] = cursor.fetchall()

        except Exception as error:
            error_color = '\033[91m'
            print(f'{error_color}error: {error}')
            result['error'] = error
        else:
            good_color = '\033[92m'
            print(f'{good_color}result: {result}')
        finally:
            normal_color = '\033[94m'

            print(f'query: {query}')
            print(f'args: {args}')
            print(f'{normal_color}------')

        return result
db = DB()


