# Creates a file in /tmp.

file { '/tmp/school':
  ensure  => present,
  path    => '/tmp/school',
  owner   => 'www-data',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
}
