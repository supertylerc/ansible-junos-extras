# junos_ping

## About

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

* No IPv6
* No support for multiple routing instances

These issues are not insurmountable; however, it was decided that these
issues should not clock the first alpha release.

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
