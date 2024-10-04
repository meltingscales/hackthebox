# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update -qq && apt-get install -y \
    curl \
    gnupg2 \
    build-essential \
    libssl-dev \
    libreadline-dev \
    zlib1g-dev \
    libpq-dev \
    libsqlite3-dev \
    sqlite3 \
    nodejs \
    yarn \
    git

# Install RVM (Ruby Version Manager)
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import - \
    && curl -sSL https://rvm.io/pkuczynski.asc | gpg --import - \
    && curl -sSL https://get.rvm.io | bash -s stable

# Install Ruby 2.6.3 using RVM
RUN /bin/bash -l -c "rvm install 2.6.3"

# Set Ruby 2.6.3 as the default version
RUN /bin/bash -l -c "rvm use 2.6.3 --default"

# Install Bundler
RUN /bin/bash -l -c "gem install bundler"

# Clone the CVE-2020-8165 repository
RUN git clone https://github.com/masahiro331/CVE-2020-8165.git

# Set working directory inside the container
WORKDIR /CVE-2020-8165

# Install Gems into vendor/bundle
RUN /bin/bash -l -c "bundle install --path vendor/bundle"

# Expose port 3000 for Rails server if needed (optional)
EXPOSE 3000

# Set default command to open a bash shell
CMD ["/bin/bash"]
