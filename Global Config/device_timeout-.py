line con 0
 exec-timeout {{ console_minutes }} {{ console_seconds }}

line vty 0 4
 exec-timeout {{ vty_minutes }} {{ vty_seconds }}
