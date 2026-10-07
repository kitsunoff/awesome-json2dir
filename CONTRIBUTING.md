# Contribution Guidelines

Thank you for adding to the list.

## Adding an entry

1. The project must implement, extend or invert the [`json2dir` conversion scheme](https://github.com/alurm/json2dir#conversion-scheme).
2. The project must have a public repository with a README.
3. Put the entry in the matching section:
   - **Ports and rewrites**: JSON to directory tree, same scheme.
   - **Alternative takes**: same scheme, unusual approach.
   - **Inverse tools**: directory tree to JSON.
   - **Tooling**: wrappers and tools built around existing implementations.
   - **Rebuttals**: projects arguing against `json2dir`.
   - **Articles and usage**: write-ups, discussions and real-world setups that use json2dir. These are not counted in *At a glance*.
4. Use this format:

   ```markdown
   - [owner/repo](https://github.com/owner/repo) ![Language](https://img.shields.io/badge/-Language-COLOR?style=flat-square&logo=LOGO&logoColor=white) - Short description ending with a period.
   ```

5. Add a row to the **At a glance** table and update the project count badge.
6. If your project fills an item in **Wanted**, tick it and link it.
7. One project per pull request.
8. Optional: mention the result of the [conformance suite](conformance/README.md) in the pull request.

## Changing the specification

Changes to [RFC J2D-1](spec/rfc-json2dir.md) need a matching change to the [conformance cases](conformance/cases), and the self-test must pass:

```bash
python3 -m unittest discover --start-directory conformance
```

## Style

- Descriptions are in English, start with a capital letter and end with a period.
- Describe what the project does, not how great it is.
