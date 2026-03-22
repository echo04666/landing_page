# Design System Specification: Galactic High-Fidelity

## 1. Overview & Creative North Star: "The Neon Monolith"
This design system is built upon the Creative North Star of **"The Neon Monolith."** We are moving away from the cluttered, "noisy" interfaces typical of early Web3 and toward a high-end, editorial gaming experience. The aesthetic balances the vast, silent void of deep space with the high-energy pulse of a digital frontier.

By utilizing intentional asymmetry, we break the "template" look. We favor large, expansive typography paired with hyper-dense data modules. The layout should feel like a premium heads-up display (HUD) for a high-stakes interstellar player—authoritative, sophisticated, and innovative.

---

### 2. Colors: Tonal Depth & Radiant Accents
The palette is rooted in a "Void-First" philosophy. We do not use borders to define space; we use light and shadow.

#### The "No-Line" Rule
**Explicit Instruction:** 1px solid borders are prohibited for sectioning. Structural boundaries must be defined solely by shifting from `surface` to `surface-container-low` or `surface-container-high`. The eye should follow the light, not the lines.

#### Surface Hierarchy & Nesting
Treat the UI as a physical stack of semi-translucent materials. 
- **Base Layer:** `surface` (#0e0e11)
- **Primary Sections:** `surface-container-low` (#131316)
- **Interactive Cards:** `surface-container` (#19191d)
- **Pop-overs/Modals:** `surface-container-highest` (#25252a)

#### The "Glass & Gradient" Rule
To achieve a "bespoke" feel, use **Glassmorphism** for all floating elements. Use the `surface` color at 60% opacity with a `40px` backdrop blur. 
- **Signature Glow:** Apply a linear gradient from `primary` (#e08dff) to `secondary` (#00eefc) at a 45-degree angle for high-energy CTAs. This creates a visual "soul" that flat colors cannot replicate.

---

### 3. Typography: The Geometric Voice
We use a triad of typefaces to establish an editorial hierarchy that feels both futuristic and trustworthy.

- **Display (Space Grotesk):** Our "Hero" voice. Use `display-lg` for impactful headlines. The wide apertures and geometric forms suggest innovation.
- **Headlines & Titles (Inter):** The "Functional" voice. Inter provides the legibility required for complex Web3 data (wallets, marketplace listings) while maintaining a modern edge.
- **Labels (Plus Jakarta Sans):** The "Micro" voice. Used for metadata and button labels (`label-md`). Its slightly wider stance ensures readability at small scales against dark backgrounds.

**Hierarchy Strategy:** Use extreme contrast. Pair a `display-lg` headline with `body-sm` metadata to create a sense of scale and premium design intentionality.

---

### 4. Elevation & Depth: Tonal Layering
We do not use standard material shadows. Depth is an environmental effect.

- **The Layering Principle:** To lift a card, do not add a shadow immediately. Instead, place a `surface-container-highest` card atop a `surface-dim` background. The delta in luminance creates the lift.
- **Ambient Shadows:** For floating modals, use an "Atmospheric Glow." Instead of a black shadow, use a 4%-8% opacity shadow tinted with `secondary` (#00eefc) with a `64px` blur. It should look like the element is emitting light, not blocking it.
- **The "Ghost Border" Fallback:** If a boundary is strictly required for accessibility, use the `outline-variant` token at **15% opacity**. It should be felt, not seen.

---

### 5. Components: The High-Energy Library

#### Buttons: The Kinetic Pulse
- **Primary:** Gradient fill (`primary` to `primary-dim`). No border. `0.25rem` (DEFAULT) roundedness. On hover, apply a `secondary` glow (shadow-drop) and a subtle 2px upward translation.
- **Secondary:** Transparent background with a `secondary` "Ghost Border" (20% opacity). On hover, the border opacity snaps to 100%.

#### Cards: The Data Monolith
- **Rule:** No divider lines. Use `spacing-8` (2rem) of vertical white space or a shift to `surface-container-low` to separate header from body.
- **Visuals:** Use a "Subtle Glow" border on hover—a 1px `outline-variant` that fades in, giving the impression of the card "powering up."

#### Input Fields: The HUD Input
- **Style:** Background `surface-container-lowest`. Bottom-only border (2px) using `outline-variant`. 
- **Focus State:** The bottom border transforms into a `secondary` (#00eefc) to `tertiary` (#ff6b98) gradient.

#### Web3 Specifics: Wallet & Asset Modules
- **Transaction Chips:** Use `secondary_container` for "Pending" and `tertiary_container` for "Critical/Action Required." 
- **Inventory Grids:** Ensure items are housed in `surface-container` cards with sharp `0.25rem` corners to maintain the "Monolith" aesthetic.

---

### 6. Do's and Don'ts

#### Do
- **Do** use `display-lg` for large, empty states to create an editorial feel.
- **Do** use `primary` and `secondary` gradients for progress bars and "Level Up" moments.
- **Do** lean into asymmetry; allow some elements to bleed off the edge of the grid to suggest a larger digital world.

#### Don't
- **Don't** use 100% white (#FFFFFF) for text. Always use `on-surface` (#f3f0f4) to prevent retina fatigue on deep black backgrounds.
- **Don't** use standard "Drop Shadows." They feel "Web 2.0." Stick to tonal shifts and ambient glows.
- **Don't** use rounded corners larger than `xl` (0.75rem) unless it's a pill-shaped chip. We want "sharp and clean," not "bubbly."
- **Don't** use dividers. If you feel the need for a line, add more space (`spacing-12`).

---

### 7. Spacing & Rhythm
This system thrives on "Breathing Room." High-energy gaming platforms are often cramped; we differentiate by being expansive. 
- Use `spacing-16` (4rem) for major section vertical padding.
- Use `spacing-4` (1rem) for internal component padding.
- Always align typography to a strict baseline grid to ensure that even with asymmetrical layouts, the experience feels "Trustworthy" and engineered.