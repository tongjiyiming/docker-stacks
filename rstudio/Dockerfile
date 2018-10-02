FROM rocker/rstudio-stable:latest
## Work-around to make Docker Hub use the Dockerfile
## from https://github.com/rocker-org/rocker-versioned/tree/master/rstudio

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    wget \
    git-core \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    gdal-bin \
    proj-bin \
    libgdal-dev \
    libproj-dev \
    libgeos-dev \
    libudunits2-dev \
    libcairo2-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

COPY install_libs.R /tmp
RUN Rscript /tmp/install_libs.R
