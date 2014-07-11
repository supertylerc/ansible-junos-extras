# ansible-junos-extras

## About

This repository contains a number of useful Ansible modules geared
toward Juniper Networks devices.  These modules perform a variety of
functions, but they largely focus on retrieving operational data.

## Installation

### Latest

The `master` branch is considered the latest and greatest.  If you are
paranoid about stability, though, you should follow the instructions for
the latest stable tag.

> Despite the above statement, `master` is always considered stable and
> is used as the production release internally.

Run the following commands:

```bash
mkdir $HOME/src && cd $_
git clone https://github.com/supertylerc/ansible-junos-extras.git
cd
echo "source $HOME/src/ansible-junos-extras/env-setup" >> $HOME/.zshrc
```

> I make a lot of assumptions (source directory, $SHELL, etc).  Adjust
> the instructions for your preferred environment.

### Latest Stable Tag

Tagged versions are guaranteed more stable than the `master` branch.  If
you're overly paranoid, you should grab the latest tagged version that
coincides with your current `major`.`minor` release.  If you're using
1.0.x, for example, you should grab the latest tagged release for 1.0.x.
If you're using 1.0.x and you're overly paranoid, you should _not_ get
any of the 1.1.x tagged releases without testing thoroughly first.

To get a tagged release:

```bash
mkdir $HOME/src && cd $_
git clone https://github.com/supertylerc/ansible-junos-extras.git -b v1.0.0
cd
echo "source $HOME/src/ansible-junos-extras/env-setup" >> $HOME/.zshrc
```

## Usage

### Example Playbook

The below playbook might be called `junos_baseline.yml`.

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
        peers="{{ peers }}"
      register: ipsec
    - name: Get BGP Information
      junos_bgp_summary:
        host={{ inventory_hostname }}
      register: bgp
    - name: Pre-Change Ping
      junos_ping:
        host={{ inventory_hostname }}
      register: ping
    - name: Pre-Change IPSec Information
      debug:
        var=ipsec.results
    - name: Pre-Change BGP Information
      debug:
        var=bgp.results
    - name: Pre-Change Ping Information
      debug:
        var=ping.results
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!
> This is the most basic playbook example.  More sophisticated playbooks
> could return only specific data, push configurations, and rerun
> everything to return a post-change baseline.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_baseline.yml
```

> This assumes you're currently in the same directory as your playbook.

### Example Output

```bash
╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-11 - 15:18:57
╰─○ ansible-playbook junos_baseline.yml

PLAY [Baseline]
***************************************************************

TASK: [Get IPSec Information]
*************************************************
ok: [fw01.hq.example.com]

TASK: [Get BGP Information]
***************************************************
ok: [fw01.hq.example.com]

TASK: [Pre-Change Ping]
*******************************************************
ok: [fw01.hq.example.com]

TASK: [Pre-Change IPSec Information]
******************************************
    "ipsec.results": {
ok: [fw01.hq.example.com] => {
        "ike": {
            "9119268": {
                "address": "1.1.1.1",
                "index": "9119268",
                "state": "UP"
            },
            "9119269": {
                "address": "2.2.2.2",
                "index": "9119269",
                "state": "UP"
            }
        },
        "ipsec": {
            "131077": {
                "address": "2.2.2.2",
                "index": "131077",
                "interface": "st0.3",
                "name": "TEST-VPC_1",
                "state": "up"
            },
            "131078": {
                "address": "1.1.1.1",
                "index": "131078",
                "interface": "st0.4",
                "name": "TEST-VPC_2",
                "state": "up"
            }
        }
    }
}

TASK: [Pre-Change BGP Information]
********************************************
ok: [fw01.hq.example.com] => {
    "bgp.results": {
        "10.0.0.1": {
            "accepted_prefixes": "0",
            "active_prefixes": "0",
            "address": "10.0.0.1",
            "asn": "65501",
            "received_prefixes": "0",
            "rib": "inet.0",
            "state": "Established",
            "suppressed_prefixes": "0"
        },
        "10.0.0.2": {
            "accepted_prefixes": "1",
            "active_prefixes": "1",
            "address": "10.0.0.2",
            "asn": "65501",
            "received_prefixes": "1",
            "rib": "inet.0",
            "state": "Established",
            "suppressed_prefixes": "0"
        }
    }
}

TASK: [Pre-Change Ping Information]
*******************************************
ok: [fw01.hq.example.com] => {
    "ping.results": {
        "10.0.0.1": {
            "success": true
        },
        "10.0.0.2": {
            "success": true
        },
        "10.1.1.1": {
            "success": true
        },
        "10.1.1.2": {
            "success": false
        },
        "10.2.2.1": {
            "success": true
        }
    }
}

PLAY RECAP
********************************************************************
fw01.hq.example.com        : ok=6    changed=0    unreachable=0    failed=0

╭─tyler at deathstar in /etc/ansible using ‹ruby-2.1.1› 14-07-11 - 15:22:11
╰─○
```

### Warnings

Depending on the function of your device(s), the `junos_ping` module can
be very expensive in terms of execution time.  It shouldn't effect your
devices CPU or memory usage, though.  On a test device with ~500 ARP
entries, it took about 90 seconds to complete.

## Documentation

See the `docs` folder for documentation on specific modules.  Or read
the source code.

## Known Issues

* `junos_ipsec_summary` module does not have a default value for `peers`
* No Continuous Integration Tests/Validators
* `junos_ping` module does not support routing instances or IPv6
* Code needs to be refactored and deduplicated

This issue is not insurmountable; however, it was decided that this
issue should not block the first alpha release.

### Contributing!

Please contribute!  If you can help resolve these issues, that would be
awesome.  Or any other issues you discover or features you want.
Actually, I'd really just love any sort of contribution.

If you write a module, it would be really awesome to have it included
here.

## Credits

* [Jeremy Schulman][5] - For creating [ansible-junos-stdlib][6], the
  inspiration and basis of this module.

## Version

`1.0.0`

## Author

Tyler Christiansen
[web][1]
[twitter][2]
<a href="mailto:tyler@oss-stack.io?GitHub - ansible-junos-extras">e-mail</a>

## License

[BSD 2-Clause License][3].  See [LICENSE][4] for more detail.

[1]: http://oss-stack.io/ "OSS Stack"
[2]: https://twitter.com/oss_stack "Tyler Christiansen (@oss_stack) on Twitter"
[3]: http://opensource.org/licenses/BSD-2-Clause "BSD 2-Clause License"
[4]: LICENSE "BSD 2-Clause License"
[5]: https://twitter.com/nwkautomaniac "Jeremy Schulman (@nwkautomaniac) on Twitter"
[6]: https://github.com/Juniper/ansible-junos-stdlib "Ansible Junos Module"
