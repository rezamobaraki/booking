module.exports = {
  apps : [{
    name: 'Booking',
    script: 'python /var/www/html/app/manage.py runserver_plus 0.0.0.0:8000;',
    merge_logs: true,
    autorestart: true,
    append_env_to_name: true,
    max_memory_restart: '500M',
  }],
};