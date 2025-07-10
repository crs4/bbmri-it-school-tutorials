# Hl7v2, CDA, IHE Tutorial

In this tutorial we will acquire familiarity with HL7v2 and CDA standards, with some examples and 
exercise with the aim to understand how to use them in practice. 
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
b) It is a request message or a response message?
c)Which is the value of QPD.1.1?
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
the reference to a stylesheet. In oder to be able to render the document, you need to run 
the browser without the security restrictions, so that it can access the stylesheet.
You should see a result like this:

![CDA rendered](./CDA/CDA_rendered.png)


## IHE: Implementing a PDQ Consumer

In this section we will implement a PDQ Consumer using the HL7v2 library `hl7apy`. As PDQ supplier 
we'll use a Mirth Connect impllementation that we will run in a Docker container. This implementation has
a simple demographics table; the "PDQ_SERVER_ACTOR_LOCAL_DOMAIN" channel recieves at input
the request message from the consumer, extracts the query parameters from the message and 
creates the DB equery to search for results. Then, according to the results, it builds the response 
message and sends it back to the consumer.
Tip: have always a look to the IHE soecificaitons of the transactio, here: 
https://profiles.ihe.net/ITI/TF/Volume2/ITI-21.html
In particular, the sections related to "message semantics" and "query parameters".

1. First, let's run the docker container. From ./mirth-connect, run:
    ```bash
    docker compose up -d 
    ```
2. This step is not mandatory but it is useful if you want to see in practice who a 
   Mirth Connect channel works.
   After that, let's start the Mirth Connect administrator app, in a way to check the Mirth Channels 
   and also to inspect the code of the PDQ Server channel.
   From a browser, go to http://localhost:8087 and download the administrator launcher. 
   In the login prompt that appears, type admin for both username and password. 
3. Now, let's implement the PDQ Consumer in Python to send some HL7 queries to the Supplier.
   First, install the `hl7apy` library:
   ```bash
    pip install hl7apy
    ```
   Then, we will proceed to write the code. Refer to this example of PDQ Consumer here: 
   https://github.com/crs4/hl7apy/blob/develop/examples/iti_21/client.py
   This code can be copied in a local .py file, let's name it `pdq_consumer.py`.
   We will do several chanhes to this code. We have to modify the msg template message to set up
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
      - Sending Application (MSH.3): Choose a code for your custom apllication
      - Sending Facility (MSH.4): Choose a code for your custom facility
      - Receiving Application (MSH.5): Set it to the code of the receiving application (Mirth Connect PDQ Supplier): 'ARS_APP'
      - Receiving Facility (MSH.6): Set it to the code of the receiving facility (Mirth Connect PDQ Supplier): 'ARS_PDQ_SUPPL'
      - MSH.7: Set it to the current date and time in the format YYYYMMDDHHMMSS
      - MSH.10: Assign to it a unique identifier for the message; use the uuid library for that
      - QPD.1: Set it to "IHE PDQ Query"
      - QPD.2: It must be a unique query identifier; use the uuid library for that
   
   Now, we have to set the query parameters. Theu are repetitions of the QPD.3, as per specification. 
   try to execute the python module several times, trying som queries. Under ./mirth-connect there is 
   the file demographics.csv that contains a dump of all demographics that is queried by the PDQ consumer