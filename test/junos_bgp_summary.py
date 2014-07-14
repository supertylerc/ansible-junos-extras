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
from jnpr.junos import Device
import json

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True),
            user=dict(required=False, default='tyler'),
            passwd=dict(required=False, default=None)),
        supports_check_mode=False)

    m_args = module.params
    m_results = dict(changed=False)
    dev = Device(m_args['host'], user=m_args['user'], passwd=m_args['passwd'])
    try:
        dev.open()
        results = {}
        rpc_results = dev.rpc.get_bgp_summary_information()
        for item in rpc_results:
            peer = item.findtext('peer-address')
            if peer:
                results[peer] = {"address": item.findtext('peer-address'),
                                 "asn": item.findtext('peer-as'),
                                 "state": item.findtext('peer-state'),
                                 "rib": item.findtext('bgp-rib/name'),
                                 "active_prefixes": item.findtext('bgp-rib/active-prefix-count'),
                                 "received_prefixes": item.findtext('bgp-rib/received-prefix-count'),
                                 "accepted_prefixes": item.findtext('bgp-rib/accepted-prefix-count'),
                                 "suppressed_prefixes": item.findtext('bgp-rib/suppressed-prefix-count')}
    except Exception as err:
        msg = 'unable to connect to {}: {}'.format(m_args['host'], str(err))
        module.fail_json(msg=msg)
        return
    else:
        dev.close()
        module.exit_json(results=results)
from ansible.module_utils.basic import *
main()
