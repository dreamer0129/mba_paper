# Institutional DeFi on the XRP Ledger: What's Live and What's Next

**发布日期**: February 25, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/institutional-defi-xrp-ledger/](https://ripple.com/insights/institutional-defi-xrp-ledger/)

## 支付相关度评估
**评级**: 🔴 高度相关
**关键词匹配数**: 9

## 摘要
XRPL is pioneering Institutional DeFi. Explore innovations such as AMM, DID, price oracles and other features shaping the future of regulated onchain finance.

## 核心内容

Team Ripple

Institutional adoption of blockchain-powered finance has accelerated in the past year, with tokenized real-world assets (RWAs), stablecoins, and decentralized liquidity markets as major drivers of growth. Yet, for this transformation to scale, financial institutions need a robust, compliance-focused, and interoperable blockchain infrastructure—one that can support digital assets, seamless cross-border transactions, and institutional-grade decentralized finance (DeFi).

The XRP Ledger (XRPL) meets this challenge head-on, building on its core strengths—a native DEX, low fees, rapid settlement times, and a compliance-friendly architecture—to create an advanced institutional DeFi ecosystem. Several key capabilities are live, with others on their way, which will support the XRPL as a safe, secure, and scalable layer 1 for financial institutions looking to use blockchain in a regulated environment.

XRPL has made significant strides in enhancing liquidity, improving price transparency, and introducing new compliance tools to better cater to the needs of institutions.

While this blog highlights several of the newest features live on the XRP Ledger, they build upon core functionalities that have been supporting financial use cases for over a decade. The move towards a more automated and integrated system within XRPL’s native Decentralized Exchange (DEX) is designed to facilitate greater institutional participation by ensuring constant liquidity and minimal slippage. XRPL’s Central Limit Order Book (CLOB) has powered decentralized trading since its inception, providing efficient price discovery and deep liquidity across assets.

Meanwhile, Payments—one of the ledger’s first native capabilities—continues to facilitate fast, low-cost global transactions, with additional payment primitives like Payment Channels for scalable micropayments, Checks for deferred settlement, and Escrows for conditional transfers. These are just some of the long-standing features that, combined with recent innovations, make XRPL one of the most mature and robust blockchains for institutional DeFi. With over 2.8B transactions having been processed to date, XRPL continues moving from strength to strength.

XRPL’s Automated Market Maker (AMM), built on the XLS-30 standard, introduces protocol-level liquidity for tokenized assets, stablecoins, and real-world assets (RWAs). Unlike traditional AMMs, XRPL’s version integrates directly with its native order book (CLOB)-based DEX, and enables price optimization to determine whether swapping within a liquidity pool, through the order book, or both provides the best rate and executes accordingly. Its continuous auction mechanism mitigates impermanent loss, making liquidity provision more appealing to institutional players.

Thanks to AMM Clawback, all key tokens, including Ripple USD (RLUSD), can fully leverage the network’s AMM liquidity pools. By enabling issuers to “claw back” funds from a trustline in specific circumstances—like lost account access or malicious activity—this amendment satisfies crucial regulatory requirements for fraud prevention and transaction reversals. Clawback remains an optional feature, intentionally disabled by default that can only be enabled for issued assets and never for XRP.

Key Use Cases

Now that XLS-40 is live, institutions and developers can create and manage decentralized identifiers (DIDs) directly on the Ledger. This feature enables self-sovereign identity, allowing users to establish verifiable identities without relying on centralized intermediaries.

By leveraging DIDs, institutions can enhance security, privacy, and compliance while maintaining decentralization. This lays the groundwork for permissioned access to financial markets, identity verification for tokenized real-world assets (RWAs), and broader institutional adoption of DeFi.

Key Use Cases

Real-time and accurate price feeds are critical for institutional DeFi—especially when dealing with tokenized assets and cross-chain transactions. To meet this need, the XRP Ledger integrates protocol-native oracles, providing a built-in mechanism for bringing off-chain data (like stablecoin rates and real-world asset valuations) onchain. Because these oracles are embedded directly into the XRPL—much like its native AMM—they avoid reliance on separate third-party layers, ensuring more efficient and trustworthy data flows.

Providers such as Band Protocol and DIA are already live on the XRPL mainnet, delivering robust price feeds that span both crypto and traditional markets. This is essential for institutions, given that much of the data required still resides in legacy Web2 systems.

Key Use Cases

XRPL is evolving with new features that bring greater compliance functions, expanded lending, and more ways to build onchain financial products. These changes will enable institutions to meet regulatory requirements, offer new lending options, and give developers more flexibility to build and deploy financial applications.

Stay informed on what's coming on Open Source Ripple

Enhancing the ‘Identity Stack’ in finance tools will enable institutions to build secure, compliant trading venues on XRPL.

Credentials are designed to be a lightweight feature and are additive to the recent Decentralized Identity (DID) standard. The Credentials standard introduces a new ‘Credential’ ledger object along with new transaction types for creating, accepting, and deleting credentials. The XLS-70 spec for Credentials on the XRPL is currently undergoing the amendment voting process as part of the rippled 2.3.0 release.

Ripple Senior Software Engineer, Mayukha Vadari, recently outlined how to consider Credentials as a modular building block to DID. It can be applied to attest to specific criteria (e.g. KYC) pertaining to a user and issued to their DID. This is critical in terms of enabling a smooth onboarding process when accessing products like tokenized RWAs.

Credentials and DID give rise to two additional features, Permissioned Domains and a Permissioned DEX, that help facilitate a flexible, institutional-grade identity system on XRPL.

Permissioned Domains allow entities, such as financial institutions, to establish environments on the XRPL that require specific credentials for access. This setup enables organizations to define membership criteria, such as Know Your Customer (KYC) credentials from trusted issuers, and manage participation within their domain. Importantly, this system preserves user privacy by verifying credential validity without exposing personal information.

Building upon this, the Permissioned DEX extends the XRPL’s native DEX to operate within these controlled domains, ensuring that only accounts with valid credentials can create or fill orders. This approach allows institutions to engage in decentralized trading while adhering to regulatory requirements, such as Anti-Money Laundering (AML) and KYC rules, all within a decentralized framework.

While DIDs serve as a foundational “fingerprint” for each user, Credentials provide the identity and compliance layer required for different scenarios. Building on these foundations, Permissioned Domains and Permissioned DEX protocols enforce membership and compliance rules by requiring the appropriate DID-based Credentials, all while preserving the open nature of the XRPL.

Traditional financial instruments such as stocks, bonds, and other securities possess intricate data requirements that can be challenging to represent onchain as fungible tokens. For instance, two bonds may be identical in all regards except their expiry dates, which is a critical detail and makes it inappropriate to present both as equivalent.

To solve this, the XRPL developer community has introduced Multi-Purpose Tokens (MPTs) which bridge the gap between fungible and non-fungible tokens. They are akin to “semi-fungible” tokens whereby key associated metadata can be attached. This provides them with more flexibility than fungible tokens, while they’re not truly unique such as with NFTs.

Currently undergoing validator voting, MPT introduces a more flexible, efficient, and metadata-rich token standard that allows institutions to tokenize and trade bonds, RWAs, and structured financial products with enhanced functionality.

Key Use Cases

The XRP Ledger-native lending protocol adds a pivotal dimension to the XRPL’s DeFi capabilities. This proposed amendment will enable crypto-native businesses to integrate lending with Ripple Payments, DEX, RWAs, and stablecoins, using a default RLUSD vault to reduce liquidity fragmentation and AMM for seamless FX swaps. It will also look to streamline asset allocation and fund admin for crypto-native managers with automated returns, real-time valuations, diversified strategies, and compliant execution via RWAs and onchain KYC.

Institutional DeFi requires robust, scalable, and secure financial products. The XRPL-native lending protocol addresses these needs by providing a decentralized, protocol-native solution for lending that reduces reliance on intermediaries, enhances transparency, and offers a higher degree of security.

The lending protocol specs, XLS-65d, will allow for the pooling of assets (public or private) represented by Vault shares, with optional Permissioned Domain access, while XLS-66d will introduce on-ledger, fixed-term, uncollateralized lending with off-chain underwriting and first-loss capital protection, allowing financial institutions to issue credit and manage risk directly on the blockchain. You can expect these developments to undergo voting in Q2 of 2025.

Key Use Cases:

As announced in September, Ripple, in collaboration with the community, is committed to bringing permissionless programmability to the XRPL. Programmability on the XRPL offers an opportunity to seamlessly connect its powerful, native building blocks with the flexibility of custom on-chain business logic. This vision focuses on preserving what makes the XRPL special—its efficiency, reliability, and simplicity—while empowering builders to unlock new possibilities. This goal requires a measured approach, with careful steps that ensure the robustness of the network.

The first step of this broader effort will see the introduction of 'Extensions,’ a feature that allows developers to attach small pieces of code to existing XRPL primitives, enhancing their functionality without the need for entirely new smart contracts.

This approach can enable the customization of features like escrows, automated market makers (AMMs), and tokens, making them more adaptable to specific use cases while maintaining efficiency and security. For instance, “Smart Escrows” allow developers to incorporate custom release conditions, such as notary approvals or price-based triggers, without needing to rebuild the escrow mechanism from scratch. This method preserves the robustness of XRPL’s native features while offering tailored solutions for complex requirements.

The timeline toward deployment is outlined below:

For a detailed overview on ‘Extensions’ and broader programmability efforts you can dive into RippleX Devto blog.

The XRPL EVM sidechain serves a complementary role to the XRPL, but is not a replacement for mainnet programmability.

Set for Mainnet launch in Q2 2025, the XRPL EVM Sidechain offers a great opportunity to attract EVM ecosystem developers to the XRPL ecosystem. It can also be used to launch protocols that are not currently possible on the XRPL - especially ones that are already written in Solidity, or specifically require the EVM. This bridged solution, using a cross-chain approach, is useful if a project requires an alternative form of programmability.

Key Benefits:

As tokenization and decentralized finance continue to evolve, XRPL is positioning itself as a leader in regulated onchain finance. With deep liquidity, compliance-friendly features, and seamless institutional integration, the next phase of Institutional DeFi will be built on XRPL.

While a dedicated roadmap page is in development, the broader XRPL ecosystem is actively shaping the future of institutional DeFi through innovations such as Automated Market Makers (AMMs), Price Oracles, Decentralized Identifiers (DIDs), and new tokenization standards. These developments reflect ongoing collaboration across the network to enhance security, efficiency, and institutional-grade financial tools.

Visit xrpl.org to learn more and get started today.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
