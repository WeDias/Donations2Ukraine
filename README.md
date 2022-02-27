# Donations2Ukraine

- ## About
  Real-time value of donations made with cryptocurrencies to help ukraine. Made with Python and Flask.  
  Available at: https://donations2ukraine.herokuapp.com/

- ## API
  ```
  # GET /api/v1/donated  
  $ curl https://donations2ukraine.herokuapp.com/api/v1/donated

  > {"donated_usd":8284226.8166}
  ```

- ## How to install and run

- ### Cloning the repository
  To clone the repository run the following command:
  ```
  $ git clone https://github.com/WeDias/Donations2Ukraine.git
  ```

- ### Installing the dependencies
    Inside the newly cloned project folder run the following command to install the dependencies:
    ```
    $ pip install -r requirements.txt
    ```

- ### Executando a aplicação
    Inside the project, run the following command to run the application:
    ```
    $ flask run
    ```
    Or just run app.py file

- ### Viewing the application
    To view the application, after running it, access the following link in your browser:
    ```
    http://127.0.0.1:5000/
    ```
