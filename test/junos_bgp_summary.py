#!/usr/bin/env python2.7

DOCUMENTATION = '''
---
module: junos_bgp_summary
author: Tyler Christiansen
version_added: "0.0.1"
short_description: Get BGP neighbor summary
description:
  - Gets BGP neighbor summary information for BGP neighbors in Junos.
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

def get_bgp_summary(dev):
    results = {}
    try:
        rpc_results = dev.rpc.get_bgp_summary_information()
    except Exception as err:
        msg = "Unable to call RPC.  Error: {}".format(str(err))
        module.fail(msg=msg)
        return
    for item in rpc_results:
        peer = item.findtext('peer-address')
        if peer:
            base = 'bgp-rib'
            address = item.findtext('peer-address')
            asn = item.findtext('peer-as')
            state = item.findtext('peer-state')
            rib = item.findtext('bgp-rib/name')
            active = item.findtext(base + '/active-prefix-count')
            received = item.findtext(base + '/received-prefix-count')
            accepted = item.findtext(base + 'accepted-prefix-count')
            suppressed = item.findtext(base + '/suppressed-prefix-count')
            results[peer] = {"address": address,
                             "asn": asn,
                             "state": state,
                             "rib": rib,
                             "active_prefixes": active,
                             "received_prefixes": received,
                             "accepted_prefixes": accepted,
                             "suppressed_prefixes": suppressed}
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
    results = get_bgp_summary(dev)
    dev.close()
    module.exit_json(results=results)
from ansible.module_utils.basic import *
main()
