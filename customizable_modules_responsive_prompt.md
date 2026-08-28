# Customizable Modules Dashboard --- Responsive Claude Code Prompt

## Visual References

I have attached 3 visual references.

### Reference 1 --- Current Home Page

Use this as the visual foundation. Preserve the existing Home Page
structure, visual language, spacing rhythm, typography, header,
greeting, search, and updates section.

Do not redesign unrelated sections.

### Reference 2 --- macOS Widget Gallery

Use this as inspiration for the **Edit Modules** and **Add to Home**
experience.

Use it for: - Edit mode interaction - Browsing modules - Search -
Selecting module card variants - Previewing cards - Bottom sheet /
picker experience

Do not copy the UI literally. Adapt the concept to this Zoo / Animal
Management Command Centre application.

### Reference 3 --- Card Size Reference

Use this to establish a predefined responsive grid and card sizing
system.

Cards should: - Snap to the grid - Support predefined widths and
heights - Support different sizes based on card type - Allow height to
increase where content requires it

Do not copy the reference literally. Use it as a sizing and layout
concept.

------------------------------------------------------------------------

# PROJECT GOAL

Redesign and implement the Home Page **Modules** section as a polished,
customizable dashboard system.

The application must work responsively across:

-   Mobile
-   Tablet
-   Desktop
-   Large Desktop

Do not redesign the entire application.

Preserve the existing: - Header - Greeting - Search - Updates / Recent
Activity section - Typography - Overall visual language - Existing
spacing rhythm where possible

Focus primarily on improving the **Modules** area and adding the
complete **Edit Modules** experience.

------------------------------------------------------------------------

# CORE CONCEPT

In this product:

-   **Module** = a product feature or functional area
-   **Module Card** = a representation of that module on the Home page
-   A module can have multiple card/layout variants
-   Users can customize which module cards appear
-   Users can reorder cards
-   Cards can support different predefined sizes

Do not use **Widget** as the primary user-facing terminology.

## Example

### Medical Module

Available module card variants:

-   Default card
-   Hospital overview
-   Pending requests
-   Pharmacy status
-   Administration tasks

### Species Management Module

Available module card variants:

-   Default card
-   Statistics card
-   Population summary

Each module can have different card variants depending on the
information or navigation it represents.

------------------------------------------------------------------------

# DEFAULT HOME PAGE

The Home Page should remain clean and organized.

## Structure

1.  Greeting / Header
2.  Search
3.  Updates / Recent Activity
4.  Modules

The Modules section should have:

**Modules** **Edit**

The default experience should show the user's selected or default module
cards.

Do not show every available module card by default.

Use a responsive grid system.

Avoid making every card visually different. All cards should feel like
part of one unified design system.

------------------------------------------------------------------------

# MODULE CARD TYPES

## 1. Default Module Card

Use for standard module navigation.

Content: - Gradient background - Module icon - Module name - Minimal
layout

Example:

``` text
┌──────────────┐
│              │
│     Icon     │
│              │
│ Medical      │
└──────────────┘
```

## 2. Data / Statistics Card

Use for: - Species Management - Population - Counts - Important KPIs

Content: - Module name - Icon - Important number - Supporting label -
Optional subtle background texture

Example:

Species Management

2,411 Species

110,020 Animal Population

## 3. Image / Context Card

Use when an image provides meaningful context.

Content: - Large contextual image - Subtle overlay - Module name -
Optional important status or number

Example:

Hospital

241 Active Cases

## 4. Status / Request Card

Use for: - Pending Requests - Approvals - Follow Up - Tasks

Content: - Clear count - Status - Optional preview - Navigation
affordance

## 5. Alert Card

Use for: - Mortality - Fetal Death - Critical Cases

Use restrained semantic colors.

Do not make alert cards overly bright or decorative.

------------------------------------------------------------------------

# RESPONSIVE BREAKPOINT SYSTEM

Use the following responsive breakpoints.

  Device                             Breakpoint
  ---------------------------------- ------------------
  Mobile                             Below 768px
  Tablet Portrait                    768px -- 899px
  Tablet Landscape / Small Desktop   900px -- 1199px
  Desktop                            1200px -- 1599px
  Large Desktop                      1600px and above

Use responsive layout changes rather than creating completely separate
applications.

The same component system should adapt progressively.

------------------------------------------------------------------------

# MOBILE EXPERIENCE

## Breakpoint

Below **768px**

Mobile should be optimized for smaller screens and touch interaction.

Do not simply shrink the Tablet or Desktop layout.

## Module Grid

Use:

-   2-column grid where space allows
-   1-column layout for larger or detailed cards
-   Horizontal full-width cards when required

Recommended layout:

``` text
┌───────────┐ ┌───────────┐
│ Medical   │ │ Pharmacy  │
└───────────┘ └───────────┘

┌─────────────────────────┐
│ Hospital                │
│ 241 Active Cases        │
└─────────────────────────┘

┌─────────────────────────┐
│ Species Management      │
│ 2,411 Species           │
└─────────────────────────┘
```

## Mobile Typography

Recommended:

-   Body: 14px -- 16px
-   Card labels: 14px -- 16px
-   Section heading: 22px -- 26px
-   Main greeting: 28px -- 32px
-   Large statistics: 28px -- 40px

Do not make text smaller than 14px for normal readable content.

## Mobile Spacing

Recommended:

-   Page horizontal padding: 16px -- 20px
-   Grid gap: 12px
-   Card padding: 14px -- 16px

## Mobile Editing Experience

Do not overcrowd the screen.

When the user enters Edit Modules:

-   Cards should remain touch-friendly
-   Drag interaction should work with touch
-   Remove controls should be easy to tap
-   Use a clear Done action
-   Use a bottom sheet for Add Module

The Add Module bottom sheet can occupy most of the screen.

Suggested flow:

1.  Edit
2.  -   Add Module
3.  Bottom sheet opens
4.  Search or browse modules
5.  Select card
6.  Select size
7.  Add to Home

------------------------------------------------------------------------

# TABLET EXPERIENCE

## Breakpoints

### Tablet Portrait

768px -- 899px

Use a **4-column grid**.

### Tablet Landscape

900px -- 1199px

Use a **6-column grid**.

Tablet is a primary experience and should not feel like a reduced
desktop.

Prioritize:

-   Touch interaction
-   Comfortable spacing
-   Readability
-   Clear card hierarchy
-   Drag and drop

## Recommended Tablet Typography

-   Body: 14px -- 16px
-   Module card title: 16px -- 18px
-   Section heading: 24px -- 28px
-   Main greeting: 30px -- 36px
-   Large statistics: 34px -- 44px

Do not reduce all fonts just because the screen is smaller than desktop.

Tablet needs comfortable readable typography.

## Tablet Spacing

-   Page horizontal padding: 24px -- 32px
-   Grid gap: 12px -- 16px
-   Card padding: 16px -- 20px

## Tablet Module Picker

Use a large bottom sheet.

The sheet should feel optimized for touch and can occupy approximately
70%--90% of the screen height.

Suggested structure:

``` text
Add to Home

[ Search modules                    🔍 ]

[ All ] [ Medical ] [ Operations ] [ Admin ]

Medical

[ Card Preview ] [ Card Preview ]

[ Card Preview ] [ Card Preview ]
```

Categories can use horizontal tabs or another compact navigation pattern
that works naturally on tablet.

------------------------------------------------------------------------

# DESKTOP EXPERIENCE

## Breakpoint

1200px -- 1599px

Use an **8-column grid**.

Use the additional width to show more module cards horizontally.

Do not excessively stretch cards.

Prioritize:

-   Productivity
-   Information density
-   Efficient scanning
-   More simultaneous content

## Desktop Typography

Recommended:

-   Body: 14px -- 16px
-   Module card title: 16px -- 20px
-   Section heading: 28px -- 32px
-   Main greeting: 34px -- 40px
-   Large statistics: 44px -- 56px

Typography should increase slightly compared with Tablet, but avoid
dramatic scaling.

## Desktop Spacing

-   Page horizontal padding: 32px -- 48px
-   Grid gap: 16px -- 20px
-   Card padding: 20px -- 24px

## Desktop Module Picker

Use the larger screen efficiently.

The Add Module experience can become:

-   A large modal
-   A drawer
-   A wide panel
-   Or an expanded bottom-sheet style panel

Recommended structure:

``` text
┌──────────────────────────────────────────────────────┐
│ Add to Home                                      ×   │
├───────────────┬──────────────────────────────────────┤
│ All Modules   │ Medical                              │
│ Medical       │                                      │
│ Operations    │ [ Preview ] [ Preview ] [ Preview ] │
│ Administration│                                      │
│               │ [ Preview ] [ Preview ]             │
│               │                                      │
│               │              Cancel   Add to Home    │
└───────────────┴──────────────────────────────────────┘
```

Desktop should allow the user to browse categories and previews
efficiently.

------------------------------------------------------------------------

# LARGE DESKTOP EXPERIENCE

## Breakpoint

1600px and above.

Use a **12-column grid**.

Do not allow the interface to become excessively stretched.

Use:

-   Maximum content width where appropriate
-   More horizontal card placement
-   Larger layouts for important cards
-   Additional whitespace

Do not simply make every card huge.

Use the extra space primarily for:

-   More columns
-   Better information density
-   Improved hierarchy
-   More visible module cards

------------------------------------------------------------------------

# CARD SIZE SYSTEM

Use predefined grid-based sizes.

Do not allow arbitrary free resizing.

Supported sizes should include:

## Small

Typical use:

-   Default module card
-   Simple navigation
-   Icon + module name

## Medium

Typical use:

-   Hospital summary
-   Pharmacy
-   Lab
-   Requests

## Large

Typical use:

-   Species Management
-   Statistics
-   Image + data
-   Important module overview

## Tall

Typical use:

-   Follow Up
-   Pending items
-   Activity
-   Task lists

## Full Width

Use only where a larger summary requires it.

A card should only expose sizes that are appropriate for that card.

Example:

### Default Medical Card

Supported sizes:

-   Small
-   Medium

### Species Statistics

Supported sizes:

-   Medium
-   Large

### Follow Up

Supported sizes:

-   Tall
-   Large

------------------------------------------------------------------------

# RESPONSIVE GRID BEHAVIOR

The grid should adapt by changing the number of columns.

  Screen             Grid
  ------------------ -----------------------------------------
  Mobile             2 columns or 1 column depending on card
  Tablet Portrait    4 columns
  Tablet Landscape   6 columns
  Desktop            8 columns
  Large Desktop      12 columns

Cards should use spans rather than fixed pixel widths.

Examples:

-   Small = 1--2 columns
-   Medium = 2--3 columns
-   Large = 3--6 columns depending on breakpoint
-   Tall = predefined width × 2 rows
-   Full width = all available columns

The layout should preserve hierarchy across breakpoints.

A large desktop card may reduce its column span on tablet or stack on
mobile.

------------------------------------------------------------------------

# RESPONSIVE CARD HEIGHTS

Use consistent grid row units.

Do not use arbitrary heights.

Recommended approach:

-   Mobile base row: approximately 130px -- 160px
-   Tablet base row: approximately 150px -- 180px
-   Desktop base row: approximately 160px -- 200px

Cards can span multiple rows.

Example:

-   Small: 1 row
-   Medium: 1 row
-   Large: 1--2 rows
-   Tall: 2 rows

Card content must remain readable without awkward clipping.

------------------------------------------------------------------------

# RESPONSIVE TYPOGRAPHY RULE

Use **Inter** throughout the application.

Do not use completely different typography systems for each breakpoint.

Use fluid responsive typography where appropriate.

Use `clamp()` for headings and large statistics.

Example concept:

``` css
font-size: clamp(minimum, responsive value, maximum);
```

Avoid sudden and excessive typography jumps at breakpoints.

The main responsive changes should come from:

-   Grid columns
-   Card spans
-   Content density
-   Spacing
-   Layout structure

Do not make tablet typography unnecessarily small.

------------------------------------------------------------------------

# EDIT MODULES MODE

When the user clicks **Edit**, enter a dedicated **Edit Modules** mode.

Show:

**Edit Modules** **Done**

Behavior:

-   Cards become draggable
-   Cards can be reordered
-   Cards snap to the responsive grid
-   Removable cards show a subtle remove control
-   Required/core cards cannot be removed if applicable
-   Show `+ Add Module`
-   Done saves the layout

The editing experience should feel inspired by macOS/iPadOS widget
editing, but should match the visual identity of this application.

## Drag Behavior

When dragging:

-   Lift the dragged card visually
-   Add subtle elevation
-   Show the target position
-   Move other cards intelligently
-   Prevent overlapping
-   Snap the card into the nearest valid grid position

Desktop can support mouse drag.

Tablet and mobile must support touch drag.

------------------------------------------------------------------------

# ADD MODULE EXPERIENCE

When the user clicks:

**+ Add Module**

Open the module picker.

## User Flow

1.  User enters Edit Modules
2.  User clicks + Add Module
3.  Module picker opens
4.  User searches or browses modules
5.  User selects a module
6.  Available card variants appear
7.  User selects a card variant
8.  Available sizes appear
9.  User selects a supported size
10. User clicks Add to Home
11. Card is added to the dashboard
12. User can reorder it
13. User clicks Done

------------------------------------------------------------------------

# MODULE PICKER CONTENT

## Header

**Add to Home**

Include:

-   Close action
-   Search modules

Example:

``` text
Add to Home                                      ×

[ Search modules............................ 🔍 ]
```

## Categories

Examples:

-   All Modules
-   Medical
-   Animal Management
-   Operations
-   Administration

The category navigation must adapt responsively.

### Mobile

Horizontal scrollable tabs or compact category list.

### Tablet

Horizontal tabs or compact sidebar depending on available space.

### Desktop

Sidebar navigation is preferred if it improves browsing efficiency.

------------------------------------------------------------------------

# CARD PREVIEWS

When a user selects a module, show its available card variants.

Example:

## Medical

``` text
┌──────────────┐   ┌────────────────────────┐
│      ♥       │   │ 🏥 Hospital            │
│              │   │                        │
│ Medical      │   │ 241 Active Cases       │
└──────────────┘   └────────────────────────┘

┌───────────────────────────────────────────┐
│ Pending Requests                      24  │
│                                           │
│ Review requests →                         │
└───────────────────────────────────────────┘
```

Previews should represent actual module cards.

Do not use generic placeholder rectangles.

------------------------------------------------------------------------

# SIZE SELECTION

After selecting a card variant, show only supported sizes.

Example:

**Choose Size**

[Small](#small) [Medium](#medium) [Large](#large)

Do not show unavailable sizes.

Use clear selected states.

The user should then click:

**Add to Home**

------------------------------------------------------------------------

# EXAMPLE MODULES

Use these modules where relevant:

-   Medical
-   Hospital
-   Species Management
-   Mortality
-   Diet & Kitchen
-   Follow Up
-   Pharmacy
-   Lab
-   Fetal Death
-   Eggs
-   Administer
-   Users
-   Parivesh
-   Security

Use realistic mock data.

Examples:

### Species Management

-   2,411 Species
-   110,020 Animal Population

### Hospital

-   241 Active Cases

### Pending Requests

-   24 Pending

### Follow Up

-   8 Due Today

### Pharmacy

-   42 Medicine Requests

------------------------------------------------------------------------

# TECHNICAL IMPLEMENTATION

First inspect the existing project structure and existing Home Page
implementation.

Do not break existing functionality.

Reuse existing components where possible.

Create reusable components such as:

-   ModuleGrid
-   ModuleCard
-   ModuleCardVariants
-   EditModulesMode
-   ModulePicker
-   ModulePickerBottomSheet
-   ModuleCategoryFilter
-   ModulePreview
-   ModuleSizeSelector

Keep the system data-driven.

Suggested structure:

## Module

-   id
-   name
-   icon
-   category
-   availableCardVariants

## Card Variant

-   id
-   moduleId
-   type
-   supportedSizes
-   defaultSize
-   data

Keep separate:

-   Module definitions
-   Card definitions
-   Dashboard layout state
-   UI components

Persist the customized layout locally for now.

The layout should remain after refresh.

------------------------------------------------------------------------

# INTERACTION REQUIREMENTS

Implement:

-   Drag and drop
-   Touch drag support
-   Mouse drag support
-   Smooth reordering
-   Responsive grid snapping
-   Collision handling
-   Add module cards
-   Remove module cards
-   Predefined size selection
-   Search modules
-   Category filtering
-   Selected card state
-   Selected size state
-   Module picker transitions
-   Edit mode transitions
-   Local persistence

Do not stop after creating static UI.

Implement the complete interaction and state changes.

------------------------------------------------------------------------

# DESIGN DIRECTION

Use:

-   Inter typography
-   Modern enterprise design
-   Premium and professional visual language
-   Clear information hierarchy
-   Generous but controlled whitespace
-   Soft gradients where appropriate
-   Consistent card structure

Avoid:

-   Random colors for every card
-   Too many gradients
-   Heavy shadows
-   Excessive borders
-   Excessive rounded containers
-   Decorative UI without purpose
-   Generic dashboard appearance

Different card types can have different visual treatments, but they must
feel like part of one design system.

------------------------------------------------------------------------

# FINAL IMPLEMENTATION GOAL

Transform the existing Modules section into a polished, responsive,
customizable module dashboard.

The experience should conceptually take inspiration from:

**macOS / iPadOS widget customization**

But adapt it specifically for this enterprise Zoo / Animal Management
Command Centre.

The Home Page should remain simple in normal mode.

Customization controls should appear only when the user enters **Edit
Modules** mode.

Use one unified responsive component system across:

-   Mobile
-   Tablet
-   Desktop
-   Large Desktop

Do not create separate unrelated designs for each breakpoint.

The same system should progressively adapt through:

-   Number of grid columns
-   Card spans
-   Card stacking
-   Spacing
-   Typography scale
-   Content density
-   Module picker layout
-   Touch vs mouse interaction

Start by inspecting the existing implementation.

Then implement the complete experience end-to-end.

Preserve unrelated parts of the existing application.

After implementation, review and refine:

-   Responsive behavior
-   Grid alignment
-   Typography
-   Spacing
-   Card hierarchy
-   Tablet usability
-   Desktop information density
-   Mobile touch experience
-   Drag and drop behavior
-   Edit flow

The final result should feel production-ready.
