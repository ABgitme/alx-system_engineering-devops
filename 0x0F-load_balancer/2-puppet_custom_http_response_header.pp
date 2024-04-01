# Define a class for configuring custom HTTP response header

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Configure custom HTTP response header using sed
  file { '/etc/nginx/sites-enabled/default':
    ensure      => present,
    owner       => 'root',
    group       => 'root',
    mode        => '0644',

    # Insert the line with `add_header` after any line containing "server_name _"
    insert_line => after,
    match       => /server_name _/,
    line        => 'add_header X-Served-By $HOSTNAME;',
  }


  # Restart Nginx to apply changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }
