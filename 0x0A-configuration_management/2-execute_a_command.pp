# Kills a process named killmenow

exec {"pkill":
  command => 'pkill killmenow',
  }