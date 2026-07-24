# Gemini Visual Style Prompt

Use this prompt to create diagrams that match the visual style of [How I Approach It](../assets/diagrams/how-i-approach-it.svg).

The reference image is the approved standard. Every new image still needs checking for missing words, spelling mistakes, small text and visual drift before it is published.

## Reusable Prompt

```text
Create a clear, playful diagram for a public GitHub repository called Practical AI Sales Workflows.

Use the approved colours, typography and playful illustrated style from How I Approach It, but do not copy its three-card layout every time. The repository should feel useful, warm and human, not like a corporate presentation. Change only the content supplied in the diagram brief.

Audience

The audience is nontechnical B2B salespeople. They should understand the diagram within a few seconds without needing to understand GitHub, coding or technical AI terminology.

Visual style

- Warm white or very pale tinted background
- Dark navy text: #152238
- Teal as the main accent: #2A9D8F
- Warm amber for warnings, questions or human decisions: #E9C46A
- Pale grey cards or sections: #F4F6F8
- Friendly editorial or illustrated style
- Use sticker shapes, sticky notes, speech bubbles, curved paths or slightly uneven layouts where they help
- Use simple, characterful line illustrations rather than generic corporate icons
- Small doodles, stars, ticks or squiggles are welcome when they add energy without adding clutter
- Use generous spacing, but do not leave large dead areas
- Not every stage needs to sit inside the same rectangular card
- Avoid rigid grids unless the information genuinely needs one
- Avoid the look of a consultancy slide, process map or internal training deck
- Strong contrast
- No gradients
- No decorative AI imagery
- No robots, glowing brains, circuit boards or futuristic dashboards
- Use a clear sans serif typeface such as Inter or Arial

Writing style

- Use plain British English
- Use proper capitalisation
- Keep text short and conversational
- Do not use em dashes
- Do not use unnecessary hyphens
- Avoid corporate language and technical jargon
- Do not rewrite, shorten or add to the supplied wording without permission
- Do not invent facts, stages, outputs or terminology

Layout

- Create a landscape image at 1600 by 900 pixels
- Make it readable when displayed at approximately 700 pixels wide on GitHub
- Use no more than five main sections
- Use a clear visual direction, which can be curved, stepped or left to right
- Keep each box to a heading and no more than two short lines
- Make the most important message visually obvious
- Make human decisions visually distinct from AI supported work
- Do not imply that AI sends messages, changes systems or makes final decisions automatically

Accessibility

- Do not rely on colour alone to communicate meaning
- Use readable font sizes
- Avoid pale text
- Make labels understandable without needing a separate key

Output

Create one polished diagram.

Also provide:

1. A plain text list of every word shown in the image
2. A suggested filename using lowercase words and hyphens
3. Suggested alt text for GitHub
4. A PNG version
5. An SVG version if supported

Diagram brief

Title:
[Insert title]

Main point:
[What someone should understand within five seconds]

Sections or stages:
[Insert the exact stages]

Exact text to display:
[Insert the exact wording]

Important distinction:
[What must not be misunderstood]

Do not generate additional concepts or alternative designs. Follow the approved colours, writing style and accessibility rules, while keeping the layout lively and human.
```

## Before Publishing

- Compare the image against the plain text list word by word
- Check it at the size it will appear on GitHub
- Reject missing words, rewritten labels or smaller text
- Add concise alt text that explains the information, not every decorative detail
- Keep the downloaded original outside the repository and add an optimised copy for the README
