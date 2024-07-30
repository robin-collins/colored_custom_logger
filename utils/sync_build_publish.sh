#!/bin/bash

check_and_activate_pyenv_ccl() {
    # Check if the pyenv ccl is already active
    if [[ "$(pyenv version-name)" == "ccl" ]]; then
        echo 'pyenv ccl is already active'
        return 0
    else
        echo 'activating pyenv ccl'
        pyenv activate ccl
        return $?
    fi
}

build_python_package() {
    local package_dir="${1:?Package directory must be provided}"
    local build_output
    local build_status

    # Change to the package directory
    if ! cd "${package_dir}"; then
        echo "Error: Unable to change to directory ${package_dir}" >&2
        return 1
    fi

    # Ensure the directory contains a pyproject.toml or setup.py file
    if [[ ! -f "pyproject.toml" && ! -f "setup.py" ]]; then
        echo "Error: Neither pyproject.toml nor setup.py found in ${package_dir}" >&2
        return 1
    fi

    # Clean up any existing build artifacts
    echo "Cleaning up existing build artifacts..."
    rm -rf build dist *.egg-info

    # Build the package
    echo "Building the Python package..."
    build_output=$(python -m build 2>&1)
    build_status=$?

    if [[ ${build_status} -ne 0 ]]; then
        echo "Error: Package build failed" >&2
        echo "Build output:" >&2
        echo "${build_output}" >&2
        return ${build_status}
    fi

    # Check if the build was successful
    if [[ -d "dist" && "$(ls -A dist)" ]]; then
        echo "Package built successfully"
        echo "Built artifacts:"
        ls -l dist
    else
        echo "Error: No distribution files found after build" >&2
        return 1
    fi

    return 0
}

# Usage example:
# build_python_package "/path/to/your/package"
#
# Check the return status
# if [[ $? -eq 0 ]]; then
#     echo "Build successful"
# else
#     echo "Build failed"
# fi

upload_to_pypi() {
  twine upload dist/*
}

main() {
  CURRENT_DIR=$(pwd)
  SCRIPT_DIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
  PROJECT_DIR=$(cd -- "${SCRIPT_DIR}/.." &>/dev/null && pwd)

  # change to PROJECT_DIR
  cd "${PROJECT_DIR}" || exit
  
  check_and_activate_pyenv_ccl;
  python utils/sync_versions.py
  # check that the last command exited successfully
  if [ $? -ne 0 ]; then
      echo 'sync_versions.py failed'
      exit 1
  else
      echo 'sync_versions.py succeeded'
      build_python_package "${PROJECT_DIR}"
      # Check the return status
      if [[ $? -eq 0 ]]; then
          echo "Build successful"
          upload_to_pypi
      else
          echo "Build failed"
      fi
  fi
  
}

main;

