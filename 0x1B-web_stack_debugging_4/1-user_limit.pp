# Enable the user holberton to login and open files without error.
exec { 'increase-file-limits-for-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/50000/; /^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}
