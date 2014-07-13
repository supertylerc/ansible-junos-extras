# junos_lldp

## About

## Usage

### Example Playbook

The below playbook might be called `junos_lldp.yml`.

```yaml
---
- name: LLDP Data
  hosts: cs01.hq.example.com
  connection: local
  gather_facts: no
  tasks:
    - name: Ping Hosts in Arp Cache
      junos_lldp:
        host={{ inventory_hostname }}
        user=tyler
      register: lldp_neighbors
    - name: LLDP Neighbor Information
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
