{
  description = "A shell with Hugo and Python";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          requests
        ]);
        helloPackage = pkgs.python3Packages.buildPythonPackage {
          pname = "hello";
          version = "0.1.0";
          src = ./.;
          format = "pyproject";
          
          nativeBuildInputs = with pkgs.python3Packages; [
            setuptools
          ];
        };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv
          ];
        };
        defaultPackage = helloPackage;
      });
}
