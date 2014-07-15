#!/usr/bin/env python2.7

DOCUMENTATION = '''
---
module: junos_bgp_routes
author: Tyler Christiansen
version_added: "1.1.0"
short_description: Get BGP Route Metrics
description:
  - Gets information on BGP routes.
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
  detail:
    description:
      - add detail flag
    required: false
    default: true
  route:
    description:
      - specific prefix
    required: false
    default: all
  active:
    description:
      - show only active route
    required: false
    default: False
  protocol:
    description:
      - select which protocol
    required: false
    default: bgp
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
            detail=dict(required=False, default=True),
            route=dict(required=False, default='all'),
            active=dict(required=False, default=False),
            protocol=dict(require=False, default='bgp')),
        supports_check_mode=False)

    m_args = module.params
    m_results = dict(changed=False)
    dev = Device(m_args['host'], user=m_args['user'], passwd=m_args['passwd'])
    try:
        dev.open()
    except Exception as err:
        msg = 'unable to connect to {}: {}'.format(m_args['host'], str(err))
        module.fail_json(msg=msg)
        return
    results = {}
    args = {"protocol": m_args['protocol']}
    if m_args['active']:
        args["active_path"] = True
    if m_args['detail']:
        args["detail"] = True
    try:
        routes = dev.rpc.get_route_information(**args)
        routes = routes.find('route-table')
    except Exception as err:
        msg = 'unable to get route information on {}: '\
              '{}'.format(m_args['host'], str(err))
        module.fail_json(msg=msg)
        return
    for route in routes:
        if route.tag != 'rt':
            continue
        prefix = '{}/{}'.format(route.findtext('rt-destination'),
                                route.findtext('rt-prefix-length'))
        if m_args['route'] != 'all':
            from netaddr import IPAddress, IPNetwork
            try:
                address = IPAddress(m_args['route'])
            except Exception as err:
                address = IPNetwork(m_args['route'])
            if host_address not in IPNetwork(prefix):
                continue
        results[prefix] = []
        for entry in route:
            if entry.tag != 'rt-entry':
                continue
            active = False
            if entry.find('current-active'):
                active = True
            preference = entry.findtext('preference')
            preference2 = entry.findtext('preference2')
            nh = {"protocol": entry.findtext('protocol-nh/to'),
                  "interface": entry.findtext('nh/via'),
                  "direct": entry.findtext('nh/to')}
            asn = {"local": entry.findtext('local-as'),
                   "peer": entry.findtext('peer-as')}
            peer = entry.findtext('peer-id')
            as_path = entry.findtext('as-path')
            as_path = as_path.splitlines()
            as_path = dict([x.split(':') for x in as_path])
            for k, v in as_path.items():
                as_path[k] = v.lstrip()
            local_pref = entry.findtext('local-preference')
            communities = []
            try:
                for community in entry.find('communities'):
                    communities.append(community.text)
            except Exception as err:
                pass
            stats = {"prefix": prefix,
                     "preference": preference,
                     "preference2": preference2,
                     "next_hop": nh,
                     "autonomous_system": asn,
                     "peer_id": peer,
                     "as_path": as_path,
                     "local_preference": local_pref,
                     "communities": communities}
            results[prefix].append(stats)
    dev.close()
    module.exit_json(results=results)
from ansible.module_utils.basic import *
main()
