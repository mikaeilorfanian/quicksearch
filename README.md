# Intro
This is an Autocomplete API that you can use to suggest results to a user as the user types a string in your search box.   
You can create the search engine by running the server and sending it a `GET` request. The corpus that is fed to the search engine is a simple text file and this app comes with one for testing purposes(see `fixture_for_testing.txt`).   
This readme has instructions for    
- running the app   
- creating the search engine   
- running tests and a `PEP 8` checker   

Plus, there are some general notes about the implementation details of the application.   
# How to Run the App
This project uses pipenv instead of pip (instructions for pip come later).
## pipenv
1. Go to project directory.   
2. Make a virtual env and install requirements:   
    `$ pipenv install --dev`       
3. Activate virtual env:    
    `$ pipenv shell`   
4. Run server:    
    `$ python web_interface.py <path_to_titles_file>`    
    Example: there is a file called `fixture_for_testing.txt` in this directory for conveniece and testing purposes.    
    To create the search engine from that file, run    
        `$ python web_interface.py ./fixture_for_testing.txt`    
5. To search for "Google", send a `GET` request to    
    `http://127.0.0.1:5000/search/google`    
    The response is a JSON array.    
    An empty array means no hits were found.    

## pip
Only steps 2 and 3 from above are different if you're using `pip`.    
`pip install` the app requirements using `dev-requirements.txt`.    
This will install packages for running tests as well.   
Then run the dev server like step #4 above.

# Running Tests
Make sure you've activate the virtual env (step #3 above), then run    
`$ pytest`    
`$ flake8 --max-line-length=120`     

Note: tests do not cover the web (interface) part of the application.

# General Notes
- The search engine's data structures are created during the handling of the first request. So, the processing of the first request takes longer than later requests.    
- The data structures are in memory so if you stop the server they go away. Running the server and processing a request will generate them again.   
- I gave preferrence to testing the search engine's data structures and its search algorithm. These parts of the application were developed using TDD. Look at the commit history to see the evolution of the app.       
- I've tried to speed up the search feature in expense of memory and the initial creation of the search-engine.    
- The structure of modules and packages can be improved, but currently this lack of organization is not a major pain.    
