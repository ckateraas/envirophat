# Prometheus and EnviroPhat Server (PEPS)

This repo contains fragments needed to export metrics to Prometheus from Pimoroni's EnviroPhat, running on a RaspberryPi Zero on Raspberry OS.
Soldering instructions and how to install the OS are not covered here.

## Packages 

You can use Pimoroni's own Bash script to install all dependencies and set all needed configurations:

```sh
curl https://get.pimoroni.com/envirophat | bash
```

Or go for a more manual install. If you do the manual install, then you need the following packages:

```
apt install -y python3-pip \
python3-smbus \
raspi-gpio \
i2c-dev \
i2c-bcm2708 \
python3-envirophat \
```

And then enable I2C, which the EnviroPhat requires. This is done with `raspi-config`.

## Install the server

There's not much to install, just move the `peps.py` file to the place where the systemd service file expects it to be.

```sh
nstall --target-directory=/usr/local/bin peps.py
```

## systemd service file

This repo includes a `.service` file which tells systemd how to manage the process.
Add the serivce file, `peps.service`, in `/etc/systemd/system/ .
Then start the service:

```sh
systemctl enable peps
systemctl start --now peps
```
## Metrics endpoint

You can now view the metrics on `<RPi Zero IP>:8000`.
If you want to change the port or interface, then just edit `peps.py`.
