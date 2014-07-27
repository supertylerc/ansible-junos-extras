# junos_ospf

## About

## Usage

### Example Playbook

The below playbook might be called `junos_ospf.yml`.

```yaml
---
- name: OSPF Summary
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Get OSPF Summary
      junos_ospf:
        host={{ inventory_hostname }}
      register: ospf
    - debug: var=ospf
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!  I'm
> looking into ways around this.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_ospf.yml
```

> This assumes you're currently in the same directory as your playbook.

### Example Output

```bash
╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-26 - 19:41:56
╰─○ ansible-playbook junos_ospf.yml

PLAY [OSPF Summary]
***********************************************************

TASK: [Get OSPF Summary]
******************************************************
ok: [fw01.hq.example.com]

TASK: [debug var=ospf]
********************************************************
ok: [fw01.hq.example.com] => {
    "ospf": {
        "changed": false,
        "invocation": {
            "module_args": "host=fw01.hq.example.com",
            "module_name": "junos_ospf"
        },
        "results": {
            "10.0.0.4": {
                "address": "169.254.100.1",
                "adjacent_time": "1d 18:49:53",
                "area": "0.0.0.0",
                "bdr": "0.0.0.0",
                "dr": "0.0.0.0",
                "holdtime": "30",
                "id": "10.0.0.4",
                "interface": "st0.6",
                "priority": "128",
                "state": "Full",
                "uptime": "1d 18:49:57"
            },
            "10.0.1.3": {
                "address": "10.10.1.30",
                "adjacent_time": "6w3d 08:06:55",
                "area": "0.0.0.0",
                "bdr": "10.10.1.30",
                "dr": "10.10.1.1",
                "holdtime": "39",
                "id": "10.0.1.3",
                "interface": "reth1.0",
                "priority": "128",
                "state": "Full",
                "uptime": "6w3d 08:06:55"
            },
            "10.0.2.8": {
                "address": "169.254.100.3",
                "adjacent_time": "03:44:42",
                "area": "0.0.0.0",
                "bdr": "0.0.0.0",
                "dr": "0.0.0.0",
                "holdtime": "32",
                "id": "10.0.2.8",
                "interface": "st0.0",
                "priority": "128",
                "state": "Full",
                "uptime": "03:44:42"
            }
        }
    }
}

PLAY RECAP
********************************************************************
fw01.hq.example.com        : ok=2    changed=0    unreachable=0 failed=0

╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-26 - 19:42:02
╰─○
```

### Variables

This module assumes your username is the same as the user running the
playbook.  You can modify this by adding the `user` variable.

## Known Issues

None!  :)

## Version

`1.0.0`

## Author

Tyler Christiansen
[web][1]
[twitter][2]
<a href="mailto:tyler@oss-stack.io?GitHub - decrypt">e-mail</a>

## License

[BSD 2-Clause License][3].  See [LICENSE][4] for more detail.

[1]: http://oss-stack.io/ "OSS Stack"
[2]: https://twitter.com/oss_stack "Tyler Christiansen (@oss_stack) on Twitter"
[3]: http://opensource.org/licenses/BSD-2-Clause "BSD 2-Clause License"
[4]: LICENSE "BSD 2-Clause License"
