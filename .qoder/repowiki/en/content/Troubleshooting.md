# Troubleshooting

<cite>
**Referenced Files in This Document**   
- [quick_validate.py](file://skill-creator/scripts/quick_validate.py)
- [package_skill.py](file://skill-creator/scripts/package_skill.py)
- [init_skill.py](file://skill-creator/scripts/init_skill.py)
- [SKILL.md](file://algorithmic-art/SKILL.md)
- [forms.md](file://document-skills/pdf/forms.md)
- [check_bounding_boxes.py](file://document-skills/pdf/scripts/check_bounding_boxes.py)
- [check_fillable_fields.py](file://document-skills/pdf/scripts/check_fillable_fields.py)
- [README.md](file://README.md)
</cite>

## Table of Contents
1. [Introduction](#introduction)
2. [Common Configuration Errors](#common-configuration-errors)
3. [Missing Dependencies and Script Path Issues](#missing-dependencies-and-script-path-issues)
4. [Template Resolution Failures](#template-resolution-failures)
5. [Permission and Access Issues](#permission-and-access-issues)
6. [Malformed YAML and Frontmatter Problems](#malformed-yaml-and-frontmatter-problems)
7. [PDF Form Processing Errors](#pdf-form-processing-errors)
8. [Diagnostic Tools and Validation Scripts](#diagnostic-tools-and-validation-scripts)
9. [Preventive Measures and Best Practices](#preventive-measures-and-best-practices)

## Introduction
This troubleshooting guide addresses common issues encountered when using and developing skills in the Claude ecosystem. The document covers error patterns, root causes, debugging techniques, and solutions for configuration errors, missing dependencies, template resolution failures, and permission issues. It provides actionable resolution steps and examples from real issues in the codebase, organized by symptom and impact level. The guide also includes preventive measures and best practices to avoid common pitfalls when creating and using skills.

## Common Configuration Errors
Configuration errors are among the most frequent issues encountered when developing skills. These typically involve incorrect naming conventions, missing required fields in the SKILL.md frontmatter, or improper directory structure.

The most common configuration error occurs when the skill name in the YAML frontmatter doesn't follow the required hyphen-case convention (lowercase letters, digits, and hyphens only). Names cannot start or end with a hyphen, contain consecutive hyphens, or include uppercase letters. This is validated by the quick_validate.py script which checks for proper naming format.

Another frequent configuration issue is missing required fields in the YAML frontmatter. Every skill must have both 'name' and 'description' fields. The description field cannot contain angle brackets (< or >) as these can interfere with parsing. These validation rules are enforced by the quick_validate.py script.

**Section sources**
- [quick_validate.py](file://skill-creator/scripts/quick_validate.py#L33-L54)

## Missing Dependencies and Script Path Issues
Missing dependencies and broken script paths are common issues that prevent skills from functioning correctly. The skill ecosystem relies on various external tools and libraries that must be properly installed and accessible.

For document processing skills, several dependencies are required:
- pandoc for text extraction and conversion
- LibreOffice for PDF conversion
- Poppler utilities (pdftoppm) for converting PDFs to images
- Python libraries like pypdf for PDF manipulation

When these dependencies are missing, scripts will fail with import errors or command not found messages. The most effective way to diagnose dependency issues is to run the specific script and examine the error output. For example, if check_fillable_fields.py fails with "ModuleNotFoundError: No module named 'pypdf'", this indicates the pypdf library needs to be installed.

Script path issues often occur when scripts are executed from the wrong directory. Many scripts expect to be run from their containing directory and use relative paths to access other files. Running scripts from a different location can cause file not found errors.

**Section sources**
- [docx/SKILL.md](file://document-skills/docx/SKILL.md#L190-L197)
- [check_fillable_fields.py](file://document-skills/pdf/scripts/check_fillable_fields.py#L2)

## Template Resolution Failures
Template resolution failures occur when the system cannot locate or properly process template files. This is particularly critical in skills like algorithmic-art which rely on template files as starting points for generated artifacts.

The algorithmic-art skill requires using templates/viewer.html as the literal starting point for all HTML artifacts. Common template resolution issues include:
- Not reading the template file before implementation
- Creating HTML from scratch instead of using the template
- Modifying fixed sections of the template (header, sidebar structure, Anthropic branding)
- Changing the sidebar layout or styling

The template must be used exactly as provided, with only the variable sections (algorithm, parameters, UI controls) being customized. The template contains extensive comments marking exactly what to keep versus replace.

**Section sources**
- [algorithmic-art/SKILL.md](file://algorithmic-art/SKILL.md#L105-L127)

## Permission and Access Issues
Permission and access issues can prevent skills from reading files, writing outputs, or executing scripts. These issues are typically related to file system permissions or restricted access to certain directories.

When packaging skills, the package_skill.py script requires write permissions to the output directory. If the output directory is not writable, the script will fail with a permission error. Similarly, when creating new skills with init_skill.py, the script needs write permissions to the target directory.

For PDF processing skills, permission issues can occur when trying to read input PDFs or write output files. The scripts must have read access to input files and write access to the output location.

**Section sources**
- [package_skill.py](file://skill-creator/scripts/package_skill.py#L68-L74)
- [init_skill.py](file://skill-creator/scripts/init_skill.py#L214-L219)

## Malformed YAML and Frontmatter Problems
Malformed YAML in the SKILL.md frontmatter is a common source of skill validation failures. The YAML frontmatter must be properly formatted with correct syntax and structure.

Common YAML issues include:
- Missing or incorrect frontmatter delimiters (---)
- Improper indentation
- Unquoted special characters
- Missing required fields (name, description)

The quick_validate.py script performs basic validation of the YAML frontmatter, checking for the presence of required fields and proper format. It uses regular expressions to extract the frontmatter and validate its content.

**Section sources**
- [quick_validate.py](file://skill-creator/scripts/quick_validate.py#L21-L37)

## PDF Form Processing Errors
PDF form processing errors are common when working with the PDF skill and typically fall into two categories: fillable form field issues and non-fillable form field issues.

For fillable forms, the most common error is not properly identifying whether a PDF has fillable fields before proceeding. The workflow requires running check_fillable_fields.py first to determine the appropriate processing path. Skipping this step can lead to using the wrong processing method.

For non-fillable forms, the primary source of errors is incorrect bounding box specification in fields.json. Common issues include:
- Label and entry bounding boxes that intersect
- Entry bounding boxes that are too small for the text content
- Incorrect coordinate systems (PDF vs image coordinates)
- Targeting text labels instead of checkbox squares for checkboxes

The check_bounding_boxes.py script validates these conditions and provides specific error messages for each type of issue. The validation process requires both automated checking with this script and manual inspection of validation images.

**Section sources**
- [forms.md](file://document-skills/pdf/forms.md#L1-L206)
- [check_bounding_boxes.py](file://document-skills/pdf/scripts/check_bounding_boxes.py#L1-L71)

## Diagnostic Tools and Validation Scripts
The skill ecosystem provides several diagnostic tools and validation scripts to help identify and resolve issues.

The skill-creator toolkit includes three primary scripts:
- quick_validate.py: Performs basic validation of a skill's structure and frontmatter
- package_skill.py: Packages a skill directory into a zip file, with built-in validation
- init_skill.py: Creates a new skill from template with proper structure

For PDF processing, specialized diagnostic tools include:
- check_fillable_fields.py: Determines if a PDF has fillable form fields
- check_bounding_boxes.py: Validates that bounding boxes in fields.json don't intersect and are properly sized
- create_validation_image.py: Generates images showing bounding box placement for visual verification

These tools should be used systematically during skill development and document processing to catch issues early.

**Section sources**
- [quick_validate.py](file://skill-creator/scripts/quick_validate.py#L1-L65)
- [package_skill.py](file://skill-creator/scripts/package_skill.py#L1-L111)
- [init_skill.py](file://skill-creator/scripts/init_skill.py#L1-L304)

## Preventive Measures and Best Practices
To avoid common pitfalls when developing and using skills, follow these best practices:

1. **Always validate skills before use**: Run quick_validate.py on any new skill to catch configuration errors early.

2. **Follow template guidelines exactly**: When a skill specifies using a template as the starting point, do not create files from scratch. Use the template as literally specified.

3. **Check dependencies before execution**: Verify that all required tools and libraries are installed and accessible before running scripts.

4. **Follow the prescribed workflow**: For complex skills like PDF processing, follow the documented workflow steps in order. Skipping steps like checking for fillable fields can lead to errors.

5. **Use proper naming conventions**: Skill names must be in hyphen-case (lowercase with hyphens), without leading/trailing hyphens or consecutive hyphens.

6. **Validate bounding boxes thoroughly**: For PDF form processing, use both automated validation (check_bounding_boxes.py) and manual inspection of validation images to ensure accuracy.

7. **Package skills properly**: Use package_skill.py to create distributable skill packages, which includes built-in validation.

8. **Initialize skills correctly**: Use init_skill.py to create new skills with proper structure and example files.

Following these practices will help prevent the most common issues and ensure skills function as intended.

**Section sources**
- [README.md](file://README.md#L90-L117)
- [quick_validate.py](file://skill-creator/scripts/quick_validate.py#L1-L65)
- [package_skill.py](file://skill-creator/scripts/package_skill.py#L1-L111)
- [init_skill.py](file://skill-creator/scripts/init_skill.py#L1-L304)