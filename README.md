# NGINX-intro
This repository is part of the course https://www.udemy.com/course/nginx-crash-course

The course use node but I decided to use FastAPI as I find it more suitable 

## How to run the project
0) Make sure you have no process running on port 80 since this port will be mapped to nginx
1) We need docker-compose as well as docker installed 
2) Run `docker-compose up -d --build` for the very first time or just `docker-compose up -d`
3) Test if the server is running calling `localhost/health` in your browser
4) Test if the second servier is running calling `localhost:81/health`