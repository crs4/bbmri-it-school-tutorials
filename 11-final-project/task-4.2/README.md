# Task 4.2: simple automated execution

## Your task objective

1. Automate the execution of your ETL process
2. Implement a strategy to handle errors (e.g., re-run and/or notify
   administrator)
3. Implement a notification mechanism to notify someone when the ETL has
   completed.


## Instructions

There are many options to your your ETL process automatically executed,
periodically.  A simple and effective approach is to use system timers (e.g.,
cron jobs or systemd timer units). In recent times, cron seems to be falling out
of favour (e.g., many important Linux distributions don't install it by
default), so we suggest using systemd timers as a simple solution.


### Systemd Timer

* The timer has two components:  the *service* and the *timer*.  Each one is
defined in its own file -- e.g., `etl.service` and `etl.timer`.

Example service file:
```
[Unit]
Description=ETL Process
RefuseManualStart=no
RefuseManualStop=yes

[Service]
Type=oneshot
ExecStart=/usr/local/bin/my-command
```
The command to be executed is defined by `ExecStart`.

This is an example timer file:
```
[Unit]
Description=Run the ETL process
RefuseManualStart=no
RefuseManualStop=no

[Timer]
OnCalendar=Sat *-*-* 8:15:00
Persistent=true
Unit=myetl.service

[Install]
WantedBy=timers.target
```
Note:
* `OnCalendar`: specifies when the timer should be triggered. In the example
above, the timer is triggered every Saturday at 8:15:00.
* `Unit`: specifies the service that should be triggered by this timer (the
specified service must correspond to the name of the service file).

Both service and timer files must be placed in a location where systemd will
find them -- e.g., `/etc/systemd/system/`.


* Create systemd service and timer units to run your ETL once per week.
    + Turn on `Persistent` so that any downtime during at the specified
    execution time will not cause the execution to be missed.
* Consider failure cases and decide what you want to do (e.g., re-run)
* Install the service and the timer by placing the files in the directory
`/etc/systemd/service/`
* Run `sudo systemctl daemon-reload` to reload all configuration files
* Run `sudo systemctl enable --now <etl timer>`, where `<etl timer>` is the name of the
  timer file without the `.timer` extension
* Run `systemctl list-timers` and verify that your timer is present

#### Additional information
* The Arch Linux wiki has
[documentation](https://wiki.archlinux.org/title/Systemd/Timers) which you may
find useful for this task.
