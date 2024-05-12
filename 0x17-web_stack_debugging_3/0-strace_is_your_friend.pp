# automated fix for Apache is returning a 500 error.
exec{'fix-Apache':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
  path    => ['/usr/local/bin/','/bin/','/usr/bin/']
}
