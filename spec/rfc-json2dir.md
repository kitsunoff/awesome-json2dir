# RFC J2D-1: The json2dir Directory Tree Format

```text
awesome-json2dir                                awesome-json2dir contributors
Request for Comments: J2D-1                                      October 2026
Category: Community Specification
Version: 1.0
```

## Status of This Memo

This document specifies the json2dir format for the community of its implementers. It is **not** an IETF RFC and has not been through any standards body. It borrows the shape of an RFC because the format deserves one.

This document describes the behavior of the reference implementation, [alurm/json2dir](https://github.com/alurm/json2dir), and tightens it where independent implementations need firm ground. Distribution of this memo is unlimited. It is dedicated to the public domain under CC0 1.0.

## Abstract

json2dir is a format that describes a directory tree as a single JSON object. Objects describe directories, strings describe regular files, and two-element arrays describe symbolic links and executable files. This document defines the format, the processing a consumer performs to materialize a document on a file system, the behavior when the target already has content, and the security properties a consumer must preserve.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Overview](#2-overview)
3. [Input](#3-input)
4. [Conversion Scheme](#4-conversion-scheme)
5. [Existing Content](#5-existing-content)
6. [Processing Model](#6-processing-model)
7. [Command-Line Interface](#7-command-line-interface)
8. [Conformance](#8-conformance)
9. [Security Considerations](#9-security-considerations)
10. [Platform Considerations](#10-platform-considerations)
11. [IANA Considerations](#11-iana-considerations)
12. [References](#12-references)
13. [Appendix A. Grammar](#appendix-a-grammar)
14. [Appendix B. Acknowledgements](#appendix-b-acknowledgements)

## 1. Introduction

Configuration often needs to become files: dotfiles, generated project skeletons, test fixtures, container contents. Many tools can emit JSON. json2dir lets any of them emit a whole directory tree as one value that is easy to read, diff, generate and review.

### 1.1. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

### 1.2. Terminology

- **Document**: A JSON text that follows this specification.
- **Producer**: Software that writes documents.
- **Consumer**: Software that reads a document and creates the tree it describes. The reference implementation is a consumer.
- **Target directory**: The directory in which a consumer creates the tree. The document root corresponds to it.
- **Member**: A name and value pair of a JSON object [RFC8259].
- **Entry**: A file system object: a directory, a regular file, a symbolic link, or another kind of file.

## 2. Overview

The following document:

```json
{
  "greeting": "Hello, world!",
  "dir": {
    "subfile": "Content.\n",
    "subdir": {}
  },
  "symlink": ["link", "target path"],
  "script": ["script", "#!/bin/sh\necho Howdy!"]
}
```

describes this tree inside the target directory:

```text
.
├── greeting        regular file, content "Hello, world!"
├── dir/            directory
│   ├── subfile     regular file, content "Content.\n"
│   └── subdir/     empty directory
├── symlink         symbolic link to "target path"
└── script          executable file
```

## 3. Input

A document is a JSON text as defined in [RFC8259], encoded in UTF-8 [RFC3629].

A consumer MUST reject input that:

1. is not a well-formed JSON text, including input that is empty;
2. is not valid UTF-8;
3. contains anything other than insignificant whitespace after the JSON value;
4. uses extensions to JSON, such as comments, trailing commas, or the literals `NaN` and `Infinity`;
5. contains a string escape that denotes an unpaired surrogate, such as `"\ud800"`, because such a string cannot be encoded as UTF-8.

Producers MUST NOT emit a byte order mark. A consumer MAY ignore a byte order mark at the start of the input, as [RFC8259] permits.

## 4. Conversion Scheme

Each JSON value in a document maps to exactly one entry.

| JSON value | Entry |
| --- | --- |
| Object | Directory |
| String | Regular file |
| `["link", target]` | Symbolic link |
| `["script", content]` | Executable regular file |

### 4.1. Root

The root value of a document MUST be an object. It describes the content of the target directory. A consumer MUST reject a document whose root is not an object.

An empty root object, `{}`, is valid and describes no entries.

### 4.2. Objects

An object describes a directory. Each member describes one entry inside that directory: the member name is the entry name, and the member value describes the entry.

A consumer MUST create a directory for each object member that does not already exist as a directory (see [Section 5](#5-existing-content)), then process the members of that object inside it.

A consumer MUST support documents with at least 64 levels of nested objects below the root. A consumer MAY reject deeper documents.

Member names in an object SHOULD be unique, as [RFC8259] recommends. Producers MUST NOT emit duplicate names. When a consumer encounters duplicate names, it MUST either reject the document or use the value of the last occurrence and ignore the others.

#### 4.2.1. Names

A *simple name* is a string that:

1. is not empty;
2. is neither `.` nor `..`;
3. does not contain the character `/` (U+002F);
4. does not contain the character NUL (U+0000).

Producers MUST emit only simple names.

A consumer MUST reject a document with a member name that is not a simple name, with one exception. The *trimmed name* is the name with any trailing sequence of `/` and `/.` removed; for example, the trimmed name of `a/` and of `a/./` is `a`. A consumer MAY accept a name whose trimmed name is a simple name. If it does, it MUST NOT create, modify or remove any entry other than the one named by the trimmed name, and the rules of [Section 5](#5-existing-content) apply to that entry. Names such as `/a`, `./a`, `a/b` and `a/..` have no such trimmed name and MUST be rejected.

A name is used as an entry name exactly, with no Unicode normalization or case folding. Its UTF-8 encoding is the byte sequence of the entry name.

### 4.3. Strings

A string describes a regular file. The content of the file MUST be exactly the UTF-8 encoding of the string after JSON escapes are decoded. A consumer MUST NOT add, remove or convert any characters, including line terminators and NUL characters.

The permissions of the file are the platform default for a newly created file. On POSIX systems, that is mode `0666` restricted by the process file mode creation mask. A consumer MUST NOT set any execute permission on the file.

### 4.4. Arrays

An array describes a symbolic link or an executable file. The array MUST have exactly two elements, and both MUST be strings. The first element is the *kind* and the second is the *payload*.

The kind MUST be one of `"link"` and `"script"`. Kinds are case-sensitive. A consumer MUST reject an array of any other shape and an array with any other kind.

#### 4.4.1. Links

`["link", target]` describes a symbolic link whose target is exactly the payload.

A consumer MUST NOT resolve, normalize, validate or follow the target. The target MAY be absolute, MAY point outside the target directory, and MAY point to a path that does not exist.

#### 4.4.2. Scripts

`["script", content]` describes a regular file with the payload as its content, created as in [Section 4.3](#43-strings), and then made executable: on POSIX systems, the consumer MUST add execute permission for the owner, the group and others (mode bits `0111`) to the permissions of the file.

### 4.5. Other Values

Numbers, `true`, `false` and `null` have no meaning in this format. A consumer MUST reject a document that contains them as member values at any depth.

## 5. Existing Content

The target directory MAY already contain entries. This section defines how a consumer treats them. An entry that the document does not name MUST be left unchanged.

### 5.1. Directories

When a member value is an object and an entry with that name already exists and is a directory, the consumer MUST use the existing directory. Entries inside it that the object does not name MUST be left unchanged. The consumer MUST NOT change the permissions of the existing directory.

### 5.2. Other Entries

When an entry with the member name already exists and is not a directory, the consumer MUST replace it with the entry the member describes. The new entry MUST be indistinguishable from one created when no entry existed. In particular:

1. a regular file that replaces an executable file MUST NOT keep its execute permissions;
2. a regular file that replaces a longer file MUST NOT keep any of the old content.

The RECOMMENDED way to replace an entry is to remove it and then create the new one.

### 5.3. Symbolic Links Are Not Followed

When the existing entry is a symbolic link, the consumer MUST replace the link itself. It MUST NOT write through the link, create entries inside the directory it points to, or modify the entry it points to. This holds for every kind of member value, including objects: an object member whose name is a symbolic link to a directory replaces the link with a new directory.

### 5.4. Directories in the Way

When a member value is not an object and an entry with that name already exists and is a directory, the consumer MUST fail. It MUST NOT remove the directory or any of its contents.

## 6. Processing Model

A consumer MUST parse the complete document according to [Section 3](#3-input) before it creates, modifies or removes any entry.

A consumer SHOULD also validate the complete document against [Section 4](#4-conversion-scheme) before it changes the file system. The reference implementation validates members while it creates them, so a consumer MAY instead report an invalid member after it has created entries for other members.

A consumer MAY process members in any order. For a document that a consumer accepts, the resulting tree MUST NOT depend on that order, on file systems where different names denote different entries (see [Section 9](#9-security-considerations)). The reference implementation processes the members of each object in ascending order of the UTF-8 bytes of their names.

When a consumer fails, it MUST report the failure (see [Section 7](#7-command-line-interface)). It MAY leave entries created before the failure in place. This specification does not require changes to be atomic.

A consumer MUST NOT create, modify or remove any entry outside the target directory, except through the targets of symbolic links that the document itself describes, which a consumer never follows ([Section 4.4.1](#441-links)).

This specification does not define ownership, timestamps, extended attributes, access control lists, or permissions beyond those in [Section 4](#4-conversion-scheme).

## 7. Command-Line Interface

A command-line consumer SHOULD provide the interface of the reference implementation:

```text
json2dir < document.json
```

1. The document is read from standard input.
2. The target directory is the current working directory.
3. The exit status is 0 on success and non-zero on failure.
4. Diagnostics are written to standard error.
5. The command takes no arguments, and it fails with a usage message when it is given any.

A consumer MAY offer other interfaces, such as options that name an input file or a target directory, in addition to or instead of this one.

## 8. Conformance

A producer conforms to this specification when every document it emits follows Sections [3](#3-input) and [4](#4-conversion-scheme) and uses only simple names.

A consumer conforms at one of two levels:

| Level | Requirements |
| --- | --- |
| Core | Sections [3](#3-input), [4](#4-conversion-scheme) and [6](#6-processing-model) |
| Full | Core, and [Section 5](#5-existing-content) |

The [json2dir conformance suite](../conformance/README.md) tests both levels. It is informative: passing it is strong evidence of conformance, but this document is the authority.

## 9. Security Considerations

A document is a program for the file system. Consumers SHOULD treat documents from untrusted sources the way they treat untrusted code: a document can create executable files and symbolic links that point anywhere.

**Name validation.** The rules of [Section 4.2.1](#421-names) exist so that a document cannot name an entry outside the directory it describes. A consumer that accepts names with trailing separators MUST still meet [Section 5.3](#53-symbolic-links-are-not-followed) for them: on POSIX systems, a path with a trailing `/` resolves through a symbolic link, so passing such a name to system calls unchanged can follow a link that the consumer meant to replace.

**Symbolic links in the target.** [Section 5.3](#53-symbolic-links-are-not-followed) prevents a pre-existing link from redirecting writes. A consumer that checks an entry and then acts on it by path is still exposed to a race: another process can replace the entry between the check and the use (TOCTOU). The reference implementation makes no attempt to guard against this. When a consumer writes into a directory that other users can modify, it SHOULD operate relative to open directory descriptors and refuse to follow links, for example with `openat`, `mkdirat` and `O_NOFOLLOW` on POSIX systems.

**Privileges.** Consumers SHOULD NOT run with more privileges than the target directory requires.

**Resource use.** A small document can describe many entries, and a deep document can exhaust a recursive consumer's stack. Consumers MAY limit document size, nesting depth and entry count, provided they meet the minimum in [Section 4.2](#42-objects).

**Name collisions.** On case-insensitive or normalizing file systems, two different names can refer to the same entry. The rules of [Section 5](#5-existing-content) then apply between members of the same document, and the result depends on processing order. Producers SHOULD avoid names that differ only by case or Unicode normalization.

## 10. Platform Considerations

**Non-POSIX systems.** Symbolic links and execute permissions are not available on every platform. A consumer that cannot create the entry an array describes MUST reject the document rather than create an approximation, such as a copy instead of a link.

**Binary content.** File content is a JSON string and therefore valid Unicode text. This version of the format cannot describe files whose content is not valid UTF-8.

**File system limits.** File systems limit name length, path length and the set of allowed characters. A consumer MUST report a failure when the file system rejects an entry, as for any other error.

## 11. IANA Considerations

This document has no IANA actions. Documents are JSON texts and use the media type `application/json` and the file name extension `.json`.

## 12. References

### 12.1. Normative References

- **[RFC2119]** Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997. <https://www.rfc-editor.org/rfc/rfc2119>
- **[RFC3629]** Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003. <https://www.rfc-editor.org/rfc/rfc3629>
- **[RFC5234]** Crocker, D., Ed., and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008. <https://www.rfc-editor.org/rfc/rfc5234>
- **[RFC7405]** Kyzivat, P., "Case-Sensitive String Support in ABNF", RFC 7405, December 2014. <https://www.rfc-editor.org/rfc/rfc7405>
- **[RFC8174]** Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017. <https://www.rfc-editor.org/rfc/rfc8174>
- **[RFC8259]** Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, December 2017. <https://www.rfc-editor.org/rfc/rfc8259>

### 12.2. Informative References

- **[JSON2DIR]** Urmancheev, A., "json2dir: directory archives, made human-readable". <https://github.com/alurm/json2dir>
- **[POSIX]** IEEE and The Open Group, "The Open Group Base Specifications Issue 8", IEEE Std 1003.1-2024. <https://pubs.opengroup.org/onlinepubs/9799919799/>
- **[SUITE]** "json2dir Conformance Suite". [conformance/README.md](../conformance/README.md)

## Appendix A. Grammar

The following grammar restates [Section 4](#4-conversion-scheme) using ABNF [RFC5234] [RFC7405] and the rules of [RFC8259]. The value of `name` MUST be a simple name ([Section 4.2.1](#421-names)); that constraint is not expressible in ABNF.

```text
document   = ws directory ws
directory  = begin-object [ member *( value-separator member ) ] end-object
member     = name name-separator entry
name       = string
entry      = directory / file / link / script
file       = string
link       = begin-array quotation-mark %s"link" quotation-mark
             value-separator string end-array
script     = begin-array quotation-mark %s"script" quotation-mark
             value-separator string end-array
```

## Appendix B. Acknowledgements

Alan Urmancheev designed json2dir and wrote the reference implementation. The authors of every implementation listed in [awesome-json2dir](../README.md) tested the format by building it again, in more languages than anyone asked for.
