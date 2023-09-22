# Create a puppet manifest to kill a process named 'killmenow'

exec { 'kill_killmenow_process':
command     => 'pkill killmenow',
refreshonly => true,
onlyif      => 'pgrep killmenow',
path        => '/bin:/usr/bin:/sbin:/usr/sbin',
}
