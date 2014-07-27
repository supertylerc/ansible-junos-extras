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

#### To Do

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
