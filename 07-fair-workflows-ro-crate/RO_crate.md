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
