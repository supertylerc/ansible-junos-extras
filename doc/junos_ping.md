# ansible-junos-ping

## About

## Installation

Run the following commands:

```bash
mkdir $HOME/src && cd $_
git clone https://github.com/supertylerc/ansible-junos-ping.git
cd
echo "source $HOME/src/ansible-junos-ping/env-setup" >> $HOME/.zshrc
```

> I make a lot of assumptions (source directory, $SHELL, etc).  Adjust
> the instructions for your preferred environment.

## Usage

### Example Playbook

The below playbook might be called `junos_ping.yml`.

```yaml
---
- name: Pre-Change Ping
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Ping Hosts in Arp Cache
      junos_ping:
        host={{ inventory_hostname }}
      register: arp_cache
  - debug: var=arp_cache
- name: Post-Change Ping
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Ping Hosts from Previous Run
      junos_ping:
        host={{ inventory_hostname }}
        checktype=post
        targets="{{arp_cache.results}}"
      register: post
    - debug: var=post
```

> The debug statements are there for you to see the results of your
> tests.  If you remove them, you won't actually know the results!  I'm
> looking into ways around this.

### Running the Playbook

Run the following:

```bash
ansible-playbook ./junos_ping.yml
```

> This assumes you're currently in the same directory as your playbook.

### Variables

You'll probably notice that there are a few options to take care of.
First, this assumes your username is the same as the user running the
playbook.  You can modify this by adding the `user` variable.

Second, the `checktype`.  This defaults to `pre` and is not required.  If
`checktype=pre`, the task will load the remote device's ARP table/cache
and attempt a ping of each IP.  It performs 3 pings with the `rapid`
parameter and determines success based on the results.

If you set `changetype` to `post`, you must _also_ set the `targets`
variable.  The `targets` variable is expected to be a dump of a Python
`dict` in string format, which later gets reconstructed into a proper
`dict`.  It was done this way so that you could easily register
variables and pass them between multiple `junos_ping` tasks.

## Known Issues

* Code needs to be refactored/deduplicated
* No IPv6
* No support for multiple routing instances
* No Continuous Integration Tests/Validators

These issues are not insurmountable; however, it was decided that these
issues should not clock the first alpha release.

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
