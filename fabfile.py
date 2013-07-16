from fabric.api import task, run, env, cd, sudo

env.hosts = ['rballou@robballou.com']

@task
def deploy():
    with cd('/var/www/vhosts/wildfires.robballou.com'):
        run('git checkout -- .')
        run('git pull')
    sudo('service apache2 restart', shell=False)
