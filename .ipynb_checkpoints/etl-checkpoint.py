import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    '''
    Fills in the staging table.
    Used the print function to check 
    which query executed last,
    in case of error.
        
    Arguments:
    cur  -- cursor
    conn -- connection to the DB
    
    Return: None
    '''
    for query in copy_table_queries:
        print('Running', query)
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    '''
    Fills in the DB tables from the staging table.
    Used the print function to check 
    which query executed last,
    in case of error.
        
    Arguments:
    cur  -- cursor
    conn -- connection to the DB
    
    Return: None
    '''
    for query in insert_table_queries:
        print('Running', query)
        cur.execute(query)
        conn.commit()


def main():
    '''
    This function will read the config file then connect to database.
    It will run the load_staging_tables and insert_tables function, 
    then close the connection to database.
    
    Return: None
    '''
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()