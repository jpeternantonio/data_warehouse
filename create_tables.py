import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    '''
    Drop all tables in the DB.
    Used the print function to check 
    which query executed last,
    in case of error.
    
    Arguments:
    cur  -- cursor
    conn -- connection to the DB
    
    Return: None
    '''
    for query in drop_table_queries:
        print('Running: ', query)
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''
    Create all tables in the DB.
    Used the print function to check
    which query executed last,
    in case of error.
    
    Arguments:
    cur  -- cursor
    conn -- connection to the DB
    
    Return: None
    '''
    for query in create_table_queries:
        print('Running: ', query)
        cur.execute(query)
        conn.commit()


def main():
    '''
    Read the config file. Connect to Database.
    Will drun the drop_tables function then create tables function.
    Lastly, will close the connection to database.
    
    Return: None
    '''
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()