#!/usr/bin/expect -f

spawn su root
expect "Password:"
send -- "Hk-yZS\r"
interact
