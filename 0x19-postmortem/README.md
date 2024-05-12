Postmortem
On release of ALX's System Engineering & DevOps project 0x19, approximately 06:00 EST Addis Ababa, code 500 an Internal server error occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the local host led to 500 Internal Server Error.
Debugging Process


used ps-aux to check the active processes. There were two Apache2 processes operating correctly: www-data and root.
examined the /etc/apache2/ directory's sites-available folder. discovered that the content being served by the web server was in the directory /var/www/html/.
ran strace on the root Apache process's PID in a single terminal. In another, the server was accessed via curl. The results were not what was expected because strace yielded no helpful information.
examined files in the /var/www/html/ directory by hand and tools like ls, grep, find and file found the incorrect .phpp file extension 
Summation
In summary, I discovered two Apache2 processes—one running as root and the other as www-data—when I used ps-aux to verify the processes that were currently executing. Subsequent examination of the /etc/apache2/ directory's sites-available section indicated that the web server was delivering content from /var/www/html/.
I ran strace on the Apache process PIDs in an attempt to diagnose problems. Tracing the www-data process revealed a -1 ENOENT (No such file or directory) error while visiting /var/www/html/wp-settings.php, trying to load .phpp extension fileThis allowed me to find and fix the incorrect.phpp file extension in the wp-settings.php file.
Curl testing later validated the resolution, with an A-ok response of 200. I wrote a script to automate this fix.


Prevention
To avoid such problems in the future:

Frequent Monitoring: To promptly spot any anomalies or problems, do routine monitoring of server processes and records.
Automated Testing: Implement automated testing protocols to verify the accuracy of file systems and web server setups.
