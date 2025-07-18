# Hl7v2, CDA, IHE Tutorial

In this tutorial we will acquire familiarity with HL7v2 and CDA standards, with some examples and 
exercises with the aim to understand how to use them in practice. 
We will then learn how to use HL7v2 in the context of IHE profile by implementing a Patient Demographics Query (PDQ)
Consumer actors in python, using the HL7v2 library `hl7apy`. We will perform the query against a 
PDQ Supplier, developed with Mirth Connect, that we will run with a Docker container.

## HL7 v2: "Reading a message structure".

Given this HL7v2 message:

```
MSH|^~\&|ARS_APP|ARS_PDQ_SUPPL|PDQ_Consumer|Consumer_Facility|20250707112234||RSP^K22^RSP_K21|7b1bf755-99d2-4929-9904-08fade31cf52|D|2.5|||||IT||EN
MSA|AA|123456|
QAK|QRY12345|OK||1
QPD|Q22^Find Candidates^HL7|QRY12345|@PID.5.1.1^Smith~@PID.5.2^Amy
PID|||IHERED-1005^^^IHERED&1.3.6.1.4.1.21367.13.20.1000&ISO||Smith^Amy^^^^^L||19610228|F|||5660 S Palo Verde^^Tucson^USA^85706^^H
```



a) What is the message type? In which context this message has been used?
b) How many segments are there in the message?
b) It is a request message or a response message?
c) How many components does the QPD.1.1 field have? Which is the value of QPD.1.1?
d) Which is the unique identifier of the message?

## CDA: Inspecting the document and its structure
Given the CDA document under /CDA named sample:CDA.xml, inspect the raw xml document 
structure and identify: 

1) Who is the related patient?
2) Who are the author and the custodian of the document?
3) Which is the unique identifier of the document?
4) Does the component has a structured body? Identify it 
5) How many sections are there in the document?
6) How many observations are there in the document?

Then, render the CDA document in a browser. Notice that the sample_cda document always has 
the reference to a stylesheet. In order to be able to render the document, you need to run 
the browser without the security restrictions, so that it can access the stylesheet.
You should see a result like this:

![CDA rendered](./CDA/rendering.png)


## IHE: Implementing a PDQ Consumer

In this section we will implement a PDQ Consumer using the HL7v2 library `hl7apy`. As PDQ supplier 
we'll use a Mirth Connect implementation that we will run in a Docker container. This implementation has
a simple demographics table; the "PDQ_SERVER_ACTOR_LOCAL_DOMAIN" channel receives at input
the request message from the consumer, extracts the query parameters from the message and 
creates the DB query to search for results. Then, according to the results, it builds the response 
message and sends it back to the consumer.
Tip: have always a look to the IHE specifications of the transaction, here: 
https://profiles.ihe.net/ITI/TF/Volume2/ITI-21.html
In particular, the sections related to "message semantics" and "query parameters".

1. First, let's run the docker container. From ./mirth-connect, run:
    ```bash
    docker compose up -d 
    ```
   You should see a message like this:
   ```
   ✔ Network mirth-connect_default  Created    0.0s
   ✔ Container postgres             Started      0.1s
   ✔ Container mirth                Started      0.0s                                                                                                                                                                           
    ```
2. This step is not mandatory but it is useful if you want to see in practice who a 
   Mirth Connect channel works.
   After having run the container, let's start the Mirth Connect administrator app, in a way to check 
   the Mirth Channels and also to inspect the code of the PDQ Server channel.
   From a browser, go to http://localhost:8087 and download the administrator launcher. 
   The page will look like this:
          ![Mirth Connect web page](./mirth-connect/img/mirth_web_page.png)
   Click on "Download Administrator Launcher", that will download the installer for the Mirth Connect
   application. Install it and run the application. At startup, you should see this page:
         ![Mirth Connect launcher](./mirth-connect/img/mirth-connect-launcher.png)
   Click on "Launch"; this will open the Mirth Connect Administrator application: 
           ![Mirth Connect launcher](./mirth-connect/img/mirth-connect-login.png)

   Type admin/admin as username and password. The application will open. At the first time, you
   shall see a form that allows you to change the username and password and fill some mandatory
   information. Fill the form and confirm the operation. The Mirth Connect Dashboard will then open:
            ![Mirth Connect dashboard](./mirth-connect/img/mirth-connect-dashboard.png)

   Here you can see the active channels. As soon as the channels will receive messages, the counters 
   in the dashboard will increase, and you can als chedk message logs by double-clicking on the channel. 
   Now let's focus on the PDQ_SERVER_ACTOR_LOCAL_DOMAIN channel. In the left pannel click on "Channels", 
   then search for the channel named "PDQ_SERVER_ACTOR_LOCAL_DOMAIN". Double-click on it to open the channel 
   in editing mode and see how it is implemented; click on the "Destinations" tab and then to "Edit transformers"
   Click on some of the javascript step to see all the code that parses the HL7 v2 input message, extracts the
   query parameters from it, creates the output message and sends it back to the consumer:
               
   ![Mirth PDQ Channel](./mirth-connect/img/mirth-pdq-channel.png)

   
3. Now, let's implement the PDQ Consumer in Python to send some HL7 queries to the Supplier.
   First, install the `hl7apy` library:
   ```bash
    pip install hl7apy
    ```
   Then, we will proceed to write the code. Refer to this example of PDQ Consumer here: 
   https://github.com/crs4/hl7apy/blob/develop/examples/iti_21/client.py
   This code can be copied in a local .py file, let's name it `pdq_consumer.py`.
   We will do several chanel to this code. We have to modify the msg template message to set up
   all the values according to our use case. To do that, it is better to parse the message first. 
   At line 32, let's define the parsed message:
    ```python
       parsed_msg = parse_message(msg)
    ```
   In this way we can assign the fields value to the message directly with the dot notation. Remember
   that HL7 apy either supports the notation by field name or by index. For example, to set the value
   of the sending application (MSH.3) we can do:
    ```python
       parsed_message.msh.sending_application = 'BBMRI-IT-SCHOOL-APP'
    ```
   Or, in alternative, we can do:
    ```python
       parsed_messagem.msh.msh_3 = 'BBMRI-IT-SCHOOL-APP'
    ```
   Proceed in the same way and add the code to set the valued of the following fields:
      - Sending Application (MSH.3): Choose a code for your custom application
      - Sending Facility (MSH.4): Choose a code for your custom facility
      - Receiving Application (MSH.5): Set it to the code of the receiving application (Mirth Connect PDQ Supplier): 'ARS_APP'
      - Receiving Facility (MSH.6): Set it to the code of the receiving facility (Mirth Connect PDQ Supplier): 'ARS_PDQ_SUPPL'
      - MSH.7: Set it to the current date and time in the format YYYYMMDDHHMMSS
      - MSH.10: Assign to it a unique identifier for the message; use the uuid library for that
      - QPD.1: Set it to "IHE PDQ Query"
      - QPD.2: It must be a unique query identifier; use the uuid library for that
   
   Now, we have to set the query parameters. They are repetitions of the QPD.3, as per specification. 
   try to execute the python module several times, trying som queries. Under ./mirth-connect there is 
   the file demographics.csv that contains a dump of all demographics that is queried by the PDQ consumer. 
   Try different king of queries, involving the following fields:
      - Query with last name = "Smith". We expect 4 responses: Smith Albert, Smith CHarles, Smith Amy, Smith Carrie.
      - Query with last name = Smith and gender = "F". We expect 2 responses: Smith Amy, Smith Carrie.
      - Query with date of birth = "19610131"- We expect 2 responses: Smirth Charles, Hon Charles.
      - Query with address city = "Tucson". We expect 8 responses in total.
   Now, force an application reject to be forced by the PDQ Supplier. Make a query with an unknown parameter code, for example:
   for example "PID.x.x". Check the message response error sent by the PDQ supplier.
   
   For each query, write a simple piece of code that parses the received message, scans the results and 
   writes a simple json with all the main attributes for each result: id, last name, first name, date of birth.
