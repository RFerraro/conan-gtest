from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="gtest:shared", pure_c=False)
    filtered_builds = []
    for settings, options in builder.builds:
        if settings["compiler"] == "Visual Studio":
            pdbOptions = options.copy()
            pdbOptions.update({"gtest:include_pdbs": "True"})
            filtered_builds.append([settings, pdbOptions])
        
        filtered_builds.append([settings, options])

    builder.builds = filtered_builds
    builder.run()

