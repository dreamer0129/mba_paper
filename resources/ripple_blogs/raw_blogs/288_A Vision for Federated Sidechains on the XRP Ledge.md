# A Vision for Federated Sidechains on the XRP Ledger

**发布日期**: December 16, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/a-vision-for-federated-sidechains-xrp-ledger/](https://ripple.com/insights/a-vision-for-federated-sidechains-xrp-ledger/)

## 支付相关度评估
**评级**: 🟡 中度相关
**关键词匹配数**: 4

## 摘要
Federated sidechain ledgers allow for experimentation and specialization. Discover the power of the XRPL on a sidechain that acts as its own blockchain.

## 核心内容

Team Ripple

Over the last nine years, the XRP community has been committed to advancing the innovation and forward progress of the XRP Ledger (XRPL) to dramatically increase its decentralization, performance, and feature set.

Among the most-requested features we have heard from developers and contributors to the XRP Ledger is smart contract capabilities brought about by the exponential growth in decentralized finance (DeFi). In fact, the number of DeFi developers has grown 110% since 2019, and that number is projected to grow well beyond 2021. However, we at Ripple have long advocated against features that would compromise the XRP Ledger’s highly efficient focus on payments.

Today, we are proposing a strategy that enables the best of both worlds: Federated Sidechains for the XRP Ledger. This will enable developers to implement new features, such as native smart contracts that interoperate seamlessly with XRP and the XRP Ledger, while also allowing the XRP Ledger to maintain its existing, “lean and efficient” feature set.

Federated Sidechains allow for experimentation and specialization, so developers can enjoy the power of the XRPL on a sidechain that acts as its own blockchain. For example, imagine the potential to branch out into new functionality by slimming down the XRPL’s features to a specific subset for a particular use case—or even creating a private, parallel network for a permissioned blockchain. Federated Sidechains could very well make this a reality.

In order to understand the vision for Federated Sidechains, it is first important to define a federator: a piece of software that connects to at least two instances of the XRPL software. The federator software means anyone who wanted to could run a sidechain to the XRP Ledger. On one side, the federator is connected to XRP Ledger Mainnet. On the other side, it connects to one or more sidechains. The federator would be run only by parties who operate validators on at least one sidechain.

The vision is that each sidechain would function as its own blockchain. They’d have their own ledger and transactions just as the XRP Ledger does. What makes them sidechains is the federation system which allows XRP and issued tokens to move from one chain to another.

Federated Sidechains could use XRP as their primary asset. In that case, people could use the federation system to move XRP from XRPL to the sidechain. Then, the moved XRP could be used on the sidechain just as it is on the main chain. Anyone could move XRP from either chain to the other.

Alternatively, sidechains could use their own native asset, so people with accounts on both ledgers could move XRP to and from the issued asset on the sidechain.

Functionality:

Federated assets imported onto XRPL itself would trade on the XRPL’s integrated decentralized exchange (DEX). XRP imported onto sidechains would be used for liquidity on their integrated DEX as well.

This strategy requires three things:

Each sidechain would have a “trust” account on the XRPL Mainnet. This account can hold assets on the XRPL on behalf of users of the sidechain. The account would use a multisign or threshold key with the signers being the validators of the sidechain. Each sidechain validator operator registers a signing key that signs transactions on XRPL; thus, the validators of the sidechain can collectively create transactions to manage the sidechain’s Mainnet account.

The XRP Ledger Mainnet has one native asset, XRP, and an unlimited number of issued tokens that can represent anything else but don’t have the same status as XRP. It wouldn’t make sense for each sidechain to start with a whole new set of 100 billion XRP, so instead, sidechains have two options for their native asset: either have a new native asset for the sidechain, or set aside some real XRP for use on the sidechain. If the sidechain uses XRP as its native asset, then the chain’s account on the Mainnet holds the sidechain’s total amount of XRP “in trust” for use in the sidechain. If the sidechain creates a different native asset, that asset can be issued on XRPL Mainnet by the sidechain’s Mainnet account.

The sidechain can hold other assets and tokens issued natively on the XRPL Mainnet; just like with XRP, the sidechain’s Mainnet account holds the total amount in use on the sidechain. The ownership of that asset within the sidechain can change as a result of transactions and events in the sidechain that the XRPL Mainnet never needs to see. Whenever an asset—XRP or otherwise—needs to move “out of” the sidechain, the sidechain’s Mainnet account sends that amount of XRP to its intended recipient on the Mainnet. This could even be another sidechain’s account, allowing assets to cross from one sidechain through the Mainnet to any other sidechain. Conversely, to send funds “into” a sidechain, you would send funds to that sidechain’s Mainnet account.

Someone who establishes a new sidechain should pick a set of initial validators and have them negotiate appropriate threshold or multi-signing keys. They would then create the sidechain’s XRPL Mainnet account and set it up so that only the sidechain validators’ collective signing power can control that account. If the sidechain’s validators change, then the Mainnet account should change its keys to match the new list of trusted validators. (Note: The XRP Ledger’s native multi-signing lists are limited to 8 keys or fewer, but threshold keys can support as many signers as necessary for each of the sidechain’s validators to be included).

With this software, anyone can choose to run a sidechain to the XRP Ledger. For developers, it unlocks new use cases like native DeFi capabilities and smart contracts. Developers can also build and launch blockchain features that are “baked” into these sidechains; in the future, successful features could even be ported to the XRPL Mainnet.

The developers managing a sidechain also have the freedom to decide how their chains work. They would choose their own validators for their sidechain and could change the system’s rules as they need (with the cooperation of their sidechain’s validators). For example, a sidechain could operate without transaction fees or reserve requirements, it could operate without its own copy of the XRP Ledger’s decentralized exchange, or it could add new transaction types and functionality for storing large chunks of data on-ledger. The possibilities are limitless: a sidechain can be strictly permissioned or (nearly) permissionless, centralized or (mostly) decentralized. You could even run a sidechain temporarily while letting it manage real value and gracefully shut it down after it has served its purpose.

Immediate advantages of Federated Sidechains for developers include:

Horizontal scaling: Sidechains can have their own fee system, their own reserve system, and their own transaction capacity. Someone who wants to create a system with thousands of users that can hold XRP has a better option than being the custodian or putting all the accounts on XRPL directly.

Low risk: The XRP Ledger doesn’t need to change at all. Even the changes that would be helpful are quite minimal.

Low effort: Anyone who needs or wants to experiment with a blockchain can get started with a complete system ready out of the box, based on powerful, stable, and sustainable XRP Ledger technology.

Long roadmap: New features can be added over a long period of time-based on feedback on what people find interesting. This would be a continuous stream of new features and capabilities.

Succeeding in this vision requires a few changes to the XRPL software that wouldn’t be used on XRPL itself in order to support the sidechain features. The primary change to the software would be to support the unique node list (UNL) being stored in the ledger. Pseudo-transactions to change the UNL would be needed. A “hint” UNL would need to be supported to avoid the chicken and egg problem of needing the UNL to get the ledger and the ledger to get the UNL.

Support for the coordination of creating threshold and/or multisign keys and signing XRPL transactions introduced by the federator is also necessary. Some API enhancements would likely be needed to handle pseudo-transactions introduced by the federator or federator-federator communication through the peer network.

The XRP Ledger mainnet could also use a flag to indicate whether an issued asset was permitted to federate or not. Some asset issuers, for example, might insist that all holders of their assets be directly represented on the main chain for regulatory purposes while others could allow their assets to freely trade on sidechains. (It’s always possible to privately allocate some of your own resources to others, with or without a sidechain to automate the process, but the legal responsibilities of doing so can vary based on jurisdiction and circumstances.)

Sidechains would have a special entry in their ledgers that tracks the last sidechain transaction that has been executed on the main chain and the last main chain transaction that has been executed on the sidechain.

When federators see a new transaction on the sidechain that affects the main chain, they coordinate the submission of that transaction to the main chain. When federators see a new transaction on the main chain that affects the sidechain, they coordinate the submission of that transaction to the main chain.

Making these changes is probably the biggest part of this effort because even though they won’t be enabled on XRPL, there is still risk associated with changing the software. For example, some existing code may need to be moved or adjusted which carries the risk of inadvertently changing behavior.

The outlined strategy is a starting point to gather feedback from the XRP Ledger community. We invite developers and contributors to the community to head to our Dev To community page to review and provide feedback. Let’s build a roadmap for innovative, new use cases together.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
