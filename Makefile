CLEAN_FILES ?= .coding-aider-plans/* .aider.chat.history.md

PROMPT_FILE ?= .aider.prompt.md

TEST_MODEL ?= aider-sonnet
TEST_CHAT_MODE ?= --chat-mode code --edit-format diff
TEST_COMMAND_ARGS ?= --no-fancy-input --no-pretty --no-detect-urls --no-check-update --no-suggest-shell-commands --verbose --map-tokens 0 $(TEST_CHAT_MODE)
TEST_READ_FILES ?= --read docs/ai/plan.md --read docs/practice-exercises.md --read docs/chain_of_responsability.md --read docs/refactor/smells/large-class.md
TEST_COMMAND ?= $(TEST_MODEL) $(TEST_READ_FILES) $(TEST_COMMAND_ARGS)

RESULTS_DATE ?= $(shell date +%Y-%m-%d_%H-%M-%S)
RESULTS_DIR ?= docs/prompt-driven-design/$(RESULTS_DATE)


run: clean
	@echo "Running tests..."
	bash -ic "$(TEST_COMMAND) --message \"\$$(cat '$(PROMPT_FILE)')\""

save:
	@echo "Saving results..."
	current_version=$$(cat VERSION); \
	new_version=$$(echo "$$current_version" | awk -F. '{OFS="."; $$NF+=1; print}'); \
	echo $$new_version > VERSION; \
	mkdir -p $(RESULTS_DIR); \
	cp -R .coding-aider-plans $(RESULTS_DIR); \
	cp .aider.chat.history.md $(RESULTS_DIR); \
	cp .aider.prompt.md $(RESULTS_DIR); \
	git add $(RESULTS_DIR) -f; \
	git add VERSION; \
	git commit -m "saved $(RESULTS_DATE)"; \
	git tag -a "$$new_version" -m "saved $(RESULTS_DATE)";

.PHONY: all clean
clean:
	rm -rf $(CLEAN_FILES)
