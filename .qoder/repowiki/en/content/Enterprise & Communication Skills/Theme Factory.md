# Theme Factory

<cite>
**Referenced Files in This Document**   
- [SKILL.md](file://theme-factory/SKILL.md)
- [arctic-frost.md](file://theme-factory/themes/arctic-frost.md)
- [botanical-garden.md](file://theme-factory/themes/botanical-garden.md)
- [tech-innovation.md](file://theme-factory/themes/tech-innovation.md)
- [desert-rose.md](file://theme-factory/themes/desert-rose.md)
- [forest-canopy.md](file://theme-factory/themes/forest-canopy.md)
- [golden-hour.md](file://theme-factory/themes/golden-hour.md)
- [midnight-galaxy.md](file://theme-factory/themes/midnight-galaxy.md)
- [modern-minimalist.md](file://theme-factory/themes/modern-minimalist.md)
- [ocean-depths.md](file://theme-factory/themes/ocean-depths.md)
- [sunset-boulevard.md](file://theme-factory/themes/sunset-boulevard.md)
- [theme-showcase.pdf](file://theme-factory/theme-showcase.pdf)
</cite>

## Table of Contents
1. [Introduction](#introduction)
2. [Theme Application Process](#theme-application-process)
3. [Available Themes](#available-themes)
4. [Theme Structure and Format](#theme-structure-and-format)
5. [Practical Examples of Theme Application](#practical-examples-of-theme-application)
6. [Troubleshooting Theme Issues](#troubleshooting-theme-issues)
7. [Creating Custom Themes](#creating-custom-themes)
8. [Conclusion](#conclusion)

## Introduction

The Theme Factory skill provides a comprehensive toolkit for styling digital artifacts with professional themes to ensure visual consistency and polish across various formats. This skill enables users to apply cohesive design elements to presentation slide decks, documents, reports, HTML landing pages, and other artifacts. The system offers 10 pre-set themes, each with carefully curated color palettes and font pairings that create distinct visual identities suitable for different contexts and audiences. Additionally, the skill supports on-the-fly generation of custom themes when existing options don't meet specific requirements.

**Section sources**
- [SKILL.md](file://theme-factory/SKILL.md#L1-L60)

## Theme Application Process

The process for applying themes to artifacts follows a standardized workflow designed to ensure consistency and user satisfaction. First, users should view the `theme-showcase.pdf` file to visually evaluate all available themes without making modifications to the showcase file itself. After reviewing the options, users select their preferred theme from the available collection. Once a theme is chosen, the system reads the corresponding theme file from the `themes/` directory and applies the specified colors and fonts consistently throughout the target artifact. The application process ensures proper contrast and readability while maintaining the theme's visual identity across all elements of the document or presentation.

The skill is designed to work with various artifact types, including slide decks, documents, and HTML content. During application, the system preserves the structural integrity of the original artifact while transforming its visual presentation according to the selected theme's specifications. This approach allows for professional styling without compromising the content's organization or functionality.

**Section sources**
- [SKILL.md](file://theme-factory/SKILL.md#L21-L57)

## Available Themes

The Theme Factory includes 10 professionally designed themes, each tailored for specific contexts and audiences. These themes are defined in individual markdown files within the `themes/` directory and provide complete specifications for color palettes and typography.

### Arctic Frost

A cool and crisp winter-inspired theme that conveys clarity, precision, and professionalism. This theme features a palette of Ice Blue (`#d4e4f7`), Steel Blue (`#4a6fa5`), Silver (`#c0c0c0`), and Crisp White (`#fafafa`). Headers use DejaVu Sans Bold, while body text uses DejaVu Sans. Ideal for healthcare presentations, technology solutions, winter sports, clean tech, and pharmaceutical content.

**Section sources**
- [arctic-frost.md](file://theme-factory/themes/arctic-frost.md#L1-L20)

### Botanical Garden

A fresh and organic theme featuring vibrant garden-inspired colors for lively presentations. The color palette includes Fern Green (`#4a7c59`), Marigold (`#f9a620`), Terracotta (`#b7472a`), and Cream (`#f5f3ed`). Headers use DejaVu Serif Bold, while body text uses DejaVu Sans. Best suited for garden centers, food presentations, farm-to-table content, botanical brands, and natural products.

**Section sources**
- [botanical-garden.md](file://theme-factory/themes/botanical-garden.md#L1-L20)

### Tech Innovation

A bold and modern theme with high-contrast colors perfect for cutting-edge technology presentations. The palette features Electric Blue (`#0066ff`), Neon Cyan (`#00ffff`), Dark Gray (`#1e1e1e`), and White (`#ffffff`). Both headers and body text use DejaVu Sans, with headers in bold weight. This theme is ideal for tech startups, software launches, innovation showcases, AI/ML presentations, and digital transformation content.

**Section sources**
- [tech-innovation.md](file://theme-factory/themes/tech-innovation.md#L1-L20)

### Additional Themes

The Theme Factory includes seven other professionally designed themes:

- **Desert Rose**: A soft and sophisticated theme with dusty, muted tones using FreeSans fonts, ideal for fashion, beauty brands, and interior design.
- **Forest Canopy**: A natural and grounded theme with earth tones using FreeSerif Bold for headers, suitable for environmental presentations and sustainability reports.
- **Golden Hour**: A rich and warm autumnal palette with FreeSans typography, perfect for restaurant presentations and hospitality brands.
- **Midnight Galaxy**: A dramatic cosmic theme with deep purples and FreeSans typography, designed for entertainment industry and gaming presentations.
- **Modern Minimalist**: A clean grayscale theme with DejaVu Sans typography, versatile for tech presentations and modern business proposals.
- **Ocean Depths**: A professional maritime theme with Deep Navy and Teal colors using DejaVu Sans, ideal for corporate presentations and financial reports.
- **Sunset Boulevard**: A warm and vibrant theme inspired by golden hour sunsets with DejaVu Serif Bold headers, perfect for creative pitches and marketing presentations.

All themes are accessible through the `theme-showcase.pdf` visual reference.

**Section sources**
- [desert-rose.md](file://theme-factory/themes/desert-rose.md#L1-L20)
- [forest-canopy.md](file://theme-factory/themes/forest-canopy.md#L1-L20)
- [golden-hour.md](file://theme-factory/themes/golden-hour.md#L1-L20)
- [midnight-galaxy.md](file://theme-factory/themes/midnight-galaxy.md#L1-L20)
- [modern-minimalist.md](file://theme-factory/themes/modern-minimalist.md#L1-L20)
- [ocean-depths.md](file://theme-factory/themes/ocean-depths.md#L1-L20)
- [sunset-boulevard.md](file://theme-factory/themes/sunset-boulevard.md#L1-L20)
- [theme-showcase.pdf](file://theme-factory/theme-showcase.pdf)

## Theme Structure and Format

Themes in the Theme Factory are structured as markdown files with a consistent format that defines all necessary styling elements. Each theme file follows a standardized structure with specific sections that ensure comprehensive theme definition.

The core structure includes:
- **Theme Name**: The primary heading that identifies the theme
- **Description**: A brief explanation of the theme's character and intended use
- **Color Palette**: A section listing all colors with descriptive names, hex codes, and usage guidelines
- **Typography**: Specification of font families for headers and body text
- **Best Used For**: Guidance on appropriate contexts and industries for the theme

This standardized format ensures that all themes are documented consistently and contain the necessary information for proper application. The markdown format makes themes easily readable and maintainable while providing clear documentation of design decisions. Each theme file is self-contained, allowing for straightforward updates and modifications without affecting other themes in the collection.

**Section sources**
- [SKILL.md](file://theme-factory/SKILL.md#L43-L49)

## Practical Examples of Theme Application

The Theme Factory skill can be applied to various artifact types, transforming their visual presentation while preserving content structure.

### HTML Artifacts

When applying themes to HTML artifacts created with the artifacts-builder skill, the system modifies CSS variables and class definitions to reflect the selected theme's color palette and typography. For example, applying the Arctic Frost theme to an HTML landing page would update the site's primary color variables to Steel Blue (`#4a6fa5`) and background colors to Crisp White (`#fafafa`), while changing font-family declarations to use DejaVu Sans. The system ensures that all interactive elements, such as buttons and navigation menus, maintain proper contrast and visual hierarchy according to the theme's specifications.

### Documents

For document formats like DOCX, the theme application process updates style definitions for headings, body text, and other elements. When applying the Botanical Garden theme to a report, the system would set heading styles to use DejaVu Serif Bold in Fern Green (`#4a7c59`) and body text to use DejaVu Sans in a suitable contrast color. The system also updates document elements like headers, footers, and page backgrounds to maintain visual consistency throughout the document.

### Presentations

In PowerPoint (PPTX) presentations, theme application involves updating slide masters, color schemes, and font schemes. Applying the Tech Innovation theme to a pitch deck would transform the presentation with Dark Gray (`#1e1e1e`) backgrounds, Electric Blue (`#0066ff`) accent colors for titles and key elements, and DejaVu Sans typography throughout. The system ensures that all slide layouts, including title slides, content slides, and section dividers, adhere to the theme's visual identity.

**Section sources**
- [SKILL.md](file://theme-factory/SKILL.md#L3-L4)
- [artifacts-builder/SKILL.md](file://artifacts-builder/SKILL.md#L3-L4)

## Troubleshooting Theme Issues

When applying themes to artifacts, several common issues may arise that affect visual consistency across formats.

### Theme Application Failures

If a theme fails to apply completely, verify that the target artifact format supports the styling elements defined in the theme. Some formats may have limitations on color depth, font embedding, or CSS capabilities. Check that the artifact file is not corrupted and that the theme file is properly formatted with valid hex codes and recognized font names. Ensure that the theme application process has sufficient permissions to modify the target file.

### Visual Inconsistencies Across Formats

Different file formats may render colors and fonts slightly differently, leading to visual inconsistencies. To address this, test the themed artifact in the intended viewing environment and make minor adjustments if necessary. For critical presentations, export the artifact to the final format early in the process and verify the appearance. When sharing across platforms, consider providing fallback fonts and testing color appearance on different display types.

### Font Availability Issues

If specified fonts are not available in the target environment, the system may substitute default fonts, altering the intended appearance. To prevent this, use widely available fonts like those specified in the themes (DejaVu Sans, FreeSans, etc.) or embed fonts when the format supports it. For HTML artifacts, include web font links in the document head to ensure consistent typography across viewing environments.

**Section sources**
- [SKILL.md](file://theme-factory/SKILL.md#L50-L57)

## Creating Custom Themes

When none of the existing themes meet specific requirements, the Theme Factory skill supports creating custom themes on-the-fly. To generate a new theme, provide a description of the desired aesthetic, context, or industry focus. The system will create a theme with appropriate color combinations and font pairings that match the requested style.

The custom theme generation process follows the same structural format as pre-set themes, ensuring consistency in documentation and application. Generated themes include a descriptive name, color palette with hex codes and usage guidelines, typography specifications, and recommendations for appropriate use cases. After generating a custom theme, it is presented for review and verification before application to ensure it meets the user's expectations.

Custom themes are created using design principles consistent with the existing collection, maintaining professional quality and visual coherence. The system considers factors like color psychology, contrast ratios for readability, and font pairing harmony when generating new themes. This ensures that even custom themes maintain the high standards of visual consistency and polish that define the Theme Factory skill.

**Section sources**
- [SKILL.md](file://theme-factory/SKILL.md#L58-L60)

## Conclusion

The Theme Factory skill provides a powerful solution for ensuring visual consistency and professional polish across digital artifacts. With 10 pre-set themes covering various industries and contexts, users can quickly apply cohesive design elements to presentations, documents, and HTML content. The standardized theme structure in markdown format ensures clear documentation and easy maintenance, while the ability to create custom themes on-the-fly provides flexibility for unique requirements.

By following the systematic application process and understanding the characteristics of each theme, users can effectively enhance their artifacts with professional styling that reinforces their message and brand identity. The skill integrates seamlessly with other document and presentation tools, making it a valuable component in any professional workflow that requires consistent, high-quality visual communication.