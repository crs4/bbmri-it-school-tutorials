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

* Create systemd service and timer units to run your ETL once per week.
    + Turn on `Persistent` so that any downtime during at the specified
    execution time will not cause the execution to be missed.
* Consider failure cases and decide what you want to do (e.g., re-run)


#### Additional information
* The Arch Linux wiki has
[documentation](https://wiki.archlinux.org/title/Systemd/Timers) which you may
find useful for this task.
