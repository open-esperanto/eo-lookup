#!/usr/bin/env bash

distTarget=${1}

root=$(dirname ${0})
default="${root}/default.nix"
twine=$(nix-build -A pkgs.python3Packages.twine --no-out-link ${default})
pythonDist=$(nix-build -A ${distTarget} --no-out-link ${default})

printf "Publishing packages:\n"
find ${pythonDist}/*

printf "PyPI username: "
read -s username
printf "\nPyPI password: "
read -s password
printf "\n"

${twine}/bin/twine upload --username ${username} --password ${password} ${pythonDist}/*
