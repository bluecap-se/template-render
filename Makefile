define HELP_MESSAGE
Usage: make [COMMAND]

Commands:
	templates   Compiles templates
	styles      Compiles CSS
	clean       Removes built files
	help        Display this help message.
endef

export HELP_MESSAGE

build_dir          := ./build/
source_html        := $(wildcard src/templates/*/*.tmpl)
#build_html         := $(patsubst src/%.tmpl, build/%.html, $(wildcard src/templates/*/*.tmpl))

.PHONY: templates help


templates: $(source_html)

	mkdir -p $(patsubst src/%.tmpl,build/%.html, $<)
	python render_template.py $< > $(patsubst src/%.tmpl,build/%.html, $<)


clean:

	rm -rf $(build_dir)


help:

	@echo "$$HELP_MESSAGE"
