# Task 3.1: set up the Bridgehead

## Your task objective

In this task first task you will setup a Bridgehead -- the component that
communicates with the Sample Locator to evaluate queries on your BB's sample
catalogue and return the results.

## Description of artifacts

To connect the Bridgehead into the locator you will be provided with:
* The certificate of the Certificate Authority of the locator (`root.crt.pem`);
* The private key for your biobank (`<site-id>.priv.crt.pem`, where `<site-id>` is
  the name of your biobank without the `BB-` prefix);
* A template of the configuration file for your biobank site;
* The docker compose with the bridgehead services:
  - blaze
  - focus
  - beam-proxy

You can download the required files at [BIMS data folder](https://space.crs4.it/s/CA2ZXRbJmHStm95).

## Instructions to spin up the bridgehead

1. Create the directory `/home/ubuntu/bridgehead`
2. Copy into the directory:
   * the docker compose file
   * the environment file
   * the `root.crt.pem` file
   * the `<site-id>.priv.crt.pem`

3. Copy the environment file to a file called `.env` (which read automatically by docker compose)
4. Edit the .env file with substituting the `<site-id>` with the name of your site. For your site's name use the following table:

   | Biobank | Site ID |
   | --- | --- |
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

5. Bring up the docker compose. Check that all services are up and running by
   using this command to follow the log printouts:

   ```bash
   docker compose logs -f
   ```
   You may need to wait as the processes start.

6. With your browser, go to <https://locator.bschn.ikmx.cloud/search> and run an empty search.
   Your site should appear in the list of results.
