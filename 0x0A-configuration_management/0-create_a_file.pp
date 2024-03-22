#creating a file in a directory with content and permissions
file { '/tmp/school':
  ensure  => file,           # Ensure that the file exists
  content => 'I love Puppet',  # Content of the file
  mode    => '0744',         # File permission
  owner   => 'www-data',     # File owner
  group   => 'www-data',     # File group
}
