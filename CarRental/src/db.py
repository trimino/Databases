import mysql.connector
from mysql.connector import errorcode

# @brief: get the credentials for the database from a file
# @param: no parameters
# @return: return a list else return None
def get_credentials():
    credentials = []
    try:
        with open ('credentials.txt') as f:
            credentials = f.readlines()
        return credentials
    except FileNotFoundError:
        print('Could not find the credentials.txt')
        return None




class DB_ERROR(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.message    = message
        self.errors     = errors

class DB:
    def __init__(self, credentials):

        
        self.mydb = mysql.connector.connect(
            host        = 'localhost',
            user        = 'carrental',
            password    = 'password',
            database    = 'CarRental'
        )

        self.type = {
            'Compact'   : 1,
            'Medium'    : 2,
            'Large'     : 3,
            'SUV'       : 4,
            'Truck'     : 5,
            'VAN'       : 6
        }

        self.category = {
            'Basic' : 0,
            'Luxury': 1
        }

        self.tables = ['Customer', 'Vehicle', 'Rental']


    # @brief: insert data into the database 
    # @param1: needs to be in the format 'INSERT INTO <table> ' (space is necessary)
    # @param2: values to be inserted into to the database
    # @return: return the number of rows affected 
    def insert_data(self, statement, *args):
        statement = statement + 'VALUES ('
        if len(args) == 0:
            return 0

        types = []
        for k,v in self.type.items():
            types.append(k)
        
        cats = []
        for k,v in self.category.items():
            cats.append(k)
        
        values = []
        for x in args:
            statement = statement + '%s,'
            if x in types:
                values.append( self.convert_type(x) )
            elif x in cats:
                values.append( self.convert_category(x))
            else:
                values.append(x)
    
        statement = statement[:-1] + ')'

        self.execute_state(statement, values)

        

    # @brief: view data from a specific 
    # @param1: table to query database
    # @return: the result and if NULL then return "NOTHNG FOUND"
    def view_data(self, table, *args):
        pass

    # @brief: delete a certain tuple in the database from a specific table
    # @param: the table and any arguments
    # @return: the amount of rows affected
    def delete_data(self, table, *args):
        pass

    # @brief: update a certain record in the database
    # @param1: is the table that you would like to work on 
    # @param1: a = {'custName' : 'UPDATED NAME','phone'    : '(698) 696-9699' }
    # @param2: is a dictionary of attributes that are going to be updated and their new values
    # @param2: c = {'custName' : 'PETER DEREK'} -> PETER DEREK is the filter
    # @param3: is a dictionary of conditions that will filter this update  
    # @return: the amount of rows affected
    def update_data(self, table, attributes, conditions):
        values = []
        statement = 'UPDATE {} SET '.format(table)

        # there is nothing to update so return 
        if len(attributes) == 0:
            return -1

        for k,v in attributes.items():
            statement = statement + k + '=' + '%s' + ','
            values.append(v)
        
        statement = statement[:-1] + ' WHERE '

        for k,v in conditions.items():
            if ' ' in v:
                statement = statement + k + '=' + '\'' + v + '\''+ ','
            else:
                statement = statement + k + '=' + v +','    
            

        statement = statement[:-1]
        return self.execute_state(statement, values)
        
        

    # @brief: convert the "car_type"(string) to an int
    # @param: the string that is of value of: Medium, Compact ...
    # @return: the corresponding int to the string value
    def convert_type(self, car_type):

        list_converter = []
        for key, value in self.type.items():
            list_converter.append(key)
        
        try:
            if isinstance(car_type, str):
                if car_type in list_converter:
                    return self.type[ car_type ]
                else:
                    raise DB_ERROR('not found in conversion', 'INVALID KEY')
            else:
                raise DB_ERROR('invalid type', 'NOT OF TYPE STRING')
        except DB_ERROR as e:
            print('Message: {}'.format(e.message))
            print('ERROR: {}'.format(e.errors))
            
        

    # @brief: convert the "car_year" (string) to an int
    # @param: the string that is of value: Basic or Luxury
    # @return: the corresponding int to the string value
    def convert_category(self, category):

        list_converter = []
        for key, value in self.category.items():
            list_converter.append(key)
        
        try:
            if isinstance(category, str):
                if category in list_converter:
                    return self.category[ category ]
                else:
                    raise DB_ERROR('not found in conversion', 'INVALID KEY')
            else:
                raise DB_ERROR('invalid type', 'NOT OF TYPE STRING')
        except DB_ERROR as e:
            print('Message: {}'.format(e.message))
            print('ERROR: {}'.format(e.errors))   


    def execute_state(self, statement, values):
        try:
            self.mycursor = self.mydb.cursor()

            self.mycursor.execute(statement, tuple(values))

            self.mydb.commit()

            num_affect = str(self.mycursor.rowcount)

            self.mycursor.close()

            return num_affect

        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return -1
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return -1
            else:
                print(e)
                return -1

    
    def close_db(self):
        self.mydb.close()
        


c = get_credentials()
db = DB(c)
# i = db.insert_data('INSERT INTO Customer (custName, phone) ', 'PETER DEREK', '(817) 999-9699')
# print(i)

a = {
    'custName' : 'UPDATED NAME',
    'phone'    : '(698) 696-9699'
}

c = {
    'custName' : 'PETER DEREK'
}
j = db.update_data('Customer', a, c)