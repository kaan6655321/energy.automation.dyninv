#!/usr/bin/env python

'''
Example custom dynamic inventory script for Ansible, in Python.
'''

import os
import sys
import argparse
from tempfile import mkdtemp

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory);

class dynInventory(object):

    def __init__(self):
        self.inventory = {}
        self.get_args()
	self.working_dir = mkdtemp()
        self.inv_fromfile(self.args.path)
	


    def inv_fromfile(self, path):
    	inventory = os.path.join(self.working_dir, path)
        name      = os.path.basename(inventory).split('.')[0]

	if not os.path.isfile(inventory):
            print "inventory is ",inventory
            print "name is ",name
            print "path is ",path
	    raise IOError('Inventory file "{}" not found in folder'.format(path))

        else:
            print "I read the content and print output as JSON\n"


    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', action = 'store')
        self.args = parser.parse_args()

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
#ExampleInventory()
dynInventory()
