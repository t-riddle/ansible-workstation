# Workstation Configuration Ansible Roles
These roles are designed to configure workstations for development and infrastructure management.

## Ubuntu

### Prerequisites
* `git`
* `ansible`

### Deployment

Deploying Ubuntu requires the following settings:
* `inventories/hosts.yml`
  ```yaml
  all:
    hosts:
      workstation-name:
        ws_home_dir: "/path/to/home/dir"
        ws_username: "workstation_username"
        ssh_enable: true # Only if provisioning SSH - see host_vars below for example settings
  ```
The fonts are used for the `powerlevel10k` theme configured to improve the ZSH experience.

* `inventories/host_vars/workstation-name.yml`
  ```yaml
  vault:
    username: 'vault_username'
    password: 'vault_password'
    uri: 'https://vault.example.com'

  ssh_keys:
    - key_name: 'my-server-ssh-key'
      ssh_contents: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=kv/data/my-secret/path auth_method=userpass mount_point=userpass username={{ vault.username }} password={{ vault.password }} url={{ vault.uri }}')['my-server-ssh-key'] }}"
      host_list: my-server-1 my-server-2 my-server-3
    - key_name: 'my-github-ssh-key'
      ssh_contents: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=kv/data/my-secret/path auth_method=userpass mount_point=userpass username={{ vault.username }} password={{ vault.password }} url={{ vault.uri }}')['my-github-ssh-key'] }}"
      host_list: github.com
  ```
    * Encrypt the file above with `ansible vault --vault-id yourId@prompt workstation-name.yml` if storing sensitive information
* Example command for provisioning locally:
  * If using encrypted files: `ansible-playbook --ask-vault-pass inspiron-ubuntu.yml --become --ask-become-pass --connection=local`
  * Without encrypted files: `ansible-playbook inspiron-ubuntu.yml --become --ask-become-pass --connection=local`