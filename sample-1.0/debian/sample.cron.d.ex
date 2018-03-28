#
# Regular cron jobs for the sample package
#
0 4	* * *	root	[ -x /usr/bin/sample_maintenance ] && /usr/bin/sample_maintenance
