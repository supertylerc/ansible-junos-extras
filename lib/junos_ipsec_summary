#!/usr/bin/env python2.7

DOCUMENTATION = '''
---
module: junos_ipsec_summary
author: Tyler Christiansen
version_added: "0.0.1"
short_description: Get IPSec Info
description:
  - Gets IKE Phase 1 & 2 Info for Specified Peers
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
  peers:
    description:
      - list of gateway IPs of remote IPSec peers
    required: false
    default: all
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
            passwd=dict(required=False, default=None),
            peers=dict(required=False, default='all')),
        supports_check_mode=False)

    m_args = module.params
    m_results = dict(changed=False)
    dev = Device(m_args['host'], user=m_args['user'], passwd=m_args['passwd'])
    if m_args['peers'] != 'all':
        import ast
        m_args['peers'] = ast.literal_eval(m_args['peers'])
    try:
        dev.open()
    except Exception as err:
        msg = 'unable to connect to {}: {}'.format(m_args['host'], str(err))
        module.fail_json(msg=msg)
        return
    results = {"ike": {}, "ipsec": {}}
    try:
        sa_info = dev.rpc.get_ike_security_associations_information()
        base = 'multi-routing-engine-item/' \
               'ike-security-associations-information'
        sa_info = sa_info.find(base)
    except Exception as err:
        msg = 'unable to get phase 1 sa info on {}: ' \
              '{}'.format(m_args['host'], str(err))
        module.fail_json(msg=msg)
        return
    for sa in sa_info:
        index = sa.findtext('ike-sa-index')
        state = sa.findtext('ike-sa-state')
        remote = sa.findtext('ike-sa-remote-address')
        if m_args['peers'] == 'all':
            results["ike"][index] = {"index": index,
                                     "peer": remote,
                                     "state": state}
        else:
            if remote in m_args['peers']:
                results["ike"][index] = {"index": index,
                                         "peer": remote,
                                         "state": state}
    try:
        sa_info = dev.rpc.get_security_associations_information(detail=True)
        base = 'multi-routing-engine-item/' \
               'ipsec-security-associations-information'
        sa_info = sa_info.find(base)
    except Exception as err:
        msg = "can't get phase 2 sa info for {}: " \
              "{}".format(m_args['host'], str(err))
        module.fail_json(msg=msg)
        return
    for sa in sa_info:
        peer = sa.findtext('sa-remote-gateway')
        vpn = sa.findtext('sa-vpn-name')
        state = sa.findtext('sa-block-state')
        index = sa.findtext('sa-tunnel-index')
        interface = sa.findtext('sa-df-bit-policy-name/sa-bind-interface')
        if m_args['peers'] == 'all':
            results['ipsec'][index] = {"index": index,
                                       "address": peer,
                                       "name": vpn,
                                       "state": state,
                                       "interface": interface}
        else:
            if peer in m_args['peers']:
                results['ipsec'][index] = {"index": index,
                                           "address": peer,
                                           "name": vpn,
                                           "state": state,
                                           "interface": interface}
    dev.close()
    module.exit_json(results=results)
from ansible.module_utils.basic import *
main()
