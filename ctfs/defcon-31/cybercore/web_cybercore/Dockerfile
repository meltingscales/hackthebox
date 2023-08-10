FROM node:alpine

# Install packages
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories
RUN apk add --update --no-cache supervisor mariadb mariadb-client openssl

# Setup app
RUN mkdir -p /app

# Add application
WORKDIR /app
COPY challenge .

# Install dependencies
RUN yarn

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# Setting up Flag
COPY --chown=root flag.txt /flag.txt

# Expose the port node-js is reachable on
EXPOSE 1337

# Populate database and start supervisord
COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
