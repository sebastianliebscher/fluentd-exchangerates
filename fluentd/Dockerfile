FROM fluent/fluentd:v1.15.2-debian-1.0
USER root
RUN gem install fluent-plugin-elasticsearch --no-document --version 5.2.3 \
    && gem sources --clear-all \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem
USER fluent
