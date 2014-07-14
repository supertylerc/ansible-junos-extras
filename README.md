[![Issues in Pending](https://badge.waffle.io/supertylerc/ansible-junos-extras.png?label=pending&title=Pending)](https://waffle.io/supertylerc/ansible-junos-extras)
[![Issues in Ready](https://badge.waffle.io/supertylerc/ansible-junos-extras.png?label=ready&title=Ready)](https://waffle.io/supertylerc/ansible-junos-extras)
[![Issues In Progress](https://badge.waffle.io/supertylerc/ansible-junos-extras.png?label=in%20progress&title=In%20Progress)](https://waffle.io/supertylerc/ansible-junos-extras)
[![Code Quality](https://scrutinizer-ci.com/g/supertylerc/ansible-junos-extras/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/supertylerc/ansible-junos-extras/?branch=master)

# ansible-junos-extras

## About

This repository contains a number of useful Ansible modules geared
toward Juniper Networks devices.  These modules perform a variety of
functions, but they largely focus on retrieving operational data.

## Installation

### Bleeding Edge

`ansible-junos-extras` is a [rolling release][7].  The `master` branch
should always be considered stable.  Individual feature branches exist
for development code, and "more stable" releases are available in tagged
or milestone releases.

> Although `master` is considered stable, if you are paranoid about
> stability, stick to a tagged version.

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

### Development

Development work is performed on branches.  There is a separate branch
for each feature or bug fix.

## Usage

While the sections below go over general usage, they may not cover every
module available.  For a more complete listing of modules and how to use
them, see the `doc` directory in this repository.

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
    - name: Get Pre-Change IPSec Information
      junos_ipsec_summary:
        host={{ inventory_hostname }}
        peers="{{ peers }}"
      register: ipsec
    - name: Get Pre-Change BGP Information
      junos_bgp_summary:
        host={{ inventory_hostname }}
      register: bgp
    - name: Pre-Change Ping
      junos_ping:
        host={{ inventory_hostname }}
      register: ping
    - name: Get Pre-Change LLDP Information
      junos_lldp:
        host={{ inventory_hostname }}
        user=tyler
      register: lldp_neighbors
    - name: Display Pre-Change LLDP Neighbor Information
      debug:
        var=lldp_neighbors.results
    - name: Display Pre-Change IPSec Information
      debug:
        var=ipsec.results
    - name: Display Pre-Change BGP Information
      debug:
        var=bgp.results
    - name: Display Pre-Change Ping Information
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

TASK: [Get Pre-Change IPSec Information]
*************************************************
ok: [fw01.hq.example.com]

TASK: [Get Pre-Change BGP Information]
***************************************************
ok: [fw01.hq.example.com]

TASK: [Pre-Change Ping]
*******************************************************
ok: [fw01.hq.example.com]

TASK: [Get Pre-Change LLDP Information]
*********************************************************
ok: [fw01.hq.example.com]

TASK: [Display LLDP Neighbor Information]
*************************************
ok: [fw01.hq.example.com] => {
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

TASK: [Display Pre-Change IPSec Information]
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

TASK: [Display Pre-Change BGP Information]
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

TASK: [Display Pre-Change Ping Information]
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

## Contributing!

Please contribute!

If you want to add new features to existing modules, create new
features, fix bugs, or just update documentation, please do so!  I only
ask that you dedicate a branch to an individual feature/task/update, and
that it follow the following naming conventions:

* `feat/` for a new feature or module
* `bug/` for a bug fix
* `doc/` for a documentation update

## Roadmap

`master` follows the latest tagged version.  The latest tagged version is
`v1.0.0`.

The next milestone, [`v1.1.0`][8], will include the following:

* [GH1][9]: `junos_ipsec_summary`: add default value for 'peers'
* [GH2][10]: `junos_ping`: add IPv6 support
* [GH3][11]: `junos_ping`: add 'routing-instance' support
* [GH4][12]: `junos_lldp`: add LLDP module
* [GH8][13]: Add Support for Scrutinizer

## Credits

* [Jeremy Schulman][5] - For creating [ansible-junos-stdlib][6], the
  inspiration and basis of this module.

## Version

`1.0.0`

## Author

Tyler Christiansen

[web][1] | [twitter][2] |
<a href="mailto:tyler@oss-stack.io?GitHub - ansible-junos-extras">e-mail</a>

## License

[BSD 2-Clause License][3].  See [LICENSE][4] for more detail.

[1]: http://oss-stack.io/ "OSS Stack"
[2]: https://twitter.com/oss_stack "Tyler Christiansen (@oss_stack) on Twitter"
[3]: http://opensource.org/licenses/BSD-2-Clause "BSD 2-Clause License"
[4]: LICENSE "BSD 2-Clause License"
[5]: https://twitter.com/nwkautomaniac "Jeremy Schulman (@nwkautomaniac) on Twitter"
[6]: https://github.com/Juniper/ansible-junos-stdlib "Ansible Junos Module"
[7]: https://en.wikipedia.org/wiki/Rolling_release "Rolling Releases"
[8]: https://github.com/supertylerc/ansible-junos-extras/issues?milestone=1&state=open "ansible-junos-extras v1.1.0"
[9]: https://github.com/supertylerc/ansible-junos-extras/issues/1 "GH1 - Add Default Value for `peers`"
[10]: https://github.com/supertylerc/ansible-junos-extras/issues/2 "GH2 - Add IPv6 Support"
[11]: https://github.com/supertylerc/ansible-junos-extras/issues/3 "GH3 - Add `rounting-instance` Support"
[12]: https://github.com/supertylerc/ansible-junos-extras/issues/4 "GH4 - Add LLDP Module"
[13]: https://github.com/supertylerc/ansible-junos-extras/issues/8 "GH8 - Add Scrutinizer Support"
