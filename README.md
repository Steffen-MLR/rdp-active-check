# RDP Active Check for checkmk 2.3.0
Active Check for RDP in checkmk 2.3.0+ using the check api

## Why?

The existing Plugin on checkmk Exchange was made for an old checkmk version and doesnt work anymore in new checkmk versions.

I rewrote the Plugin orinally made by Matthias Haehnel (https://exchange.checkmk.com/p/rdp).

Now it is compatible with the new check API introduced in checkmk 2.3.0.

## How to Install?

Download the MKP from https://exchange.checkmk.com/p/rdp-active-check and install it in checkmk. 

The Rule Name in Wato is "Check RDP Service". If you dont configure anything, the check Defaults to IP-Adress of the Host and Port 3389.