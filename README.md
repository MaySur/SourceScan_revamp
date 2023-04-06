# Web Application with Flask and React
## About:
* This is a revamp of the cloudbased application that was incomplete; this is the link: [Source Scan](https://github.com/MaySuresh/Source-Scans)
* A more detailed discription can be found here in my [WebPage](https://maysur.github.io/Resume/project1.html)
* For this new project it is the same idea but it is a web application and I am working independently 
***
## Overview:
* For this project we will be using the RedditAPI in Python which will be the backend, then we will use React for the frontend.
* We will Utilize the Flask Library to handle the connection.
***

## Setup:
* Make a desginated folder for the flask-server under the same parent folder
    * Create a `server.py` file under the flask-server folder which will serve as the backend.
* Then run the commands to create a react app outside the flask-server directory
    ```
    npx create-react-app client 
    cd client
    ```
* We now need to install various packages for the back-end so we will set up a virtual environment in the flask-server dir. Then running running the virtual environment.
    ```
    python3 -m venv <name>
    .\<name>\Scripts\activate
        pip install Flask
        pip install praw
    ```
* Then we install Flask in the virtual environment with the folllowing command: `pip install Flask`
* Now we have finished setting up the environment, if there are any errors with the React Setting, learn React.

## Building the backend:

* First, we will need to create a Flask instance:
    ```
    app = Flask(__name__)
    ```
    * The above line create a new Flask instance. 
    * The `__name__` argument is a special keyword that will be used to find the root path. 
    * With this it creates a new instance of the Flask class which will be used to define routes, views and more for the web application.
* Next we will use a Flask decorator that will specify a URL route on which we can access this specific function.  
    ```
    @app.route("/data")
    ```
    * This above code we have the Flask class instance which was stored in the app variable as a Flask decorator.
    * Next we use the `route` function from the Flask library to set up a route.
    * We then add a tag to the main route so that we can access the data in this route.

* We then set up a our fucntion of what we want displayed on our webpage.
* We then need to set up code that will enble us to start a local devlopment server which will listen for incoming HTTP requests.
    ```
    app.run(debug = True)
    ```
    * We use the Flask instance once again and use the `run` function which used to start the Flask development server.
    * When this is called Flask starts a local web server that listens for incoming requests on the computer's IP address and a specific port, i.e. localhost.
    * `degbug = True` parameter is enabled to have additinol information that will help us debug during development.
* After setting all this up we now can run the python file which will give us a local server.
  ```
  flask run
  ```
* Next we go to a browser and look up:
    ```
    localhost:5000/point
    ```
    * We need to specify the port number to 5000 as it is Flask's default port number.
## Building the front end:
* If nerver learnt or use Reactjs learn beofre moving forward.

* We first need to go into the client folder that was set up by React and go into src folder and edit the `package.json`
* We need to configre this file to connect out front-end to the back-end.
* We will edit in the main json instance and add this line:
    ```
      "proxy" : "http://127.0.0.1:5000/",
    ```
    * This will just tell React under which port our backend it running on, which is 5000

* We now can configure the front-end as needed
* First cd into the client folder and then:
    ```
    npm start
    ```
    * To start our front end react server.
* We then set up useState in app.js to recieve data from the back end like so:
    ```
    const [data, setData] = useState([{}])
    ```
* Then we set up useEffect to conect the `/data` to the front end like so:
    ```
    useEffect(() =>{
    fetch("/data").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
    
  }, [])
    ```
    * In here we are using the useEfect to use the fetch method which will have a paramtere of a url tag, in this case `/data`.
    * Then the `then` function will take what ever is inside `/data` and converts it to json format.
    * Then we will take the json and use the setData varaible that was created at useState anb pass it as data.
    * We also add a console.log as a verification that we actually got the data.
## Displaying on the webpage:
* In order to display it on the webpage we need to go into App.js and inside the div tags edit like so:
    ```
    {(typeof data.point === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.point.map((point,i) =>(
          <li key = {i}> {point}</li>
        ))
      )     
    }
    ```
    * What we are basically doing is first checking that actually got it, if not we we will check the type of the data and is it is undefined it means we have not got it yet so we add that Loading message.
    * If infact we got the data we will use the map javascript function to map each json value and display it

And that is how we can display data from the back-end.
