# Ideas platform

Web application, where a visitor can see already posted ideas and post his ideas. Required fields are a title and the corresponding content. Users should also have the ability to up and down vote posted ideas.

# Live demo

### Install Dependencies

Install dependencies via

```
npm install
```

and

```
bower install
```

You should find that you have two new
folders in your project.

* `node_modules` - contains the npm packages for the tools we need
* `vendor` - contains the angular framework files and other files from vendors

# Structure
Frontend (AngularJS) part can be found inside `public` folder. 
Index file for the application is located in `api/templates/api/index.html`

# Database
Database config can be found in `ideas/settings.py`

### Run the Application

In order to run the application, we need first to active our virtual environment for python3. 
We do this using

```
source env/bin/activate
```

Then we run 
```
./manage runserver
```

Now browse to the app at `http://localhost:8000`.


## Testing

You can run frontend unit tests using
```
npm test
```

and backend unit tests using
```
./manage test
```

## Build

You can build minified version using (! not tested !)
```
gulp clean-build
```

and change `DEBUG = True` to `DEBUG = False` our `ideas/settings.py`
