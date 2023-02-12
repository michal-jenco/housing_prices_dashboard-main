**Housing prices dashboard - task for the 2nd round of interviews**

Instructions:
  1. Download this repository to any location in your PC
  2. Run _install_venv.bat_ .. this will create a virtual environment for the project and install the required packages. This requires that you have Python 3 installed globally on your machine
  3. Run _start_server.bat_ to start the server. The chosen port is 5000, can be changed in the script in case you have port conflicts on your machine
  4. Go to "localhost:5000" in your web browser to see and interact with the application

What was implemented:
  1. A form that enables inputting the house parameters
  2. A predict button that sends the values to the server without refreshing the page
  3. A text field under the button that displays the result of the last prediction
  4. A table containing all previous predictions. The table is updated after every prediction. Table uses a local database and is pre-filled with the 3 predictions provided in your example

What wasn't implemented:
  1. A graph to visualize valuable data
  2. Docker deployment (was able to successfuly build a docker package using the Dockerfile, however running it gave errors I wasn't able to solve

What it looks like on my end:

![image](https://user-images.githubusercontent.com/36048121/218333084-6e9c4f4b-def9-414f-acb4-37c4d2c2d3ba.png)

Developed on Windows 10 and tested on the current version of Chrome (Version 109.0.5414.120 (Official Build) (64-bit))
