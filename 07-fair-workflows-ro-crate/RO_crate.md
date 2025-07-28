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
`sample-crate` folder. Activate support for JSON (or Javascript) if available
in your editor. Add the following content to the file and save it to disk:

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
