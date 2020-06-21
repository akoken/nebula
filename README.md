# Nebula
Sends Slack notification when IMAX ticket sale is available for a movie.

> This application currently supports Cinemaximum in Turkey. You should implement your own parsing algorithm for another cinema company.

## Usage

First you need to set up an [incoming webhook integration](https://my.slack.com/services/new/incoming-webhook/) in your Slack workspace. Then spin up a container:

```
docker run -d --name moviebot --restart=always \
-e MOVIE_NAME="Avengers Sonsuzluk Taşı" \
-e MOVIE_URL="https://www.cinemaximum.com.tr/avengers-sonsuzluk-savasi-filmi" \
-e SLACK_WEBHOOK_URL="https://hooks.slack.com/services/hjsa64jnVTFkLDJ4kbRLoU9" \
akoken/nebula:latest
```
## Kubernetes

If you have a Kubernetes cluster, you can also use deploy.yml file to run the application. You just need to update environment variables in yaml file before you run the following command:

```
kubectl create -f deploy.yml
```

## How it works
This application requests movie web page every five minutes. If it finds 'IMAX' in the response text, it triggers the Slack webhook url that you indicated.
