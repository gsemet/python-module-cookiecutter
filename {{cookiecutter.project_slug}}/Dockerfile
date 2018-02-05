FROM        python:3.6

WORKDIR     /app
ADD         Pipfile* Makefile /app/
COPY        deps/    /app/deps/
# Disable PBR try to read version from git information for modules in the deps/ directory
# If PBR cannot find metadata information (only for sdist/bdist/wheel packages), it will try
# to find the version according to the git tree, and so try to connect to upstream remote.
# In the case of docker, the upstream is unavailable, thus making PBR failing for no reason,
# since the versionning is actually handled by the git submodule mechanism.
ENV         PBR_VERSION=0.0.1

# Only install dependencies
RUN         make install-local-only-deps

ADD         * /app/

# Only install current package
RUN         make install-local-only-curpackage

# Add here default arguments for the application. Can be overriden by environment variables
# Modify the default entrypoint to execute your command
# ENTRYPOINT  [ "pipenv", "run", "<my-command>"]
