# Define a class for configuring custom HTTP response header

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

exec {'HTTP header':
  command  => 'sed -i "/server_name _/a\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
