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
    repository = "sammy-tri/libezgripper",
    commit = "a2afce144e8b1fe7e82b35bf8a25172429df1783",
    sha256 = "78795ad1ac2428cff176a714a20e4a94a922535f0820ea5f20601b47293c2651",  # noqa
    build_file = "//tools/libezgripper:package.BUILD.bazel",
)
