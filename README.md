# InstrumentLibrary
This web application serves as a v1 minimum viable product intended to track all musical instruments owned by employees at Acme Corp, categorized by department.  At a recent company event, several of the employees learned that there were quite a few musicians among them, but not everyone owned instruments.  In order to allow everyone the ability to jam, the engineering department decided to build this Instrument Library to keep track of all instruments available to borrow.

Note: Acme Corp employees all have Google accounts.  In order to create, edit or delete an instrument from the library, you will need to be authenticated as a Google user to proceed.  In order to log in, click the "login" button at the bottom left of any page.

# Getting Started

1. A Vagrant machine is necessary to run this project.  This program functions as a virtual server, which allows this program to be run on a local machine as if it were communicating with a live server on the internet

- In order to download and run a Vagrant machine:

  - VirtualBox is the software that actually runs the program.  Please download a version [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

  - Create a folder on your machine for where you would like to download the Vagrant machine.  Visit [this page](https://www.vagrantup.com/downloads.html) and download the version of Vagrant specific to your operating system into your created folder

  - Open a Terminal or Git Bash window and "cd" to the folder where you downloaded Vagrant.  Once in this folder, type the command `vagrant up` to install the Vagrant machine.  Soon you will be ready to sign in to the machine and run the Instrument Library program, but first you need to download all relevant files in order that they are accessible on your Vagrant machine.  Move to the next instruction.

2.  Every Vagrant machine has a folder which it shares with the machine it is downloaded on called "Vagrantfile".  You can find this file in the same folder that you created to download Vagrant.  Any file that is placed in the Vagrantfile will also be accessible once you sign in to the Vagrant machine.  Download the following files and place them into the Vagrantfile:

  - new_application.py
  - internalinstrumentlibrary.db
  - Folder: static
  - Folder: templates

3.  Now you are ready to run the program.  Make sure you have changed directory to the folder you created for Vagrant, and type `vagrant ssh`.  This will log you into the virtual machine.  Then type the command `python new_application.py`.  If you do not have Python installed, please go [here](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html) to install Python.

4.  Once you see that the program is running, please access "http://localhost:5000", and you should see the main page of the application.  If you are experiencing an error, try to adjust the port at the end of the URL (the last 4 digits).  Other commonly used ports are 8080 and 8000.

5.  Now, go explore!

# Built With

- Python 2.7
- Sublime Text
- Udacity - courses and instruction
- Google OAuth 2.0
- Stack Overflow
- Vagrant
- VirtualBox

# Special Thanks to

- Adrian Gyuricska - CSS Template
- Mandar Waghe (github: mvcman) - Posted code helped with debugging my program

# Authors

Dominic Dabrowiecki
