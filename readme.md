# Portfolio Site

This Django project is intended to be a general portfolio for projects I contribute to. Given this is my first full 
Django project I anticipate significant changes to be made over time.

## Getting Started

Following the instructions below will allow you to get a copy of the project up and running on your local machine in a 
dev environment using SQLite. To deploy elsewhere with a full database solution and web server, refer to Django 
documentation including:
* https://docs.djangoproject.com/en/3.0/topics/install/#get-your-database-running
* https://docs.djangoproject.com/en/3.0/topics/install/#install-apache-and-mod-wsgi

### Prerequisites

This project has been developed with Python 3.8, therefore the main prerequisite is having Python 3.8 installed on your
machine. We recognise this project will work with older versions but remains untested.


### Installing

The install instructions assume you have created a venv with Python 3.8, but you could also use another 
virtual environment type such as conda.

1. Clone the repo locally

2. Open your terminal, navigate to the root of this project and launch your python venv

3. Install Django 3.0.8 to your venv
    ```
    pip install django
    ```
4. With Django installed and remaining in the root folder make migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
   
 5. Launch the application by running the server
    ```
    python manage.py runserver
    ```

## Running the tests

To be updated when test cases populated

```
Test execution
```


## Authors

* **Jamie Barrett** - [jb-0](https://github.com/jb-0)


## License

This project is licensed under the ...... - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* I want to acknowledge the various resources that were key in building this site:
    * https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
