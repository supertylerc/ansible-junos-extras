# ansible-junos-bgp

## About

## Installation

Run the following commands:

```bash
mkdir $HOME/src && cd $_
git clone https://github.com/supertylerc/ansible-junos-bgp.git
cd
echo "source $HOME/src/ansible-junos-bgp/env-setup" >> $HOME/.zshrc
```

> I make a lot of assumptions (source directory, $SHELL, etc).  Adjust
> the instructions for your preferred environment.

## Usage

### Example Playbook

The below playbook might be called `junos_bgp.yml`.

```yaml
---
- name: Pre-Change BGP Summary
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Get BGP Summary
      junos_bgp_summary:
        host={{ inventory_hostname }}
      register: bgp_summary
    - debug: var=bgp_summary

- name: Post-Change BGP Summary
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Ping Hosts from Previous Run
      junos_bgp_summary:
        host={{ inventory_hostname }}
      register: post_bgp_summary
    - debug: var=post_bgp_summary
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!  I'm
> looking into ways around this.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_bgp.yml
```

> This assumes you're currently in the same directory as your playbook.

### Example Output

```bash
╭─tchristiansen52 at us160536 in /etc/ansible using ‹ruby-2.1.1› 14-07-02 - 16:42:41
╰─○ ansible-playbook junos_bgp.yml

PLAY [Pre-Change BGP Summary]
*************************************************

TASK: [Get BGP Summary]
*******************************************************
ok: [cs01.hq.example.com]

TASK: [debug var=bgp_summary]
*************************************************
ok: [cs01.hq.example.com] => {
    "bgp_summary": {
        "changed": false,
        "invocation": {
            "module_args": "host=cs01.hq.example.com",
            "module_name": "junos_bgp_summary"
        },
        "results": {
            "10.0.0.2": {
                "accepted_prefixes": "0",
                "active_prefixes": "0",
                "address": "10.0.0.2",
                "asn": "65000",
                "received_prefixes": "0",
                "rib": "inet.0",
                "state": "Established",
                "suppressed_prefixes": "0"
            },
            "10.0.0.3": {
                "accepted_prefixes": null,
                "active_prefixes": null,
                "address": "10.0.0.3",
                "asn": "65000",
                "received_prefixes": null,
                "rib": null,
                "state": "Connect",
                "suppressed_prefixes": null
            },
            "10.0.0.4": {
                "accepted_prefixes": "2",
                "active_prefixes": "2",
                "address": "10.0.0.4",
                "asn": "65000",
                "received_prefixes": "2",
                "rib": "inet.0",
                "state": "Established",
                "suppressed_prefixes": "0"
            },
            "10.0.0.1": {
                "accepted_prefixes": "2",
                "active_prefixes": "1",
                "address": "10.0.0.1",
                "asn": "65000",
                "received_prefixes": "2",
                "rib": "inet.0",
                "state": "Established",
                "suppressed_prefixes": "0"
            }
        }
    }
}

PLAY [Post-Change BGP Summary]
************************************************

TASK: [Ping Hosts from Previous Run]
******************************************
ok: [cs01.hq.example.com]

TASK: [debug var=post_bgp_summary]
********************************************
ok: [cs01.hq.example.com] => {
    "post_bgp_summary": {
        "changed": false,
        "invocation": {
            "module_args": "host=cs01.hq.example.com",
            "module_name": "junos_bgp_summary"
        },
        "results": {
            "10.0.0.2": {
                "accepted_prefixes": "0",
                "active_prefixes": "0",
                "address": "10.0.0.2",
                "asn": "65000",
                "received_prefixes": "0",
                "rib": "inet.0",
                "state": "Established",
                "suppressed_prefixes": "0"
            },
            "10.0.0.3": {
                "accepted_prefixes": null,
                "active_prefixes": null,
                "address": "10.0.0.3",
                "asn": "65000",
                "received_prefixes": null,
                "rib": null,
                "state": "Connect",
                "suppressed_prefixes": null
            },
            "10.0.0.4": {
                "accepted_prefixes": "2",
                "active_prefixes": "2",
                "address": "10.0.0.4",
                "asn": "65000",
                "received_prefixes": "2",
                "rib": "inet.0",
                "state": "Established",
                "suppressed_prefixes": "0"
            },
            "10.0.0.1": {
                "accepted_prefixes": "2",
                "active_prefixes": "1",
                "address": "10.0.0.1",
                "asn": "65000",
                "received_prefixes": "2",
                "rib": "inet.0",
                "state": "Established",
                "suppressed_prefixes": "0"
            }
        }
    }
}

PLAY RECAP
********************************************************************
cs01.hq.example.com            : ok=4    changed=0    unreachable=0
failed=0
```

### Variables

This module assumes your username is the same as the user running the
playbook.  You can modify this by adding the `user` variable.

## Known Issues

* No Continuous Integration Tests/Validators

This issue is not insurmountable; however, it was decided that this
issue should not block the first alpha release.

### Contributing!

Please contribute!  If you can help resolve these issues, that would be
awesome.  Or any other issues you discover or features you want.

## Credits

* [Jeremy Schulman][5] - For creating [ansible-junos-stdlib][6], the
  inspiration and basis of this module.

## Version

`0.0.1`

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
[5]: https://twitter.com/nwkautomaniac "Jeremy Schulman (@nwkautomaniac) on Twitter"
[6]: https://github.com/Juniper/ansible-junos-stdlib "Ansible Junos Module"
