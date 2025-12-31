# MPC and HSM for Key Management Part 1: Demystifying Technology Options for Digital Asset Custody

**发布日期**: December 16, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/mpc-and-hsm-for-key-management-part-1-demystifying-technology-options-for-digital-asset-custody/](https://ripple.com/insights/mpc-and-hsm-for-key-management-part-1-demystifying-technology-options-for-digital-asset-custody/)

## 支付相关度评估
**评级**: 🟡 中度相关
**关键词匹配数**: 3

## 摘要
Rising digital asset diversity sparks demand for secure crypto custody solutions. Learn how banks are poised to leverage a wide array of custodian options.

## 核心内容

Team Ripple

The rapidly growing universe of digital asset types, tokenization and use cases is driving an urgent demand for more secure institutional digit asset custody solutions. Providers are rushing to fulfill this need by providing high net worth individuals, family offices, enterprises and others with a wider array of custodian options.

Banks and financial services institutions have a unique opportunity to leverage their long history as custodians of traditional assets to diversify their portfolios and offer trusted digital asset custody solutions for clients. But how to make sense of the different key management technology and protection options available?

In this first post in a two-part series, we’ll look at three technology decisions providers must make as part of rolling out a crypto custody solution.

At the core of any custodian strategy lies the ability to securely hold and access a range of digital assets. This access is granted through cryptographic private keys, which enable the transfer or control of the asset. Securing these keys is paramount, and that begins with a choice of wallet.

Hot wallets are those connected to the web. Designed for real-time transactions, they are ideal for high-frequency, low-risk activities. They are ideal for permissioned use cases requiring fast, automated access to liquidity and web transactions, for example conveniently accessing funds on the go. However, their constant connection to the internet—while convenient for accessing funds—makes them more vulnerable to attacks and often requires the use of additional advanced protection technologies.

On the other hand, cold wallets feature offline storage of private keys within a physical hardware wallet, which means the process of accessing funds within a cold wallet can be extremely manual. While this can pose challenges for many institutional needs, it also helps to de-risk the storage of digital assets. Given their nature and enhanced security to mitigate the risk of cyber-attacks, they are best used for crypto custody or low-frequency, high-risk transactions.

Another more recent form of cold wallet technology to come on the scene is air-gapped cold wallets, which are hardware wallets completely disconnected from any wireless network, including WiFi and bluetooth. “Air-gap” is a computer security term referring to the complete isolation of a device or a network from other networks or devices.

Last but not least, account abstraction—which leverages smart contracts to manage funds—allows users to retain full control over their wallet and funds. They are protected by a multi signature wallet from either cold wallets or hot wallets.

Within institutional wallets, there are two primary options today for managing private keys. The most straightforward and simplest to understand are Hardware Security Modules (HSMs). These are physical hardware devices or cloud-based storage options that have been specifically developed to protect crypto keys using a combination of physical security, cryptographic isolation, secure communications and detailed audits and logs. They are ideal for use cases like air-gapped wallets that are disconnected from the internet, high-level security standards or assets held in long-term storage.

While secure options for owners, HSMs are useless if the wrong person acquires control of the device. Multiparty Computation (MPC) technique was developed to avoid this single point of failure. This cryptographic technique involves “sharding” private keys into multiple distinct shares (often 2-3 shards) that are geographically distributed across multiple databases, cloud services or other storage options. This means that even if one part of a private key is compromised, the overall key remains unusable.

To add these extra layers of security and peace of mind, an MPC wallet requires additional computational resources. This performance tax is why most MPC solutions are limited to 3-4 different shards and better suited for permissioned use cases, fast or automated access to liquidity, and scenarios where cost, compliance or technical limitations make HSMs unfeasible.

Some MPC solutions have adopted versions of this approach where the service provider holds at least one of the key shards. However, this model means that the bank doesn’t have complete control of their own crypto assets and those of their clients. Mature regulated entities are ultimately responsible for the safekeeping of those assets, but are relinquishing part of that control with these types of solutions. To ensure the utmost safety and security, the physical storage of key share material should be managed by a single entity—the institution itself.

Beyond wallet types and key protection strategies, custodians must decide whether to host their custody solution with a provider or on their own servers.

A Software as a Service (SaaS) implementation is fairly straightforward. Managed by a third-party provider such as Metaco, they run in the cloud, allowing for fast deployment and near instant scaling. Like with other SaaS solutions, they require less up-front cost or ongoing resources. Everything is stored in the cloud and managed by the third-party, making them deploy-and-forget solutions that allow providers to focus on their core business requirements.

Conversely, on-premise (on-prem) custody solutions offer complete control of all data and processes and are ideal for banks and financial institutions that have strict risk, compliance or regulatory requirements. In these setups, the institution designs and provisions the hardware, manages and maintains all security considerations, and services process and software upgrades for the life of the system. The trade off for this control is the high up-front cost to deploy a solution and the ongoing resource requirements to manage it.

While these choices can seem overwhelming, the digital asset use cases for each provider and their clients will help dictate which combination of wallet, key security and solution type is best.

Contact us to learn more about the technical considerations and solutions criteria that will inform crypto custody provider technology choices.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
