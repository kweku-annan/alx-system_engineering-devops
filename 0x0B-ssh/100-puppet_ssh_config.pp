# Makes changes to SSH configuration file

file {'~/.ssh/config':
  ensure  => present,
  content => "Host 3.84.158.247\n\tForwardAgent Yes",
  }
