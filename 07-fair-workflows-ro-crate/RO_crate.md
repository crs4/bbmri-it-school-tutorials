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


## ro-crate-py

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
