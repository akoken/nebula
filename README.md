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

If you have a Kubernetes cluster, you can also use deploy.yml file to run the application. Please do not forget to update environment variables in yaml file before you run the following command.

```
kubectl create -f deploy.yml
```

## How it works
This application requests movie web page every five minutes. If it finds 'IMAX' in the response text, it triggers the Slack webhook url that you indicated.

<img src="https://camo.githubusercontent.com/e0a2d3d0a9754f70bc26a40adf7aafc5ff5b5fc0/68747470733a2f2f336e706f7274616c766864736c63366d666e6a6b366638772e626c6f622e636f72652e77696e646f77732e6e65742f626c6f672f323031372f53637265656e73686f742e706e67" data-canonical-src="https://3nportalvhdslc6mfnjk6f8w.blob.core.windows.net/blog/2017/Screenshot.png" width="277" height="600" />
