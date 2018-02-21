# Nebula
Sends Slack notification when IMAX ticket sale is available for a movie.

## Usage

First you need to set up an [incoming webhook integration](https://my.slack.com/services/new/incoming-webhook/) in your Slack workspace. Then spin up a container:

```
docker run -d --name moviebot --restart=always \
-e MOVIE_NAME="Avengers Sonsuzluk Taşı" \
-e MOVIE_URL="https://www.cinemaximum.com.tr/avengers-sonsuzluk-savasi-filmi" \
-e SLACK_WEBHOOK_URL="https://hooks.slack.com/services/hjsa64jnVTFkLDJ4kbRLoU9" \
akoken/nebula:latest
```
