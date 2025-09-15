# Task 3.3: Load FHIR resources into the Bridgehead

## Your task objective
In this task you will load all the fhir resources you previously 
generated into you own bridgehead.
At the end of the task you will be able to have all your FHIR resources properlu
uploaded into your FHIR server (bridgehead)

## Instructions
We will use the blazectl tool to load the resources. Blazectl is a command line tool
to interact with the Blaze FHIR server used in the bridgehead.
The syntax to upload resources is the following:

```bash
   blazectl upload <directory containing the resources> --server <fhir server url> 
```
You have the blazectl tool already installed in your bridgehead VM.
First, copy the two directories containing the FHIR resources you generated in the previous task
into the bridgehead VM. You can use `scp` command for that, providing also yout 
key file to access the VM. For example:

```bash
   scp -i <your-key-file.pem> -r <directory-containing-resources> ubuntu@<bridgehead-ip>:/home/ubuntu/
```
Once you have coped the directories into the bridgehead VM, you can use the blazectl command to upload them.
You will have to upload first the organizations and then the cases.

If all goes well, you should see a summary of the uploaded resources at the end of the command execution.
You can also perform a get in your FHIR server and check that the number of resources 
provided in the output bundle for Patient and Specimens is the one you expect.
