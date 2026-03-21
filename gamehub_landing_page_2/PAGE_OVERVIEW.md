# GameHub Landing Page — Overview

A single-page site for **GameHub**, a **Web3 smart-banking–style** scenario that fuses **gaming with the real economy**: indie studios raise funds by preselling **game utility tokens** (on the page: **GHT**), while players gain **in-game redemption rights** and an optional path to **limited physical merchandise**—with **smart-contract escrow and automated splits** as the trust backbone.

---

## Purpose

Help visitors understand **what they are buying**, **how money moves**, **what happens when they redeem or do not redeem**, and **why the stack is credible**, so they can decide whether to connect a wallet, buy tokens, or follow the project.

---

## What Visitors Learn From This Page

| Topic | Information conveyed |
|--------|----------------------|
| **Product story** | GameHub bridges **virtual gaming value** and **real-world assets** (skins, currency, optional figurines). |
| **Fundraising status** | **Target 200,000 HKD**, **raised 85,000 HKD** so far (~**42.5%**), so users see how close the round is to goal. |
| **Token economics (sale)** | **20 HKD per token**, **10,000 tokens** available, aligned with a **200,000 HKD** cap at full subscription. |
| **What one token buys (virtual)** | **1 token** maps to **rare in-game skin + in-game currency** (the broader scenario values the bundle at **~25 HKD** of in-game value vs **20 HKD** paid—a designed “supporter upside”). |
| **Physical upgrade** | Holders can add **+50 HKD** to redeem a **limited official figurine** with **shipping included** (ties the digital voucher to **physical fulfillment**). |
| **How to pay** | **eHKD**, **USDC**, **credit card**, **FPS**, **Open Banking**—signaling both **CeFi rails** and **digital assets**. |
| **On-chain anchor** | Example **smart contract** address and a path to **block explorer** (e.g. PolygonScan), so users know where to verify the contract. |
| **Money after purchase** | Funds sit in **smart contract custody** until redemption or rules trigger release—not immediately spendable by the studio in an opaque way. |
| **Split on redemption (in-game path)** | On redemption, proceeds are allocated **40% development**, **20% art & servers**, **30% marketing & publishing**, **10% platform fee**—matching **8 / 4 / 6 / 2 HKD per 20 HKD** in the full scenario. |
| **If tokens are not redeemed** | After expiry / lock-up, funds can **flow to the studio** for continuity, **minus platform fee** (the page echoes this “sustainability” clause; the detailed model cites e.g. **18 HKD** to studio, **2 HKD** platform on expiry). |
| **Physical add-on (extended model)** | The landing page focuses on the **+50 HKD** upgrade; a fuller product design can route that top-up through a **separate flow** to **production, logistics, studio, and platform** (e.g. **30 / 10 / 5 / 5 HKD** split in the scenario doc). |
| **Trust & compliance posture** | **SSI + ZKP** for privacy-sensitive proofs, **DeFi liquidity** (e.g. Uniswap) for secondary market context, and **partners** (Chainalysis, Open Banking, Polygon, thirdweb) for **AML, banking rails, chain, and contract tooling**. |
| **Who builds it & what’s next** | Team positioning (indie devs + blockchain + gaming) and **roadmap**: **Q3 2025** token sale → **Q4 2025** beta → **Q1 2026** full launch **including physical shipment** and exchange-related rollout. |
| **Where to go deeper** | Footer entry points: **contract**, **social**, **FAQ**, **privacy**—for due diligence and community. |

---

## Functional Flows (Product-Level, as Reflected on the Landing Narrative)

The page does not run these steps in software; it **describes** the intended **SBIF-style** lifecycle so users mentally map **purchase → custody → redemption → settlement**.

1. **Studio / project setup** (background, not shown as a wizard on this page)  
   Define raise cap (**200,000 HKD**), token count (**10,000**), price (**20 HKD**), redemption window (e.g. **12 months after game launch** in the full scenario), and **split percentages** baked into contracts.

2. **User buys token**  
   User pays via **fiat or stablecoin** channels → tokens are **minted / delivered** to a **self-custody or hosted wallet**; **funds lock in a GameFunding-style contract** rather than going straight to the studio wallet.

3. **User redeems — virtual only**  
   User claims **in-game bundle** (skin + currency). Contract (plus **oracle / server attestation** in a full build) confirms fulfillment → **automatic split**: development, art/infra, marketing, platform fee as shown on the page.

4. **User redeems — with physical upgrade**  
   User pays **additional 50 HKD** (page-level promise); extended architecture records obligation **on-chain**, fulfills **off-chain production & logistics**, then **updates status on-chain** when shipped/delivered.

5. **Expiry — unredeemed tokens**  
   After the deadline, **unredeemed** positions trigger **release rules**: studio receives the bulk **net of platform fee**, aligning with “project continuity” messaging on the page and the detailed **18 / 2 HKD** style settlement in the scenario.

6. **Secondary liquidity (context on page)**  
   **DeFi / DEX** mention sets expectation that tokens may trade **after primary sale**, separate from the **redemption** path.

---

## On-Page Sections (Content Map)

| Area | What it communicates |
|------|----------------------|
| **Navigation** | Brand, jump links (Presale, Utilities, Flow, Roadmap), **Connect Wallet**. |
| **Hero** | Headline on **virtual ↔ real**, supporting line on **GHT tokenomics**, **Buy GHT** CTA, **funding progress** toward **200,000 HKD**. |
| **Token sale card** | Price, supply, **payment methods**, contract snippet, explorer CTA. |
| **Token utilities** | **Virtual redemption** vs **+50 HKD physical** upgrade. |
| **Fund flow** | **Percentage split** on redemption + **note on unredeemed / lock-up** release. |
| **Trust & innovation** | **SSI / ZKP / DeFi** plus **partner** names. |
| **Team & roadmap** | Team framing and **Q3 2025 → Q4 2025 → Q1 2026** milestones. |
| **Footer** | Contract, social, FAQ, legal link, copyright. |

---

## Note on Naming and Scope

The scenario document sometimes refers to **game prop vouchers (FT)**; this landing implementation uses **GHT (GameHub Token)** as the ticker. The **economic intent** is the same: **presale financing + contract-enforced allocation + optional real-world redemption**. A live product would add **live pool balances**, **purchase UI**, and **oracle-backed redemption** beyond what this static page demonstrates.
