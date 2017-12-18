#!/usr/bin/env bash

root=$(dirname ${0})
default="${root}/default.nix"
twine=$(nix-build -A pkgs.twine --no-out-link ${default})
pythonDist=$(nix-build -A pythonDist --no-out-link ${default})

printf "PyPI username: "
read -s username
printf "\nPyPI password: "
read -s password
printf "\n"

${twine}/bin/twine upload --username ${username} --password ${password} ${pythonDist}/*
