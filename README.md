# MongoDB-PythonConnection

## MongoDB-PythonConnection

This repository provides a simple guide and code examples for connecting to a MongoDB database using Python, as well as storing and retrieving data.

### Prerequisites
- Docker

### Usage
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mykytashch/MongoDB-PythonConnection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MongoDB-PythonConnection
   ```

3. Build the Docker image:

   ```bash
   docker build -t mongodb-python .
   ```

4. Run the Docker container:

   ```bash
   docker run -it mongodb-python
   ```

   This will execute the Python code inside the container.

5. View the output:

   You will see the successful connection message and the documents retrieved from the MongoDB collection.

### Code Explanation
The `mongodb_python.py` file contains the code for connecting to the MongoDB server, performing a ping to confirm the successful connection, selecting a database, selecting a collection, inserting documents into the collection, and retrieving all documents from the collection.

- To connect to the MongoDB server, the `pymongo` library is used, and the connection URL is provided as an argument to the `MongoClient` constructor.
- A ping command is sent to the server to verify the successful connection.
- A database and a collection are selected. If they do not exist, they will be created when the first document is inserted.
- Several documents are created as Python dictionaries.
- The documents are inserted into the collection using the `insert_many()` method.
- Finally, all documents are retrieved from the collection using the `find()` method, and each document is printed.

Feel free to modify the code to suit your needs and explore more functionalities of MongoDB with Python.

### License
This project is licensed under the [MIT License](LICENSE).

**Note:** Make sure you have Docker installed and running on your machine before executing the steps mentioned above.

For any questions or issues, please open an issue in the GitHub repository.
