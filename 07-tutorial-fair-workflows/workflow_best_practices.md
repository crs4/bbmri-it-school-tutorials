# Workflow Best Practices

## Introduction

Workflows are a powerful way to encapsulate complex data analyses in a reproducible manner. However, to ensure workflows remain usable over time, it's essential to follow best practices for testing, continuous integration, and maintenance. This tutorial will guide you through setting up tests for Galaxy workflows, automating these tests with GitHub Actions, and implementing maintenance automation using LifeMonitor.

> 💡 **Applicability to other workflow systems**
>
> While this tutorial primarily focuses on Galaxy workflows, it's important to note that the best practices discussed here—testing, continuous integration, and maintenance automation—apply to workflows developed with any workflow management system. The specific tools and commands may differ (e.g., replacing `Planemo` with the appropriate testing framework for your workflow manager), but the core principles remain the same. You can adapt these practices to `NextFlow`, `Snakemake`, `CWL`, or any other workflow system by substituting the appropriate tools and commands for your platform.

> 📚 **Galaxy Workflow Best Practices**
>
> For more information about best practices for Galaxy workflows, you can follow this link: [Best Practices for Maintaining Galaxy Workflows](https://planemo.readthedocs.io/en/latest/best_practices_workflows.html)

---

## 1. Keep workflows versioned

Version control is crucial for maintaining reproducibility and tracking changes in your workflows over time. Let's set up a GitHub repository to properly version your Galaxy workflows.

### Create a repository for your workflow

1. Go to [GitHub](https://github.com) and sign in to your account
2. Click on the "+" icon in the upper right corner and select "New repository"
3. Give your repository a name (e.g., `my-galaxy-workflow`)
4. Add a description (optional)
5. Choose "Public" or "Private" visibility
6. Initialize the repository with a README file
7. Click "Create repository"

### Add your workflow to the repository

1. In Galaxy, navigate to the workflow you want to version
2. Click on the workflow menu (⋮) and select "Download" or "Export"
3. Save the workflow as a `.ga` file on your computer
4. Clone your GitHub repository locally:

    ```bash
    git clone https://github.com/yourusername/my-galaxy-workflow.git
    cd my-galaxy-workflow
    ```

5. Copy your workflow file into the repository:

    ```bash
    cp path/to/downloaded/workflow.ga .
    ```

6. Commit and push your workflow:

    ```bash
    git add workflow.ga
    git commit -m "Add initial workflow"
    git push
    ```

> 💡 There are different conventions on how to structure the repository layout. In the Galaxy world, a valid and frequently used layout is the IWC (<https://github.com/galaxyproject/iwc>). This is what we assume to use in this tutorial.

### Versioning best practices

1. **Use Semantic Versioning**: Adopt [Semantic Versioning](https://semver.org/) (e.g., MAJOR.MINOR.PATCH) to clearly communicate changes in your workflows.
2. **Tag Releases**: Use Git tags to mark specific versions of your workflows:

    ```bash
    git tag -a v1.0.0 -m "First stable release"
    git push --tags
    ```

3. **Maintain a Changelog**: Create a CHANGELOG.md file to document changes, improvements, and fixes for each version.

---

## 2. Test your workflows

Testing is a crucial part of workflow development. It ensures that your workflow behaves as expected and continues to work over time despite tool updates or other changes.

### Generate tests for your workflow

Galaxy workflows can be tested using the Planemo tool, which provides a convenient way to create and run tests for your workflows.

> 📚 **Planemo Documentation**
>
> Planemo is a command-line tool that assists in building and testing Galaxy tools and workflows. For detailed information about Planemo's features and usage, visit the [Planemo Documentation](https://planemo.readthedocs.io/en/latest/index.html).

After familiarizing yourself with Planemo, you can follow the tutorial at
[Hands On: Generate Workflow Tests With Planemo](https://training.galaxyproject.org/training-material/topics/fair/tutorials/ro-crate-galaxy-best-practices/tutorial.html#hands-on-generate-workflow-tests-with-planemo-1) as a guideline for adding tests to your workflow.

#### Workflow repository layout example

Once tests are generated with Planemo, your repository should follow a structured organization. A typical workflow repository layout includes:

```
my-galaxy-workflow/
├── workflows/
│   └── my_workflow.ga        # The Galaxy workflow definition
├── test-data/                # Directory containing test inputs and expected outputs
│   ├── input1.fastq
│   ├── input2.fastq
│   └── expected_output.txt
└── .github/
    └── workflows/
        └── test-workflow.yml  # GitHub Actions CI configuration
```

For a real-world example, take a look at the [parallel-accession-download](https://github.com/iwc-workflows/parallel-accession-download) repository.

> ⚠️ WARNING
> Make sure to add all test cases and test data to your repository through git to ensure they are versioned along with your workflow.

---

