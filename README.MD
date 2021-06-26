# ASUS WRT API  
Forked from https://github.com/vrachieru/asuswrt-api   

## What
Fetches information from a local ASUS WRT router. 

Pseudo monitors setup for WAN connection status. Useful when a Load Balancer is setup between two WAN connections, and when 1/2 WANs are down. This is easily missed unless one checks the admin UI.   

Extended to send a telegram message when the alert fires. A telegram bot (https://core.telegram.org/bots) needs to be setup in prior. 

## How

-   Create a 'creds.py' file from 'creds.py.sample', that has the appropriate credentials.

-   Execute,

    >   python wan.py

-   Setup crontab for a check every hour

    >   0 * * * * cd /opt/asus-wrt/scripts && python wan.py > /opt/asus-wrt/logs/cmd.log 2>&1