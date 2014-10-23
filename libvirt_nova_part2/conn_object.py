#!/usr/bin/python

import libvirt

url = 'qemu:///system'
conn = libvirt.open(url)

print conn.getVersion()
