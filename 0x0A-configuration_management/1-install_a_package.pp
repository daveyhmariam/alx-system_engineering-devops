# Define a class to manage the installation of Flask
class install_flask {
  
  # Define the command to install Flask version 2.1.0 using pip3
  $pip_command = '/usr/bin/pip3'
  $flask_version = '2.1.0'
  
  exec { 'install_flask':
    command     => "${pip_command} install Flask==${flask_version}",
    path        => ['/usr/bin', '/bin'],
    unless      => "${pip_command} show Flask | grep Version | grep ${flask_version}",
  }
}
