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

        try:
            if args:
                cursor.execute(query, args)
            else:
                cursor.execute(query)

            if is_select:
                result['result'] = cursor.fetchall()

        except Exception as error:
            print(f'error: {error}')
            result['error'] = error
        #print(f'result: {result}')
        return result
db = DB()


