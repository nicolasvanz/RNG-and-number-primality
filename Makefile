.ONESHELL:
SHELL := /bin/bash


GREEN=\033[0;32m
RED=\033[0;31m
NC=\033[0m

VENVNAME=venv
VENVBIN=$(VENVNAME)/bin/

CURR_DIR=$(PWD)
OUTPUT_DIR=$(CURR_DIR)/output
RNG_OUTPUT=$(OUTPUT_DIR)/rng_output.csv
PRIMALITY_OUTPUT=$(OUTPUT_DIR)/primality_output.csv
PRIMALITY_FALSE_POSITIVES=$(OUTPUT_DIR)/false_positives.txt
PRIMALITY_PRIMES=$(OUTPUT_DIR)/primes.txt

PLOT_RNG_OUTPUT=$(OUTPUT_DIR)/rng.pdf
PLOT_PRIMALITY_OUTPUT=$(OUTPUT_DIR)/primality.pdf

define done
    @echo -e "${GREEN} DONE${NC}"
endef

define plot
	@echo -e "${GREEN} Plotting...${NC}"
	@-$(VENVBIN)python3 plot.py ${1} ${2} ${3} ${4}
endef

.PHONY: dependencies
dependencies:
	@echo -e "${GREEN} Installing virtualenv using pip3${NC}"
	@pip3 install virtualenv --user
	$(call done)

.PHONY: setup
setup:
	@echo -e "${GREEN} Creating new virtual environment${NC}"
	@python3 -m virtualenv $(VENVNAME)
	@echo -e "${GREEN} Installing requirements${NC}"
	@$(VENVBIN)pip3 install -r requirements.txt
	@echo -e "${GREEN} Virtual environment successfully created!${NC}"
	$(call done)

.PHONY: testrng
testrng:
	@echo -e "${GREEN} Running Random Number Generator test...${NC}"
	@-$(VENVBIN)python3 rng_test.py $(RNG_OUTPUT)
	$(call done)

.PHONY: testprime
testprime:
	@echo -e "${GREEN} Running Primality test...${NC}"
	@-$(VENVBIN)python3 primality_test.py $(PRIMALITY_OUTPUT) $(PRIMALITY_FALSE_POSITIVES) $(PRIMALITY_PRIMES)
	$(call done)

.PHONY: plotrng
plotrng:
	$(call plot, $(RNG_OUTPUT), $(PLOT_RNG_OUTPUT), 1, "Random number Generators")
	$(call done)

.PHONY: plotprime
plotprime:
	$(call plot, $(PRIMALITY_OUTPUT), $(PLOT_PRIMALITY_OUTPUT), 1000000, "Prime number generators")
	$(call done)

.PHONY: clean
clean:
	@echo -e "${RED} Removing virtual environment${NC}"
	@rm -rf $(VENVNAME)/
	@echo -e "${RED} Removing python cached files${NC}"
	@find . | grep -E "(/__pycache__)" | xargs rm -rf
	$(call done)