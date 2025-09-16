# Task 3.3: Load FHIR resources into the Bridgehead

## Your task objective

Load into you own Bridgehead the FHIR resources you generated in the previous
task.

## Instructions

Use the `blazectl` tool (already installed in your VM, at
`/usr/local/bin/blazectl`) to load the resources. Blazectl is a command line
tool to interact with the Blaze FHIR server used in the bridgehead.

The syntax to upload resources is the following:

```bash
   blazectl upload <directory containing the resources> --server <fhir server url>
```

You will have to upload first the organizations and then the cases.

⚠️ **Note** Make sure the FHIR resources (JSON files) are on the VM where the
Bridgehead is running (i.e., not on your laptop).  If you need to copy the files
into the bridgehead VM, you can use `scp` command -- for example:

```bash
   scp -i <your-key-file.pem> -r <directory-containing-resources> ubuntu@<bridgehead-ip>:/home/ubuntu/
```
Once you have copied the directories into the Bridgehead VM, you can use `blazectl` to load them into the Bridgehead.

If all goes well, you should see a summary of the uploaded resources at the end of the command execution.

You can also perform a GET in your FHIR server and check that the number of resources
provided in the output bundle for Patient and Specimens is the one you expect.
