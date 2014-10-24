#!/usr/bin/python

import libvirt

url = 'qemu:///system'
conn = libvirt.open(url)

for domain_id in conn.listDomainsID():
    domain = conn.lookupByID(domain_id)
    print domain.name()
    print domain.UUIDString()
