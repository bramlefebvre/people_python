# Backend written in Python using the Django framework

## Endpoints
Api docs in api.yml.

### Search
GET /people/search

Query parameters name (string) and age (int). Returns all Persons filtered in the following way. If name is given it filters so that only Persons whose name contains the name field are retained. If age is given it filters so that only Persons with that age are retained. If both name and age are given both filters are applied. Name is case insensitive. Returns the Persons in a JSON array e.g.
`
[{
    "name": "John",
    "age": 30
}]
`
### Create
POST /people/create

Expects a json containing data of a person e.g.
`
{
    "name": "John",
    "age": 30 
}
`.
If the name is already present or the age is below 18 the person will not be created and the http response will have status code 400, otherwise the person is created and the http response will have status code 201.



# To get this to work (on windows)

- Make sure you have Python installed
- Go to the terminal and navigate to this folder
- Create a virtual environment. Execute: "py -m venv .venv"
- Set permission for activate script. Execute: "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process"
- Activate the virtual environment. Execute: ".venv\scripts\activate"
- Install Django in the virtual environment. Execute "py -m pip install django"
- To get the development server running: "py manage.py runserver"
- The server runs at http://localhost:8000
- You can use Postman to do calls 
- In order to clear the test database. To get in the shell: "py manage.py shell", then in the shell execute
`from people.models import Person` and then `Person.objects.all().delete()`

