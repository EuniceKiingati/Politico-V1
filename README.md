# Politico
A system for managing elections

[![Build Status](https://travis-ci.org/EuniceKiingati/Politico-V1)]
(https://travis-ci.org/EuniceKiingati/Politico-V1)
[![Coverage Status](https://coveralls.io/repos/248658/builds)](https://coveralls.io/github/EuniceKiingati/Politico-V1)]

Heroku link  
https://dashboard.heroku.com/apps/eunice-politico-v1

Documentation link  
https://documenter.getpostman.com/view/4074074/RzZ1qN7c  




**How should this be manually tested?**
1. Create  a virtual environment with the command  
`$ virtualenv -p python3 venv`  

1. Activate the venv with the command     
`$ source venv/bin/activate`

1. Install git  
1. clone this repo  
`$ git@github.com:Hesbon5600/Store-Manager-V1.git"`   
  
1. install requirements      
`$ pip install -r requirements.txt`   
  
1. now we are ready to run. 
	1. for tests run  
         
	`$ pytest`   
	1. for the application run  
	`$ flask run`  

If you ran the application you can test the various api end points using postman. The appi endpoints are  

|Endpoint|functionality|contraints(requirements)|
|-------|-------------|----------|
|post /api/v1/auth/signup|create a user|user information|
|post /api/v1/auth/login | login |requires authentication |
|get /api/v1/parties| get all the parties| pass a token |
|get /api/v1/parties/</partyID>|return a single party| party id, pass token|
|post /api/v1/parties | create a new party entry| party data, pass token|
|post /api/v1/offices | create a new office| party id, pass token|
|get /api/v1/offices | get all offices entries| pass token|
|get/api/v1/offices/<officeID>|get a single office entry| office id, pass token| 
|delete /api/v1/parties/<partyID> | delete a party| party id, pass token|
|put /api/v1/parties/<partyID> | update a parties|party id, party data, pass token|


