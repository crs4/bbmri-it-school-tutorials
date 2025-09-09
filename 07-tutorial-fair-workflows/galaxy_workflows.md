# Introduction to the Galaxy workflow manager

Galaxy is a web-based platform that enables accessible, reproducible, and collaborative biomedical data analyses through workflows.  In this section, you'll get to familiarize yourself with the usage of Galaxy and how to extract provenance data from the analyses executed on the platform.

## A short introduction to Galaxy

Complete this tutorial from the Galaxy Training Network: [A short introduction to Galaxy](https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-short/tutorial.html).  Don't abandon your work environment on the Galaxy server as we'll keep using it in later steps of this tutorial.

## Galaxy and FAIR Workflows

Galaxy embraces the FAIR (Findable, Accessible, Interoperable, Reusable) principles, providing robust support for creating and sharing reproducible workflows.  Also, the Galaxy community has created a very extensive body of training material.

If you're interested in studying this topic further, feel free to explore the Galaxy Training Network's section on [FAIR Data, Workflows, and Research](https://training.galaxyproject.org/training-material/topics/fair/).

### Workflow Run RO-Crates in Galaxy

Since version 23.00, Galaxy has introduced the ability to export workflows as **Workflow Run RO-Crates** (WRROC). As we saw during the lecture, WRROC packages can capture workflow execution details, including inputs, outputs, parameters, etc. in a structured, machine-readable format, while also maintaining some degree of human readability.

### Export a Workflow Run RO-Crate from Galaxy

Export a workflow as an RO-Crate in Galaxy:

#### 1(a): execute your workflow in Galaxy

Choose a workflow from the Galaxy interface and execute it by clicking on the **Run** button (you may need to configure the workflow inputs first).

---

#### 1(b): select a workflow invocation

As an alternative to executing the workflow again, you can select a previous workflow invocation from the history from the workflow invocation list (you can find it by clicking on the *Workflow Invocations* on left menu)

![Selecting a workflow invocation from the Galaxy interface](images/screenshot_select-workflow-invocation.png)
*Figure: Selecting a workflow invocation from the list of executed workflows in Galaxy*

---

#### 2: go to the **Export** tab

<p align="center">
    <img src="images/screenshot_export-wizard-1.png" alt="the Export tab selection" />
</p>
<p align="center"><em>Figure: Selecting the Export tab in the workflow export wizard</em></p>

---

#### 3: select **Research Object Crate** as output format and then **next** to continue

<p align="center">
    <img src="images/screenshot_export-wizard-2.png" alt="Selecting Research Object Crate as output format" />
</p>
<p align="center"><em>Figure: Selecting Research Object Crate as the output format in the workflow export wizard</em></p>

---

#### 4: select **Temporary Direct Download** as destination and then **next** to continue

<p align="center">
    <img src="images/screenshot_export-wizard-3.png" alt="Selecting Temporary Direct Download as destination" />
</p>
<p align="center"><em>Figure: Selecting Temporary Direct Download as the destination in the workflow export wizard</em></p>

---

#### 5: click on **Generate Download Link** to download the .crate.zip file

After clicking, the system will produce the crate archive and automatically start the download.

#### 6: examine the contents of the .crate.zip file

The exported RO-Crate package contains comprehensive metadata, workflow definitions, and execution provenance needed to understand, evaluate, and potentially reproduce your workflow execution. It serves as a FAIR digital object that can be shared, cited, and reused across different platforms. For more details on how to examine and utilize RO-Crates, please refer to the [next tutorial on RO-Crate](RO_crate.md).
