# RO-Crate tutorial

[RO-Crate](https://w3id.org/ro/crate/) is a method for aggregating data
together with their metadata. This tutorial will help you get familiar with
it.

## Creating a simple RO-Crate

You can turn any folder in your computer into an RO-Crate by adding a
[JSON-LD](https://json-ld.org/) metadata file named
`ro-crate-metadata.json`. Create a new folder named `sample-crate` and add a
`data.csv` file to it:

```bash
mkdir sample-crate
cd sample-crate
touch data.csv
```

Launch a text editor and create an `ro-crate-metadata.json` file inside the
`sample-crate` folder. Add the following content to the file and save it to
disk:

```json
{
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {"@id": "./"},
            "conformsTo": {"@id": "https://w3id.org/ro/crate/1.1"}
        },
        {
            "@id": "./",
            "@type": "Dataset",
            "name": "Example crate",
            "description": "An example RO-Crate",
            "datePublished": "2025-07-28",
            "license": {"@id": "http://spdx.org/licenses/CC0-1.0"},
            "hasPart": [{"@id": "data.csv"}]
        },
        {
            "@id": "data.csv",
            "@type": "File",
            "name": "CSV data"
        },
        {
            "@id": "http://spdx.org/licenses/CC0-1.0",
            "@type": "CreativeWork",
            "name": "CC0-1.0"
        }
    ]
}
```

The first line sets the JSON-LD _context_ for the rest of the file. The
context maps shortcut terms to their full URIs, allowing to keep the file
concise. For instance, without the context, we'd have to write
`http://schema.org/CreativeWork` instead of simply `CreativeWork`. The
`@graph` section contains four entities:

* The _RO-Crate Metadata Descriptor_, with an `@id` of
  `ro-crate-metadata.json`: this is a required entity through which the file
  self-identifies as the _RO-Crate Metadata Document_. Note that the `about`
  property references the second entity through its `@id`.

* The _Root Data Entity_ (RDE), with an `@id` of `./`: this means that the
  document describes the contents of the directory in which the RO-Crate
  Metadata Document is located. The RDE has several properties: the ones shown
  here constitute a minimal set. In particular, `hasPart` points to the _Data
  Entities_ of the RO-Crate, which describe mainly files and folders. The RDE
  also references a `license` that indicates how the RO-Crate may be used.

* A _Data Entity_ that describes the `data.csv` file.

* A _Contextual Entity_ that describes the crate's license.


## Validating an RO-Crate

How can we check that an RO-Crate conforms to the specifications? The
[RO-Crate Validator](https://github.com/crs4/rocrate-validator) has been
developed for this purpose. It provides a Command Line Interface (CLI) and a
Python API for programmatic usage. Move back to the directory that contains
`sample-crate` and install the validator:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install roc-validator
```

Run the CLI tool as follows:

```bash
rocrate-validator -y validate -v -w 79 -o err.txt sample-crate
```

The `err.txt` file should contain the following output:

```
                                                                               
 ╭────────────────────────── - Validation Report - ──────────────────────────╮ 
 │                                                                           │ 
 │                                                                           │ 
 │  RO-Crate: sample-crate                                                   │ 
 │  Target Profile: ro-crate-1.1 (autodetected)                              │ 
 │  Validation Severity: REQUIRED                                            │ 
 │                                                                           │ 
 │  ╭────────────────── Requirements Checks Validation ───────────────────╮  │ 
 │  │                                                                     │  │ 
 │  │ ╭─ Severity: REQUIRE─╮╭─ Severity: RECOMME─╮╭─ Severity: OPTIONAL─╮ │  │ 
 │  │ │                    ││                    ││                     │ │  │ 
 │  │ │         39         ││         0          ││          0          │ │  │ 
 │  │ │                    ││                    ││                     │ │  │ 
 │  │ ╰────────────────────╯╰────────────────────╯╰─────────────────────╯ │  │ 
 │  │ ╭──────── PASSED Checks ────────╮╭──────── FAILED Checks ─────────╮ │  │ 
 │  │ │                               ││                                │ │  │ 
 │  │ │              39               ││               0                │ │  │ 
 │  │ │                               ││                                │ │  │ 
 │  │ ╰───────────────────────────────╯╰────────────────────────────────╯ │  │ 
 │  │                                                                     │  │ 
 │  ╰─────────────────────────────────────────────────────────────────────╯  │ 
 │  ╭───────────────────────── Overall Progress ──────────────────────────╮  │ 
 │  │ Profiles            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1/1   0:00:02 │  │ 
 │  │ Requirements        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16/16 0:00:02 │  │ 
 │  │ Requirements Checks ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39/39 0:00:02 │  │ 
 │  ╰─────────────────────────────────────────────────────────────────────╯  │ 
 │                                                                           │ 
 ╰───────────────────────────────────────────────────────────────────────────╯ 
                                                                               
  ─────────────── [OK] RO-Crate is a valid ro-crate-1.1 !!!   ────────────────
                                                                               
```

Let's break down the output:

* The first line reports the path of the processed RO-Crate, in this case
  `sample-crate`.

* The second line indicates that the validation has been run against the
  `ro-crate-1.1` profile. A profile is a set of additional requirements --
  with respect to the base RO-Crate specification -- that specializes RO-Crate
  for a particular domain or use case. In our case, we did not specify any
  profile, and the RO-Crate does not indicate conformance to any particular
  profile, so the validation ran against the base specifications. You can get
  information on all the profiles supported by the validator by running
  `rocrate-validator profiles list`.

* The third line indicates that the validator performed only checks with
  `REQUIRED` severity, which is the default value: you can set the severity
  level to `RECOMMENDED` or `OPTIONAL` via the `-l` option of the `validate`
  subcommand. What's the meaning of this? The RO-Crate specification follows
  [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) to indicate
  requirement levels. When the severity is set to `REQUIRED`, only
  requirements listed in the specification as "REQUIRED", "MUST", "MUST NOT",
  "SHALL", "SHALL NOT" are checked; when it's set to `RECOMMENDED`,
  requirements listed as "RECOMMENDED", "NOT RECOMMENDED", "SHOULD", "SHOULD
  NOT" are also checked; when it's set to `OPTIONAL`, requirements listed as
  "OPTIONAL" and "MAY" are also checked.

Our RO-Crate satisfies all "REQUIRED" constraints, so the rest of the output
reports that there was no violation and the RO-Crate is valid. But does it
also satisfy all "RECOMMENDED" constraints? You can verify this by checking
the output of:

```bash
rocrate-validator -y validate -l RECOMMENDED -v -w 79 -o err.txt sample-crate
```

If you open `err.txt` you will see a summary similar to the one above, with
the difference that in this case a failed validation is reported. After the
summary, the validator writes detailed information on every check that failed.

The validator has several subcommands with many options. You can explore them
by passing the `--help` option to the top-level `rocrate-validator` command
and to any of the subcommands. You can also check the full documentation at
https://rocrate-validator.readthedocs.io/ .


## RO-Crate in Python

The [ro-crate-py](https://github.com/ResearchObject/ro-crate-py) library
provides a Python API to create and consume RO-Crates. Installation is done
via pip (note that the package name is `rocrate`):

```bash
pip install rocrate
```

This part of the tutorial is based on [RO-Crate in
Python](https://gxy.io/GTN:T00341), which in turn is based on the ro-crate-py
documentation.

### Creating an RO-Crate

In its simplest form, an RO-Crate is a directory tree with an
`ro-crate-metadata.json` file at the top level. This file contains metadata
about the other files and directories, represented by [data
entities](https://www.researchobject.org/ro-crate/1.1/data-entities.html). These
metadata consist both of properties of the data entities themselves and of
other, non-digital entities called [contextual
entities](https://www.researchobject.org/ro-crate/1.1/contextual-entities.html). A
contextual entity can represent, for instance, a person, an organization or an
event.

Suppose Alice and Bob worked on a research project together, and then wrote a
paper about it; additionally, Alice prepared a spreadsheet containing
experimental data, which Bob then used to generate a diagram. For the purpose
of this tutorial, you can just create empty files for these documents:

```bash
mkdir exp
touch exp/paper.pdf
touch exp/results.csv
touch exp/diagram.svg
```

Let's build an RO-Crate to represent this information:

```python
from rocrate.rocrate import ROCrate

crate = ROCrate()
paper = crate.add_file("exp/paper.pdf", properties={
    "name": "manuscript",
    "encodingFormat": "application/pdf"
})
table = crate.add_file("exp/results.csv", properties={
    "name": "experimental data",
    "encodingFormat": "text/csv"
})
diagram = crate.add_file("exp/diagram.svg", dest_path="images/figure.svg", properties={
    "name": "bar chart",
    "encodingFormat": "image/svg+xml"
})
```

We've started by adding the data entities. Now we add contextual entities
representing Alice and Bob:

```python
from rocrate.model import Person

alice_id = "https://orcid.org/0000-0000-0000-0000"
bob_id = "https://orcid.org/0000-0000-0000-0001"
alice = crate.add(Person(crate, alice_id, properties={
    "name": "Alice Doe",
    "affiliation": "University of Flatland"
}))
bob = crate.add(Person(crate, bob_id, properties={
    "name": "Bob Doe",
    "affiliation": "University of Flatland"
}))
```

We have created all the entities we need. Now we need to express the
relationships between them. This is done by adding _properties_ that reference
other entities:

```python
paper["author"] = [alice, bob]
table["author"] = alice
diagram["author"] = bob
```

You can also add whole directories together with their contents. In RO-Crate,
a directory is represented by the `Dataset` entity:

```bash
mkdir exp/logs
touch exp/logs/log1.txt
touch exp/logs/log2.txt
```

```python
logs = crate.add_dataset("exp/logs")
```

Finally, we serialize the crate to disk:

```python
crate.write("exp_crate")
```

This should generate an `exp_crate` directory containing copies of all the
files we added and an `ro-crate-metadata.json` file containing a JSON-LD
representation of the metadata. Note that we have chosen a different
destination path for the diagram, while the paper and the spreadsheet have
been placed at the top level with their names unchanged (the default). The
resulting directory layout should be as follows:

```
exp_crate/
|-- images/
|   `-- figure.svg
|-- logs/
|   |-- log1.txt
|   `-- log2.txt
|-- paper.pdf
|-- results.csv
`-- ro-crate-metadata.json
```

Some applications and services support RO-Crates stored as ZIP archives. To
save the crate in ZIP format, you can use `write_zip`:

```python
crate.write_zip("exp_crate.zip")
```

#### Appending elements to property values

What ro-crate-py entities actually store is their JSON representation:

```python
paper.properties()
```

```json
{
  "@id": "paper.pdf",
  "@type": "File",
  "name": "manuscript",
  "encodingFormat": "application/pdf",
  "author": [
    {"@id": "https://orcid.org/0000-0000-0000-0000"},
    {"@id": "https://orcid.org/0000-0000-0000-0001"},
  ]
}
```

When `paper["author"]` is accessed, a new list containing the `alice` and
`bob` entities is generated on the fly. For this reason, calling `append` on
`paper["author"]` will _not_ modify the `paper` entity. To add an author, use
the `append_to` method instead:

```python
donald = crate.add(Person(crate, "https://en.wikipedia.org/wiki/Donald_Duck"))
paper.append_to("author", donald)
```

#### Adding entities with an arbitrary type

An entity can be of any type listed in the [RO-Crate
context](https://www.researchobject.org/ro-crate/1.1/context.jsonld). However,
only a few of them have a counterpart (e.g., `File`) in the library's class
hierarchy, either because they are very common or because they are associated
with specific functionality that can be conveniently embedded in the class
implementation. In other cases, you can explicitly pass the type via the
`properties` argument:

```python
from rocrate.model import ContextEntity

hackathon = crate.add(ContextEntity(crate, "#bh2021", properties={
    "@type": "Hackathon",
    "name": "Biohackathon 2021",
    "location": "Barcelona, Spain",
    "startDate": "2021-11-08",
    "endDate": "2021-11-12"
}))
```

### Consuming an RO-Crate

You can load an RO-Crate from a directory or ZIP file by passing its path to
the `ROCrate` constructor:

```python
crate = ROCrate("exp_crate")  # or ROCrate("exp_crate.zip")
for e in crate.get_entities():
    print(e.id, e.type)
```

```
ro-crate-metadata.json CreativeWork
./ Dataset
paper.pdf File
results.csv File
images/figure.svg File
logs/ Dataset
https://orcid.org/0000-0000-0000-0000 Person
https://orcid.org/0000-0000-0000-0001 Person
...
```

The first two entities shown in the output are the [metadata file
descriptor](https://www.researchobject.org/ro-crate/1.1/metadata.html) and the
[root data
entity](https://www.researchobject.org/ro-crate/1.1/root-data-entity.html),
respectively. The former represents the metadata file, while the latter
represents the whole crate. In ro-crate-py, these are special entities created
and managed by the `ROCrate` object, and are always present. The other
entities are the ones we added in the [section on RO-Crate
creation](#creating-an-ro-crate). As shown above, `get_entities` allows to
iterate over all entities in the crate. You can also access only data entities
with `crate.data_entities` or only contextual entities with
`crate.contextual_entities`. For instance:

```python
for e in crate.data_entities:
    author = e.get("author")
    if not author:
        continue
    elif isinstance(author, list):
        print(e.id, [p.get("name") for p in author])
    else:
        print(e.id, repr(author.get("name")))
```

```
paper.pdf ['Alice Doe', 'Bob Doe']
results.csv 'Alice Doe'
images/figure.svg 'Bob Doe'
```

You can fetch an entity by its `@id` as follows:

```python
article = crate.get("paper.pdf")
print([a["name"] for a in article["author"]])
```

```
['Alice Doe', 'Bob Doe']
```

You can also get all entities of a certain type:

```python
print(crate.get_by_type("File"))
```

```
[<paper.pdf File>, <results.csv File>, <images/figure.svg File>]
```

Note that the string representation of an entity is in the `<ID TYPE>` format.

### Command Line Interface

`ro-crate-py` includes a hierarchical CLI: the `rocrate` tool. `rocrate` is
the top-level command, while specific functionalities are provided via
sub-commands. Currently, the tool allows to initialize an existing directory
tree as an RO-Crate (`rocrate init`), to modify the metadata of an existing
RO-Crate (`rocrate add`) and to save an existing RO-Crate directory as a ZIP
archive (`rocrate write-zip`).

```console
$ rocrate --help
Usage: rocrate [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add
  init
  write-zip
```

To try the CLI, get a copy of the ro-crate-py repository:

```bash
git clone --depth 1 --branch 0.14.0 https://github.com/ResearchObject/ro-crate-py
cd ro-crate-py/test/test-data/ro-crate-galaxy-sortchangecase
```

This directory is already an RO-Crate. Delete the metadata file to get a plain
directory tree:

```bash
rm ro-crate-metadata.json
```

Now the directory tree contains several files and directories, including a
[Galaxy](https://usegalaxy.org/) workflow and a
[Planemo](https://planemo.readthedocs.io/) test file, but it's not an RO-Crate
anymore, since there is no metadata file. Initialize the crate:

```bash
rocrate init
```

This creates an `ro-crate-metadata.json` file that lists files and directories
found by recursively walking the current directory tree. Note that the Galaxy
workflow is listed as a plain `File`:

```json
{
  "@id": "sort-and-change-case.ga",
  "@type": "File"
}
```

ro-crate-py has some support for the [Workflow
RO-Crate](https://w3id.org/workflowhub/workflow-ro-crate/1.0) profile, whose
main goal is to describe a computational workflow and associated resources.
We can change the metadata to list the Galaxy file as a computational workflow
by running the following command:

```bash
rocrate add workflow -l galaxy sort-and-change-case.ga
```

If you check `ro-crate-metadata.json` now, you will see that the workflow has
a type of `["File", "SoftwareSourceCode", "ComputationalWorkflow"]` and has a
`programmingLanguage` property that points to a `ComputerLanguage` entity that
represents the Galaxy workflow language. Also, the workflow is linked from the
RDE via the `mainEntity` property, as prescribed by the profile.

The library also supports adding entities from the [Workflow Testing
RO-Crate](https://w3id.org/ro/wftest) profile. Workflow Testing RO-Crate is an
extension of Workflow RO-Crate that contains guidelines on describing tests
being run for the workflow. The following commands add a test suite, a test
instance, and a test definition (see the profile for more information on these
entities).

```bash
rocrate add test-suite -i test1
rocrate add test-instance test1 http://example.com -r jobs -i test1_1
rocrate add test-definition test1 test/test1/sort-and-change-case-test.yml -e planemo -v '>=0.70'
```

You can get help on using the toolkit by adding the `--help` option to the
base command or any subcommand. For instance:

```console
$ rocrate add test-instance --help
Usage: rocrate add test-instance [OPTIONS] SUITE URL

Options:
  -r, --resource TEXT
  -s, --service [jenkins|travis|github]
  -i, --identifier TEXT
  -n, --name TEXT
  -c, --crate-dir PATH            The path to the root data entity of the
                                  crate. Defaults to the current working
                                  directory.
  -P, --property KEY=VALUE        Add an additional property to the metadata
                                  for this entity. Can be used multiple times
                                  to set multiple properties.
  --help                          Show this message and exit.
```


## RO-Crate for best-practice workflow repositories

The [repo2rocrate](https://github.com/crs4/repo2rocrate) software package
generates a Workflow Testing RO-Crate for a workflow repository that follows
community best practices. It currently supports Galaxy (based on
[IWC](https://iwc.galaxyproject.org/) guidelines),
[Nextflow](https://www.nextflow.io/) and
[Snakemake](https://snakemake.readthedocs.io/). The tool assumes that the
workflow repository is structured according to the community guidelines and
generates the appropriate RO-Crate metadata for the various entities. Several
command line options allow to specify additional information that cannot be
automatically detected or needs to be overridden.

To try the software, we'll clone one of the iwc-workflows repositories, whose
layout is known to respect the IWC guidelines. Since it already contains an
RO-Crate metadata file, we'll delete it before running the tool.

```
pip install repo2rocrate
git clone https://github.com/iwc-workflows/parallel-accession-download
cd parallel-accession-download/
rm -fv ro-crate-metadata.json
repo2rocrate --repo-url https://github.com/iwc-workflows/parallel-accession-download
```

This adds an `ro-crate-metadata.json` file at the top level with metadata
generated based on the tool's knowledge of the expected repository layout,
turning the repository root into a Workflow Testing RO-Crate.

To explore the set of options provided by repo2rocrate, use the `--help`
option:

```console
$ repo2rocrate --help
Usage: repo2rocrate [OPTIONS]

Options:
  -r, --root DIRECTORY            workflow repository root
  -l, --lang [nextflow|snakemake|galaxy]
                                  workflow language (default: auto-detect)
  -w, --workflow PATH             workflow file (default: auto-detect)
  -o, --output PATH               output directory or zip file. The default is
                                  the repository root itself, in which case
                                  only the metadata file is written
  --repo-url TEXT                 workflow repository URL
  --wf-name TEXT                  workflow name
  --wf-version TEXT               workflow version
  --lang-version TEXT             workflow language version
  --license TEXT                  license URL
  --ci-workflow TEXT              filename (basename) of the GitHub Actions
                                  workflow that runs the tests for the
                                  workflow
  --diagram TEXT                  relative path of the workflow diagram
  --version                       print version and exit
  --help                          Show this message and exit.
```


## Exploring Workflow Run RO-Crates

[Workflow Run RO-Crate](https://w3id.org/ro/wfrun) is a set of three RO-Crate
profiles for describing provenance information related to the execution of a
computational workflow:

* [Process Run Crate](https://w3id.org/ro/wfrun/process) describes the
  execution of an "implicit workflow", where one or more tools contributed to
  the same computation;
* [Workflow Run Crate](https://w3id.org/ro/wfrun/workflow) is similar to
  Process Run Crate, but assumes that the execution is orchestrated by a
  workflow manager;
* [Provenance Run Crate](https://w3id.org/ro/wfrun/provenance) extends
  Workflow Run Crate with specifications for describing the execution of each
  step of the workflow.

An example of a Provenance Run Crate can be found at
https://doi.org/10.5281/zenodo.7774351: scroll down to the "Files" section and
click on the `ml-predict-pipeline-cwltool-runcrate.crate.zip` link to download
it.

Unpack the crate into a `ml-predict-pipeline-cwltool-runcrate` directory:

```
unzip -d ml-predict-pipeline-cwltool-runcrate{,.crate.zip}
```

In addition to the RO-Crate metadata file, the directory contains the workflow
file `packed.cwl`, a `README.md` file, and input/output files involved in the
computation. The metadata file contains a detailed description of the entities
involved in the execution, down to the level of individual steps: this can
make it hard to focus on the most important items, i.e., the process
executions and related input and output parameters. A tool that helps with
this is [runcrate](https://github.com/ResearchObject/runcrate):

```
pip install runcrate
runcrate report ml-predict-pipeline-cwltool-runcrate
```

After running the above commands, you should see the following output:

```
action: #5d08a759-9b0e-434f-a5f0-ac95dc0ad619
  instrument: packed.cwl (['File', 'SoftwareSourceCode', 'ComputationalWorkflow', 'HowTo'])
  started: 2023-02-21T12:44:53.363530
  ended: 2023-02-21T12:45:11.260305
  inputs:
    tissue_low>0.9 <- packed.cwl#main/tissue-high-filter
    tissue_high <- packed.cwl#main/tissue-high-label
    4 <- packed.cwl#main/tissue-high-level
    tissue_low <- packed.cwl#main/tissue-low-label
    9 <- packed.cwl#main/tissue-low-level
    tissue_low>0.99 <- packed.cwl#main/tumor-filter
    tumor <- packed.cwl#main/tumor-label
    1 <- packed.cwl#main/tumor-level
    #b6b5f30b-d459-4b37-ad6c-3cab115d138d <- packed.cwl#main/slide
  outputs:
    254eb2d60fd6705c88a6b7746336ba86e09e23c7 <- packed.cwl#main/tissue
    a1e03e58562319274d4ff792d2090763b7926d72 <- packed.cwl#main/tumor

action: #cf0a0a63-5eb2-4f3d-8c62-7a575aab0799
  step: packed.cwl#main/extract-tissue-low
  instrument: packed.cwl#extract_tissue.cwl (SoftwareApplication)
  started: 2023-02-21T12:44:54.774746
  ended: 2023-02-21T12:44:56.740995
  inputs:
    tissue_low <- packed.cwl#extract_tissue.cwl/label
    9 <- packed.cwl#extract_tissue.cwl/level
    #b6b5f30b-d459-4b37-ad6c-3cab115d138d <- packed.cwl#extract_tissue.cwl/src
  outputs:
    8cdd835383bcc344a0dbc6892ac6949765400b5c <- packed.cwl#extract_tissue.cwl/tissue

action: #21ca24a9-66a9-4c3a-911c-51c235bcd2ed
  step: packed.cwl#main/extract-tissue-high
  instrument: packed.cwl#extract_tissue.cwl (SoftwareApplication)
  started: 2023-02-21T12:44:56.753244
  ended: 2023-02-21T12:44:58.538525
  inputs:
    tissue_low>0.9 <- packed.cwl#extract_tissue.cwl/filter
    8cdd835383bcc344a0dbc6892ac6949765400b5c <- packed.cwl#extract_tissue.cwl/filter_slide
    tissue_high <- packed.cwl#extract_tissue.cwl/label
    4 <- packed.cwl#extract_tissue.cwl/level
    #b6b5f30b-d459-4b37-ad6c-3cab115d138d <- packed.cwl#extract_tissue.cwl/src
  outputs:
    254eb2d60fd6705c88a6b7746336ba86e09e23c7 <- packed.cwl#extract_tissue.cwl/tissue

action: #db496cbd-3e6d-4c6a-8766-acc7d6a6bd3f
  step: packed.cwl#main/classify-tumor
  instrument: packed.cwl#classify_tumor.cwl (SoftwareApplication)
  started: 2023-02-21T12:44:58.553005
  ended: 2023-02-21T12:45:11.256012
  inputs:
    tissue_low>0.99 <- packed.cwl#classify_tumor.cwl/filter
    8cdd835383bcc344a0dbc6892ac6949765400b5c <- packed.cwl#classify_tumor.cwl/filter_slide
    tumor <- packed.cwl#classify_tumor.cwl/label
    1 <- packed.cwl#classify_tumor.cwl/level
    #b6b5f30b-d459-4b37-ad6c-3cab115d138d <- packed.cwl#classify_tumor.cwl/src
  outputs:
    a1e03e58562319274d4ff792d2090763b7926d72 <- packed.cwl#classify_tumor.cwl/tumor
```

The report contains a section for every _action_ (process execution), showing
its _instrument_ (the software that was executed), starting and ending times,
and input and output parameters. Parameter lines are in the form:

```
actual_value <- formal_parameter
```

Where the formal parameter represents a sort of logical "slot" that can be
filled by different actual values at runtime.

The first action corresponds to the execution of the whole workflow, while the
others correspond to the execution of individual steps (note they have a line
that reports the step's identifier).
