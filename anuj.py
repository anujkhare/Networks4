#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet(N):
	
	"Create an empty network and add nodes to it."
	
	net = Mininet( controller=Controller )
	
	#info( '*** Adding controller\n' )
	#net.addController( 'c0' )
	N = int(N)

	host_array = [None] * N
	switch_array = [None] * N

	info( '*** Creating Network\n' )
	for i in range(N):
		host_array[i] = net.addHost('h'+ str(i+1))		
		switch_array[i] = net.addSwitch( 's' + str(i+1))
		net.addLink (host_array[i], switch_array[i])
		if (i>0):
			net.addLink (switch_array[i - 1], switch_array[i])
	

	receiver = net.addHost ('h0')
	net.addLink (receiver, switch_array[0])
	
	info( '*** Starting network\n')
	net.start()
	
	info( '*** Running CLI\n' )
	CLI( net )
	
	info( '*** Stopping network' )
	net.stop()

if __name__ == '__main__':
	n = 5
	if len(sys.argv) == 2:
		print "Using n from command line"
		#print "You need to specify n (No. of hosts)"
		n = sys.argv[1]
	
	print "Using default value of n (=5)"
	#setLogLevel( 'info' )
	emptyNet(n)
