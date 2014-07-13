# junos_lldp

## About

## Usage

### Example Playbook

The below playbook might be called `junos_lldp.yml`.

```yaml
---
- name: LLDP Data
  hosts: firewalls
  connection: local
  gather_facts: no
  tasks:
    - name: Get LLDP Info
      junos_lldp:
        host={{ inventory_hostname }}
        user=tyler
      register: lldp_neighbors
    - name: Display LLDP Neighbor Information
      debug: var=lldp_neighbors.results
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!  I'm
> looking into ways around this.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_lldp.yml
```

> This assumes you're currently in the same directory as your playbook.

### Example Output

```bash
╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-12 - 23:26:15
╰─○ ansible-playbook junos_lldp.yml

PLAY [LLDP Data]
**************************************************************

TASK: [Get LLDP Info]
*********************************************************
ok: [fw01.sj.example.com]

TASK: [Display LLDP Neighbor Information]
*************************************
ok: [fw01.sj.example.com] => {
    "lldp_neighbors.results": {
        "xe-0/0/26.0": {
            "local_int": "xe-0/0/26.0",
            "local_parent": "-",
            "remote_chassis-id": "2c:21:72:a0:1d:00",
            "remote_port-desc": "xe-2/1/0.0",
            "remote_sysname": "as01.example.com",
            "remote_type": "Mac address"
        },
        "xe-1/0/30.0": {
            "local_int": "xe-1/0/30.0",
            "local_parent": "-",
            "remote_chassis-id": "2c:21:72:a0:1d:00",
            "remote_port-desc": "xe-0/1/0.0",
            "remote_sysname": "as01.example.com",
            "remote_type": "Mac address"
        }
    }
}

PLAY RECAP
********************************************************************
fw01.sj.example.com         : ok=2    changed=0    unreachable=0 failed=0

╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-12 - 23:26:26
╰─○
```

### Variables

You'll probably notice that there are a few options to take care of.
First, this assumes your username is the same as the user running the
playbook.  You can modify this by adding the `user` variable.

## Known Issues

None!

## Version

`1.0.0`

## Author

Tyler Christiansen [web][1] | [twitter][2] |
<a href="mailto:tyler@oss-stack.io?GitHub - ansible-junos-extras">e-mail</a>

## License

[BSD 2-Clause License][3].  See [LICENSE][4] for more detail.

[1]: http://oss-stack.io/ "OSS Stack"
[2]: https://twitter.com/oss_stack "Tyler Christiansen (@oss_stack) on Twitter"
[3]: http://opensource.org/licenses/BSD-2-Clause "BSD 2-Clause License"
[4]: LICENSE "BSD 2-Clause License"
