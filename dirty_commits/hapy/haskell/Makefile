UNAME := $(shell uname)
SED_COMMAND := $(shell printf '/extra-libraries/ c \\\n  extra-libraries:     HSrts-ghc$(GHC_VERSION)')
all:
	@echo === Building Haskell MyModule ===
	@echo '>>> ./update_libghc_version.sh'
	@./update_libghc_version.sh
	@echo '>>> cabal-1.20 sandbox init'
	@cabal-1.20 sandbox init
	@echo
	@echo '>>> cabal-1.20 install --enable-shared'
	@cabal-1.20 install --enable-shared
	@echo
ifeq ($(UNAME),Linux)
	@echo '>>> cp dist/dist-sandbox-*/build/*.so ../python'
	@cp dist/dist-sandbox-*/build/*.so ../python
else ifeq ($(UNAME),Darwin)
	@echo '>>> cp dist/dist-sandbox-*/build/*.dylib ../python'
	@cp dist/dist-sandbox-*/build/*.dylib ../python
else
	@echo 'Unsupported OS!'
endif

clean:
	@echo === Cleaning Haskell Build ===
	rm -f cabal-1.20.sandbox.config
	rm -rf .cabal-1.20-sandbox
	rm -rf dist
