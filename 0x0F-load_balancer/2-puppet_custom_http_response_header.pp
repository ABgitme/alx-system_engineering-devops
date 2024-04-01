# Define a class for configuring custom HTTP response header

exec { 'system update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['system update'],
}

exec {'HTTP header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
