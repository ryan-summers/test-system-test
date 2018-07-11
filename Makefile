

all: unit integration manufacturing regression

unit:
	mkdir -p build/unit/
	gcc src/unit/basic_unit.c -o build/unit/basic_unit_test

integration:
	mkdir -p build/integration/
	gcc src/integration/basic_integration.c -o build/integration/basic_integration_test

regression:
	mkdir -p build/regression/
	gcc src/regression/basic_regression.c -o build/regression/basic_regression_test
	
manufacturing:
	mkdir -p build/manufacturing/
	gcc src/manufacturing/basic_manufacturing.c -o build/manufacturing/basic_manufacturing_test
