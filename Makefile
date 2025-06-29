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
	@if [ -z "$(HF)" ]; then \
		echo "❌ Error: HF token is empty!"; \
		echo "Please check that HF secret is set in GitHub repository"; \
		exit 1; \
	else \
		echo "✅ HF token is present"; \
	fi
	pip install huggingface_hub[cli]
	huggingface-cli login --token "$(HF)"
	mkdir -p deploy_temp
	cp -r app/ deploy_temp/
	cp requirements.txt deploy_temp/
	cp README.md deploy_temp/
	cd deploy_temp && \
	git init -b master && \
	git lfs install && \
	git config user.name "GitHub Actions" && \
	git config user.email "actions@github.com" && \
	echo "*.pkl filter=lfs diff=lfs merge=lfs -text" > .gitattributes && \
	echo "*.joblib filter=lfs diff=lfs merge=lfs -text" >> .gitattributes && \
	echo "*.h5 filter=lfs diff=lfs merge=lfs -text" >> .gitattributes && \
	echo "*.bin filter=lfs diff=lfs merge=lfs -text" >> .gitattributes && \
	echo "*.safetensors filter=lfs diff=lfs merge=lfs -text" >> .gitattributes && \
	git add . && \
	git commit -m "Deploy ML app to Hugging Face Spaces" && \
	git remote add space https://haikalthrq:$(HF)@huggingface.co/spaces/haikalthrq/mlops-ci-cd-practice && \
	git push --force space master
	@echo "Deployment completed!"

run:
	python app/app.py

.PHONY: install format test train eval update-branch deploy run