# dyatel
A system daemon makes periodic checks and actions to achieve a specified number of errors.

Default configuration file `/etc/dyatel/default.yaml` or you can specify DYATEL_CONFIG system environment:

    export DYATEL_CONFIG=/root/dyatel.yaml

Awailable resource:

- http

## Install

    pip install dyatel

## Example config file `/etc/dyatel/default.yaml`

```
---
- task:
  - check:
    name: prodtest
    type: http
    url: https://microservice.net/api/1.1/
    method: get
    pause: 5
    expectation:
      status: 200
    exception:
      count: 3
    action:
      command: /usr/bin/supervisorctl restart app
      pause: 30
```

## Systemd Unit

Add Systemd Unit

    vi /lib/systemd/system/dyatel.service

```
[Unit]
Description=Simplified simple zebra service
After=syslog.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/usr/local
ExecStart=/usr/local/bin/dyatel.py
StandardOutput=syslog
StandardError=syslog

[Install]
WantedBy=multi-user.target
```

Activate and start dyatel service

    systemctl enable dyatel && systemctl start dyatel

