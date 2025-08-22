Module 16 – CSS 

---------------------------------------------------
4. CSS Selectors & Styling
---------------------------------------------------

Q1: What is a CSS selector? Provide examples of element, class, and ID selectors.
- A CSS selector is a pattern used to target and style HTML elements.
- Examples:
  - Element selector:
    ```
    p {
      color: blue;
    }
    ```
  - Class selector:
    ```
    .highlight {
      background-color: yellow;
    }
    ```
  - ID selector:
    ```
    #header {
      font-size: 24px;
    }
    ```

Q2: Explain the concept of CSS specificity. How do conflicts between multiple styles get resolved?
- Specificity determines which CSS rule applies when multiple rules target the same element.
- Priority order:
  1. Inline styles
  2. ID selectors
  3. Class, attribute, and pseudo-class selectors
  4. Element selectors and pseudo-elements
- If specificity is the same, the last defined style is applied.

Q3: What is the difference between internal, external, and inline CSS? Discuss the advantages and disadvantages of each approach.
- Inline CSS:
  * Written inside the HTML element using style attribute.
  * Example: `<p style="color:red;">Text</p>`
  * Advantage: Quick and specific.
  * Disadvantage: Hard to maintain, not reusable.

- Internal CSS:
  * Written inside `<style>` tag in the head of an HTML page.
  * Advantage: Centralized styling for one page.
  * Disadvantage: Cannot be reused across multiple pages.

- External CSS:
  * Written in a separate .css file and linked to HTML.
  * Example: `<link rel="stylesheet" href="style.css">`
  * Advantage: Best for reusability and maintainability.
  * Disadvantage: Requires extra HTTP request.


---------------------------------------------------
5. CSS Box Model
---------------------------------------------------

Q1: Explain the CSS box model and its components.
- Every element is a box with:
  1. Content – actual text or image
  2. Padding – space between content and border
  3. Border – surrounds the padding
  4. Margin – space outside the border
- Total element size = content + padding + border + margin.

Q2: What is the difference between border-box and content-box in CSS? Which is the default?
- content-box (default):
  Width and height apply only to content. Padding and border are added outside.
- border-box:
  Width and height include content, padding, and border. Easier for layouts.

---------------------------------------------------
6. CSS Flexbox
---------------------------------------------------

Q1: What is CSS Flexbox, and how is it useful for layout design? Explain flex-container and flex-item.
- Flexbox (Flexible Box Layout) is a 1D layout system for arranging items in rows or columns.
- `flex-container`: Parent element with display:flex.
- `flex-item`: Child elements inside the container.

Q2: Describe the properties justify-content, align-items, and flex-direction.
- `flex-direction`: Sets the main axis (row, column, row-reverse, column-reverse).
- `justify-content`: Aligns items along the main axis (flex-start, center, flex-end, space-between, space-around).
- `align-items`: Aligns items along the cross axis (stretch, flex-start, center, flex-end).

---------------------------------------------------
7. CSS Grid
---------------------------------------------------

Q1: Explain CSS Grid and how it differs from Flexbox. When would you use Grid over Flexbox?
- CSS Grid is a 2D layout system that controls both rows and columns.
- Flexbox is 1D (only rows OR columns).
- Use Grid for page layouts, dashboards, complex grids.
- Use Flexbox for navbars, buttons, or single-row/column alignment.

Q2: Describe the grid-template-columns, grid-template-rows, and grid-gap properties.
- grid-template-columns: Defines column widths.
  Example: grid-template-columns: 200px 1fr 2fr;
- grid-template-rows: Defines row heights.
  Example: grid-template-rows: 100px auto 50px;
- grid-gap (or gap): Space between rows and columns.
  Example: gap: 20px;

---------------------------------------------------
8. Responsive Web Design with Media Queries
---------------------------------------------------

Q1: What are media queries in CSS, and why are they important?
- Media queries apply styles depending on device screen size, resolution, or orientation.
- Important for making websites responsive across mobile, tablet, and desktop.

Q2: Write a basic media query that adjusts font size for screens smaller than 600px.
```
@media (max-width: 600px) {
  body {
    font-size: 14px;
  }
}
```

---------------------------------------------------
9. Typography and Web Fonts
---------------------------------------------------

Q1: Explain the difference between web-safe fonts and custom web fonts. Why might you use a web-safe font over a custom font?
- Web-safe fonts: Pre-installed on all systems (e.g., Arial, Times New Roman).
- Custom web fonts: Downloaded from services like Google Fonts.
- Web-safe fonts load faster and work offline, while custom fonts provide more design options.

Q2: What is the font-family property in CSS? How do you apply a custom Google Font to a webpage?
- font-family defines the typeface of text.
  Example: body { font-family: Arial, sans-serif; }
- To use Google Font:
  1. Add in head:
     ```
     <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
     ```
  2. Apply in CSS:
     body { font-family: 'Roboto', sans-serif; }
