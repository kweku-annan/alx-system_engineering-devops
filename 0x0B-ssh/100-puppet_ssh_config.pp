# Makes changes to SSH configuration file

file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host 3.84.158.247\n\tForwardAgent Yes",
  }
