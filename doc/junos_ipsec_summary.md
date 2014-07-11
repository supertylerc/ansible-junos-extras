# junos_ipsec_summary

## About

## Usage

### Example Playbook

The below playbook might be called `junos_ipsec.yml`.

```yaml
---
- name: IPSec
  hosts: fw01.hq.example.com
  connection: local
  gather_facts: no
  vars:
    peers:
      - 1.1.1.1
      - 2.2.2.2
  tasks:
    - name: Get IPSec Information
      junos_ipsec_summary:
        host={{ inventory_hostname }}
        user=tyler
        peers="{{ peers }}"
      register: ipsec
    - debug: var=ipsec.results
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!  I'm
> looking into ways around this.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_ipsec.yml
```

> This assumes you're currently in the same directory as your playbook.

### Example Output

```bash
╭─tchristiansen52 at us160536 in /etc/ansible using ‹ruby-2.1.1› 14-07-10 - 20:47:50
╰─○ ansible-playbook junos_ike.yml

PLAY [IPSec]
******************************************************************

TASK: [Get IPSec Information]
*************************************************
ok: [fw01.hq.example.com]

TASK: [debug var=ipsec.results]
***********************************************
ok: [fw01.hq.example.com] => {
    "ipsec.results": {
        "ike": {
            "276690054": {
                "address": "2.2.2.2",
                "index": "276690054",
                "state": "UP"
            },
            "293303156": {
                "address": "1.1.1.1",
                "index": "293303156",
                "state": "UP"
            }
        },
        "ipsec": {
            "131078": {
                "address": "1.1.1.1",
                "index": "131078",
                "interface": "st0.4",
                "name": "TEST-VPC_1",
                "state": "up"
            },
            "131079": {
                "address": "2.2.2.2",
                "index": "131079",
                "interface": "st0.5",
                "name": "TEST-VPC_2",
                "state": "up"
            }
        }
    }
}

PLAY RECAP
********************************************************************
fw01.hq.example.com        : ok=2    changed=0    unreachable=0 failed=0

╭─tchristiansen52 at us160536 in /etc/ansible using ‹ruby-2.1.1› 14-07-10 - 20:48:01
╰─○
```

### Variables

This module assumes your username is the same as the user running the
playbook.  You can modify this by adding the `user` variable.

This module _requires_ a varible, `peers`.  This variable __must__ be a
list, even if there is only one item/element in the list.  This is where
you should put the IP addresses of the IPSec peers you're interested in.

## Known Issues

* No default value for `peers`

## Version

`1.0.0`

## Author

Tyler Christiansen
[web][1]
[twitter][2]
<a href="mailto:tyler@oss-stack.io?GitHub - ansible-junos-ipsec">e-mail</a>

## License

[BSD 2-Clause License][3].  See [LICENSE][4] for more detail.

[1]: http://oss-stack.io/ "OSS Stack"
[2]: https://twitter.com/oss_stack "Tyler Christiansen (@oss_stack) on Twitter"
[3]: http://opensource.org/licenses/BSD-2-Clause "BSD 2-Clause License"
[4]: LICENSE "BSD 2-Clause License"
