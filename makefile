check_cisco: check_cisco.c
	gcc `net-snmp-config --cflags` `net-snmp-config --libs` `net-snmp-config --external-libs` check_cisco.c -o check_cisco
