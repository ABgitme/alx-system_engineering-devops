# Define a class for configuring custom HTTP response header

exec {'system update':
  command  => 'apt-get update'
  user     => 'root',
  provider => 'shell',
}
# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['system update']
}
file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://youtube.com/watch?v=QH2-TGUlwu4/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Configure custom HTTP response header using sed
exec {'HTTP header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}


# Restart Nginx to apply changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
  }
