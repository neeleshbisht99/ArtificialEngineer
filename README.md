Artifical Engineer represents a cutting-edge autonomous agent designed to navigate the complexities of software engineering.

The easiest way to run Artifical Engineer is inside a Docker container.

To start the app, run these commands, replacing `$(pwd)/workspace` with the path to the code you want to work with.

```bash
# Your OpenAI API key, or any other LLM API key
export LLM_API_KEY="sk-..."

# The directory you want artificialEngineer to modify. MUST be an absolute path!
export WORKSPACE_BASE=$(pwd)/workspace

docker run \
    -e LLM_API_KEY \
    -e WORKSPACE_MOUNT_PATH=$WORKSPACE_BASE \
    -v $WORKSPACE_BASE:/opt/workspace_base \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3000:3000 \
    --add-host host.docker.internal=host-gateway \
    ghcr.io/artificialEngineer/artificialEngineer:0.3.1
```