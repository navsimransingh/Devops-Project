**Devops Engineer Interview**

**1.Project Description**
The website allows  to check list of hashes (which is provided in form of text file) with the virtualtotal.com database using their API
This script takes text file from the website and then run the hash file(in the text format) using python script .the python script  send each hash
to virustotal.com via API,runs lightweight python web server locally.It returns the information about the hashes in the form of html-table
with the underlying structure

hash_value (MD5 or Sha256)  | Fortinet detection name | Number of engines detected | Scan Date |

**2.Project Files**

    1.HTML.PY-This module provides a few classes to easily generate Html tables and lists.

    2.sample_hash_input.txt - this txt provides all the hash values.

    3.html_gen_py-this is used generation of html page on the browser.

    4.virustotal.py-this is python script filewhich is used to check the hash values with virus total api.

    5.web server.py- thispython file is used to generate local host server.

    6.file form.html-file form html provide the first webpage where we can choose and upload the file.It is written with html and css.

    7.app.py-this is main file which will help to run the code.It renders file form.html with virustotal.py.


**Technology stack used**

    1.Python
    2.Html
    3.Linux
    4.Css
    5.Gitlab



-------------------------------**Instructions to run the code**-------------------------------------------------


**1.Requirements**
Script was tested on MacOS 10.14.2

**2.Dependencies**

  1.install python with homebrew

     brew install python
     
  2.Install virustotal-api using pip:

     pip install virustotal-api
  3.Install HTML.py module from [here:] (https://www.decalage.info/python/html#attachments)

     curl -sSL http://www.decalage.info/files/HTML.py-0.04.zip > HTML.py-0.04.zip

     sudo python setup.py install

**3.Usage**

      1.Run the app.py file in code editor(like visual studio code) 
    
      2.use the url in the console to check the corrsponding output.
    
      3.web page will open where we can upload the the text files contain the hash values using choose file>upload button
    
      4.Check the corrsponding url(https:localhost:8080) in the console and paste in the browser to check the output
    
      5.Webpage will render the hash values with virustotal api and show in the table format
      
**Issue Encountered**
      
      1.Virustotal api process 4 hash values/minute,it take time to render all the hash value, so there is delay of 15 second for every  
        request giving to the server.user can go to the link http://localhost:8000 to see the result at the end.

