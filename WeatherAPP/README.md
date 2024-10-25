# WeatherAPP Project

This project is a virtual assistant developed in python language using FlowiseAI for its operation and flow, from HuggingFace. The objective is to provide weather data and related queries, from a specified location. This can be current data or forecasts, however, for queries needing historical data, only data from Boulder, CO is available.
It has a simple and intuitive graphical interface including login interface, developed with Hugginface's Gradio framework. Besides GraphQL is used as the query language that communicates the application with flowise and the necessary APIs. It may be displayed however errors may appear in the case that you try to use my application because the database or the HugginFace space goes into disabled mode due to disuse.

## Prerequisites

- Python
- Docker. Grant all necessary permissions.
- Git
- Configure FlowiseAI, HuggingFace

## Installation

1. Clone this repository:

   `git clone https://gitlab.com/printai_test/weatherBoulder.git`

   `cd weatherBoulder`

2. Configure the environment variables:

   The application requires five environment variables, corresponding to the FlowiseAI account from HuggingFace, in the APIEndpoints option, OpenWeatherApi used to consult the weather in a specified location, and supabase credentials from the database that store the users data. An example file `env.example` is included in the repository. You must copy this file to `.env` or rename it and fill in the necessary values.
   
   If you do not have the base image used in the Dockerfile(specified at the beginning of the file) available on your machine, you need to install it with the command `docker pull python:[version]` to be able to run the Dockerfile and docker-compose without problems or you can run `docker compose up --build` and it will run the necessary installations automatically.

3. Run the DockerCompose:
   Running the `docker compose up` script will build and deploy the container corresponding to the application based on the `Dockerfile` files and ports defined in the `docker-compose` itself.

   During the execution a link will be printed to allow access to the deployed application and the results of the unit test of the application, which are defined in the files inside the tests folder.

   In gradio, if you want to generate a public link during a few hours, you can set `(share=True)` in `launch()`, in the line where the execution is defined in the code.

## App
   It looks like a local execution of the aplication, but it is also deployed publicly from a Huggingface space, just like Flowise and GraphQL. Which you can access at:
   - GraphQL by strawberry: Space(https://huggingface.co/spaces/esthermariamh/GraphQL), Service(https://esthermariamh-graphql.hf.space)
   - Weather Assistant App: Space(https://huggingface.co/spaces/esthermariamh/WeatherAssistant), Service(https://esthermariamh-weatherassistant.hf.space)
   - FlowiseAI: as it is a drag and drop tool and different from the previous ones, it is better to follow the instructions in the documentation and configure it, for the safety of the current flow. See https://docs.flowiseai.com/configuration/deployment/hugging-face.
   
   In the Data folder, there is the skeleton of the used flow, exported as a json, and other files with the code and data describing the defined flow.

## Considerations
   ### Docker permissions.
   Grant all permissions to Docker to avoid execution errors before proceeding with everything:
   
   - Windows: open and login to your Docker Daemon application before proceeding to deploy everything. 
   - Linux: you can run the script with `sudo` in front, but it is more advisable to add your user to the Docker group, as Docker generally uses a group called docker to allow access to your socket. To do this run the command `sudo usermod -aG docker $USER`. You will then need to log out and log back in (or reboot your machine) for the changes to take effect.

   ### Docker Tets
   In the **Test** section, it is explained in detail how to run the tests individually from the deployment of the application in the Docker container, this is done in this way due to the increased complexity that would bring running Docker inside it, however if necessary it is possible to use another base image, docker:dind.

   Info: Docker inside a container can be complex and is often not the best practice. The reason is that containers are usually isolated processes, and Docker is a container management system that might not work optimally inside another container. Docker-in-Docker (docker:dind) is useful for CI/CD environments, but might be an unnecessary overhead if you only need to run Docker occasionally inside a container.

   ### GraphQL
   The GraphQLSpace folder contains the files where the querys schema is defined and executed, using Strawberry as the query language framework and Uvicorn for deployment. In order to achieve communication with Flowise, it is necessary that it is in a public and accessible link, permanently without mutations in the link, that is why it is deployed in a HugginFace Space, using all the files present in that directory.

## Tests
   
   If you want to run the tests performed to include the test to the Dockerfile, you should rename the file Xtest_docker.py to test_docker.py. Also you must run the `pytest` script and all the results will be displayed in the terminal using the testing framekork Pytest.
   If you want to know the coverage of the tests performed, you can try `pytest --cov=./tests tests` 

   #### Prerequisites to run the tests individually or the coverage:

   - Gradio
   - Pytest(pytest, pytest-mock, pytest-cov)

   For ease of use, you can create a virtual environment using the requirements.txt file:
   1. Run `python -m venv environment_name`.
   2. Run `environment_name `source environment_name` (Window), `source environment_name `bin_activate` (Linux).
   3. `pip install -r requirements.txt`.
   4. Ready to run the tests.
   
   The `test_app` file has individual functions for testing bot operations, account management in login and DB and GUI configuration.

   The `test_graphql` file has individual functions for testing the diferent consults.

   The `test_docker` file has a function to test the operation of the container that is created.

