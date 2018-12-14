module.exports = {
  apps : [{
    name: 'Coursework3',
    script: 'manage.py',
    args: 'runserver 0.0.0.0:8000', 
    cwd: '/home/vova/Coursework3/back_end', 
    exec_interpreter: 'python3',
    exec_mode: 'fork'
  }]
};
