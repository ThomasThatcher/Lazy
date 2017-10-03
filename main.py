#!/usr/bin/python
import subprocess
import sys
import re

host    = sys.argv[1]
command = sys.argv[2]

def remote_ssh_command(c):
	# prog = subprocess.Popen(["ssh", host, command], stderr=subprocess.PIPE)
	# errdata = prog.communicate()[1]
	prog = subprocess.Popen(["ssh", host, c], stderr=subprocess.PIPE)
	stdout = prog.communicate()[0]
	stderr = prog.communicate()[1]
	if len(stderr) is not 0:
		print "Error Returned from " + host ":"
		print stderr
	else:
		print "Command completed successfully..."
		print "Output:" + stdout

if command = "restartls":
	remote_ssh_command("service lsws restart")
else:
	sys.stderr.write("Error: Invalid input")

