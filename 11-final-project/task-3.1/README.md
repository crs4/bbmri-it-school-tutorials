# Task 3.1

## Your task objective

In this task first task we will setup a Bridgehead, the component that communicates with the Sample Locator to send the query results of our biobank

## Description of artifacts

To connect the Bridgehead into the locator you will be provided with

* The certifcate of the CA of the locator
* The private key for your biobank
* A template of the configuration file for your site biobank
* The docker compose with the bridgehead services:
  - blaze
  - focus
  - beam-proxy

You can download the required files at [BIMS data folder](https://space.crs4.it/s/CA2ZXRbJmHStm95).

## Instructions to spin up the bridgehead

1. Create the directory `/home/ubuntu/bridgehead`
1. Copy into the directory: 
   * the docker compose file
   * the environment file
   * the root.crt.pem file
   * the <site-id>.priv.crt.pem

1. Copy the environent file to .env
1. Edit the .env file with substituting the `<site-id>` with the name of your site. For your site's name use the following table:
   
   | Biobank | Site ID |
   | Sun | sun-test |
   | Mercury | mercury-test |
   | Venus | venus-test |
   | Earth | Earth-test |
   | Moon | moon-test |
   | Mars | mars-test |
   | Jupiter | jupiter-test |
   | Saturn | saturn-test |
   | Uranus | uranus-test |
   | Neptune | neptune-test |

1. Run the docker compose and check with 
    
   ```bash
   docker compose logs -f 
   ```

   that all services are up and running: you may need to wait

1. Go with your browser to https://locator.bschn.ikmx.cloud/search and run an empty search. 
   Your site should appear in the results' list
