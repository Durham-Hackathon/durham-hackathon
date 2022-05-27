default: build

all: install build

h help:
	@grep '^[a-z]' Makefile

install:
	bundle config --local path vendor/bundle
	bundle install --full-index

build:
	JEKYLL_ENV=production bundle exec jekyll build --trace

upgrade:
	bundle update

s serve:
	bundle exec jekyll serve --trace --livereload --baseurl ''

build-dev:
	bundle exec jekyll build

build-prod:
	JEKYLL_ENV=production bundle exec jekyll build
