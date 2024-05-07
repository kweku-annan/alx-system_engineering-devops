# Installs flask from pip3

package { 'flask':
  ensure => installed,
  ensure => '2.1.0',
  name => 'flask',
  provider => 'pip3',
  }
