# Task 0.0: setup

## Your task objective

1. Get your computer connected to the VM dedicated to your biobank.  Customize the
VM to your liking.
2. Connect to the mock Directory and Sample Locator services that have been
   created for these exercises.

## Instructions

### Part 1
1. Install an SSH client on your computer, if you don't already have one.
2. Generate an SSH key.  Pass the public key to the instructors.
3. Get the public IP address and hostname of your dedicated VM from the
   instructors.
4. Log into your VM via SSH.  Customize it to your liking.
5. Create an SSH config entry for your VM, so you can reconnect to it more easily.


#### Additional information

You might find the tutorial on [SSH and Data
Transfer](https://github.com/crs4/bbmri-it-school-tutorials/blob/main/09-remote-services/ssh-and-data-transfer.md)
useful.

* The VM that has been provisioned for you is an installation of Ubuntu 24.04 (Noble).
* The VM is only accessible via SSH (it does not have a desktop environment).
* You'll find various pre-installed software packages, including the following:
    + Remote access: screen, tmux
    + File transfer: rsync, sftp
    + Package management: apt, apt-get, aptitude
    + docker, docker compose
    + Editors: vim, neovim
    + python3, ipython3
    + jq
    + git
    + blazectl
    + Feel free to install additional software as you deem fit.  It's your biobank!
* You have `sudo` power (no password needed)


### Part 2

1. Visit the Directory:
    * Open your browser and visit the web site <https://directory.bbmri-school.cloud-ip.cc>.
    * Browse and/or query the catalogue to see what's in it.
2. Visit the Sample Locator:
    * Open your browser and visit the web site <https://locator.bbmri-school.cloud-ip.cc>.
    * Browse and/or query it to see what's in it.

In both cases, you should see that the platform is empty.
