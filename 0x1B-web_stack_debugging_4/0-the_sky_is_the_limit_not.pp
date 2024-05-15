# Define a custom resource to set the ULIMIT for Nginx
exec { 'increase_ulimit_for_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  notify  => Exec['nginx-restart'],
}

# Restart Nginx service to apply changes
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => ['/etc/init.d'],
  refreshonly => true,
}
