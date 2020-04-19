# ExpressVPN - Python Wrapper and Rest API (LINUX)

Full bash documentation: [https://www.expressvpn.com/support/vpn-setup/app-for-linux/](https://www.expressvpn.com/support/vpn-setup/app-for-linux/)

Fork purpose : add a RestFul web service using pyhton library 

## Installation with PyPI

If the command `expressvpn` is already installed on your Ubuntu then just run this:

```
sudo python setup.py install
```

## Download/Install the package on the official website

The package DEB for Ubuntu 64bits 2.3.4 is already part of the repository. For another OS, please refer to:
[https://www.expressvpn.com/support/vpn-setup/app-for-linux/#download](https://www.expressvpn.com/support/vpn-setup/app-for-linux/#download)

```bash
git clone git@github.com:ezekri/expressvpn-python.git evpn && cd evpn
sudo dpkg -i expressvpn_2.3.4-1_amd64.deb # will install the binaries provided by ExpressVPN
sudo pip install . # will install it as a package. Or install it within a virtualenv (better option).
```

## Set up expressvpn

You can find your activation key here: [https://www.expressvpn.com/setup](https://www.expressvpn.com/setup).

```bash
expressvpn activate # paste your activate key and press ENTER.
expressvpn preferences set send_diagnostics false
```

After login and to logout, simply run:

```bash
expressvpn logout
```

NOTE that you will have to activate `expressvpn` again if you logout.

## Python bindings

### Connect

Bash
```bash
expressvpn connect
```

Python
```python
from expressvpn import connect
connect()
```

### Connect with alias

Bash
```bash
expressvpn connect [ALIAS]
```

Python
```python
from expressvpn import connect_alias
connect_alias(alias: str)
```

### Random connect

Python
```
from expressvpn.wrapper import random_connect
random_connect()
```

### Disconnect

Bash
```bash
expressvpn disconnect
```

Python
```python
from expressvpn import disconnect
disconnect()
```

## IP auto switching

Sometimes websites like Amazon or Google will ban you after too many requests. It's easy to detect because your script will fail for some obscure reason. Most of the time, if the HTML contains the word captcha or if the websites returns 403, it means that you probably got banned. But don't panic, you can use a VPN coupled with IP auto switching. Here's an example of a scraper doing IP auto switching:

```python
from expressvpn import wrapper
import logging

def main():
    while True:
        try:
            scrape()
        except BannedException as be:
            logging.info('BANNED EXCEPTION in __MAIN__')
            logging.info(be)
            logging.info('Lets change our PUBLIC IP GUYS!')
            change_ip()
        except Exception as e:
            logging.error('Exception raised.')
            logging.error(e)


def change_ip():
    max_attempts = 10
    attempts = 0
    while True:
        attempts += 1
        try:
            logging.info('GETTING NEW IP')
            wrapper.random_connect()
            logging.info('SUCCESS')
            return
        except Exception as e:
            if attempts > max_attempts:
                logging.error('Max attempts reached for VPN. Check its configuration.')
                logging.error('Browse https://github.com/philipperemy/expressvpn-python.')
                logging.error('Program will exit.')
                exit(1)
            logging.error(e)
            logging.error('Skipping exception.')
 ```

## Use of web service
Add this line to /etc/rc.local to enable service auto start:
```bash
/usr/bin/python /home/user/EXPRESSVPN-PYTHON-PATH/expressvpn/piexpressweb.py &
```

You can use Rest API client, e.g : Postman or one of the many existing mobile apps
I'm using Android app named : Advanced Rest API client. These sceenshots are coming from this app:

<img src="https://github.com/ezekri/expressvpn-python/blob/master/Screenshot1.jpg" width="50%" height="50%">
<img src="https://github.com/ezekri/expressvpn-python/blob/master/Screenshot2.jpg" width="50%" height="50%">




