# Fix Apache configuration to resolve 500 error
file { '/etc/apache2/sites-available/example.conf':
  ensure  => present,
  content => template('apache/example.conf.erb'),
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/sites-available/example.conf'],
}
