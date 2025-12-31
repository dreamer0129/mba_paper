# Beyond Proof of Work: the XRPL Consensus Solution

**发布日期**: December 16, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/beyond-proof-of-work-the-xrpl-consensus-solution/](https://ripple.com/insights/beyond-proof-of-work-the-xrpl-consensus-solution/)

## 支付相关度评估
**评级**: 🟡 中度相关
**关键词匹配数**: 4

## 摘要
The consensus validation system XRPL uses follows an anti-robustness principle, elevating reliability—a fundamentally different design from proof-of-work.

## 核心内容

Team Ripple

With the digital currency revolution continuing to gather pace, the debate between advocates of proof-of-work and newer agreement algorithms rages on. Beyond the rhetoric, the evolution of the consensus approach continues to make steady progress that, due to design limitations, transactionally-focused proof-of-work networks find it difficult to match.

As the only enterprise blockchain company today with payment products in commercial use, Ripple has found that the digital asset XRP enables its users to rapidly and inexpensively source liquidity—while also offering greater scalability than any other digital asset.

The XRP Ledger (XRPL) has a fundamentally different design from proof-of-work based blockchains like Bitcoin and Ethereum. The consensus validation system XRPL uses follows an anti-robustness principle that elevates reliability. This provides the system with a built-in safety mechanism: when safe forward progress is not clearly possible, XRPL does not make forward progress.

Despite the existence of this consensus validation enabled safety brake, XRPL has demonstrated a reliability rate of more than 99.999% since it began operation more than 58 million ledgers ago. XRPL’s history of closing a ledger roughly every five seconds attests to this consistency.

The “secret sauce” of public blockchains like Bitcoin is that every participant can confirm that every transaction complies with all system rules. As a result, system state is public: transactions are public, and everyone knows which transactions are valid and which aren’t. With such a system, validators aren’t needed to tell anyone else which transactions are valid or what transactions do. The validity of each transaction is already available to every participant.

“Consensus”, as it applies to the validation method utilized by XRPL, refers to the need to solve the double spend problem. This problem occurs when there are two (or more) “equally good” ways to make forward progress. Consensus ensures dishonest participants can’t trick honest participants into disagreeing over system state.

In such a system, the primary role of validators is to allow honest participants to agree on a way forward when two or more equally good ways to make forward progress exist. This approach thwarts attempts to double spend by preventing participants from being tricked by malicious parties into expecting the same funds to be delivered to two different destinations.

Public blockchains have no central authorities that dictate system rules. Every participant can choose whatever rules they want. However, participants who do not agree on system rules won’t be able to interoperate with each other. This creates complexity and risk when system rules are changed.

Consensus-driven systems can take a different approach: in the case of XRP Ledger, validators help protect against unintentional forking of the ledger by coordinating system rules changes. However, they cannot make any server accept a rule change it is not configured specifically to accept. To become effective after introduction, amendments to the ledger require 80% quorum approval for two consecutive weeks by the validator community.

XRPL’s consensus scheme using validators provides a cheap, reliable, decentralized, fast solution to the double spend problem. Its design also permits the network to be upgraded, when participants agree to do so, without the risk of accidental divergence.

While proof-of-work, with the massive electrical usage and transaction cost inefficiencies the approach entails, has proven to be a technological dead end, other consensus algorithms continue to innovate to provide better decentralization at lower cost and lower risk. Development continues on XRPL’s consensus algorithm to improve resilience. In this regard, the recently introduced “Negative UNL” feature is set to dramatically improve XRPL’s ability to tolerate validator outages while still making reliable forward progress.

This feature proposes bolstering the liveness of the XRPL network via functionality that enables servers to keep track of validators which have gone offline temporarily. Armed with this information, servers can adjust quorum calculations to reflect the offline validators. Because a validator going offline for a short period of time is not necessarily a sign of unreliability, Negative UNL helps UNL publishers deal with scenarios where a validator is not down long enough to trigger removal from the UNL, while still reflecting its offline status to ensure the network can make forward progress.

Ripple and others in the community will be conducting extensive public testing of the Negative UNL feature on the XRPL Devnet over the next few months. If this public testing meets all applicable requirements with regard to security, reliability, stability, and performance, an amendment to implement Negative UNL functionality could be introduced for quorum review in a future version 2.0 release.

For more information about building on XRPL, check out the RippleX Platform for developer tools, services and programs to get started.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
