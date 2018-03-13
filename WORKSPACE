# -*- python -*-

workspace(name = "sake_gripper_driver")

(DRAKE_COMMIT, DRAKE_CHECKSUM) = (
    "604d013ea1fe0c874244c11d0a2df43bba054177",
    "8068e5e152cc5ccbf178abcdf5b9e7164ec9bc87586a53dad1c735f6017215c6",
)
# Before changing the COMMIT, temporarily uncomment the next line so that Bazel
# displays the suggested new value for the CHECKSUM.
# DRAKE_CHECKSUM = "0" * 64

# Download a specific commit of Drake, from github.
http_archive(
    name = "drake",
    sha256 = DRAKE_CHECKSUM,
    strip_prefix = "drake-{}".format(DRAKE_COMMIT),
    urls = [x.format(DRAKE_COMMIT) for x in [
        "https://github.com/RobotLocomotion/drake/archive/{}.tar.gz",
    ]],
)

load("@drake//tools/workspace:default.bzl", "add_default_repositories")

# WARNING: We allow `vtk`, but should take care to avoid linking in multiple
# versions of VTK!
add_default_repositories()

load("@drake//tools/workspace:github.bzl", "github_archive")

github_archive(
    name = "libezgripper",
    repository = "SAKErobotics/libezgripper",
    commit = "58a9beaa87925babba47295afa9416eaef16c9a2",
    sha256 = "a5d94f313824cfe6f78904c754cdaa3c632ae74ea626078a9fe58cab43b84128",  # noqa
    build_file = "//tools/libezgripper:package.BUILD.bazel",
)
