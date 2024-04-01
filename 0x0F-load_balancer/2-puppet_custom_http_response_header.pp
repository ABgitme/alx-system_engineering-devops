# Define a class for configuring custom HTTP response header

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Configure custom HTTP response header using sed
  exec { 'add_custom_header':
    command  => "sudo sed -i '/server_name _/a add_header X-Served-By ${::hostname};' /etc/nginx/sites-enabled/default",
    unless   => "grep -q 'X-Served-By' /etc/nginx/sites-enabled/default",
    provider => 'shell',
    require  => Package['nginx'],
    notify   => Service['nginx'],
  }

  # Enable the default site
  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }

  # Restart Nginx to apply changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }
