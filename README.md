# MLOps CI/CD Practice

This project demonstrates the implementation of a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Machine Learning application using GitHub Actions and Hugging Face Spaces.

## Project Structure

```
mlops-ci-cd-practice/
├── .github/
│   └── workflows/
│       ├── ci.yml          # CI workflow for linting and testing
│       └── cd.yml          # CD workflow for deployment
├── app/
│   └── app.py              # Gradio application
├── data/                   # Directory for raw or processed data
├── model/                  # Directory for trained machine learning models
├── notebooks/
│   └── development.ipynb   # Jupyter notebook for exploration and training
├── results/                # Directory for evaluation results or visualizations
├── Makefile                # Makefile for managing project commands
├── requirements.txt        # List of project dependencies
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- GitHub account
- Hugging Face account

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/username/mlops-ci-cd-practice.git
   cd mlops-ci-cd-practice
   ```

2. Install the required dependencies:
   ```
   make install
   ```

### Running the Application

To run the Gradio application, use the following command:
```
make run
```

### CI/CD Workflows

- **Continuous Integration (CI)**: The CI workflow is defined in `.github/workflows/ci.yml`. It runs on every push and pull request to ensure code quality through linting.
  
- **Continuous Deployment (CD)**: The CD workflow is defined in `.github/workflows/cd.yml`. It deploys the Gradio app to Hugging Face Spaces whenever changes are pushed to the main branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.