docker build -t rails-console-dockerfile .

docker run -it --rm -v $(pwd):/app -p 3000:3000 rails-console-dockerfile

# then run:

git clone https://github.com/masahiro331/CVE-2020-8165.git
cd CVE-2020-8165/
bundle install --path venndor/bundle
bundle exec rails console