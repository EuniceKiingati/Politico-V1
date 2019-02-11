**What does this PR do?**
This PR writes tests for the endpoint for user login and signup

**Description of Task to be completed**
_The main tasks to be completed are:_
Creation of tests for endpoints to signup a user and login

**How should this be manually tested?**

1. Cretate  a virual enviroment with the command
   `$ virtualenv -p python3 venv`
2. Activate the venv with the command
   `$ source venv/bin/activate`
3. Install git
4. clone this repo
   `$ https://github.com/EuniceKiingati/Politico-V1"`
5. cd into the folder Politico-V1
6. export required enviroments
   `$ export FLASK_APP="run.py"`
7. install requirements
   `$ pip install -r requirements.txt`
8. now we are ready to run.
   
   1. for tests run
      `$ pytest`
   2. for the application run
      `$ flask run`

If you ran the application you can test the api end points using postman as follows

1. Signup a user by sending a `post` request to the endpoint `api/v1/users` with the signup data below

```
{
	"username":"Test",
	"email":"Test@email.com",
	"password":"Test123#"
}
```
1. Logina user by sending a `post` request to the endpoint `api/v1/users/login` with the logindata below

```
{
	"username":"Test",
	"password":"Test123#"
}
```
**What are the relevant pivotal tracker stories?**
[#163764668](https://www.pivotaltracker.com/story/show/163764668)
**Screenshots (if appropriate)**