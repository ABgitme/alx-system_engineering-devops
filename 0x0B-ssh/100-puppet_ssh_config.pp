# Define SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure => present,
  content => "
    # SSH Client Configuration

    Host *
        IdentityFile ~/.ssh/school
        PreferredAuthentications publickey
        PasswordAuthentication no
        GSSAPIAuthentication yes
        GSSAPIDelegateCredentials no
        HashKnownHosts yes
  ",
}
