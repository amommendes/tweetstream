FROM puckel/docker-airflow:1.10.9

USER root

RUN update-ca-certificates -f \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y \
    wget \
    git \
    libatlas3-base \
    libopenblas-base \
  && apt-get clean

RUN mkdir -p /usr/share/man/man1
RUN apt-get install -y default-jre

# SPARK
ENV SPARK_VERSION=spark-3.0.1
RUN cd /usr/ \
    && wget "http://apache.mirrors.spacedump.net/spark/$SPARK_VERSION/$SPARK_VERSION-bin-hadoop2.7.tgz" \
    && tar xzf $SPARK_VERSION-bin-hadoop2.7.tgz \
    && rm $SPARK_VERSION-bin-hadoop2.7.tgz \
    && mv $SPARK_VERSION-bin-hadoop2.7 spark

ENV SPARK_HOME /usr/spark
ENV PATH="/usr/spark/bin:${PATH}"
ENV SPARK_MAJOR_VERSION 3
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$SPARK_HOME/python/:$PYTHONPATH

RUN mkdir -p /usr/spark/work/ \
    && chmod -R 777 /usr/spark/work/

ENV SPARK_MASTER_PORT 7077

USER airflow