# Requirements

1. Docker
2. docker-compose.

# Usage

## Create the container
1. Clone this repository and navigate to the directory with the docker-compose.yml file.
2. Run the following command to start the container:

 ```bash
 docker-compose -up
```
3. Once the containers are running, you can view the example database using a MongoDB Compass



# Viewing the data in a database manager
For this example we use MongoDB Compass

1. Open MongoDB Compass and create a new connection.
2. In the connection settings, set the following parameters:

- Host: `localhost`
- Port: `27017`
- User name: `root`
- Password: `example`

3. Save and connect.
5. Once the connection is established, you can view the 'users' table in the database, along with the data.

# About the Example Database

The 'test' database contains a single table called 'users'. This table is intended to demonstrate how to use Docker and Docker Compose to set up a MonfoDB database and insert dummy data into the table for testing or development purposes.

# Troubleshooting

- If you encounter an error when running `docker-compose up`, make sure that Docker and Docker Compose are installed correctly, and that you are running the command from the directory with the `docker-compose.yml` file.
