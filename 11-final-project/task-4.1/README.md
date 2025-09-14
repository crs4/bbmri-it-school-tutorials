# Task 4.1: Dockerize


## Your task objective

1. Create Docker images to package your ETL scripts
2. Publish your new images on Docker Hub

## Instructions

## Part 1

These instructions are generic because we can't know in advance exactly what
solution you have created for your BB.

* We assume you're using Python for your scripts.  If so, you can use an
[official Python image](https://hub.docker.com/_/python/) as a base `FROM` which
to build your image.
    + The image is built on Debian Linux, so that `apt` package manager is
    available, if you should require it.
* Use COPY to copy your source code into the image.  Alternatively (better) you
  can install `git` and `git clone` your repository into the image (remember to
  clone without history).
    + **📝 Tip**: it's good practice to fix the commit ID you use to select the
      software version -- e.g., as a default value to an `ARG` called `revision`.
* If your container has a complex start up, implement an entrypoint script.
  Else, you can specify your script as the `CMD`.
* Ensure your image by default runs as a regular user, not as root.
* Test your image locally with `docker run`.  Don't forget to mount local file
directories as required to give your script access to data.


## Part 2

* Create an account on Docker Hub, if you don't already have one.
* Log in (i.e., `docker login`) from the VM, where you built the image.
* Tag the image appropriately, after which you should be able to `docker push`.


## Additional information

You may find the [Docker tutorial](https://bbmri-it-school.crs4.it/pluginfile.php/126/mod_resource/content/1/Docker%20Tutorial.pdf) useful.
