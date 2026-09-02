# Gemini Visual Style Prompt

Use this prompt to create a practical visual for this repository. The approved direction is the utility style in [How I Approach It](../assets/diagrams/how-i-approach-it.svg), not the previous illustration style.

Every image still needs checking for missing words, spelling mistakes, small text, contrast and visual drift before publication.

## Reusable Prompt

```text
Create one compact, evidence-led diagram for a public GitHub repository called Practical AI Sales Workflows.

Audience

Nontechnical B2B salespeople. They should understand the visual in a few seconds without needing to understand GitHub, coding or technical AI terminology.

Purpose

The visual must help someone make a decision, understand the evidence or take a useful next step. It must not be a decorative illustration or a generic picture of AI.

Visual system

- Flat, minimal, practical and calm
- Transparent background so it works on GitHub in light and dark mode
- Use a limited palette:
  - Dark text: #1F2937 in light mode, #F0F6FC in dark mode
  - Muted text: #57606A in light mode, #A9B1BB in dark mode
  - Borders: #D0D7DE in light mode, #30363D in dark mode
  - Blue for AI-supported work: #0969DA in light mode, #58A6FF in dark mode
  - Purple for human decisions: #8250DF in light mode, #D2A8FF in dark mode
  - Amber only for cautions or additional approval
- Use clean rounded rectangles, simple directional lines and plain labels
- Use the same corner radius, line weight and spacing throughout
- Use no illustrations, characters, robots, stars, stickers, doodles, speech bubbles, gradients or decorative shapes
- Use no icons unless their meaning is obvious without a key
- Use a clear sans-serif typeface such as Inter, Arial or system UI
- Do not place text on a bright solid background

Writing

- Use plain British English
- Keep labels short and exact
- Do not use em dashes, unnecessary hyphens, jargon or corporate language
- Do not rewrite, shorten or add to the supplied wording
- Do not invent facts, stages, outputs or terminology

Layout

- Create a landscape SVG, normally 1000 pixels wide and 300 to 430 pixels high
- Make it readable at about 700 pixels wide in a GitHub README
- Use three to five sections only
- Use a simple left-to-right flow, a small comparison or a before-and-after example
- Give each section one short heading and no more than two short lines
- Make human review or approval visually distinct from AI-supported work
- Do not imply that AI sends messages, changes systems or makes final decisions automatically
- Prefer an actual source-and-output example when the point is evidence quality

Accessibility

- Do not rely on colour alone
- Use readable font sizes and strong contrast
- Include a title and description in the SVG
- Provide concise GitHub alt text that states the information the visual conveys

Output

Create one SVG. Also provide:

1. A plain text list of every word shown
2. A suggested filename using lowercase words and hyphens
3. Suggested alt text for GitHub

Diagram brief

Title:
[Insert title]

Main point:
[What someone should understand within five seconds]

Exact text to display:
[Insert the exact labels]

Important distinction:
[What must not be misunderstood]
```

## Before Publishing

- Compare the text in the graphic against the source wording
- Check it at the approximate width used in the README
- Check both light and dark backgrounds
- Reject missing words, rewritten labels, small text and decorative clutter
- Confirm the visual helps a visitor make a choice, understand evidence or take a next step
- Add concise alt text that explains the information, not the layout
