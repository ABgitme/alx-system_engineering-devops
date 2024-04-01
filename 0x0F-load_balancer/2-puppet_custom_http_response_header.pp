# Define a class for configuring custom HTTP response header

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Configure custom HTTP response header using sed
  file_line { 'adding HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}


  # Restart Nginx to apply changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }
