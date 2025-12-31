# Back to the Future: An Interview with David Schwartz and Stefan Thomas

**发布日期**: December 16, 2025
**作者**: 未知
**来源**: [https://ripple.com/insights/back-to-the-future-an-interview-with-david-schwartz-and-stefan-thomas/](https://ripple.com/insights/back-to-the-future-an-interview-with-david-schwartz-and-stefan-thomas/)

## 支付相关度评估
**评级**: 🟡 中度相关
**关键词匹配数**: 3

## 摘要
Ripple is the leading blockchain payments company.

## 核心内容

Team Ripple

On the latest episode of Block Stars, David Schwartz aka “JoelKatz”—as he’s known online—the creator of the XRP Ledger and current CTO of Ripple, sat down with Stefan Thomas, former CTO of Ripple and current CEO of Coil, to discuss the early days of blockchain, and their time working together on the XRP Ledger, Codius and Interledger Protocol (ILP).

Listen to David Schwartz on the Block Stars podcast at Apple Podcasts here.

One of the things that most people don’t realize about David and Stefan is that, prior to Ripple, they both used to work on Bitcoin. Stefan helped create BitcoinJS, which is a JavaScript implementation of the Bitcoin blockchain. David tinkered around with Bitcoin Core, as a C++ developer with a lot of experience using applied cryptography to build distributed systems, and helped the early core contributors solve some problems via the Bitcoin forum.

Both were inspired by the decentralized nature of the technology, but also recognized some issues early on, and sought to fix them.

Change is Hard(fork)

Like any open source protocol, proposing changes requires consensus among the developers and network operators (miners and full node operators in Bitcoin’s case) to ensure that the change is both beneficial and won’t hurt the network. Anyone can propose a change, but getting that change to be implemented and released into the live network can be challenging, and rightfully so. If every proposed change were automatically implemented, it could marginalize users and/or hurt the network.

In the early days of Bitcoin, the largest proposed changes appeared on a “hardfork wishlist,” which if implemented, would require everyone to upgrade to the latest version with the change, rendering previous versions incompatible with the latest version. Normally in software this would simply be an annoyance, but in blockchain technology like Bitcoin, if one doesn’t upgrade during a hardfork, then one could experience invalid blocks, which could lead to loss of funds. In order to minimize this risk, hardforks are typically reserved for critical changes to the blockchain. But what about changes that could make the technology better, faster, and more scalable? That’s where things get complicated.

Back in 2010, many developers, like David and Stefan, wanted to see Bitcoin evolve to become a better version of itself. But other developers didn’t want to take the risk of implementing certain hardforks to achieve this. In the interview, both David and Stefan estimated that the time table to adopting most of the proposals on the Bitcoin hardfork wishlist back in 2010 was about 30 years, which might have well been never for anyone looking to contribute.

That’s roughly when David, Jed McCaleb, and Arthur Britto, struck out to create an evolution of Bitcoin, with what we now call the XRP Ledger.

In the interview, Stefan attributes joining the “Open Coin” team (later renamed Ripple Labs), to almost like stepping into the future 30 years later. The XRP Ledger was a completely redesigned system from scratch, and built to be a better, faster, more scalable version of Bitcoin. It also had features that allowed it to support other currencies, which was one of the proposals on the Bitcoin hardfork wishlist that Stefan found most inspiring.

Smart Trade Offs with Codius

As one of the first JavaScript developers in the Bitcoin world, Stefan was known as the “Bitcoin in the browser” guy, and even made his BitcoinJS implementation capable of mining. He was also the first person to implement ECDSA in JavaScript, using an existing ECC implementation. Here he was merging the two technologies together in an effort to make Bitcoin more palatable to mainstream users. In the 1990’s the internet had a “Netscape moment” when it suddenly became usable via a browser to anyone with a dial-up connection. But Bitcoin hadn’t yet hit that milestone. Stefan was working to make that happen.

When Stefan was hired at Ripple, he had a few specific tasks. One was to build a client in an attempt to make the XRP Ledger more useful. Upon doing that, he spent a lot of time thinking about smart contracts, which are self-executing contracts where the terms of the agreement are written into the code. He built a working prototype using Google’s Native Client, which was a sandbox that Google had developed to run browser plugins. His thinking was, if it’s good enough to run code on the web, then it might be suitable enough for smart contracts, especially since it didn’t require developers to learn a new scripting language. Native Client had a strong security model called software fault isolation using a subset of x86, which verifies each bytecode or assembly instruction to ensure that the code can’t do anything outside of its model. Google invested a lot of infrastructure around the project, eventually partnering with Mozilla’s asm.js, and combining the two to form WebAssembly.

The promise of using Google’s Native Client to write smart contracts was met with some critical issues, which included getting non-deterministic results. David noted how large of a problem this is in a consensus protocol because you need honest people to be able to agree on what the smart contract does bit by bit, and if they can’t, then there’s no telling who’s honest or not. This breaks the security model of a decentralized network such as the XRP Ledger.

According to Stefan and David, this investigation led to a small breakthrough discovery. In the XRP Ledger, the consensus code is run on every validating node, which comes to consensus on the resulting transaction in the ledger. In theory you could run a contract that is going to execute with a lot of non-controversial results where there’s a lot of non-determinism and it will constantly come up with different results in different validators. But the only person that would suffer is the author of the contract or the contract participant, which creates an incentive not to do that.

At the same time, the non-determinism that you get in terms of when transactions arrive, can be tolerated by the XRP Ledger consensus mechanism. With Bitcoin’s proof of work, this couldn’t be done because it’s essentially one miner that chooses what goes into a block. This is problematic in the event that a miner chooses the minority case of that non-determinism, because you can’t later verify that it is actually one of the valid outputs.

But adding the complexity of smart contract functionality into a distributed system such as the XRP Ledger wouldn’t be free. Another limitation of using Google’s Native Client that Stefan noted was that although storing smart contract code next to your data seems promising, it results in different databases. For these databases to communicate with each other, one loses a lot of the benefits of having the code next to the data, such as determinism, which is core to the XRP Ledger’s primary use case of payments. Stefan noted that optimizing for security, performance and basic functionality was key to maintaining a distributed system for payments. Introducing more complex transactions to the XRP Ledger such as smart contracts could hurt that system.

This trade off led to a more three-tier architecture, where the backend data store has some basic access controls and very little business logic. Then there’s a separate stateless business logic layer that has services, which can talk to each other, and other data stores, blockchain or not. Applications could then have more flexibility in terms of architecture. In 2013, this three-tier approach became the basis for Codius, an open source project for stateless, distributed smart contract applications.

Paying It Forward with Interledger (ILP)

While deconstructing the architecture for Codius, in order to make the relationships more explicit, one of the remaining problems to solve was how to compensate the verifiers who are running the code, and prevent people from spamming those verifiers with infinite transactions? According to Stefan, the simple hosting model seemed to make sense, where the software host is paid directly for their service. But paying with a credit card wasn’t going to scale across a distributed network of n hosts and websites. An obvious answer was to force users to pay with XRP since it’s designed for efficient payments, but the team challenged themselves to think more broadly. Codius was already extensible enough to support any data store or blockchain, so why not apply that same agnosticism to other payment methods? All they needed was a neutral way to pay for Codius hosts.

In 2014, Stefan, Evan Schwartz and team started to explore what a neutral payment protocol would look like. A few design considerations were that it should be open, scalable enough to handle all the world’s transactions, including small transactions that aren’t generally cost effective enough for other payment networks to process, and lastly, that it should support cross-currency transactions, including fiat and crypto currencies. With those pillars in place, the team published an initial whitepaper of Interledger Protocol version 1.0 (ILPv1) in 2015. It wasn’t until 2018 with ILPv4 that everyone felt like the development of ILP had reached a point that it met all the criteria for it to be used as an open standard for payments, especially with Codius.

Stitching it All Together Through Web Monetization

It was also in 2018, that Stefan decided to spin out a startup called Coil, that is built on Codius and Interledger (fun anecdote, the name “Coil” is actually an acronym for Codius + Interledger), using XRP to settle payments. Coil builds upon Stefan’s long term vision to make it easier for creators to get paid using open networks. The Coil team has recognized an opportunity to empower content publishers to charge users directly via a browser API, rather than serving ads, as part of a broader standard called Web Monetization. To date, Coil has processed over 14 billion transactions with an average transaction size of a fraction of a penny, which helps to validate Interledger’s ability to support micro-transactions at scale.

The interview with David makes it clear that Stefan has spent the last decade deconstructing blockchain technology, and connecting the dots to build the Internet of Value using the XRP Ledger, Codius, and Interledger as a foundational platform.

---
*此文档由爬虫自动生成，发布时间: 2025-12-23 19:41:33*
