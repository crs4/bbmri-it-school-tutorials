# Workflow Best Practices

## Introduction

Workflows are a powerful way to encapsulate complex data analyses in a
reproducible manner. However, to help make works more easily discoverable and
reusable over time, it's essential to follow best practices for testing,
continuous integration, and maintenance. This tutorial will guide you through
setting up tests for workflows -- using the Galaxy workflow you ran earlier as
running example --  automating these tests with GitHub Actions, and implementing
maintenance automation using LifeMonitor.

> 💡 **Applicability to other workflow systems**
>
> While this tutorial primarily focuses on Galaxy workflows, it's important to
> note that the best practices discussed here -- testing, continuous integration,
> and maintenance automation -- apply to workflows developed with any workflow
> management system. The specific tools and commands may differ (e.g., replacing
> `Planemo` with the appropriate testing framework for your workflow manager),
> but the core principles remain the same. You can adapt these practices to
> `NextFlow`, `Airflow`, `CWL`, or any other workflow system by substituting
> the appropriate tools and commands for your platform.

---

## 1. Keep workflows versioned

Version control is crucial for maintaining reproducibility and tracking changes
in your workflows over time. Let's set up a GitHub repository to properly
version your Galaxy workflows.

### Create a repository for your workflow

1. Go to [GitHub](https://github.com) and sign in
2. Click on the "+" icon in the upper right corner and select "New repository"
3. Give your repository a name (e.g., `my-galaxy-workflow`)
4. Add a description (optional)
5. Choose "Public" or "Private" visibility
6. Initialize the repository with a README file
7. Click "Create repository"

### Add your workflow to the repository

1. In Galaxy, navigate to the workflow you want to version
2. Click on the workflow menu (⋮) and select "Download" or "Export"
3. Save the workflow as a file called `workflow.ga` on your computer
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

> 💡 There are different conventions on how to structure the repository layout,
> often specific to the particular workflow type. In the Galaxy world, a
> valid and frequently used layout is the IWC
> (<https://github.com/galaxyproject/iwc>). This is what we assume to use in
> this tutorial.

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
> Planemo is a command-line tool that assists in building and testing Galaxy
> tools and workflows. For detailed information about Planemo's features and
> usage, visit the [Planemo
> Documentation](https://planemo.readthedocs.io/en/latest/index.html).

After familiarizing yourself with Planemo, follow the tutorial at
[Hands On: Generate Workflow Tests With
Planemo](https://training.galaxyproject.org/training-material/topics/fair/tutorials/ro-crate-galaxy-best-practices/tutorial.html#hands-on-generate-workflow-tests-with-planemo-1)
as a guideline for adding tests to your workflow.

#### Workflow repository layout example

Once tests are generated with Planemo, your repository should follow a
structured organization. A typical workflow repository layout includes:

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

For a real-world example, take a look at the
[parallel-accession-download](https://github.com/iwc-workflows/parallel-accession-download)
repository.

> ⚠️ WARNING
> Make sure to add all test cases and test data to your repository through git
> to ensure they are versioned along with your workflow.

---

## 3. Enrich your workflows with metadata

Adding structureed metadata is an important part of applying the FAIR principles
to your workflows. It's good practice to document your workflow thoroughly to
improve understanding, reusability, and FAIRness of your research. A
particularly valuable descriptive metadata model is the [Workflow Testing
RO-Crate](https://crs4.github.io/workflow-testing-ro-crate/) RO-Crate profile,
which was mentioned in the [RO-Crate part of this
tutorial](./RO_crate.md).

> 📚 **Workflow Testing RO-Crate**
>
> While [Workflow RO-Crate](https://about.workflowhub.eu/Workflow-RO-Crate/) is
> a community standard specializing RO-Crate to package an executable workflow
> with its relevant metadata, Workflow Testing RO-Crate further extends this model to
> include workflow testing information -- including test code that is packaged
> with the workflow in the RO-Crate itself, as well as references to "live"
> automated test execution instances that periodically execute the workflow and
> report its passing/failing test execution state. See the reference model specification at
> <https://crs4.github.io/workflow-testing-ro-crate/>

If your workflow repository is structured according to the IWC layout mentioned
earlier, you can use the **`repo2crate`** tool to automatically generate a
metadata skeleton for your workflow, which follows the RO-Crate standard.

> 📚 **`repo2crate`**
>
> The `repo2crate` tool helps automate the process of creating RO-Crate metadata
> for your workflow repository. It analyzes your repository structure to
> automatically extract metadata and generates the necessary RO-Crate metadata files.
> For more information, visit the [repo2crate GitHub repository](https://github.com/crs4/repo2crate).

To use `repo2crate`, follow these steps:

1. Install `repo2crate` using pip:
   You already did this in the [RO-Crate part of the tutorial](./RO_crate.md),
so you can skip the step if you activatf the appropriate venv.

   ```bash
   pip install repo2crate
   ```

2. Run `repo2crate` in the root of your workflow repository:

   ```bash
   repo2crate --repo-url=<your-repo-url>
   ```

The argument `<your-repo-url>` is the URL of your repository (e.g., `https://github.com/iwc-workflows/parallel-accession-download`).  `repo2crate` will integrate this datum in the metadata.

Executing this command adds a file `ro-crate-metadata.json` at the top level
of the repository, with metadata extracted based on the tool's knowledge of the
expected repository
layout.

**📝 Note.** This example shows an important advantage of following conventions
with respect to repository layout and file naming:  automation tools can work to
help you do your work!  If you don't follow conventions, `repo2crate` will not
be successful in its intent to automatically extract metadata.

Additionally, `repo2crate` creates a file containing the *workflow's test data*,
which includes both *input data* and *expected outputs* for validation purposes.
With the addition of these metadata files, your workflow becomes a full
**Workflow Testing RO-Crate**.

> 📚 **The `-o` option**
>
> The `-o` option allows you to specify the output directory and filename for
> the generated RO-Crate ZIP file. This is useful for organizing your metadata
> files and ensuring they are easily accessible. E.g.,
   ```bash
   repo2crate --repo-url=<your-repo-url> -o <output-directory>/my-workflow.crate.zip
   ```

---

## 4. Automate test execution

Creating tests for your workflows is just the first step towards ensuring
reliability. It's equally important to run these tests systematically whenever
changes are made to detect issues early, and to run them periodically to detect
when external factors have triggered or exposed a problem with your workflow
(e.g., unpinned dependencies). This is where automation becomes
essential.

A powerful and de facto standard way to automate testing on GitHub is [*GitHub
Actions*](https://docs.github.com/en/actions). GitHub Actions offer a complete
continuous integration and continuous deployment (CI/CD) platform to build
workflows to automate your build, test, and deployment pipeline. These workflows
are highly configurable, support parallel job execution, and provide detailed
feedback on test results, making them an ideal choice for automated workflow
testing.

### Step 1: Understand GitHub Actions basics

GitHub Actions is a CI/CD platform that allows you to automate your workflows. Key concepts include:

- **Workflows**: Automated processes defined in YAML files in the `.github/workflows` directory
- **Events**: Actions that trigger a workflow (e.g., push, pull request)
- **Jobs**: Sets of steps that execute on the same runner
- **Steps**: Individual tasks within a job
- **Actions**: Reusable units of code

For successful implementation of continuous testing for your workflow on the
GitHub platform, you need to understand GitHub Actions fundamentals.

Jump over to GitHub and complete the [GitHub Actions
Quickstart](https://docs.github.com/en/actions/get-started/quickstart) tutorial
before continuing here. That knowledge will be essential for the next steps.

### Step 2: Create a workflow file for testing your workflow

1. Create a `.github/workflows` directory in your repository:

    ```bash
    mkdir -p .github/workflows
    ```

2. Create a file named `test-workflow.yml` with the following content:

    ```yaml
    name: Test Galaxy Workflow

    on:
      push:
         branches: [ main ]
      pull_request:
         branches: [ main ]

    jobs:
      test:
         runs-on: ubuntu-latest
         steps:
            - uses: actions/checkout@v3

            - name: Set up Python
              uses: actions/setup-python@v4
              with:
                 python-version: '3.9'

            - name: Install Planemo
              run: pip install planemo

            - name: Test workflow
              run: planemo test [OPTIONS] workflows/*.ga
    ```


> 📚 **See the tutorial [Adding a Github workflow for running tests automatically](https://training.galaxyproject.org/training-material/topics/fair/tutorials/ro-crate-galaxy-best-practices/tutorial.html#adding-a-github-workflow-for-running-tests-automatically)** for additional insights on how to automate your test execution.

> 📚 **See the Planemo documentation**
>
> For more information on the available options for the `planemo test` command,
> check the [Planemo documentation](https://planemo.readthedocs.io/en/latest/).


3. Commit and push your workflow file:

    ```bash
    git add .github/workflows/
    git commit -m "Add GitHub Actions workflow for testing"
    git push
    ```

4. Go to your GitHub repository, click on the "Actions" tab, and you should see your workflow running.

<p align="center">
    <img src="images/screenshot_workflow_runs.png" alt="Screenshot of workflow runs in GitHub Actions">
</p>
<p align="center"><em>Example of GitHub Actions workflow runs showing test execution results</em></p>

## Automate maintenance

Maintaining workflows over time can be challenging.
[LifeMonitor](https://lifemonitor.eu) is a service that helps you automate
workflow maintenance, including the application of workflow best practices and
the periodic monitoring of the health of your workflows through test execution,
providing notifications when issues arise.

> ⚠️ **Development vs. Production Instances**
>
> LifeMonitor provides two different instances:
>
> - **Development instance**: <https://api.dev.lifemonitor.eu> - Recommended for tutorials, learning, and experimentation
> - **Production instance**: <https://lifemonitor.eu> - For monitoring production-ready workflows
>
> For the purposes of this tutorial and to experiment with LifeMonitor's
> features, **use the development instance** (<https://dev.lifemonitor.eu>).
> This will allow you to freely test the platform without affecting the **data
> associated with your account on its production environment.**

⚠️⚠️ Note ⚠️⚠️ **Use the Development Instance**. This tutorial will take your
through a process which will result in the publication of metadata pertaining to
your workflow to LifeMonitor and WorkflowHub.  Since this is an exercise, we
want that data to be clearly marked as "fake", safe to be discarded and not to
be propagated to European data indexing services.


### Step 1: Register with LifeMonitor

1. Go to [LifeMonitor](https://app.dev.lifemonitor.eu/).
2. Sign up for an account if you don't already have one. For this tutorial *we
   recommend using your GitHub identity* for this tutorial.
    * ⚠️ **Note**. You can also use your institutional identify (it it is linked with eduGAIN and thus works with [LS AAI / LS Login](https://lifescience-ri.eu/ls-login/)), but
    you'll then have to explicitly link your account with your GitHub identify
    to complete the next part of the tutorial.
3. Follow the instructions to set up your profile

### Step 2: Install the LifeMonitor GitHub App

LifeMonitor provides a [GitHub App](https://github.com/apps/lifemonitor) --
that is, a specialized application that extends the functionality of GitHub,
providing integrated workflow maintenance functions.

1. Go to the [LifeMonitor GitHub App](https://github.com/apps/lifemonitor).
   Have a look at the app description.
2. Click "Install".
3. Choose to install LifeMonitor on your specific workflow repository.
4. Complete the installation following the guide [Submitting Workflow Testing RO-Crates to LifeMonitor](https://training.galaxyproject.org/training-material/topics/fair/tutorials/ro-crate-submitting-life-monitor/tutorial.html#installing-the-lm-github-app).
   This tutorial will take you through:
    a. Configuration of your LifeMonitor account;
    b. Connecting your WorkflowHub account to LifeMonitor and enabling WorkflowHub integration;
    c. Enabling LifeMonitor workflow checks and automated monitoring, including email notifications.

### Step 3: Implement LifeMonitor suggestions

After installing the LifeMonitor GitHub App and properly configuring your
account, the automated service will start working for you.

1. The app will analyze your workflow and create issues if it finds it can suggest potential improvements
2. It may also create pull requests with automatically suggested fixes for certain issues
3. Review these suggestions and implement them as appropriate:

### Step 4: Monitor workflow health

1. Visit your dashboard on LifeMonitor at <https://app.dev.lifemonitor.eu/>.  You should see your workflow.
2. Check the status of your workflow on LifeMonitor.
3. The LM app should also have registered your workflow with the WorkflowHub
**Dev instance**.  You'll find a link on your workflow's entry in the LM
dashboard.  Follow it and check the metadata that has been automatically
published on the WorkflowHub dev instance.

## Conclusion

By following these best practices, you can help you to make your workflows more
findable and to keep them functional, reproducible, and maintainable over time.
Testing workflows, automating these tests with GitHub Actions, and using
services like LifeMonitor help you to automate maintenance operations,
detect problems early and keep your workflows in good working order over the
long term.

## Additional Resources

- [Galaxy Training Network](https://training.galaxyproject.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Planemo Documentation](https://planemo.readthedocs.io/)
- [LifeMonitor Documentation](https://lifemonitor.eu/documentation)

> 📚 **Galaxy Workflow Best Practices**
>
> For additional specific information about best practices for Galaxy workflows, follow
> this link: [Best Practices for Maintaining Galaxy
> Workflows](https://planemo.readthedocs.io/en/latest/best_practices_workflows.html)
