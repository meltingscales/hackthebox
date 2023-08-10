#!/bin/ash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-name-resolve --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo "not up" && sleep .2; done

DEVKEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 20 | head -n 1)
PRODKEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 20 | head -n 1)

mysql -u root << EOF
CREATE DATABASE cybercore;

CREATE TABLE cybercore.keystore (
  kid int(11) NOT NULL AUTO_INCREMENT,
  secret varchar(255) NOT NULL,
  PRIMARY KEY (kid)
);

CREATE TABLE cybercore.users (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username varchar(255) NOT NULL,
  password varchar(255) NOT NULL
);

INSERT INTO cybercore.users VALUES (1, '$(openssl rand -base64 30)', '$(openssl rand -base64 24 | md5sum )');

INSERT INTO cybercore.keystore VALUES (1,'${DEVKEY}');
INSERT INTO cybercore.keystore VALUES (2,'${PRODKEY}');

CREATE USER 'user'@'127.0.0.1' IDENTIFIED BY 'M@k3l@R!d3s$';

GRANT SELECT ON cybercore.* TO 'user'@'127.0.0.1';
FLUSH PRIVILEGES;
EOF

/usr/bin/supervisord -c /etc/supervisord.conf