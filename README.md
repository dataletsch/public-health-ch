Public Health Schweiz
=====================

Website of the Swiss Society for Public Health

## Development environment

The easiest way to set up your machine would be to use [Vagrant](https://vagrantup.com), then in the project folder in the terminal type:

```
vagrant liverun
```

**Backend setup**

After installing Python 3, from the project folder:

```
sudo apt-get install python3-venv python3-dev libjpeg-dev
pyvenv env
. env/bin/activate

pip install -U pip
pip install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser
```

You will be asked a few questions to create an administrator account.

**Frontend setup**

You will need to have Ruby and SASS installed on your system, e.g.:

```
sudo yum install rubygem-sass
```

Make sure a recent version of node.js, then:

```
npm install -g bower grunt-cli
npm install
bower install
```

If you have one installed, also start your local redis server (`service redis start`).

**Starting up**

Run this after completing setup:

```
./manage.py runserver &
grunt browser-sync
```

A default browser should open pointing to the default home page.

Now access the admin panel with the user account you created earlier: http://localhost:3000/admin/

## Troubleshooting

- Issues with migrating database tables in SQLite during development? Try `./manage.py migrate --fake`

## Production notes

We use Ansible for automated deployment. You need to obtain an SSH and vault keys and place these in a `.keys` folder, then:

```
ansible-playbook -s ansible/docker.yaml -i ansible/inventories/production
```