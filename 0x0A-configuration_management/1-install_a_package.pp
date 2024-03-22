# parameter ensures that Puppet only executes the command if Flask version 2.1.0 is not already installed
package { 'flask':
  require => Exec['python-installed'],
  command => '/usr/bin/pip3 install flask==2.1.0'
}

exec { 'python-installed':
  command => '/usr/bin/which python3'
}
