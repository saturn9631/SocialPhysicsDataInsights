{
	description = "A very basic flake";

	inputs = {
		nixpkgs.url = "github:nixos/nixpkgs?ref=nixpkgs-25.05-darwin";
	};

	outputs = { self, nixpkgs }: 
	let
			system = "x86_64-linux";
			#pkgs = nixpkgs.legacyPackages.${system};
			pkgs = import nixpkgs { inherit system; config.allowUnfree = true; };
	in 
	{
			devShells.${system}.default = 
				pkgs.mkShell {
					buildInputs = with pkgs; [
						jupyter-all
						python313Full
						python313Packages.cython
						python313Packages.pycuda
						python313Packages.ipython
						python313Packages.numpy
						python313Packages.pandas
						python313Packages.scipy
						python313Packages.sympy
						python313Packages.networkx
						python313Packages.torch
						python313Packages.matplotlib
						python313Packages.transformers
					];
				};
	};
}
