# Installs a Nginx server
exec { 'update':
    provider => shell,
    command => 'apt-get -y update',
    before => Exec['install'],
}

exec { 'install':
    provider => shell,
    command => 'apt-get -y install Nginx',
    before => Exec['header'],
}
exec {'header':
    provider => shell,
    environment => ["HOST=$(hostname)"],
    command => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
    before => Exec['service_start'],
}
exec {'service_start':
    provider => shell,
    command => 'sudo service nginx restart',
}
