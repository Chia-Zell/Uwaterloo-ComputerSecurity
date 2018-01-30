#!/usr/bin/expect -f
 spawn su root
 expect "Password:"
 send -- "VnSzeu" 
 interact