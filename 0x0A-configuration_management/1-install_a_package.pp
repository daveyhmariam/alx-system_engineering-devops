#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package { 'python3-pip':
  ensure => installed,
}

package { 'python3-setuptools':
  ensure => installed,
}

package { 'build-essential':
  ensure => installed,
}

package { 'python3-dev':
  ensure => installed,
}

class { 'python3': }

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [
    Package['python3-pip'],
    Package['python3-setuptools'],
    Package['build-essential'],
    Package['python3-dev'],
    Class['python3'],
  ],
}
