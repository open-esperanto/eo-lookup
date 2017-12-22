rec {
  pkgsOriginal = import <nixpkgs> {};
  pkgsSrc = pkgsOriginal.fetchzip {
    url = "https://github.com/NixOS/nixpkgs/archive/a44bbc72e6b3d7c3e9619e5c74de6b6261a8e4c8.zip";
    sha256 = "1p67601l1qblka8v8w2qfiivvns55jd3wdvwvpvcdbhhs9fbl13w";
  };
  pkgs = import (pkgsSrc) {};
  python3 = pkgs.python36.withPackages (ps: with ps; [ setuptools wheel ]);

  revoDist = pkgs.fetchzip {
    url = "https://github.com/open-esperanto/revo-archive/raw/master/revosql_2017-12-15.zip";
    sha256 = "0nlppag5v61r8y96ac4lpafzzaychlsx5sy5fag7qz3b2hqar6l7";
  };

  revoLicense = pkgs.fetchurl {
    url = "https://raw.githubusercontent.com/open-esperanto/revo-archive/master/LICENSE";
    sha256 = "0lx9mbjyabmhz3ymqg2y998n4n7ssjryflv3qm1s2rlz51zmcahv";
  };

  pyLicenseMit = "License :: OSI Approved :: MIT License";

  eoLookupRevoSrc = pkgs.stdenv.mkDerivation rec {
    name = "eo-lookup-revo-src";
    src = ./.;
    generate = ./scripts/generate.py;
    inherit python3 revoDist revoLicense;
    builder = builtins.toFile "builder.sh" ''
      source $stdenv/setup
      mkdir $out
      export DB_PATH=$revoDist/revo.db
      $python3/bin/python $generate > $out/eo_lookup_revo.json
      cp $src/eo-lookup-revo/eo_lookup_revo.py $out
      cp $src/eo-lookup-revo/README.rst $out
      cp $src/eo-lookup-revo/setup.py $out
      cp $src/eo-lookup-revo/setup.cfg $out
      cp $revoLicense $out/LICENSE.txt
    '';
  };

  eoLookupSrc = pkgs.stdenv.mkDerivation rec {
    name = "eo-lookup-src";
    src = ./.;
    generate = ./scripts/generate.py;
    inherit python3 revoDist revoLicense;
    builder = builtins.toFile "builder.sh" ''
      source $stdenv/setup
      mkdir $out
      cp $src/eo-lookup/eo_lookup.py $out
      cp $src/eo-lookup/setup.py $out
      cp $src/eo-lookup/setup.cfg $out
      cp $src/README.rst $out
      cp $src/LICENSE $out/LICENSE.txt
    '';
  };

  pythonDist = src : pkgs.stdenv.mkDerivation rec {
    name = "python-dist";
    inherit src python3;
    builder = builtins.toFile "builder.sh" ''
      source $stdenv/setup
      cp -R --no-preserve=mode,ownership $src/* .
      export SOURCE_DATE_EPOCH=315532800
      $python3/bin/python setup.py sdist bdist_wheel
      mkdir $out
      cp dist/* $out
    '';
  };

  eoLookupDist = pythonDist eoLookupSrc;
  eoLookupRevoDist = pythonDist eoLookupRevoSrc;

}