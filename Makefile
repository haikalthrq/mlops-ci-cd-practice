# MLOps CI/CD Practice Makefile

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install flake8 pytest pytest-cov

format:
	flake8 app/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 app/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test:
	@if [ -d "tests" ]; then \
		echo "Running tests..."; \
		python -m pytest tests/ -v --tb=short; \
	else \
		echo "No tests directory found, skipping tests."; \
	fi

train:
	@if [ -f "train.py" ]; then \
		echo "Training model..."; \
		python train.py; \
	else \
		echo "train.py not found, skipping training."; \
	fi

eval:
	@if [ -f "eval.py" ]; then \
		echo "Evaluating model..."; \
		python eval.py; \
	else \
		echo "eval.py not found, skipping evaluation."; \
	fi

update-branch:
	@echo "Configuring git..."
	git config --global user.name "$(USER_NAME)"
	git config --global user.email "$(USER_EMAIL)"
	@echo "Git configured successfully"

deploy:
	@echo "Deploying to Hugging Face Spaces..."
	@echo "Checking HF token..."
	@if [ -z "$(HF_TOKEN)" ]; then \
		echo "❌ Error: HF token is empty!"; \
		echo "Please check that HF_TOKEN secret is set in GitHub repository"; \
		exit 1; \
	else \
		echo "✅ HF token is present"; \
	fi
	pip install huggingface_hub[cli]
	huggingface-cli login --token "$(HF_TOKEN)"
	@echo "🚀 Uploading main app file..."
	huggingface-cli upload haikalthrq/mlops-ci-cd-practice ./app.py app.py --repo-type=space --commit-message="Deploy main app file"
	@echo "📁 Uploading model file..."
	huggingface-cli upload haikalthrq/mlops-ci-cd-practice ./model/drug_pipeline.skops model/drug_pipeline.skops --repo-type=space --commit-message="Upload model file"
	@echo "📋 Uploading requirements..."
	huggingface-cli upload haikalthrq/mlops-ci-cd-practice ./requirements.txt requirements.txt --repo-type=space --commit-message="Upload requirements"
	@echo "📄 Uploading README..."
	huggingface-cli upload haikalthrq/mlops-ci-cd-practice ./README.md README.md --repo-type=space --commit-message="Upload README"
	@echo "✅ Deployment completed!"

run:
	python app.py

.PHONY: install format test train eval update-branch deploy run