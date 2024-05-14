# Makes changes to SSH configuration file

file {'/etc/ssh/ssh_config':
  ensure  => present,
  line => "    PasswordAuthentication no",
  }
