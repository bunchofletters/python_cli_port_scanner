<H1>Basic CLI Port Scanner in Python</h1>

Given a Host name or IP, it will run through all port on 1-65535

5 Thread to speed up scanning time<br>
socket timeout set to .2 second to speed up scanning time

Can handle multiple Host input as long as it's correctly seperated with a ',' between each Host

If the host is a IPV4 and the last IPV4 number is replaced with a * it will automatically scan make a scan on all Host starting from the last decimal at 1 to 254

Does not have ways to prevent detection