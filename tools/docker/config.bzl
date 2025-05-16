"""
A quick and dirty Docker configuration repo extension
"""

BUILD_TMPL = """
package(default_visibility=["//visibility:public"])

# Platforms are a Bazel mechanism for activating groups of constraints. Targets
# can mark themselves as requiring constraints to be satisfied in order to build
# or run. If a target is incompatible with the current constrait set, it will be
# skipped automatically.
platform(
    name = "platform",
    constraint_values = [
        ":docker_yes",
    ],
)

# An underlying constraint used to establish that having (or not having) Docker
# are two related and exclusive states.
constraint_setting(
    name = "_has_docker",
    default_constraint_value = ":docker_{{FLAG}}",
)

constraint_value(
    name = "docker_yes",
    constraint_setting = ":_has_docker",
)

constraint_value(
    name = "docker_no",
    constraint_setting = ":_has_docker",
)
"""

def _config_repo_impl(rctx):
    rctx.watch("/bin/docker")
    rctx.watch("/usr/bin/docker")
    rctx.watch("/usr/local/bin/docker")
    rctx.watch("/var/run/docker.sock")

    docker = rctx.which("docker")
    flag = "yes" if docker else "no"

    rctx.file("BUILD.bazel", BUILD_TMPL.replace("{{FLAG}}", flag))

docker_config = repository_rule(
    implementation = _config_repo_impl,
)

def _config_extension(mctx):
    docker_config(
        name = "docker_config",
    )

extension = module_extension(
    implementation = _config_extension,
)
