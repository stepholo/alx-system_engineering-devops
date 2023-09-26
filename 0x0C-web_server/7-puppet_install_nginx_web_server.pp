# Install Nginx web server (w/ Puppet)
package { 'nginx':
	ensure => installed,
}

first_line { 'abababa':
	ensure => 'present',
	path   => '/etc/nginx/sites-available/default',
	after  => 'listen 80 default_server;',
	line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=DlJ7t3bKIOo permanent;',
}

file { '/var/www/html/index.html':
	content => 'Hello World!',
}

service { 'nginx':
	ensure  => running,
	require => Package['nginx'],
}
