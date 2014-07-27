#!/usr/bin/env python2.7

DOCUMENTATION = '''
---
module: junos_ospf_summary
author: Tyler Christiansen
version_added: "1.1.0"
short_description: Get OSPF neighbor summary
description:
  - Gets OSPF neighbor summary information for OSPF neighbors in Junos.
requirements:
  - py-junos-eznc
options:
  host:
    description:
      - should be {{ inventory_hostname }}
    required: true
  user:
    description:
      - login user-name
    required: false
    default: $USER
  passwd:
    description:
      - login password
    required: false
    default: assumes ssh-key
'''

import sys
import os
from jnpr.junos import Device
import json
def connect(args):
    dev = Device(args['host'], user=args['user'], passwd=args['passwd'])
    try:
        dev.open()
    except Exception as err:
        msg = "Unable to conntect to {}.\n" \
              "Error: {}".format(args['host'], str(err))
        module.fail(msg=msg)
        return
    else:
        return dev

def get_ospf_summary(dev):
    results = {}
    try:
        rpc_results = dev.rpc.get_ospf_neighbor_information(detail=True)
    except Exception as err:
        msg = "Unable to call RPC.  Error: {}".format(str(err))
        module.fail(msg=msg)
        return
    for neighbor in rpc_results:
        neighbor_address = neighbor.findtext('neighbor-address')
        interface = neighbor.findtext('interface-name')
        state = neighbor.findtext('ospf-neighbor-state')
        peer_id = neighbor.findtext('neighbor-id')
        priority = neighbor.findtext('neighbor-priority')
        holdtime = neighbor.findtext('activity-timer')
        area = neighbor.findtext('ospf-area')
        dr = neighbor.findtext('dr-address')
        bdr = neighbor.findtext('bdr-address')
        uptime = neighbor.findtext('neighbor-up-time')
        adjacent_time = neighbor.findtext('neighbor-adjacency-time')
        results[peer_id] = {"address": neighbor_address,
                            "interface": interface,
                            "state": state,
                            "id": peer_id,
                            "priority": priority,
                            "holdtime": holdtime,
                            "area": area,
                            "dr": dr,
                            "bdr": bdr,
                            "uptime": uptime.strip(),
                            "adjacent_time": adjacent_time.strip()}
    return results

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True),
            user=dict(required=False, default=os.getenv('USER')),
            passwd=dict(required=False, default=None)),
        supports_check_mode=False)

    m_args = module.params
    m_results = dict(changed=False)
    dev = connect(m_args)
    results = get_ospf_summary(dev)
    dev.close()
    module.exit_json(results=results)
from ansible.module_utils.basic import *
main()

