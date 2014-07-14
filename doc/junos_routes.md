# junos_routes

## About

## Usage

### Example Playbook

The below playbook might be called `junos_routes.yml`.

```yaml
---
- name: Pre-Change BGP Routes
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Get BGP Routes
      junos_bgp_routes:
        host={{ inventory_hostname }}
      register: bgp_routes
    - name: Display BGP Routes
      debug: var=bgp_routes.results
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!  I'm
> looking into ways around this.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_routes.yml
```

> This assumes you're currently in the same directory as your playbook.

### Example Output

```bash
╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-14 - 16:11:54
╰─○ ansible-playbook apac_groom.yml

PLAY [Pre-Change BGP Routes]
*************************************************

TASK: [Get BGP Routes]
********************************************************
ok: [cs01.hq.example.com]

TASK: [Display BGP Routes]
****************************************************
ok: [cs01.hq.example.com] => {
    "bgp_routes.results": {
        "0.0.0.0/0": [
            {
                "as_path": {
                    "AS path": "I"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65000"
                },
                "communities": [],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.1.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "10.0.0.4"
                },
                "peer_id": "10.0.0.4",
                "preference": "170",
                "preference2": "-101",
                "prefix": "0.0.0.0/0"
            }
        ],
        "10.1.128.0/22": [
            {
                "as_path": {
                    "AS path": "65001 I"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65000"
                },
                "communities": [
                    "target:65001:1000201536"
                ],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.2.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "10.0.0.4"
                },
                "peer_id": "10.0.0.4",
                "preference": "170",
                "preference2": "-101",
                "prefix": "10.1.128.0/22"
            },
            {
                "as_path": {
                    "AS path": "65001 I (Originator)",
                    "Cluster list": "10.0.0.1",
                    "Originator ID": "10.0.0.11"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65000"
                },
                "communities": [
                    "target:65001:1000201536"
                ],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.2.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "10.0.0.11"
                },
                "peer_id": "10.4.0.1",
                "preference": "170",
                "preference2": "-101",
                "prefix": "10.1.128.0/22"
            },
            {
                "as_path": {
                    "AS path": "65001 I (Originator)",
                    "Cluster list": "10.3.0.1",
                    "Originator ID": "10.3.0.8"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65000"
                },
                "communities": [
                    "target:65001:1000201536"
                ],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.2.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "10.3.0.8"
                },
                "peer_id": "10.3.0.1",
                "preference": "170",
                "preference2": "-101",
                "prefix": "10.1.128.0/22"
            }
        ],
        "10.1.132.0/22": [
            {
                "as_path": {
                    "AS path": "65002 I"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65002"
                },
                "communities": [
                    "target:65002:500367676"
                ],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.2.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "169.254.254.77"
                },
                "peer_id": "10.0.0.4",
                "preference": "170",
                "preference2": "-101",
                "prefix": "10.1.132.0/22"
            }
        ],
        "10.10.32.0/19": [
            {
                "as_path": {
                    "AS path": "I"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65000"
                },
                "communities": [],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.2.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "10.0.0.1"
                },
                "peer_id": "10.4.0.1",
                "preference": "170",
                "preference2": "-101",
                "prefix": "10.10.32.0/19"
            }
        ],
        "10.10.64.0/19": [
            {
                "as_path": {
                    "AS path": "I"
                },
                "autonomous_system": {
                    "local": "65000",
                    "peer": "65000"
                },
                "communities": [],
                "local_preference": "100",
                "next_hop": {
                    "direct": "192.168.2.1",
                    "interface": "ge-0/0/47.0",
                    "protocol": "10.3.0.1"
                },
                "peer_id": "10.3.0.1",
                "preference": "170",
                "preference2": "-101",
                "prefix": "10.10.64.0/19"
            }
        ]
    }
}

PLAY RECAP
********************************************************************
cs01.hq.example.com            : ok=2    changed=0    unreachable=0 failed=0
```

### Variables

This module assumes your username is the same as the user running the
playbook.  You can modify this by adding the `user` variable.

The following variables exist:

* `detail`:
  * description: adds the `detail` flag to the RPC for additional
    information
  * required: false
  * default: `True`
* `route`:
  * description: retrieve information only for the specified route
  * required: false
  * default: `all`
* `active`:
  * description: display only active routes
  * required: false
  * default: `False`
* `protocol`:
  * description: specific routing protocol to retrieve data for
  * required: false
  * default: `bgp`

## Known Issues

* Data might be returned for non-BGP or non-`detail` RPCs that is not
  relevant
* No IPv6 Support

## Version

`1.1.0`

## Author

Tyler Christiansen [web][1] | [twitter][2] |
<a href="mailto:tyler@oss-stack.io?GitHub - decrypt">e-mail</a>

## License

[BSD 2-Clause License][3].  See [LICENSE][4] for more detail.

[1]: http://oss-stack.io/ "OSS Stack"
[2]: https://twitter.com/oss_stack "Tyler Christiansen (@oss_stack) on Twitter"
[3]: http://opensource.org/licenses/BSD-2-Clause "BSD 2-Clause License"
[4]: LICENSE "BSD 2-Clause License"
