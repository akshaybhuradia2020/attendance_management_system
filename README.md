## Project install steps: ##
* install python runtime , mongodb and any http client(for testing purpose) in your localhost
* git clone https://github.com/akshaybhuradia2020/attendance_management_system.git
* cd proj_dir
* python -m venv venv
* pip install -r requirements.txt
* uvicorn main:app --reload


### For all end point request this url http://127.0.0.1:8000/docs ###
### Do not provide id for insert operation because mongodb generate own id ###
### For token request login api###
### For resource access you need to use Authorization header along with token ###
