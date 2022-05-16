# The Sparkify ETL Postgres Pipeline

## Project Overview
  A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer,we will building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

<br>

## Project Files
- dwh.cfg
- sql_queries.py
- create_tables.py
- etl.py


**dwh.cfg** - This file will be used to store our credentials on Amazon. Redshift Cluster address, user role, db crendtials and path to s3 files. For security,
the exact credentials must be store on your computer and must not be shared in public.

**sql_queries.py** - Python script file that contains SQL commands used to CREATE and DROP table, and INSERT values into our data tables. It contains
also copying of files from s3 bucket.

**create_tables.py** - Python file that have script for connecting to our Redshift Cluster and POSTGRES database. This will also serve as a function
in executing 'sql_queries.py'.

**etl.py** - The script connects to the Sparkify redshift database, loads log_data and song_data into staging tables, and transforms them into the five tables.

<br>


## ETL pipeline

Data are copied from the JSON files into the stating_songs and staging_events tables. Then they are sorted into the tables of the schema. The songplays table was
filtered by 'nextSongs'. The time table was extracted in year, month, day, week, hour and weekday.

All queries were stored in 'sql_queries.py'.


## Running The Scripts

In order to run the scripts, make sure you have an account in AWS, you created a Redshift Cluster and you have aws user to connect to the Postgresql database
in AWS.

Fill-up the 'dwh.cfg' using your credentials and path to S3 bucket.

Run the 'create_tables.py'.

Test by running 'etl.py' after running the analytic queries on your Redshift database to compare your results with the expected results.

You can also use SQL editor in Redshift Cluster to check your queries and database.


