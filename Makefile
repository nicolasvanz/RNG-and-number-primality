.ONESHELL:
SHELL := /bin/bash


GREEN=\033[0;32m
RED=\033[0;31m
NC=\033[0m

TEST_OUTPUT?=results.csv
PLOT_OUTPUT?=plot.pdf
VENVNAME=venv
VENVBIN=$(VENVNAME)/bin/

CURR_DIR=$(PWD)
OUTPUT_DIR=$(CURR_DIR)/output

define done
    @echo -e "${GREEN} DONE${NC}"
endef


.PHONY: dependencies
dependencies:
	@echo -e "${GREEN} Installing virtualenv using pip3${NC}"
	@pip3 install virtualenv --user
	$(call done)

.PHONY: setup
setup:
	@echo -e "${GREEN} Creating output folder${NC}"
	@mkdir -p output
	@echo -e "${GREEN} Creating new virtual environment${NC}"
	@python3 -m virtualenv $(VENVNAME)
	@echo -e "${GREEN} Installing requirements${NC}"
	@$(VENVBIN)pip3 install -r requirements.txt
	@echo -e "${GREEN} Virtual environment successfully created!${NC}"
	$(call done)

.PHONY: test
test:
	@echo -e "${GREEN} Running test...${NC}"
	@-$(VENVBIN)python3 test.py $(OUTPUT_DIR)/$(TEST_OUTPUT)
	$(call done)

.PHONY: plot
plot:
	@echo -e "${GREEN} Plotting...${NC}"
	@-$(VENVBIN)python3 plot.py $(OUTPUT_DIR)/$(TEST_OUTPUT) $(OUTPUT_DIR)/$(PLOT_OUTPUT)
	$(call done)


.PHONY: clean
clean:
	@echo -e "${RED} Removing virtual environment${NC}"
	@rm -rf $(VENVNAME)/
	@echo -e "${RED} Removing python cached files${NC}"
	@find . | grep -E "(/__pycache__)" | xargs rm -rf
	@echo -e "${RED} Removing old output files${NC}"
	@rm -rf $(OUTPUT_DIR)/
	$(call done)