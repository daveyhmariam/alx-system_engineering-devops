class { 'flask':
  # Ensure Flask is installed with pip3
  package { 'flask':
    ensure => present,
    provider => 'pip3',
    require => Class['python3'], 
  }
  pip_version => '2.1.0',
}