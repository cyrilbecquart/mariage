from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test mariage')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

#TODO
'''
def deploy():
    with lcd('/path/to/my/prod/area/'):
        local('git pull /my/path/to/dev/area/')
        local('python manage.py migrate mariage')
        local('python manage.py test mariage')
        local('/my/command/to/restart/webserver')
'''

'''
Deploy :
$ fab prepare_deployment:dev
$ fab deploy
'''