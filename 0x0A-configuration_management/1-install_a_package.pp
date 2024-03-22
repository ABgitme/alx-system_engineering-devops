# parameter ensures that Puppet only executes the command if Flask version 2.1.0 is not already installed
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['python-installed'],
}

exec { 'python-installed':
  command => '/usr/bin/which python3',
}
