Birkbeck Biocomputing II - Group 6.
======================================

Our genome browser can be found at: 
https://student.cryst.bbk.ac.uk/~ph001/biocomp2demo/

This folder contains all the files necessary to download and run this genome browser built by Group 6 for Chromosome 1. 

By copying this repository locally, updating the config.py file with your home directory, and running the install.sh script it is possible to run the web application from any server.  The instructions to do this (as provided by Andrew Martin) have been left in this ReadMe for future reference. 

This web application is made up of 3 (+ and additional front end) each led by an individual on the team, all code documentation and reflective essays are stored in the following folders: 

### Data Layer
Denzel Eggerue: createdb/docs

### Business Logic Layer
Amber Hilton: cgi-biocomp2/bl/docs

### Front End Layer
Hirushi Rajapakse: cgi-biocomp2/cgi/docs
Farah Khan: cgi-biocomp2/cgi/docs 



## Setting up 

1. Create a file called `config.sh` using one of the `config_xxxx.sh`
files as a template. At Birkbeck, you should just need to do `cp
config_bbk.sh config.sh`. The values of `html` and `cgi`
are the locations where you need to install your HTML files and CGI
scripts.

2. Create a file called `cgi-biocomp2/config.py`. You can use
`cgi-biocomp2/config_demo.py` as a template. Change `cgiURL` to point
to the path used to access a CGI script in a URL (at Birkbeck,
something like `/cgi-bin/cgiwrap/ab123/` (where `ab123` is replaced by
your username).

3. Run the install script by typing `./install.sh`

You should now be able to point your browser to the URL of the
location in which you stored the HTML.

-----------------------------------------------------------------------

How to get started with GitHub
------------------------

1. reate a **private** repository on your GitHub account.

We will assume your GitHub username is `JohnSmith` and your repository
is called `BBKProject`. Take the following steps:

```
git clone git@github.com:AmberRoseCodes/Group6-biocomputing.git
cd biocomp2
git remote rm origin
git remote add origin git@github.com:AmberRoseCodes/Group6-biocomputing.git
git push -u origin master
```

You have now created your own repository which is a copy of our project and 
synchronized it with your own GitHub.

You can now all clone the repository to your own machines or unix
accounts and edit the code. Don't forget to commit and push your
changes back to GitHub regularly and remember to pull down other
people's changes.

-----------------------------------------------------------------------

The code is organized into three main directories:

- `createdb` This is where the code will live to parse the Genbank
  file and create the database

- `html` This is where the HTML files live. If there is an alternative
  web front end then this would be in an `html2` directory

- `cgi-biocomp2` This is where the CGI scripts and all the code for
  the different layers lives.

The `cgi-biocomp2` directory contains three sub-directories that
represent the three layers of code:

- `cgi-biocomp2/cgi` contains the CGI scripts. If there is an
  alternative web front end then this would be in an directory called
  `cgi-biocomp2/cgi2`

- `cgi-biocomp2/bl` contains the business layer code.

- `cgi-biocomp2/db` contains the database access layer code.

The `install.sh` script in the top directory is a demonstration script that will copy the files to HTML and cgi-bin directories. See the instructions above for using these on the server at Birkbeck.

