<a title="Government of Ukraine, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Flag_of_Ukraine.svg">
  <img width="128" alt="Flag of Ukraine" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/256px-Flag_of_Ukraine.svg.png">
</a>

# Donations2Ukraine

  "Real-time" value of donations made with cryptocurrencies to help ukraine. Made with Python and Flask. 
  
  The total amount corresponds to all donations made in the [official wallets](https://twitter.com/Ukraine/status/1497594592438497282)
  of the government of ukraine and the amounts donated to the wallet of [NGO Come Back Alive](https://twitter.com/Ukraine_DAO).  
  
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

- ### Running the application
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
