# Arco Project

This is a containerized application with the server having a contained flask application, client running a ReactJS application with a PostgreSQL data backend and redis client to manage sessions in the server.

Each container can be build separately and all are put together with `docker-compose`

### Requirements

There are a couple of things you need to have before hand as you set up this project:

1. __Node and npm__
   
   Required for client side code. Especially when setting up the project and installing dependenices.
   
   Install npm and node
   
    ```bash
    curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
    sudo apt-get install -y nodejs npm
    ```
    > Installs Node 7.x
   
   Install application dependencies
   
   ```bash
   cd client
   npm install
   # if using yarn
   yarn install
   ```
   
   
2. __Python and Pip__
   
   The server runs a flask application and will require you to have virtualenv installed as well as pip
    ```bash
    sudo apt-get install -y python-pip
    sudo pip install virtualenv
    cd server
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    
> sets up and installs pip and virtualenv, then installs the application requirements 

3. __Docker__


### Setup